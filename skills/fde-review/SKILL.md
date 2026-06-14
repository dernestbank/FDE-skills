---
name: fde-review
description: Run report-only independent reviews of an FDE engagement, workflow map, opportunity decision, architecture, evaluation plan, deployment plan, or production change. Use before material readiness transitions or when the user requests critique. Not for silently editing the reviewed artifact; findings are applied only by the owning workflow with authorization.
argument-hint: "[engagement or artifact path] [focus:workflow|process|architecture|evaluation|security|adoption|deployment|all]"
---

# Independent FDE Review

## Outcome

Produce a source-linked review report without mutating the reviewed artifact.

## Phase 0: Intake

Identify:

- reviewed artifact and readiness
- requested focus
- decision the review must inform
- applicable risk and scope tier
- evidence package

Reject review theater: if the evidence package is absent, report that the review cannot establish readiness.

## Reviewer selection

Use the smallest set appropriate to the decision:

- workflow evidence -> workflow researcher
- process choice -> process challenger
- future-state architecture -> architecture reviewer
- evaluation readiness -> evaluation reviewer
- sensitive data, permissions, external writes, or abuse -> security reviewer
- changed human roles or approval workload -> adoption reviewer
- production rollout or autonomy -> deployment reviewer

Prompt assets live in `../fde-os/references/agents/`.

## Independent dispatch

Each reviewer receives:

- bounded mandate
- artifact and evidence paths
- relevant claim labels
- excluded decisions
- severity scale
- required output
- instruction not to edit canonical artifacts

When parallel or isolated agents are unavailable, run reviews serially with separate contexts. Preserve each initial verdict before reconciliation.

## Severity

- `BLOCKING` — cannot advance readiness without resolution or formal risk acceptance
- `HIGH` — material failure, value, security, adoption, or operability risk
- `MEDIUM` — important weakness with a viable mitigation
- `LOW` — improvement that does not block the current decision
- `NOTE` — observation or implementation-time consideration

## Reconciliation

The review coordinator:

1. deduplicates findings without erasing distinct rationales;
2. preserves reviewer disagreement;
3. checks that each finding cites evidence or is labeled as a hypothesis;
4. identifies the responsible owner and required response;
5. produces a verdict for the specific gate, not for the project in general.

## Durable output

Write a timestamped report under:

`docs/fde/engagements/<slug>/reviews/<date>-<focus>-review.md`

Include:

- scope and evidence reviewed
- reviewers and review limitations
- findings by severity
- disagreements
- required responses
- residual risks and accepting owners
- gate verdict: approve, conditionally approve, reject, or insufficient evidence

Do not directly modify the engagement dossier beyond linking the review and recording its status when authorized.

## Handoff

End with review path, blocking findings, gate verdict, owner actions, and the owning skill that should apply accepted changes.