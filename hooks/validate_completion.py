#!/usr/bin/env python3
"""Stop hook guarding advanced FDE readiness claims.

The hook checks only the dossier referenced by `.fde-os/active-engagement`.
It does not require every engagement to be complete and avoids blocking ordinary
conversation when no active dossier has been selected.
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

REQUIRED_SECTIONS = {
    "deployment-ready": [
        "Evaluation contract and results",
        "Deployment and operating model",
        "Risks, assumptions, disputes, and unknowns",
        "Decision log",
        "Next gate",
    ],
    "operational": [
        "Evaluation contract and results",
        "Deployment and operating model",
        "Risks, assumptions, disputes, and unknowns",
        "Decision log",
        "Next gate",
    ],
}

REQUIRED_ARTIFACTS = {
    "deployment-ready": ["evaluation-report.json", "deployment-plan.json"],
    "operational": ["evaluation-report.json", "deployment-plan.json", "metrics.json"],
}


def emit(decision: str, reason: str) -> None:
    print(json.dumps({"decision": decision, "reason": reason}))


def read_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    result: dict[str, str] = {}
    for line in parts[1].splitlines():
        if ":" not in line or line.lstrip().startswith("#"):
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip("'\"")
    return result


def main() -> int:
    try:
        _ = json.load(sys.stdin)
    except Exception:
        pass

    root = Path(os.getcwd())
    pointer = root / ".fde-os" / "active-engagement"
    if not pointer.exists():
        emit("allow", "No active FDE engagement pointer found")
        return 0

    try:
        raw_path = pointer.read_text(encoding="utf-8").strip()
        dossier = Path(raw_path)
        if not dossier.is_absolute():
            dossier = root / dossier
        dossier = dossier.resolve()
    except Exception as exc:
        emit("block", f"Invalid active engagement pointer: {exc}")
        return 0

    if not dossier.exists():
        emit("block", f"Active engagement dossier does not exist: {dossier}")
        return 0

    text = dossier.read_text(encoding="utf-8", errors="replace")
    frontmatter = read_frontmatter(text)
    readiness = frontmatter.get("artifact_readiness", "")
    if readiness not in REQUIRED_SECTIONS:
        emit("allow", f"Active engagement readiness is {readiness or 'unknown'}")
        return 0

    missing_sections = [
        title
        for title in REQUIRED_SECTIONS[readiness]
        if not re.search(rf"^##+\s+{re.escape(title)}\s*$", text, flags=re.MULTILINE)
    ]

    artifacts_dir = dossier.parent / "artifacts"
    missing_artifacts = [
        name for name in REQUIRED_ARTIFACTS[readiness] if not (artifacts_dir / name).exists()
    ]

    if missing_sections or missing_artifacts:
        reasons: list[str] = []
        if missing_sections:
            reasons.append("missing dossier sections: " + ", ".join(missing_sections))
        if missing_artifacts:
            reasons.append("missing readiness artifacts: " + ", ".join(missing_artifacts))
        emit("block", f"Readiness '{readiness}' is unsupported; " + "; ".join(reasons))
        return 0

    emit("allow", f"Readiness '{readiness}' has the required dossier sections and artifacts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
