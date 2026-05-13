---
name: fde-build
description: Implement an approved FDE future-state design as production-quality workflow code, deterministic services, integrations, agent tools, schemas, observability, human-review surfaces, and tests. Use after design review when the user wants implementation. Not for inventing product behavior, changing approved scope, or declaring deployment readiness without evaluation.
argument-hint: "[engagement or design path] [mode:return-to-caller optional]"
---

# Build the Approved FDE System

## Outcome

Implement the approved design, locally verify it, and return evidence for `/fde-evaluate` without mutating approved product decisions silently.

## Phase 0: Input triage

1. Resolve the engagement dossier and design artifacts.
2. Verify readiness is `design-ready` or record the explicit exception authorizing a prototype.
3. Read scope boundaries, human authority, tool contracts, evaluation contract, blocking review findings, and implementation-time unknowns.
4. If the build prompt conflicts with approved scope, stop and route the decision back to `/fde-design`.

## Execution modes

### Standalone
Own implementation, local verification, artifact updates, and the handoff to evaluation.

### Return-to-caller
When invoked with `mode:return-to-caller`, implement and locally verify only, then return a structured envelope to the outer orchestrator. Do not run deployment or stakeholder reporting.

## Build requirements

Implement proportionately:

- typed inputs and structured outputs
- deterministic validation before and after model calls
- least-privilege tool and data access
- idempotency for repeated or retried operations
- timeouts, retries, fallbacks, and circuit breakers
- human approval, rejection, edit, escalation, and override paths
- provenance and audit traces
- prompt, policy, model, tool, and schema versions
- secrets management and configuration separation
- cost, rate, and latency controls
- observability and failure classification
- fixtures and automated tests

Use the existing technology stack and project conventions where suitable. Do not force migration merely because a different stack is easier for the agent.

## Implementation units

Work through coherent units derived from the design. For each unit:

1. inspect existing patterns;
2. implement the smallest complete behavior;
3. test the normal path and material failure paths;
4. validate permissions and audit output;
5. record unresolved implementation-time unknowns;
6. avoid broad adjacent refactors unless required for correctness.

## Scope and decision policy

- The design artifact owns product and workflow decisions.
- Code and tests own implementation progress.
- Do not edit approved decisions to make the implementation appear compliant.
- When execution disproves a design assumption, document the evidence and route it back to design.
- Never fabricate a tool response, integration success, or production result.

## Local verification

At minimum run:

- schema and type checks
- unit and integration tests
- failure and retry tests
- permission/authorization tests
- audit-trace checks
- human-review flow checks
- lint/build checks appropriate to the repository

Do not claim evaluation readiness from local tests alone.

## Durable outputs

Update implementation references in the dossier without changing readiness automatically. Record:

- code and configuration paths
- versions and migrations
- tests run and results
- implementation deviations
- unresolved unknowns
- new risks and decision records
- evaluation fixtures produced

## Completion contract

Return:

- implemented units
- files changed
- verification performed
- deviations from design
- unresolved questions and risks
- evaluation assets available
- next valid skill `/fde-evaluate`

In Return-to-caller mode, return the same fields as a compact structured envelope.