# FDE OS Skill Catalog

## Recommended chain

```text
/fde-setup
  -> /fde-start
  -> /fde-discover
  -> /fde-map
  -> /fde-prioritize
  -> /fde-design
  -> /fde-review
  -> /fde-build
  -> /fde-evaluate
  -> /fde-deploy
  -> /fde-pulse
  -> /fde-compound
```

The chain is not automatically linear. Skills may stop, loop backward, or remain at the current readiness when evidence is insufficient.

## `/fde-os`

**Use for:** broad FDE requests or uncertain routing.

**Produces:** route, lifecycle gate, durable-artifact requirement, and next valid skill.

**Does not:** run the entire lifecycle as one undifferentiated prompt.

## `/fde-setup`

**Use for:** installation health, updates, missing skills, local config, and optional capabilities.

**Produces:** diagnostic report and bounded setup fixes.

**Does not:** start a client engagement.

## `/fde-start`

**Use for:** a new or resumed organization, workflow, department, or coherent business outcome.

**Produces:** canonical engagement dossier, active-engagement pointer, initial authority, scope, risk, and evidence needs.

**Readiness:** `intake`.

## `/fde-discover`

**Use for:** interviews, observation, documents, examples, systems, data, exceptions, incentives, and baselines.

**Produces:** evidence registry, stated-versus-observed process, systems/data inventories, exceptions, workarounds, and unknowns.

**Readiness:** `discovery-grounded` when evidence is representative.

## `/fde-map`

**Use for:** current-state workflow, system, data, decision, responsibility, exception, and bottleneck maps.

**Produces:** structured current-state artifacts and optional diagrams.

**Readiness:** `mapped` when the map is evidence-linked and important exceptions are represented.

## `/fde-prioritize`

**Use for:** selecting the best process, deterministic, assistive-AI, or agentic intervention.

**Produces:** opportunity inventory, risk-adjusted ranking, economics, selected pilot, rejected alternatives, and decision record.

**Readiness:** `prioritized`.

## `/fde-design`

**Use for:** future-state workflow, architecture, human authority, contracts, permissions, observability, failure handling, and evaluation/deployment hypotheses.

**Produces:** design package and review requests.

**Readiness:** `design-ready` only after applicable independent review.

## `/fde-review`

**Use for:** independent workflow, process, architecture, evaluation, security, adoption, or deployment critique.

**Produces:** timestamped report-only findings and a gate verdict.

**Does not:** silently edit the reviewed artifact.

## `/fde-build`

**Use for:** implementing an approved design.

**Produces:** production-oriented code/configuration, local verification evidence, deviations, risks, and an evaluation handoff.

**Does not:** change approved product decisions or declare deployment readiness.

## `/fde-evaluate`

**Use for:** datasets, component/model/trajectory/workflow/business tests, thresholds, model comparisons, cost, latency, escalation, and regression.

**Produces:** evaluation plan, results, failure taxonomy, regression assets, and readiness verdict.

**Readiness:** `evaluation-ready` only when thresholds and owner approval are satisfied.

## `/fde-deploy`

**Use for:** historical replay, sandbox, shadow mode, recommendation, approval, bounded autonomy, conditional autonomy, monitored production, rollback, and incidents.

**Produces:** deployment stages, monitoring, runbooks, ownership, rollback, support, and autonomy boundaries.

**Readiness:** `deployment-ready` before production; `operational` only with production evidence and improvement cadence.

## `/fde-pulse`

**Use for:** periodic production review.

**Produces:** adoption, outcomes, failures, overrides, escalations, cost, latency, incidents, drift, business metrics, and autonomy recommendation.

## `/fde-compound`

**Use for:** capturing one verified reusable lesson while context is fresh.

**Produces:** one solution/pattern document or a justified update to canonical vocabulary.

**Rule:** one learning per run.

## `/fde-handoff`

**Use for:** session context limits, team transfer, phase separation, or resumption.

**Produces:** compact handoff envelope linked to canonical sources.

## `/fde-status`

**Use for:** seeing where the active engagement stands, what evidence supports readiness, what is blocked, and how to resume.

**Produces:** a compact source-linked status view without changing readiness or decisions.

## `/fde-report`

**Use for:** decision-ready executive, workflow, technical, security, evaluation, deployment, value, or incident reports.

**Produces:** dated audience-specific report without changing readiness through presentation alone.

## Artifact locations

- engagements: `docs/fde/engagements/`
- reviews: inside each engagement
- reports: inside each engagement
- handoffs: `docs/fde/handoffs/`
- production pulse: `docs/fde/pulse-reports/`
- reusable solutions: `docs/fde/solutions/`
- reusable patterns: `docs/fde/patterns/`
- canonical vocabulary: `CONCEPTS.md`
