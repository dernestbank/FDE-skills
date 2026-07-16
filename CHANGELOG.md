# Changelog

## 0.2.0 - 2026-07-22

### Architecture

- Replaced the monolithic FDE prompt with a focused `fde-os` router and fifteen outcome-owned skills, including a read-only engagement status skill.
- Added explicit setup, build, review, production pulse, compounding, and handoff skills.
- Moved version 0.1 root agents and commands under `legacy/` to prevent duplicate active interfaces.
- Converted the Claude plugin manifest to metadata-only discovery and added a marketplace source manifest.
- Added task-shape model tiers and skill-local specialist prompt assets.

### Durable knowledge

- Added the canonical `fde-engagement/v1` dossier contract and evidence-backed readiness states.
- Added resume-before-duplicate behavior and Lightweight, Standard, and Deep scope tiers.
- Added decision, evidence, claim-label, engagement, and compounded-solution contracts.
- Added `fde-solution/v1` and one-learning-per-run compounding behavior.
- Added production pulse reports and source-linked handoffs.

### Safety and operations

- Added isolated workflow, process, architecture, evaluation, security, adoption, and deployment review prompts.
- Added privacy-aware audit logging with recursive secret redaction and response summarization.
- Reworked completion validation around the active engagement and advanced-readiness evidence.
- Added staged autonomy, meaningful human-control, prompt-injection, rollback, and ownership rules.
- Converted the unfinished MCP runtime configuration into a non-active example.

### Distribution and developer experience

- Added `/fde-setup` diagnostics, local config templates, and gitignore rules.
- Added Claude Code and ChatGPT packaging guidance.
- Added a Custom GPT system instruction package, example OpenAPI Actions schema, and MCP tool contract.
- Added architecture inspiration notes and a comprehensive skill catalog.
- Added routing, adversarial, structural, privacy, and hook regression tests.

## 0.1.0 - 2026-07-22

- Added comprehensive FDE OS core skill.
- Added lifecycle playbooks and reusable templates.
- Added project, workflow, opportunity, evaluation, deployment, and incident schemas.
- Added specialist Claude agents and slash commands.
- Added starter deterministic hooks and validation scripts.
- Added Claude plugin and MCP configuration placeholders.
- Added initial sustainability data-intake example.
