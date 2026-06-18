---
name: fde-status
description: Summarize the active or specified FDE engagement, including readiness, evidence coverage, settled decisions, blockers, review findings, current implementation or deployment state, and the next valid skill. Use when the user asks where the project stands, what remains, or how to resume. Not for advancing readiness or changing approved decisions.
argument-hint: "[engagement path optional]"
---

# FDE Engagement Status

## Outcome

Provide a concise, source-linked view of the engagement without changing its lifecycle state.

## Resolve the engagement

1. Use a user-provided dossier path when present.
2. Otherwise read `.fde-os/active-engagement`.
3. If no active pointer exists, search `docs/fde/engagements/` for an obvious match.
4. When no engagement can be resolved, route to `/fde-start` rather than inventing project state.

## Read

- dossier frontmatter and readiness
- Goal capsule and scope
- evidence registry
- assumptions, disputes, unknowns, and risks
- decision log
- linked structured artifacts
- independent reviews and blocking findings
- build, evaluation, deployment, pulse, and incident records when present
- recent handoffs

Prefer approved artifacts over chat history. Identify stale links, missing files, and version conflicts.

## Report

Return:

1. engagement and canonical dossier path;
2. coherent outcome and scope tier;
3. current readiness and evidence supporting it;
4. completed lifecycle work;
5. settled decisions and responsible owners;
6. blockers, disputes, missing evidence, and expired assumptions;
7. open reviews, approvals, incidents, or rollback conditions;
8. current implementation, evaluation, or deployment state;
9. next valid skill and why;
10. one recommended immediate action.

## Rules

- Do not promote readiness because expected files merely exist.
- Do not treat a planned metric as a measured result.
- Do not close risks or reviews without authorized evidence.
- Do not rewrite the dossier unless the user separately requests an update through the owning skill.
- If the dossier's declared readiness exceeds its evidence, flag the mismatch and recommend the owning skill or review needed to correct it.
- Keep status output compact enough to resume work quickly; link detailed artifacts rather than reproducing them.
