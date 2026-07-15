#!/usr/bin/env python3
"""Validate required semantic fields in an FDE OS workflow JSON document."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def validate(workflow: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if not workflow.get("trigger"):
        errors.append("workflow trigger is missing")
    if not workflow.get("final_output"):
        errors.append("workflow final_output is missing")
    steps = workflow.get("steps")
    if not isinstance(steps, list) or not steps:
        errors.append("workflow must contain at least one step")
        return errors

    seen_ids: set[str] = set()
    for index, step in enumerate(steps, start=1):
        prefix = f"step[{index}]"
        step_id = step.get("step_id")
        if not step_id:
            errors.append(f"{prefix} step_id is missing")
        elif step_id in seen_ids:
            errors.append(f"{prefix} duplicate step_id {step_id}")
        else:
            seen_ids.add(step_id)
        if not step.get("name"):
            errors.append(f"{prefix} name is missing")
        if not step.get("owner_id"):
            errors.append(f"{prefix} owner_id is missing")
        if not isinstance(step.get("inputs"), list):
            errors.append(f"{prefix} inputs must be a list")
        if not isinstance(step.get("outputs"), list):
            errors.append(f"{prefix} outputs must be a list")
        if not isinstance(step.get("failure_modes"), list) or not step.get("failure_modes"):
            errors.append(f"{prefix} failure_modes are missing")
        if not isinstance(step.get("evidence_refs"), list) or not step.get("evidence_refs"):
            errors.append(f"{prefix} evidence_refs are missing")
        confidence = step.get("confidence")
        if not isinstance(confidence, (int, float)) or not 0 <= confidence <= 1:
            errors.append(f"{prefix} confidence must be between 0 and 1")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()
    path = Path(args.path)
    workflow = json.loads(path.read_text(encoding="utf-8"))
    errors = validate(workflow)
    result = {"valid": not errors, "errors": errors}
    print(json.dumps(result, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
