# Evaluation Design Playbook

## Objective

Convert non-deterministic system behavior into evidence suitable for engineering and deployment decisions.

## Step 1: Define the decision

State what the evaluation will determine:

- component readiness
- model selection
- agent reliability
- workflow readiness
- business-case validation
- deployment-stage advancement

## Step 2: Establish baseline

Record current human, rules-based, or legacy-system performance using the same task definition where possible.

## Step 3: Build datasets

Create and version:

- golden normal cases
- edge cases
- adversarial and abuse cases
- regression cases
- human-disagreement cases
- representative production samples

Each case should include provenance, expected behavior, severity, tags, reviewer, and uncertainty.

## Step 4: Choose metrics

Use metrics appropriate to the risk:

- exact match or field accuracy
- precision, recall, and F-score
- groundedness and citation quality
- task completion
- correct tool and argument selection
- trajectory compliance
- escalation appropriateness
- false-positive and false-negative rates
- human override rate
- policy violation rate
- latency and cost
- business outcome

## Step 5: Define acceptance thresholds

Thresholds must reflect consequences. Critical cases may require zero uncontrolled failures even when average accuracy is high.

## Step 6: Run and classify

For every failure, classify root cause:

- missing or poor data
- retrieval failure
- instruction or prompt failure
- model capability
- tool selection
- invalid tool arguments
- integration failure
- policy failure
- insufficient validation
- workflow design failure
- expected human disagreement

## Step 7: Report honestly

Separate:

- measured results
- extrapolations
- estimates
- assumptions
- unknowns

Include confidence intervals or ranges where appropriate.

## Required outputs

- evaluation plan
- dataset manifest
- evaluation cases
- run results
- failure taxonomy
- acceptance decision
- limitations
- regression plan

## Quality checks

- Is the dataset representative?
- Are severe exceptions included?
- Are metrics tied to business consequences?
- Was human escalation actually tested?
- Were cost and latency measured?
- Can the evaluation be reproduced?
