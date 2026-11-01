#!/usr/bin/env python3
"""GAI-INT-40 candidate-v2 hardened runner proposal.

HARDENING CANDIDATE; EXECUTION BLOCKED PENDING INDEPENDENT TRUST VERIFIER. Requires separate, explicit Pedido B
authorization plus an externally enforced no-network sandbox. No network or
secret-handling code is provided. Do not interpret a passing result as a gate.
"""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import subprocess
import re
from urllib.parse import urldefrag, urljoin

from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[2]
CATALOGS = {
    "compat-v2": ("docs/matriz-casos-compatibilidade-v2-candidata.json", 15),
    "protocol-v2": ("docs/matriz-casos-protocolo-candidate-2.json", 18),
}
LOGICAL_SCHEMAS = {
    "cap11-report-result": "schemas/candidate-v2-proposed/cap11-report-result.schema.json",
    "event-receipt": "schemas/candidate-v2-proposed/event-receipt.schema.json",
    "canonical-event": "schemas/candidate-v2-proposed/canonical-event.schema.json",
}
PREFIX = "https://guivos-repositorio.github.io/Guivos-AI/schemas/"
ALLOWED_DIRS = ("schemas/candidate-v1/", "schemas/candidate-v2-proposed/")
REQUIRED_AUTH_KEYS = (
    "approved", "scope", "authorization_ref", "repository_sha",
    "operator_ref", "independent_reviewer_ref", "environment_ref",
    "offline_isolation_confirmed", "dependency_lock_digest",
)


class CampaignError(Exception):
    pass


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def allowed_path(relative):
    if not isinstance(relative, str) or not relative.startswith(ALLOWED_DIRS):
        raise CampaignError("Schema outside allowlisted directories")
    target = (ROOT / relative).resolve(strict=True)
    if not target.is_relative_to(ROOT.resolve()) or target.suffix != ".json":
        raise CampaignError("Invalid schema path")
    return target


def check_authorization(path, expected_sha):
    raise CampaignError("REV2-01: trusted authorization verifier not provisioned; do not execute")
    auth = read_json(path)
    if not isinstance(auth, dict) or any(k not in auth for k in REQUIRED_AUTH_KEYS):
        raise CampaignError("Missing separately approved Pedido B authorization fields")
    if auth["approved"] is not True or auth["scope"] != "offline_synthetic_B":
        raise CampaignError("Pedido B is not authorized for this campaign")
    if auth["offline_isolation_confirmed"] is not True:
        raise CampaignError("External no-network isolation must be confirmed")
    for key in ("authorization_ref", "repository_sha", "operator_ref",
                "independent_reviewer_ref", "environment_ref", "dependency_lock_digest"):
        if not isinstance(auth[key], str) or not auth[key].strip():
            raise CampaignError("Missing authorization field: " + key)
    if auth["repository_sha"] != expected_sha or len(expected_sha) != 40:
        raise CampaignError("Execution repository SHA does not match authorization")
    if auth["operator_ref"] == auth["independent_reviewer_ref"]:
        raise CampaignError("Executor and independent reviewer cannot be identical")
    return auth


def verify_checkout(expected_sha):
    if not re.fullmatch(r'[0-9a-f]{40}', expected_sha):
        raise CampaignError('Invalid git SHA format')
    command = subprocess.run(['git', '-C', str(ROOT), 'rev-parse', 'HEAD'],
                             capture_output=True, text=True, check=True, timeout=10)
    if command.stdout.strip() != expected_sha:
        raise CampaignError('Actual checkout SHA does not match authorization')
    status = subprocess.run(['git', '-C', str(ROOT), 'status', '--porcelain', '--untracked-files=all'],
                            capture_output=True, text=True, check=True, timeout=10)
    if status.stdout.strip():
        raise CampaignError('Dirty checkout is not permitted')


def build_registry():
    mapping, digests = {}, {}
    for directory in ALLOWED_DIRS:
        for path in sorted((ROOT / directory).glob("*.schema.json")):
            resolved = allowed_path(path.relative_to(ROOT).as_posix())
            doc = read_json(resolved)
            Draft202012Validator.check_schema(doc)
            uri = doc.get("$id")
            if not isinstance(uri, str) or not uri.startswith(PREFIX):
                raise CampaignError("Unexpected schema ID: " + str(uri))
            expected_uri = PREFIX + path.relative_to(ROOT / "schemas").as_posix()
            if uri != expected_uri:
                raise CampaignError("Schema ID and location do not match: " + uri)
            if uri in mapping:
                raise CampaignError("Duplicate schema ID: " + uri)
            mapping[uri] = Resource.from_contents(doc)
            digests[uri] = hashlib.sha256(resolved.read_bytes()).hexdigest()
    # Validate all referenced schema locations before running fixtures.
    for uri, resource in mapping.items():
        def walk(value):
            if isinstance(value, dict):
                ref = value.get("$ref")
                if isinstance(ref, str):
                    target = urldefrag(urljoin(uri, ref)).url
                    if target not in mapping:
                        raise CampaignError("Unresolved or external schema reference: " + target)
                for entry in value.values():
                    walk(entry)
            elif isinstance(value, list):
                for entry in value:
                    walk(entry)
        walk(resource.contents)
    return Registry().with_resources(mapping.items()), digests


