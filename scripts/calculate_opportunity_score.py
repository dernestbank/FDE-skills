#!/usr/bin/env python3
"""Calculate an FDE OS opportunity score from a JSON file or stdin."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


def calculate(data: dict[str, Any]) -> float:
    value = float(data["business_value_score"])
    suitability = float(data["workflow_suitability_score"])
    feasibility = float(data["technical_feasibility_score"])
    readiness = float(data["deployment_readiness_score"])
    time_to_value = float(data["time_to_value_score"])
    risk = float(data["risk_score"])
    risk_penalty = max(0.0, risk - 1.0) * 0.25
    return round(0.30 * value + 0.20 * suitability + 0.20 * feasibility + 0.15 * readiness + 0.15 * time_to_value - risk_penalty, 3)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", help="JSON opportunity file; reads stdin when omitted")
    args = parser.parse_args()
    if args.path:
        data = json.loads(Path(args.path).read_text(encoding="utf-8"))
    else:
        data = json.load(sys.stdin)
    score = calculate(data)
    data["weighted_score"] = score
    print(json.dumps(data, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
