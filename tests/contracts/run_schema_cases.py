#!/usr/bin/env python3
"""Offline candidate JSON Schema contract checks using synthetic fixtures only.

Run from repository root with: python tests/contracts/run_schema_cases.py
Prerequisite: python -m pip install 'jsonschema>=4,<5'
This is not authorization, semantic evaluation, or operational release validation.
"""
import json
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "tests" / "contracts" / "candidate-v1" / "cases.json"

def main() -> int:
    catalog = json.loads(MANIFEST.read_text(encoding="utf-8"))
    results = []
    for case in catalog["cases"]:
        schema_path = ROOT / case["schema"]
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        errors = sorted(validator.iter_errors(case["instance"]), key=lambda e: (str(e.json_path), e.message))
        observed_valid = not errors
        matched = observed_valid == case["expected_valid"]
        results.append({"case_id":case["case_id"],"schema":case["schema"],"expected_valid":case["expected_valid"],"observed_valid":observed_valid,"matched":matched,"error_paths":[e.json_path for e in errors]})
        print(f'{"PASS" if matched else "FAIL"} {case["case_id"]}: observed_valid={observed_valid} expected={case["expected_valid"]}')
    total = len(results)
    passed = sum(x["matched"] for x in results)
    print(f"Structural fixture comparison: {passed}/{total} matched.")
    print("No privacy, authorization, semantic, integration, or gate evaluation was performed.")
    return 0 if passed == total else 1

if __name__ == "__main__":
    raise SystemExit(main())
