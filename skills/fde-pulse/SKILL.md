---
name: fde-pulse
description: Produce a time-windowed production pulse report showing what users and the business actually experienced after an FDE deployment, including adoption, outcomes, failures, overrides, escalations, cost, latency, incidents, and drift. Use after deployment or for periodic operational review. Not for substituting projections when production data is unavailable.
argument-hint: "[engagement path] [window:7d|30d|quarter|custom]"
---

# FDE Production Pulse

## Outcome

Create a production evidence report under:

`docs/fde/pulse-reports/<date>-<engagement-slug>-pulse.md`

and feed verified findings back into the engagement and improvement backlog.

## Phase 0: Resolve window and sources

Use the requested time window, project config, or default 30 days. Identify authorized sources for:

- workflow and agent traces
- human reviews and overrides
- incidents and support tickets
- model and tool costs
- latency and reliability
- adoption and usage
- business KPIs
- qualitative user feedback

If production data is unavailable, produce a data-gap report rather than an invented pulse.

## Phase 1: Compare to contract

Compare actual experience with:

- deployment-stage entry and exit criteria
- evaluation thresholds
- cost and latency budgets
- expected human workload
- business-value hypothesis
- risk and incident assumptions

## Phase 2: Analyze outcomes

Report:

- volume and completion
- accuracy or quality proxies
- escalation, rejection, edit, override, and manual-fallback rates
- failure categories and recurrence
- cost per successful outcome
- median and tail latency
- uptime and tool/integration failures
- user adoption, abandonment, and workarounds
- business metrics and uncertainty
- incidents and near misses
- drift in data, behavior, policy, or workflow

Segment by user, workflow variant, risk class, data source, model/tool version, and exception class when useful.

## Phase 3: Decisions

Recommend one or more:

- continue current stage
- increase autonomy
- decrease autonomy
- pause or rollback
- improve data or deterministic controls
- revise prompt, model, tool, workflow, training, or policy
- expand the pilot
- stop the intervention

Every recommendation must name evidence, owner, and review date.

## Phase 4: Update durable knowledge

- link the pulse from the engagement dossier;
- update metrics, risks, incidents, and decision log;
- add failed production cases to regression datasets;
- identify one-learning candidates for `/fde-compound`;
- route material redesign back to discovery, mapping, prioritization, design, or evaluation.

## Output

End with report path, production verdict, autonomy recommendation, business-value status, critical incidents or drift, next review window, and recommended next skill.