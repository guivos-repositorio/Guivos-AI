#!/usr/bin/env python3
"""Validate synthetic typed AnalysisResponse fixtures with a local schema registry.

Run from repository root: python tests/contracts/run_typed_cases.py
Dependency: python -m pip install 'jsonschema>=4,<5' 'referencing>=0.35,<1'
Candidate artifacts only; not an authentication, semantic, privacy, or gate test.
"""
import json
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[2]
SCHEMA_ROOT = ROOT / "schemas" / "candidate-v1"
CASES = ROOT / "tests" / "contracts" / "candidate-v1" / "typed-cases.json"
BASE_URI = "https://guivos-repositorio.github.io/Guivos-AI/schemas/candidate-v1/"

def build_registry():
    resources = []
    for file in sorted(SCHEMA_ROOT.glob("*.schema.json")):
        doc = json.loads(file.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(doc)
        resources.append((BASE_URI + file.name, Resource.from_contents(doc)))
    return Registry().with_resources(resources)

def main():
    registry = build_registry()
    schema = json.loads((SCHEMA_ROOT / "analysis-response-typed.schema.json").read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, registry=registry, format_checker=FormatChecker())
    catalog = json.loads(CASES.read_text(encoding="utf-8"))
    count = 0
    for case in catalog["cases"]:
        errors = list(validator.iter_errors(case["instance"]))
        valid = not errors
        success = valid == case["expected_valid"]
        count += success
        print(f'{"PASS" if success else "FAIL"} {case["case_id"]} expected={case["expected_valid"]} observed={valid}')
    print(f"Structural matches: {count}/{len(catalog['cases'])}. No semantic/security assessment performed.")
    return 0 if count == len(catalog["cases"]) else 1

if __name__ == "__main__":
    raise SystemExit(main())
