---
name: fde-report
description: Generate an executive, workflow, technical, evaluation, deployment-readiness, value-realization, or incident report from approved FDE artifacts. Use when stakeholders need a decision-ready deliverable. Not for inventing missing evidence or changing readiness through presentation alone.
argument-hint: "[engagement path] [audience:executive|workflow|engineering|security|board] [report:type]"
---

# Generate an FDE Report

## Source policy

The engagement dossier and linked structured artifacts are the source of truth. Chat history may clarify intent but must not override approved artifacts.

Every material claim must remain labeled as measured, observed, documented, stakeholder-reported, estimated, assumed, disputed, or unknown.

## Report types

- engagement charter
- discovery report
- current-state assessment
- opportunity and pilot recommendation
- future-state and technical specification
- independent review report
- evaluation report
- deployment-readiness report
- production pulse or value-realization report
- incident and post-incident report

## Audience adaptation

### Executive or board
Lead with business problem, outcome, evidence, economics, risk, owner, decision required, and recommendation.

### Workflow users
Explain current pain, future behavior, authority, exceptions, review workload, training, support, and feedback.

### Engineering
Include architecture, contracts, integrations, permissions, failure handling, evaluation, operations, and implementation-time unknowns.

### Security, legal, or compliance
Include data flow, trust boundaries, access, retention, model/vendor exposure, logging, reversibility, findings, residual risk, and accepting owner.

## Composition flow

1. Resolve report type and audience from the prompt or dossier context.
2. Read only relevant approved sections and artifacts.
3. Identify contradictions, stale data, and missing evidence before drafting.
4. Preserve scope boundaries and readiness.
5. Include decisions required and responsible owners.
6. Link evidence and source artifacts.
7. State report date and evidence time window.

## Quality rules

- Do not hide negative results, disagreement, or limitations.
- Do not convert opportunity estimates into realized value.
- Do not treat technical completion as adoption or business success.
- Avoid unnecessary implementation detail in executive reports.
- Include enough detail for the target stakeholder to make the named decision.
- Prefer one canonical report over several lightly different versions; create separate reports only for genuinely different audiences or decisions.

## Durable output

Write under the engagement's `reports/` directory using a dated descriptive filename. Link it from the dossier when authorized.

## Completion

Return report path, audience, decision supported, evidence window, readiness represented, and any critical missing evidence.