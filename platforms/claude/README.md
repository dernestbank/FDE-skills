# Claude Code Packaging for FDE OS

## Canonical plugin shape

```text
.claude-plugin/
├── plugin.json
└── marketplace.json
skills/
├── fde-os/
├── fde-setup/
├── fde-start/
└── ...
hooks/
legacy/
```

Claude Code discovers the user-facing skills from `skills/<name>/SKILL.md`. Detailed procedures, prompt assets, and scripts remain inside the owning skill directory.

The active plugin intentionally has no root `agents/` or `commands/` directories. Version 0.1 files are archived under `legacy/` so they do not compete with the skill-first interface.

## Local development

1. Open or load this directory as a local plugin source using the mechanism supported by the installed Claude Code version.
2. Run `/fde-setup`.
3. Address required failures before starting an engagement.
4. Create `.fde-os/config.local.yaml` only for machine-local preferences.
5. Run `/fde-start`.

## Marketplace publication

`.claude-plugin/marketplace.json` declares this repository as a marketplace source with plugin source `./`. Before publishing:

- replace local repository details as needed;
- confirm plugin and marketplace versions match;
- run health checks and tests;
- ensure no local configuration or audit data is committed;
- review skill names and descriptions for clean invocation;
- test installation in a clean project.

## Hooks

Active hooks provide narrow defense-in-depth:

- pre-tool destructive-operation screening
- privacy-aware tool audit logging
- advanced-readiness completion checks

The hooks require a `python` command available to Claude Code. They do not replace backend authorization, project isolation, or production controls.

## Specialist work

The preferred architecture is:

- user invokes a skill;
- the skill loads only relevant references;
- the skill dispatches a specialist prompt asset in isolated context when a review or research gate fires;
- the specialist returns a report-only result;
- the owning skill reconciles and writes durable artifacts.

This avoids permanently loading every specialist role and keeps the user-facing interface compact.

## MCP

The skills do not require MCP. The `mcp/` directory contains a design example only until an actual `fde_os_mcp` server is implemented and tested. Do not enable the example as a runtime server prematurely.

## Cross-platform source of truth

Claude-specific packaging is only one distribution. The portable methodology remains in `skills/`; do not fork the lifecycle or artifact contract in platform-specific files.