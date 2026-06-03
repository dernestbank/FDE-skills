# Opportunity Prioritization Playbook

## Objective

Select high-value, feasible, measurable, and appropriately controlled opportunities rather than automating whatever appears easiest.

## Step 1: Generate opportunities

Consider:

- eliminate unnecessary work
- simplify or standardize the process
- improve data quality at the source
- connect disconnected systems
- automate deterministic transformations
- assist retrieval, extraction, drafting, or classification
- recommend decisions
- execute bounded actions
- improve monitoring and exception detection

## Step 2: Define each opportunity

Record:

- business problem
- affected workflow steps
- users and owners
- current baseline
- candidate intervention
- expected benefit
- required data and integrations
- key assumptions
- failure consequences
- measurement plan

## Step 3: Score

Score 1 to 5:

- business value
- workflow suitability
- technical feasibility
- data readiness
- deployment readiness
- time to value
- measurability
- risk

Default weighted score:

`0.30 value + 0.20 suitability + 0.20 feasibility + 0.15 readiness + 0.15 time-to-value - risk penalty`

## Step 4: Challenge the proposal

For each candidate ask:

- Can the step be removed?
- Would a policy or training change solve it?
- Would deterministic software be safer?
- Does AI materially improve the result?
- Can correctness be evaluated?
- Is historical evidence representative?
- Can the organization support the integration?
- Is the sponsor willing to own deployment risk?

## Step 5: Classify

- `BUILD_NOW`: strong evidence, high value, manageable risk
- `PROTOTYPE`: promising but requires validation
- `PREPARE_PREREQUISITES`: data, process, ownership, or infrastructure gaps
- `DO_NOT_AUTOMATE`: weak value, poor fit, or unacceptable risk

## Required outputs

- ranked opportunity inventory
- assumptions and evidence
- risk-adjusted recommendation
- recommended pilot
- rejected alternatives and reasons
- baseline and measurement plan

## Quality checks

- Is value tied to a measurable baseline?
- Were non-AI alternatives considered?
- Was risk treated as more than a numeric score?
- Is the pilot narrow enough to evaluate?
- Is ownership explicit?
