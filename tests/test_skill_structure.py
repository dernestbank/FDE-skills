from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = {
    "fde-os",
    "fde-setup",
    "fde-start",
    "fde-discover",
    "fde-map",
    "fde-prioritize",
    "fde-design",
    "fde-build",
    "fde-review",
    "fde-evaluate",
    "fde-deploy",
    "fde-pulse",
    "fde-compound",
    "fde-handoff",
    "fde-status",
    "fde-report",
}


def parse_frontmatter(text: str) -> dict[str, str]:
    assert text.startswith("---\n"), "SKILL.md must start with YAML frontmatter"
    _, raw, _ = text.split("---", 2)
    result: dict[str, str] = {}
    for line in raw.splitlines():
        if ":" not in line or line.lstrip().startswith("#"):
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip("'\"")
    return result


def test_expected_skills_exist_and_match_names() -> None:
    actual = {
        path.parent.name
        for path in (ROOT / "skills").glob("*/SKILL.md")
    }
    assert SKILLS <= actual

    for name in SKILLS:
        path = ROOT / "skills" / name / "SKILL.md"
        frontmatter = parse_frontmatter(path.read_text(encoding="utf-8"))
        assert frontmatter.get("name") == name
        description = frontmatter.get("description", "")
        assert len(description) >= 40
        assert "Use" in description
        assert "Not" in description


def test_plugin_and_marketplace_versions_match() -> None:
    plugin = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text())
    marketplace = json.loads(
        (ROOT / ".claude-plugin" / "marketplace.json").read_text()
    )
    assert plugin["version"] == marketplace["metadata"]["version"]
    assert marketplace["plugins"][0]["source"] == "./"


def test_old_commands_and_agents_are_not_active_at_root() -> None:
    assert not (ROOT / "commands").exists()
    assert not (ROOT / "agents").exists()
    assert (ROOT / "legacy" / "commands").exists()
    assert (ROOT / "legacy" / "agents").exists()


def test_skill_eval_cases_are_valid_json() -> None:
    for path in (ROOT / "tests" / "skill-evals").glob("*.json"):
        cases = json.loads(path.read_text(encoding="utf-8"))
        assert isinstance(cases, list)
        assert cases
        assert all("id" in case and "prompt" in case for case in cases)


def test_compound_owns_one_learning_per_run() -> None:
    text = (ROOT / "skills" / "fde-compound" / "SKILL.md").read_text(
        encoding="utf-8"
    )
    assert "exactly one durable learning per run" in text


def test_build_is_separate_from_evaluation() -> None:
    build = (ROOT / "skills" / "fde-build" / "SKILL.md").read_text(
        encoding="utf-8"
    )
    assert "Do not claim evaluation readiness from local tests alone" in build