def normalize_cases(catalog_id):
    filename, expected_count = CATALOGS[catalog_id]
    data = read_json(ROOT / filename)
    cases = data.get("cases")
    if not isinstance(cases, list) or len(cases) != expected_count:
        raise CampaignError("Unexpected number of cases in " + catalog_id)
    result = []
    for case in cases:
        name = case.get("schema")
        if catalog_id == "compat-v2":
            target = LOGICAL_SCHEMAS.get(name)
            expected = case.get("expected_valid_v2")
        else:
            target = name
            expected = case.get("expected_valid")
        if target is None or not isinstance(expected, bool):
            raise CampaignError("Unknown schema or non-boolean expectation")
        schema_path = allowed_path(target)
        if "instance" not in case or not isinstance(case.get("case_id"), str) or not case["case_id"].strip():
            raise CampaignError("Missing instance or case identifier")
        result.append((catalog_id, case["case_id"], schema_path, case["instance"], expected))
    return result


def main():
    parser = argparse.ArgumentParser(description="Gated synthetic offline v2 runner")
    parser.add_argument("--authorization", required=True, type=Path)
    parser.add_argument("--repo-sha", required=True)
    parser.add_argument("--evidence-out", required=True, type=Path)
    args = parser.parse_args()
    try:
        auth = check_authorization(args.authorization, args.repo_sha)
        verify_checkout(args.repo_sha)
        if args.evidence_out.exists():
            raise CampaignError("Refusing to overwrite existing evidence")
        if args.evidence_out.resolve().is_relative_to(ROOT.resolve()):
            raise CampaignError("Evidence output must be outside source repository")
        cases = [case for key in CATALOGS for case in normalize_cases(key)]
        ids = [case[1] for case in cases]
        if len(cases) != 33 or len(ids) != len(set(ids)):
            raise CampaignError("Expected 33 cases with globally unique IDs")
        registry, digests = build_registry()
        results = []
        for catalog_id, case_id, schema_path, instance, expected in cases:
            schema = read_json(schema_path)
            uri = schema["$id"]
            validator = Draft202012Validator(schema, registry=registry,
                                               format_checker=FormatChecker())
            errors = list(validator.iter_errors(instance))
            observed = not errors
            results.append({
                "catalog_id": catalog_id, "case_id": case_id, "schema_uri": uri,
                "schema_digest": digests[uri], "expected_valid": expected,
                "observed_valid": observed, "matched": observed == expected,
                "error_paths": sorted(str(e.json_path) for e in errors),
                "failure_kind": "expectation_mismatch" if observed != expected else None,
            })
        evidence = {
            "execution_status": "completed_structural_only",
            "authorization_ref": auth["authorization_ref"],
            "repository_sha": args.repo_sha,
            "environment_ref": auth["environment_ref"],
            "operator_ref": auth["operator_ref"],
            "independent_reviewer_ref": auth["independent_reviewer_ref"],
            "dependency_lock_digest": auth["dependency_lock_digest"],
            "registry_digests": digests,
            "results": results,
            "campaign_id": auth.get("campaign_id"),
            "evidence_digest": None,
            "total": len(results),
            "matched": sum(r["matched"] for r in results),
            "gate_decision_ref": None,
            "limitations": [
                "No semantic/privacy/authentication or operational validation",
                "No network isolation guarantee from Python; external sandbox required",
                "Independent trusted authorization verifier is not implemented; this candidate is intentionally blocked",
            ],
        }
        args.evidence_out.parent.mkdir(parents=True, exist_ok=True)
        with args.evidence_out.open("x", encoding="utf-8") as f:
            json.dump(evidence, f, indent=2, ensure_ascii=False)
            f.write("\n")
        print("Structural comparison completed; evidence written; no gate approved")
        return 0 if evidence["matched"] == 33 else 1
    except (CampaignError, OSError, ValueError, KeyError, TypeError, subprocess.SubprocessError) as exc:
        print("ABORT: controlled failure; see independent audit log", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
