# Deployment Rollout Playbook

## Objective

Move from evaluation evidence to production through controlled, reversible stages.

## Stages

1. Historical replay
2. Sandbox
3. Shadow mode
4. Recommendation mode
5. Approval mode
6. Bounded autonomy
7. Conditional autonomy
8. Monitored production

## For each stage define

- purpose
- allowed users and data
- permitted actions
- entry criteria
- exit criteria
- responsible approver
- monitored metrics
- incident owner
- pause and rollback triggers
- expected duration or sample size

## Default controls

- least-privilege credentials
- isolated environment where possible
- immutable action logs
- spend and rate limits
- timeout and retry policies
- idempotency keys
- human escalation
- kill switch
- rollback procedure
- version pinning

## Readiness review

Confirm:

- evaluation thresholds passed
- critical failure controls verified
- data and security approvals completed
- workflow owner accepts the future-state process
- users are trained
- human-review capacity is sufficient
- support and incident ownership is assigned
- baseline and production metrics are available
- rollback has been tested

## Rollback triggers

- critical policy violation
- security event
- material accuracy decline
- data-quality drift
- tool or integration failure spike
- excessive override or escalation
- spend or latency beyond approved limits
- negative business KPI movement

## Outputs

- deployment plan
- stage-gate checklist
- operating runbook
- monitoring dashboard specification
- incident and rollback runbooks
- ownership matrix

## Quality checks

- Is autonomy proportional to evidence?
- Can every production action be traced?
- Can the system be paused rapidly?
- Are humans prepared for escalations?
- Is there a clear owner after launch?
