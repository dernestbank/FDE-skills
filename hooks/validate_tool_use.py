#!/usr/bin/env python3
"""Conservative pre-tool hook for FDE OS.

Reads Claude hook JSON from stdin. It blocks obviously destructive or high-risk shell
commands and otherwise permits the action. Project-specific authorization should be
implemented in the MCP backend and deployment policy.
"""

from __future__ import annotations

import json
import re
import sys
from typing import Any


def emit(decision: str, reason: str) -> None:
    print(json.dumps({"decision": decision, "reason": reason}))


def main() -> int:
    try:
        payload: dict[str, Any] = json.load(sys.stdin)
    except Exception as exc:
        emit("block", f"Invalid hook payload: {exc}")
        return 0

    tool_name = str(payload.get("tool_name", ""))
    tool_input = payload.get("tool_input") or {}
    serialized = json.dumps(tool_input, ensure_ascii=False)

    destructive_patterns = [
        r"\brm\s+-rf\s+[/~]",
        r"\bmkfs\b",
        r"\bformat\s+[A-Za-z]:",
        r"\bDROP\s+(DATABASE|SCHEMA)\b",
        r"\bTRUNCATE\s+TABLE\b",
        r"\bshutdown\b",
        r"\breboot\b",
    ]
    for pattern in destructive_patterns:
        if re.search(pattern, serialized, flags=re.IGNORECASE):
            emit("block", f"Blocked destructive operation matching {pattern}")
            return 0

    if tool_name.lower().endswith("approve_action"):
        approved = bool(tool_input.get("human_approved"))
        if not approved:
            emit("block", "Consequential approval tool requires human_approved=true")
            return 0

    emit("allow", "No blocking FDE OS pre-tool rule matched")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
