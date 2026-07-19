# FDE OS Architecture

## Design goal

FDE OS is a portable Forward Deployed Engineering methodology with optional platform adapters and execution infrastructure. The core must remain useful without a backend, while production deployments move identity, authority, state, audit, evaluation, and enterprise actions into deterministic services.

## Layers

### 1. User-invoked skills

Location: `skills/<name>/SKILL.md`

Responsibilities:

- recognize a clear user outcome
- enforce prerequisites and contraindications
- coordinate the workflow
- load detailed references only when needed
- write or update durable artifacts
- produce an explicit handoff

The root `fde-os` skill routes rather than attempting to contain every procedure.

### 2. Skill-local references and prompt assets

Locations:

- `skills/<name>/references/`
- `skills/fde-os/references/agents/`

Responsibilities:

- lifecycle gates
- artifact contracts
- interaction methods
- rubrics and checklists
- specialist review prompts
- platform mappings
- solution templates

References are loaded progressively. Specialist assets run in isolated context and return report-only findings to the owning skill.

### 3. Deterministic controls

Locations:

- `scripts/`
- `skills/*/scripts/`
- `hooks/`
- `tests/`

Responsibilities:

- setup diagnostics
- JSON/schema checks
- scoring and metric calculations
- workflow validation
- privacy-aware audit logging
- destructive-operation screening
- readiness completion checks
- regression tests

Use code when the desired behavior is deterministic and testable.

### 4. Durable project knowledge

Locations:

- `docs/fde/engagements/`
- `docs/fde/solutions/`
- `docs/fde/patterns/`
- `docs/fde/pulse-reports/`
- `docs/fde/handoffs/`
- `CONCEPTS.md`

Responsibilities:

- preserve evidence and provenance
- record settled decisions and disagreement
- expose readiness and gates
- support session and team resumption
- retain production outcomes
- compound verified reusable learning

The conversation is an interaction surface, not the source of truth.

### 5. Platform packages

Locations:

- `.claude-plugin/`
- `platforms/claude/`
- `platforms/chatgpt/`

Responsibilities:

- platform metadata
- installation and publication guidance
- platform-specific instruction packaging
- Custom GPT Actions example
- ChatGPT App/MCP contracts

Platform packages may rename tools and interaction primitives, but cannot weaken authority, evidence, or readiness policy.

### 6. Execution backend

Planned location: separate `fde_os_mcp` or product repository.

Responsibilities:

- identity and role-based access
- organizations, projects, and tenancy
- versioned artifact storage
- enterprise connectors
- evaluation workers
- human-review queues
- deployment controls
- metrics and reporting
- durable audit and retention

The current `mcp/` directory contains a design example only.

## Runtime flow

```text
User request
  -> fde-os routing and prerequisite check
  -> outcome-owned skill
       -> read canonical dossier
       -> load gated references
       -> read authorized evidence
       -> ask only decision-bearing questions
       -> optionally dispatch isolated specialists
       -> reconcile findings
       -> write or update durable artifacts
       -> validate gate
       -> return handoff and next skill
  -> optional fde-compound after verified learning
```

## Engagement lifecycle

```text
intake
  -> discovery-grounded
  -> mapped
  -> prioritized
  -> design-ready
  -> evaluation-ready
  -> deployment-ready
  -> operational
```

Build activity occurs between design and evaluation but does not create a readiness state by itself. Local implementation success is not evaluation evidence.

## Active versus legacy

Active:

- `skills/`
- `hooks/`
- `.claude-plugin/`
- platform packages
- deterministic scripts and tests

Legacy:

- `legacy/agents/`
- `legacy/commands/`

Legacy files preserve version 0.1 context and migration history. They are not canonical and should not be restored to active root locations.

## Key invariants

1. One coherent independently valuable outcome per engagement dossier.
2. Resume existing artifacts before creating duplicates.
3. Evidence and claims retain provenance and labels.
4. A simpler non-AI intervention is always considered.
5. Human control must be meaningful, not ceremonial.
6. Specialists do not silently edit canonical artifacts.
7. Build does not self-approve evaluation or deployment.
8. External writes require backend authorization and project policy.
9. Production autonomy is staged, monitored, and reversible.
10. Verified learning is compounded one lesson at a time.