# FDE OS

**Forward Deployed Engineering skills for discovering real workflows, designing the right AI system, proving it with evaluations, deploying it safely, and compounding the learning.**

## Philosophy

Every FDE engagement should make the next engagement easier.

Traditional AI consulting repeatedly rediscovers the same workflow patterns, exception classes, integration constraints, evaluation methods, and adoption failures. FDE OS turns each engagement into durable project knowledge:

`setup -> start -> discover -> map -> prioritize -> design -> review -> build -> evaluate -> deploy -> pulse -> compound`

The goal is not to maximize AI usage. The goal is to create measurable business improvement with the safest and simplest combination of process redesign, deterministic software, AI judgment, agents, and human authority.

## Primary skills

| Skill | Purpose |
|---|---|
| `/fde-setup` | Diagnose the project environment and initialize local configuration |
| `/fde-start` | Start or resume an engagement and create the durable engagement dossier |
| `/fde-discover` | Investigate the real workflow, stakeholders, systems, data, exceptions, and incentives |
| `/fde-map` | Produce evidence-linked current-state workflow, system, data, and decision maps |
| `/fde-prioritize` | Rank improvement opportunities and select a risk-adjusted pilot |
| `/fde-design` | Design the future-state human/AI/deterministic operating model and architecture |
| `/fde-build` | Implement the approved design with production controls and local verification |
| `/fde-review` | Run independent business, security, evaluation, and adoption reviews |
| `/fde-evaluate` | Build datasets, metrics, acceptance thresholds, and readiness evidence |
| `/fde-deploy` | Plan and manage staged deployment, monitoring, rollback, and ownership |
| `/fde-pulse` | Report what users and the business actually experienced in production |
| `/fde-compound` | Capture one durable learning into the reusable FDE knowledge base |
| `/fde-handoff` | Create a compact, resumable session or team handoff |
| `/fde-status` | Show current readiness, evidence, decisions, blockers, and next action |
| `/fde-report` | Generate audience-specific reports from approved project artifacts |
| `/fde-os` | Route an FDE request to the right skill and enforce lifecycle rules |

## Durable engagement artifact

All core skills enrich one canonical engagement dossier rather than creating disconnected documents:

`docs/fde/engagements/<engagement-slug>/ENGAGEMENT.md`

The dossier declares:

```yaml
artifact_contract: fde-engagement/v1
artifact_readiness: intake | discovery-grounded | mapped | prioritized | design-ready | evaluation-ready | deployment-ready | operational
```

Structured evidence lives beside it in `artifacts/`. The conversation is never the source of truth.

## Compounding knowledge

Reusable knowledge is stored under:

- `docs/fde/solutions/` — solved deployment problems and patterns
- `docs/fde/patterns/` — reusable workflow, architecture, evaluation, and adoption patterns
- `docs/fde/pulse-reports/` — production outcome reports
- `CONCEPTS.md` — canonical FDE OS vocabulary

`/fde-compound` records one learning per run, with provenance, applicability boundaries, failure signals, and related patterns.

## Installation and use

### Claude Code

Open this repository as a plugin or publish it as a marketplace source. After installation, run:

```text
/fde-setup
/fde-start <engagement description>
```

### ChatGPT and other Agent Skills hosts

The `skills/*/SKILL.md` directories are the portable source of truth. Platform-specific notes live in `platforms/`.

### Local development

1. Run `/fde-setup`.
2. Review `.fde-os/config.local.example.yaml`.
3. Create `.fde-os/config.local.yaml` only for machine-local preferences.
4. Keep the local config gitignored.
5. Run the deterministic validators in `scripts/` and `tests/`.

## Design rules

1. Evidence before autonomy.
2. Observe reality before redesigning it.
3. Simplify before automating.
4. Prefer deterministic software when it is enough.
5. One coherent work unit per engagement artifact.
6. Load detailed references only when their gate fires.
7. Use specialist reviewers in isolated context for material decisions.
8. Distinguish measured, estimated, assumed, and unknown claims.
9. Make handoffs explicit and resumable.
10. Capture durable learning after delivery.

## Documentation

- `docs/ARCHITECTURE.md` — active layers, runtime flow, readiness, and invariants
- `docs/skills/README.md` — complete skill catalog and handoff chain
- `CONCEPTS.md` — canonical terminology
- `INSPIRATION.md` — architectural lessons adopted from the Compound Engineering design study
- `platforms/claude/README.md` — Claude Code packaging
- `platforms/chatgpt/README.md` — Custom GPT and ChatGPT App packaging
- `mcp/README.md` — future MCP execution layer

## Status

Version 0.2 is a methodology and plugin architecture release. The MCP backend and interactive product UI remain separate implementation work.