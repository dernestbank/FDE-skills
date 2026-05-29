---
name: fde-evaluate
description: Create and run evidence-based evaluations for deterministic components, model tasks, agent trajectories, end-to-end workflows, human escalation, cost, latency, reliability, and business outcomes. Use after design or when validating an existing AI workflow. Not for treating a demo or a few successful examples as deployment evidence.
argument-hint: "[engagement path, system, dataset, evaluation question, or result files]"
---

# Evaluate the System

## Outcome

Produce an evaluation contract and report that support an honest readiness decision.

## Preconditions

- task and business outcome are defined;
- expected behavior, human control, and failure handling are designed;
- representative evidence can be obtained or its absence is acknowledged.

If the design is not testable, route back to `/fde-design`.

## Phase 1: Baseline and claims

Record:

- current human or software baseline
- intended improvement
- consequential failure classes
- cost and latency budgets
- claims the evaluation must support

Every result must remain labeled `MEASURED`, `ESTIMATED`, or `UNKNOWN`.

## Phase 2: Dataset strategy

Create or identify:

- golden dataset
- edge-case dataset
- adversarial dataset
- regression dataset
- production-sampled dataset when permitted
- human-disagreement dataset for subjective or judgment tasks

For each case record source, representativeness, sensitivity, expected outcome, reviewer, severity, and tags. Prevent train/test leakage and over-representation of the happy path.

## Phase 3: Evaluation layers

### Component
Schema validation, parsing, transformations, APIs, database operations, policy rules, and deterministic calculations.

### Model task
Extraction, classification, groundedness, relevance, completeness, format, citation, and uncertainty.

### Agent trajectory
Tool selection, argument correctness, sequencing, authorization, intermediate validation, retry, recovery, escalation, and final action.

### Workflow
End-to-end completion, cycle time, handoffs, rework, human interventions, and business-rule compliance.

### Business
Revenue, cost, risk, quality, capacity, customer outcome, compliance, and adoption.

## Phase 4: Thresholds

Define:

- target and minimum threshold
- critical-case zero-tolerance rules
- acceptable escalation and override rates
- confidence calibration policy
- cost and latency limits
- stability and regression policy
- owner authorized to approve the threshold

Do not select thresholds after seeing results merely to create a pass.

## Phase 5: Run and analyze

Use deterministic scripts for metrics where possible. Categorize failures by root cause rather than reporting one aggregate pass rate.

Investigate:

- missing or bad data
- wrong record or tool
- unsupported inference
- policy violation
- incomplete action
- human disagreement
- integration failure
- timeout, retry, or idempotency failure
- cost or latency violation

For Standard or Deep evaluations, invoke the independent evaluation reviewer before declaring readiness.

## Durable outputs

Update:

- dossier Evaluation contract and results
- `artifacts/evaluation-plan.json`
- `artifacts/evaluation-report.json`
- dataset and case manifests
- failure taxonomy
- regression set
- decision and risk logs

## Exit gate

Set readiness to `evaluation-ready` only when required thresholds are met, critical failures are controlled, escalation works, costs are acceptable, limitations are documented, and the authorized owner approves.

Failing an evaluation is useful evidence. Do not hide it or silently narrow the claim.

## Handoff

End with measured results, failure categories, limitations, gate verdict, owner decision, and next valid skill `/fde-deploy` or `/fde-design`.