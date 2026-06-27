#!/usr/bin/env python3
"""Privacy-aware post-tool audit hook for FDE OS.

The audit log records enough metadata to reconstruct tool usage without persisting
raw credentials, large documents, model responses, or sensitive tool payloads.
Logging failures never mask the original tool result.
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SENSITIVE_KEYS = {
    "api_key",
    "apikey",
    "authorization",
    "cookie",
    "credential",
    "credentials",
    "password",
    "private_key",
    "refresh_token",
    "secret",
    "token",
}
MAX_STRING = 240
MAX_ITEMS = 40


def redact(value: Any, key: str | None = None, depth: int = 0) -> Any:
    if key and key.lower() in SENSITIVE_KEYS:
        return "<redacted>"
    if depth > 5:
        return "<depth-limit>"
    if isinstance(value, dict):
        result: dict[str, Any] = {}
        for index, (child_key, child_value) in enumerate(value.items()):
            if index >= MAX_ITEMS:
                result["<truncated>"] = f"{len(value) - MAX_ITEMS} more keys"
                break
            result[str(child_key)] = redact(child_value, str(child_key), depth + 1)
        return result
    if isinstance(value, list):
        items = [redact(item, None, depth + 1) for item in value[:MAX_ITEMS]]
        if len(value) > MAX_ITEMS:
            items.append(f"<truncated {len(value) - MAX_ITEMS} items>")
        return items
    if isinstance(value, str):
        if len(value) <= MAX_STRING:
            return value
        digest = hashlib.sha256(value.encode("utf-8", errors="replace")).hexdigest()[:12]
        return f"{value[:MAX_STRING]}...<truncated sha256:{digest} chars:{len(value)}>"
    if isinstance(value, (int, float, bool)) or value is None:
        return value
    return f"<{type(value).__name__}>"


def summarize_response(value: Any) -> dict[str, Any]:
    if isinstance(value, dict):
        summary: dict[str, Any] = {
            "type": "object",
            "keys": list(value.keys())[:MAX_ITEMS],
        }
        for key in ("status", "success", "error", "is_error", "decision"):
            if key in value:
                summary[key] = redact(value[key], key)
        return summary
    if isinstance(value, list):
        return {"type": "array", "items": len(value)}
    if isinstance(value, str):
        digest = hashlib.sha256(value.encode("utf-8", errors="replace")).hexdigest()[:12]
        return {"type": "string", "chars": len(value), "sha256": digest}
    return {"type": type(value).__name__}


def main() -> int:
    try:
        payload: dict[str, Any] = json.load(sys.stdin)
    except Exception:
        return 0

    record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "tool_name": payload.get("tool_name"),
        "tool_input": redact(payload.get("tool_input")),
        "tool_response": summarize_response(payload.get("tool_response")),
        "session_id": payload.get("session_id"),
    }

    try:
        root = Path(os.getcwd()) / ".fde-os" / "audit"
        root.mkdir(parents=True, exist_ok=True)
        with (root / "tool-actions.jsonl").open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record, ensure_ascii=False, default=str) + "\n")
    except Exception:
        pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
