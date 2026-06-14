---
name: fde-setup
description: Diagnose FDE OS plugin health, project structure, optional tool capabilities, local configuration, and artifact directories. Use after installation, after an update, or when skills cannot find their expected files. Not for starting a client engagement; use fde-start after setup.
disable-model-invocation: true
---

# FDE OS Setup

This is a lightweight health check and project initializer. Missing optional tools are capabilities, not failures.

## Phase 1: Diagnose

1. Resolve the current project root. Prefer the git root when available; otherwise use the current workspace.
2. Determine the installed FDE OS version from `.claude-plugin/plugin.json` when readable.
3. Run `scripts/check_health.py` from this skill directory. The user's working directory is not the skill directory; resolve the absolute skill path first.
4. Display the diagnostic output.

The check covers:

- plugin and marketplace metadata
- required skill directories and `SKILL.md` files
- Python availability and script compilation
- JSON/YAML parseability where supported
- `.fde-os/config.local.example.yaml`
- whether `.fde-os/config.local.yaml` is safely gitignored
- `docs/fde/engagements`, `docs/fde/solutions`, `docs/fde/patterns`, and `docs/fde/pulse-reports`
- optional git, Python, Node, Docker, MCP, browser, database, and diagram capabilities

## Phase 2: Offer bounded fixes

Ask before changing tracked project files.

Offer only relevant fixes:

- refresh `.fde-os/config.local.example.yaml` from `references/config-template.yaml`
- create `.fde-os/config.local.yaml` with all preferences commented out
- append `.fde-os/*.local.yaml` to `.gitignore`
- create missing `docs/fde/` directories
- create a minimal `CONCEPTS.md` only when absent

Never overwrite a populated local config, glossary, or `.gitignore`.

## Phase 3: Summary

Report:

- version
- required checks passed or failed
- fixes applied and declined
- optional capabilities present or missing
- recommended next command

When setup passes, recommend `/fde-start` for a new engagement or `/fde-os` for routing.