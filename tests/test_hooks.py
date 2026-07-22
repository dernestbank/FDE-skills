from __future__ import annotations

import importlib.util
from pathlib import Path
from types import ModuleType

ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, path: Path) -> ModuleType:
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_audit_redacts_secrets_and_truncates_large_values() -> None:
    module = load_module("fde_log_tool_action", ROOT / "hooks" / "log_tool_action.py")
    value = {
        "api_key": "super-secret",
        "nested": {"authorization": "Bearer secret"},
        "document": "x" * 1000,
    }
    redacted = module.redact(value)
    assert redacted["api_key"] == "<redacted>"
    assert redacted["nested"]["authorization"] == "<redacted>"
    assert "<truncated" in redacted["document"]
    assert "chars:1000" in redacted["document"]


def test_response_summary_does_not_store_raw_text() -> None:
    module = load_module("fde_log_tool_action_2", ROOT / "hooks" / "log_tool_action.py")
    raw = "sensitive body" * 100
    summary = module.summarize_response(raw)
    assert summary["type"] == "string"
    assert summary["chars"] == len(raw)
    assert raw not in str(summary)


def test_destructive_patterns_remain_present() -> None:
    text = (ROOT / "hooks" / "validate_tool_use.py").read_text(encoding="utf-8")
    assert "rm\\s+-rf" in text
    assert "DROP\\s+(DATABASE|SCHEMA)" in text
    assert "human_approved" in text


def test_completion_hook_uses_active_engagement_pointer() -> None:
    text = (ROOT / "hooks" / "validate_completion.py").read_text(encoding="utf-8")
    assert "active-engagement" in text
    assert "deployment-ready" in text
    assert "operational" in text
