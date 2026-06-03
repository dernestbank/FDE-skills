# Solution Design Playbook

## Objective

Convert a prioritized opportunity into a future-state workflow and an implementable, testable, least-privilege architecture.

## Design sequence

1. Reconfirm the problem, baseline, target, owner, and constraints.
2. Simplify or remove unnecessary current-state steps.
3. Classify every future-state step.
4. Define human authority and escalation.
5. Define component and data boundaries.
6. Define interfaces and contracts.
7. Define failure behavior and rollback.
8. Define evaluations before implementation.

## Execution classifications

- `HUMAN_ONLY`
- `DETERMINISTIC_RULE`
- `API_CALL`
- `DATABASE_OPERATION`
- `RPA_ACTION`
- `LLM_ASSIST`
- `LLM_DECISION`
- `AGENT_ACTION`
- `HUMAN_APPROVAL`
- `HUMAN_EXCEPTION`
- `NO_LONGER_REQUIRED`

## AI component specification

For every AI component define:

- business purpose
- triggering event
- authorized input
- output schema
- grounding sources
- tool allowlist
- permissions
- model-selection criteria
- prompt and policy versions
- confidence handling
- validation
- failure taxonomy
- fallback
- human-review mode
- audit and retention
- latency and spend limits

## Architecture checklist

Include:

- user and review interfaces
- orchestration and state management
- deterministic services
- model gateway
- tools and integrations
- databases and object storage
- identity, roles, and tenant isolation
- secrets management
- observability and trace storage
- evaluation runner
- queue and retry infrastructure
- deployment topology
- incident and rollback controls

## Design review

Architecture should be independently reviewed by:

- Evaluation Engineer for testability
- Security Reviewer for trust boundaries and misuse
- Adoption Specialist for workflow fit and review burden

## Required outputs

- future-state workflow
- solution architecture
- component specifications
- data and tool contracts
- human-control matrix
- security design
- evaluation plan
- deployment plan
- decision log

## Quality checks

- Is every AI component justified?
- Can deterministic validation surround probabilistic output?
- Are permissions minimal?
- Is every consequential action controlled?
- Can the system recover from duplicate or partial execution?
- Can performance be measured end to end?
