# FDE Project Knowledge

This directory is the default durable knowledge root when the plugin is used inside its own repository. Consumer projects may configure another root through `.fde-os/config.local.yaml`.

## Directories

### `engagements/`

One directory per coherent FDE outcome:

```text
engagements/<slug>/
├── ENGAGEMENT.md
├── artifacts/
├── evidence/
├── reviews/
├── reports/
├── datasets/
└── runbooks/
```

The engagement dossier is canonical. Supporting structured files contain machine-readable detail.

### `solutions/`

Verified reusable learnings produced by `/fde-compound`. Organize by category:

- workflow
- integration
- architecture
- evaluation
- security
- adoption
- deployment
- economics
- governance

### `patterns/`

Reusable templates or patterns that are broader than one solved incident but not canonical vocabulary.

### `pulse-reports/`

Time-windowed production reports created by `/fde-pulse`.

### `handoffs/`

Compact, source-linked envelopes for another session, engineer, consultant, or agent.

## Data rules

- Do not commit secrets or raw credentials.
- Redact client identity before creating reusable solutions.
- Preserve evidence provenance and claim labels.
- Version approved decisions and readiness changes.
- Keep raw restricted evidence outside the repository when required; store a controlled reference instead.
- Do not treat this directory as a substitute for a production database, identity system, retention policy, or legal recordkeeping system.
