#!/usr/bin/env python3
"""FDE OS repository health check.

This script is intentionally dependency-free so setup can run before optional
packages are installed.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

REQUIRED_SKILLS = [
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
]

OPTIONAL_TOOLS = ["git", "python", "node", "docker", "jq", "mmdc"]


def find_root(start: Path) -> Path:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            cwd=start,
            check=True,
            capture_output=True,
            text=True,
        )
        return Path(result.stdout.strip()).resolve()
    except (FileNotFoundError, subprocess.CalledProcessError):
        current = start.resolve()
        for candidate in [current, *current.parents]:
            if (candidate / ".claude-plugin" / "plugin.json").exists():
                return candidate
        return current


def check_json(path: Path) -> tuple[bool, str]:
    try:
        json.loads(path.read_text(encoding="utf-8"))
        return True, "valid"
    except Exception as exc:  # diagnostic boundary
        return False, str(exc)


def gitignored(root: Path, path: str) -> bool:
    try:
        return subprocess.run(
            ["git", "check-ignore", "-q", path], cwd=root, check=False
        ).returncode == 0
    except FileNotFoundError:
        return False


def main() -> int:
    skill_dir = Path(__file__).resolve().parent.parent
    root = find_root(Path.cwd())
    plugin_root = skill_dir.parent.parent
    if (plugin_root / ".claude-plugin" / "plugin.json").exists():
        root = plugin_root

    failures: list[str] = []
    warnings: list[str] = []

    print("FDE OS -- checking environment")
    print(f"Root: {root}")

    for rel in [".claude-plugin/plugin.json", ".claude-plugin/marketplace.json"]:
        path = root / rel
        if not path.exists():
            failures.append(f"missing {rel}")
            continue
        ok, detail = check_json(path)
        if not ok:
            failures.append(f"invalid {rel}: {detail}")

    skills_root = root / "skills"
    for name in REQUIRED_SKILLS:
        path = skills_root / name / "SKILL.md"
        if not path.exists():
            failures.append(f"missing skill: {name}")
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if not text.startswith("---"):
            failures.append(f"missing YAML frontmatter: {path.relative_to(root)}")
        if f"name: {name}" not in text[:1000]:
            failures.append(f"skill name mismatch: {path.relative_to(root)}")

    example = root / ".fde-os" / "config.local.example.yaml"
    if not example.exists():
        failures.append("missing .fde-os/config.local.example.yaml")

    local = root / ".fde-os" / "config.local.yaml"
    if local.exists() and not gitignored(root, ".fde-os/config.local.yaml"):
        warnings.append("local config exists but is not gitignored")

    required_dirs = [
        "docs/fde/engagements",
        "docs/fde/solutions",
        "docs/fde/patterns",
        "docs/fde/pulse-reports",
    ]
    for rel in required_dirs:
        if not (root / rel).exists():
            warnings.append(f"missing project directory: {rel}")

    for script in root.glob("**/*.py"):
        try:
            source = script.read_text(encoding="utf-8")
            compile(source, str(script), "exec")
        except (OSError, SyntaxError, UnicodeError) as exc:
            failures.append(f"Python compile failed: {script.relative_to(root)}: {exc}")

    print("\nOptional capabilities")
    for tool in OPTIONAL_TOOLS:
        print(f"  {'OK' if shutil.which(tool) else '--'} {tool}")

    print("\nRequired checks")
    if failures:
        for item in failures:
            print(f"  FAIL {item}")
    else:
        print("  OK all required checks passed")

    if warnings:
        print("\nProject setup warnings")
        for item in warnings:
            print(f"  WARN {item}")

    print("\nResult:", "FAILED" if failures else "HEALTHY")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
