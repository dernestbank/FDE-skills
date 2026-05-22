---
name: fde-design
description: Design the future-state operating model, deterministic and AI boundaries, human authority, data and tool contracts, enterprise architecture, observability, failure recovery, and evaluation/deployment hypotheses for a prioritized FDE pilot. Use after opportunity prioritization or when an approved pilot needs a complete system design. Not for claiming readiness without independent review and evaluation.
argument-hint: "[engagement path, selected pilot, architecture question, or design constraint]"
---

# Design the Human-Supervised System

## Outcome

Create a design that is proportionate to the selected pilot and advance readiness toward `design-ready` only after required review.

## Preconditions

- dossier readiness is `prioritized`;
- selected pilot, value hypothesis, scope, important exceptions, and owner are known;
- unresolved prerequisites are explicit.

## Phase 1: Future-state workflow

For each changed step, assign one primary execution type:

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

Explain why the selected type is superior to simpler alternatives.

## Phase 2: Human authority

Choose the lowest safe control level:

0. Human-only
1. AI assistance
2. AI recommendation
3. Human approval
4. Supervised autonomy
5. Conditional autonomy
6. Monitored autonomy

Define:

- accountable owner
- action authority
- approval and rejection behavior
- edit-and-approve behavior
- low-confidence route
- exception route
- override and appeal
- workload limits and sampling
- autonomy increase and decrease conditions

A human click is not meaningful control when the person lacks time, information, or authority to review.

## Phase 3: Component contracts

For every component define:

- business purpose
- allowed inputs and provenance
- structured output schema
- deterministic validations
- tools and least-privilege permissions
- model selection criteria
- state and memory
- confidence and uncertainty policy
- idempotency, retries, timeouts, fallbacks, and circuit breakers
- audit, retention, cost, and latency limits
- failure behavior and rollback
- evaluation method

## Phase 4: Architecture

Include:

- user and review interfaces
- orchestration
- deterministic services
- model/inference layer
- tool and enterprise integrations
- system-of-record boundaries
- data stores and queues
- identity, authorization, secrets, and tenant isolation
- observability and evaluation
- human review
- deployment environment
- incident and recovery paths

Prefer enhancing existing systems over requiring migration unless migration is itself the approved business decision.

## Phase 5: Design package

Produce:

- future-state workflow
- architecture diagram and narrative
- data and tool contracts
- human-control matrix
- trust boundaries and security assumptions
- failure-mode and recovery table
- evaluation contract
- staged-deployment hypothesis
- implementation units and implementation-time unknowns

## Phase 6: Independent review

For Standard or Deep work, route the design through `/fde-review`. At minimum:

- architecture review
- evaluation review
- security review for sensitive data or external writes
- adoption review when human work changes materially
- deployment review for production systems

Do not self-approve blocking findings. Record responses, accepted residual risk, and responsible owners.

## Durable outputs

Update:

- dossier Future-state operating model
- Architecture and integrations
- Human authority and escalation
- Evaluation contract
- Risks, assumptions, disputes, and unknowns
- `artifacts/workflow-future.json`
- `artifacts/solution-design.json`
- `artifacts/tool-contracts.json`
- decision log

## Exit gate

Set readiness to `design-ready` only after the design is complete enough to evaluate, material independent reviews are recorded, and blocking findings are resolved or formally accepted by authorized owners.

## Handoff

End with design paths, review status, blocking findings, implementation-time unknowns, readiness verdict, and next valid skill `/fde-build` when the design gate passes. Route to `/fde-review` first when required reviews are still outstanding.