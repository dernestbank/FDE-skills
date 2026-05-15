---
name: fde-compound
description: Capture one verified Forward Deployed Engineering learning as reusable project knowledge after discovery, design, evaluation, deployment, incident response, or production review. Use while context is fresh. Not for batching unrelated lessons or documenting unverified speculation.
argument-hint: "[optional learning hint] [mode:headless] [depth:lightweight|full]"
---

# Compound an FDE Learning

Every engagement should make the next engagement easier.

## Primary deliverable

Write exactly one durable learning per run to either:

- `docs/fde/solutions/<category>/<slug>.md` for a solved problem or reusable pattern; or
- `CONCEPTS.md` for durable project vocabulary.

Do not batch unrelated learnings. Run the skill again for the next lesson.

## Mode

Default to **Full**. Choose **Lightweight** only when context is tight or the learning is trivial and overlap research would add no value. In headless mode obey `depth:` and do not ask interactive questions.

State the selected mode and reason in the completion output.

## Phase 1: Identify the learning

Use the current session, engagement dossier, review, evaluation, pulse, incident, code/config change, or user hint.

The learning must contain a verified change in understanding, such as:

- an undocumented workflow rule
- a recurring exception
- an integration constraint
- a deterministic alternative that beat an AI approach
- a failed model, prompt, tool, or autonomy assumption
- an evaluation method that exposed a hidden failure
- a human-review or adoption pattern
- a deployment, monitoring, incident, or rollback lesson
- a reusable architecture or governance pattern

If several lessons exist, select the most consequential single learning and mention the others as future candidates.

## Phase 2: Ground and detect overlap

In Full mode:

1. search `docs/fde/solutions/`, `docs/fde/patterns/`, `docs/fde/pulse-reports/`, `CONCEPTS.md`, and the engagement dossier;
2. identify existing related knowledge;
3. verify evidence and final outcome;
4. decide whether to create, update, merge, cross-reference, or skip as duplicate.

Do not rewrite existing knowledge merely to produce a new file.

## Phase 3: Extract the reusable pattern

Separate:

- context-specific details
- general problem signature
- root cause
- failed approaches
- effective intervention
- evidence and validation
- applicability prerequisites
- contraindications
- failure or drift signals
- security, human, and operational implications
- related artifacts and patterns

Redact client-sensitive details while preserving technical usefulness.

## Phase 4: Write

Read `references/solution-template.md`.

Required frontmatter:

```yaml
artifact_contract: fde-solution/v1
status: verified
category: workflow | integration | architecture | evaluation | security | adoption | deployment | economics | governance
created: YYYY-MM-DD
updated: YYYY-MM-DD
source_engagements: []
tags: []
```

A solution must be understandable without the original chat session.

## Phase 5: Discoverability

Cross-reference related solutions and the source engagement. Update `CONCEPTS.md` only when the learning establishes or changes canonical vocabulary. Do not edit tracked instruction files without explicit approval.

## Quality check

Before completion verify:

- one learning only
- supported by evidence
- no confidential leakage
- clear applicability boundaries
- failed approaches included when useful
- validation described honestly
- related knowledge linked
- no duplicate or contradictory entry left unexplained

## Completion

Return:

- selected mode
- written or updated path
- one-sentence learning
- evidence source
- related knowledge
- future compound candidates, if any