# FDE Lifecycle and Readiness Gates

Load this reference only when determining the current phase, required evidence, or next valid skill.

## Lifecycle

### 0. Intake
Required evidence:
- coherent business outcome and workflow boundary
- sponsor, project owner, workflow owner, and decision authority
- initial scope and exclusions
- security and regulatory context
- success hypothesis and access needs

Exit readiness: `intake`.

### 1. Discovery and observation
Required evidence:
- stakeholder accounts and representative examples
- systems, communication channels, and data sources
- stated process versus observed behavior
- exceptions, workarounds, incentives, and knowledge dependencies
- baseline metric sources or explicit metric gaps

Exit readiness: `discovery-grounded`.

### 2. Current-state mapping
Required evidence:
- ordered steps with actors, systems, inputs, outputs, decisions, controls, failures, and exceptions
- evidence references and confidence
- system, data, decision, and responsibility views
- unresolved disputes and missing observations

Exit readiness: `mapped`.

### 3. Opportunity prioritization
Required evidence:
- process-elimination and deterministic alternatives considered
- business value, suitability, feasibility, readiness, measurability, time-to-value, and risk scores
- assumptions and sensitivity
- selected pilot and rejected alternatives

Exit readiness: `prioritized`.

### 4. Future-state design
Required evidence:
- execution classification for every changed step
- human-control level and authority
- architecture, data, integration, permissions, trust boundaries, observability, and failure recovery
- independent review findings and responses
- evaluation and deployment hypotheses

Exit readiness: `design-ready`.

### 5. Build and local verification
Required evidence:
- approved design and implementation units
- code, configuration, integrations, schemas, and human-review paths
- local deterministic, permission, failure, and audit-trace tests
- deviations, implementation-time unknowns, and new risks

Building does not itself advance artifact readiness. The design remains `design-ready` until evaluation evidence supports the next transition.

### 6. Evaluation
Required evidence:
- baseline and representative datasets
- golden, edge, adversarial, regression, and disagreement cases as applicable
- component, model-task, trajectory, workflow, and business metrics
- acceptance thresholds, cost and latency budgets, failure taxonomy, and escalation tests
- honest result labels and owner approval

Exit readiness: `evaluation-ready`.

### 7. Deployment readiness
Required evidence:
- approved rollout stages
- training, support, monitoring, incident, rollback, and ownership plans
- data and security approval
- production thresholds and autonomy boundaries

Exit readiness: `deployment-ready`.

### 8. Operation and improvement
Required evidence:
- production traces and business metrics
- adoption, override, escalation, failure, cost, latency, and incident data
- versioned improvements and regression results
- accepted ownership and operating cadence

Exit readiness: `operational`.

## Gate rules

1. Readiness is the strongest state supported by evidence, not the agent's intended next step.
2. Missing critical evidence blocks advancement.
3. A documented risk acceptance may resolve a risk but never converts an unknown into evidence.
4. Approval must come from the role authorized for the decision.
5. A later phase may reveal a false earlier assumption; downgrade readiness when the foundation no longer holds.
6. Do not require heavyweight artifacts for low-risk work when a compact evidence record satisfies the gate.
7. Do not compress high-risk work into a lightweight process because the user wants speed.

## Standard handoff chain

`fde-start -> fde-discover -> fde-map -> fde-prioritize -> fde-design -> fde-review -> fde-build -> fde-evaluate -> fde-deploy -> fde-pulse -> fde-compound`

Skills may loop backward when evidence disproves an assumption.