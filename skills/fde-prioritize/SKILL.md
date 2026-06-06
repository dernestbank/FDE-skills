---
name: fde-prioritize
description: Generate, score, challenge, and rank process, deterministic automation, AI-assistance, and agentic opportunities from an accepted current-state map. Use to select the best pilot or decide what not to automate. Not for architecture design before a pilot is selected.
argument-hint: "[engagement path, workflow, candidate opportunity, or prioritization constraints]"
---

# Prioritize the Right Intervention

## Outcome

Select one risk-adjusted pilot and advance readiness toward `prioritized`.

## Preconditions

- dossier readiness is `mapped` or equivalent evidence is reviewed;
- baseline and important exceptions are visible;
- decision authority for pilot selection is known or explicitly missing.

## Phase 1: Generate intervention candidates

For each bottleneck, consider in this order:

1. remove the work;
2. simplify or standardize the process;
3. correct the upstream cause;
4. improve data quality or system integration;
5. implement deterministic rules, API calls, database operations, or RPA;
6. assist a human with retrieval, extraction, drafting, or recommendations;
7. use bounded AI judgment;
8. use an agent for multi-step action;
9. retain human-only execution.

Do not treat `AI agent` as the default candidate.

## Phase 2: Score

Score each coherent opportunity from 1 to 5 on:

- business value
- workflow suitability
- technical feasibility
- data readiness
- deployment readiness
- time to value
- measurability
- risk severity and uncertainty

Use the deterministic scoring script when available. Keep the numeric result separate from the final judgment; weights do not erase fatal risks or missing prerequisites.

Default categories:

- `BUILD_NOW`
- `PROTOTYPE`
- `PREPARE_PREREQUISITES`
- `DO_NOT_AUTOMATE`

## Phase 3: Economics

Connect value to:

- revenue
- cost
- risk
- cycle time
- quality
- capacity
- customer experience
- compliance

For each estimate provide baseline, formula, evidence source, uncertainty range, sensitivity, and possible value displacement. Do not double-count time, labor, and capacity benefits.

## Phase 4: Independent challenge

For Standard or Deep engagements, dispatch the process challenger using `../fde-os/references/agents/process-challenger.md` before final ranking.

Require explicit answers to:

- What is the strongest non-AI alternative?
- What prerequisite would invalidate this candidate?
- Which downstream bottleneck could become worse?
- What new carrying cost or failure mode does the intervention create?
- Can the claimed outcome be measured in a pilot?

## Phase 5: Select one pilot

Recommend one current pilot with:

- problem and affected user
- intervention class
- expected value and uncertainty
- scope and non-goals
- prerequisite data and access
- important exceptions
- risk and human-control hypothesis
- pilot metric and stop criteria
- rejected alternatives and reasons

Preserve surrounding opportunities as a backlog, not as requirements for the current pilot.

## Durable outputs

Update:

- dossier Opportunity decisions
- `artifacts/opportunities.json`
- baseline and success metrics
- risk and assumption registers
- decision log

## Exit gate

Set readiness to `prioritized` only when one coherent pilot is selected, alternatives were considered, value is measurable, and material assumptions and risks are visible.

## Handoff

End with pilot recommendation, decision owner, unresolved prerequisites, readiness verdict, and next skill `/fde-design`.