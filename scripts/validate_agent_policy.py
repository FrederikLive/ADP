#!/usr/bin/env python3
"""Dependency-free checks for the optional ADP agent-assignment policy example/schema."""
import copy
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT / "schema/agent-policy.schema.json").read_text())
EXAMPLE = json.loads((ROOT / "examples/AGENT_POLICY.json").read_text())


def errors_for(value):
    errors = []

    def check(schema, data, location="$"):
        if "$ref" in schema:
            ref = schema["$ref"]
            if not ref.startswith("#/$defs/"):
                errors.append(location + ": unsupported schema ref")
                return
            check(SCHEMA["$defs"][ref.split("/")[-1]], data, location)
            return
        if "const" in schema and data != schema["const"]:
            errors.append(location + ": wrong constant")
        if "enum" in schema and data not in schema["enum"]:
            errors.append(location + ": invalid enum")
        kind = schema.get("type")
        types = kind if isinstance(kind, list) else [kind]
        matches = {
            "object": lambda a: isinstance(a, dict),
            "array": lambda a: isinstance(a, list),
            "string": lambda a: isinstance(a, str),
            "integer": lambda a: isinstance(a, int) and not isinstance(a, bool),
            "number": lambda a: isinstance(a, (int, float)) and not isinstance(a, bool),
            "boolean": lambda a: isinstance(a, bool),
            "null": lambda a: a is None,
        }
        if kind is not None and not any(matches[t](data) for t in types):
            errors.append(location + ": wrong type")
            return
        if isinstance(data, str) and len(data) < schema.get("minLength", 0):
            errors.append(location + ": too short")
        if isinstance(data, (int, float)) and not isinstance(data, bool):
            if "minimum" in schema and data < schema["minimum"]:
                errors.append(location + ": below minimum")
        if isinstance(data, list):
            if schema.get("uniqueItems") and len({json.dumps(v, sort_keys=True) for v in data}) != len(data):
                errors.append(location + ": duplicates")
            for i, item in enumerate(data):
                if "items" in schema:
                    check(schema["items"], item, location + "[" + str(i) + "]")
        if isinstance(data, dict):
            for req in schema.get("required", []):
                if req not in data:
                    errors.append(location + "." + req + ": missing")
            props = schema.get("properties", {})
            extra = schema.get("additionalProperties", True)
            for key, val in data.items():
                if key in props:
                    check(props[key], val, location + "." + key)
                elif extra is False:
                    errors.append(location + "." + key + ": unknown")
                elif isinstance(extra, dict):
                    check(extra, val, location + "." + key)

    check(SCHEMA, value)
    return errors


def assert_rejected(mutator, reason):
    candidate = copy.deepcopy(EXAMPLE)
    mutator(candidate)
    assert errors_for(candidate), "Should reject " + reason


def main():
    assert not errors_for(EXAMPLE), "Example failed schema: " + str(errors_for(EXAMPLE))
    assert EXAMPLE["orchestration"]["mode"] == "advisory"
    assert EXAMPLE["resources"]["max_api_spend_usd"] == 0
    assert "authority" not in SCHEMA["properties"], "Policy must not grant authority"
    assert SCHEMA.get("additionalProperties") is False
    assert not errors_for({
        "schema_version": 1,
        "orchestration": {"mode": "harness_native"},
        "resources": {"optimization": "privacy_first"},
    })
    assert_rejected(lambda x: x["orchestration"].update(mode="unlimited"), "unsupported routing mode")
    assert_rejected(lambda x: x["resources"].update(max_api_spend_usd=-1), "negative budget")
    assert_rejected(lambda x: x.update(authority={"lead": "unlimited"}), "authority escalation")
    assert_rejected(lambda x: x["roles"]["lead_programmer"].update(api_key="secret"), "credentials in role")
    assert_rejected(lambda x: x["resources"].update(optimization="whatever"), "unknown optimization")
    assert_rejected(lambda x: x["routing"].update(evaluate_per_contract="yes"), "non-boolean")
    assert_rejected(lambda x: x["resources"].update(approved_providers=["openai", "openai"]), "duplicates")
    print("VERIFIED: optional agent policy example and negative cases")


if __name__ == "__main__":
    main()
