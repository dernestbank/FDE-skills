---
name: fde-deploy
description: Plan, review, and manage staged deployment of an evaluated human-supervised AI workflow through historical replay, sandbox, shadow, recommendation, approval, bounded autonomy, conditional autonomy, and monitored production. Use for rollout, monitoring, incident, ownership, rollback, or autonomy decisions. Not for bypassing failed evaluations.
argument-hint: "[engagement path, deployment stage, production issue, or rollout constraint]"
---

# Deploy with Controlled Autonomy

## Outcome

Create an operable rollout and advance readiness toward `deployment-ready` or `operational` only when production evidence supports it.

## Preconditions

- design and evaluation artifacts exist;
- critical evaluation failures are controlled;
- authorized owners for business, technical, security, and workflow decisions are known;
- monitoring and rollback can be implemented.

A user request for production does not override failed prerequisites.

## Default progression

1. historical replay
2. sandbox
3. shadow mode
4. recommendation mode
5. approval mode
6. bounded autonomy
7. conditional autonomy
8. monitored production

Choose the lowest stage that can prove the next uncertainty.

## Stage contract

For each stage define:

- purpose and uncertainty tested
- permitted data and actions
- entry criteria
- exit criteria
- owner and approver
- user cohort and volume
- evaluation and business metrics
- alerts and thresholds
- rollback or pause triggers
- support and communication
- duration or minimum evidence volume

## Operability

Define:

- production owner and on-call responsibility
- dashboards and alerts
- runbooks and incident severity
- kill switch and rollback
- data recovery and reconciliation
- versioning and change control
- model, prompt, tool, policy, and dataset provenance
- capacity, rate, cost, and latency limits
- vendor and integration failure behavior
- user support and feedback path

## Human operations

Measure approval time, rejection, edit-and-approve, escalation, override, sampling workload, alert fatigue, and workaround creation. Reduce autonomy when humans cannot review meaningfully.

## Independent review

Before production or increased autonomy, run `/fde-review` with deployment focus. Include security and adoption reviewers when applicable.

## Rollback and pause triggers

At minimum consider:

- critical-case failure
- accuracy or groundedness degradation
- excessive override or escalation
- data-quality drift
- policy or permission violation
- tool or integration failure spike
- cost or latency breach
- security incident
- user harm or unsafe workaround
- business KPI deterioration

## Durable outputs

Update:

- dossier Deployment and operating model
- Human authority and escalation
- Risks and decision log
- `artifacts/deployment-plan.json`
- monitoring and ownership matrix
- runbooks and incident scenarios
- `artifacts/incident-log.json`
- `artifacts/metrics.json`

## Readiness

- Set `deployment-ready` when rollout, controls, ownership, security, monitoring, support, and rollback are approved.
- Set `operational` only after production evidence and an improvement cadence exist.

## Handoff

End with current stage, permitted autonomy, owners, monitored metrics, rollback triggers, open risks, readiness verdict, and next skill `/fde-pulse` after sufficient production evidence.