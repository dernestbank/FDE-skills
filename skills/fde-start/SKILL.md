---
name: fde-start
description: Start or resume one coherent Forward Deployed Engineering engagement, establish authority and scope, and create the canonical FDE engagement dossier. Use for a new client, department, workflow, AI transformation project, or when resuming an existing engagement. Not for detailed workflow interviews; hand off to fde-discover after intake.
argument-hint: "[organization, workflow, business problem, or existing dossier path]"
---

# Start or Resume an FDE Engagement

## Outcome

Create or resume:

`docs/fde/engagements/<slug>/ENGAGEMENT.md`

with `artifact_contract: fde-engagement/v1` and readiness `intake`.

## Phase 0: Resume check

1. Search `docs/fde/engagements/` for an obvious matching dossier.
2. If the user supplied a path, read it first.
3. Resume a match rather than creating a duplicate unless the user explicitly needs a separate coherent outcome.
4. Preserve approved decisions, evidence, disputes, and readiness.

## Phase 1: Coherent-work gate

Determine whether the request contains more than one independently valuable and testable business outcome. Shared stakeholders or systems do not make separate outcomes one engagement.

When several outcomes exist:

- propose a plain-language breakdown;
- choose the current engagement from user context when already clear;
- otherwise ask which outcome this dossier owns;
- record the surrounding outcomes without making them active scope.

## Phase 2: Intake

Establish only the information required to authorize discovery:

- organization or confidential label
- department and workflow boundary
- business outcome and customer
- sponsor, project owner, workflow owner, and decision authority
- initial scope and exclusions
- known systems and data sensitivity
- legal, regulatory, security, timing, and budget constraints
- baseline and success hypotheses
- available evidence and access requests

Use one decision-bearing question at a time when interactive discovery is necessary. Do not turn intake into the full workflow interview.

## Scope tier

Classify:

- Lightweight
- Standard
- Deep

Deep includes high consequence, regulated data, cross-functional scope, unclear authority, or proposed high autonomy.

## Write the dossier

Read `../fde-os/references/artifact-contract.md` before writing.

Create the dossier plus an `artifacts/` directory. Write the dossier path to `.fde-os/active-engagement` so hooks and later skills can resolve the active engagement. At minimum populate:

- Goal capsule
- Scope boundaries
- Stakeholders and authority
- Evidence registry
- Baseline and success hypotheses
- Risks, assumptions, disputes, and unknowns
- Decision log
- Next gate

Do not invent missing names, metrics, systems, or authority. Mark them `UNKNOWN`.

## Exit gate

Readiness remains `intake` until the coherent outcome, owner or owner gap, scope, initial authority, constraints, and discovery access needs are recorded.

## Handoff

End with:

- dossier path
- scope tier
- readiness
- missing authority or access
- immediate risks
- recommended next skill: `/fde-discover`

When intake reveals that no discovery is warranted, explain why and route to the appropriate later skill without fabricating readiness.