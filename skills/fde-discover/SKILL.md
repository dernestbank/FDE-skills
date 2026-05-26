---
name: fde-discover
description: Discover how a business workflow actually operates through stakeholder interviews, observation, documents, systems, data, examples, exceptions, incentives, and baseline evidence. Use after fde-start or when a workflow description is incomplete, disputed, or based only on SOPs. Not for proposing architecture before current-state evidence is adequate.
argument-hint: "[engagement path, workflow, stakeholder, evidence source, or discovery question]"
---

# Discover the Real Workflow

## Outcome

Advance a canonical dossier from `intake` toward `discovery-grounded` by collecting representative, source-linked evidence.

## Phase 0: Load and assess

1. Locate the engagement dossier or route to `/fde-start` if none exists.
2. Read current scope, settled decisions, evidence, assumptions, and unknowns.
3. Classify discovery depth as Lightweight, Standard, or Deep.
4. Create a short user-facing work spine for Standard or Deep work when the host supports task tracking.

## Phase 1: Existing-context scan

Search the authorized project sources before asking the stakeholder to repeat known information:

- dossier and prior decisions
- SOPs and training material
- system documentation
- incident and complaint records
- metrics and dashboards
- representative files, emails, tickets, transactions, or logs
- existing process maps and audits

For Standard or Deep work, dispatch an extraction-tier workflow researcher using `../fde-os/references/agents/workflow-researcher.md`. Give it bounded sources and require provenance. Carry only a concise gist in the main dialogue; retain the evidence dossier for on-demand reading.

## Phase 2: Pressure test

Identify only material gaps:

- problem evidence
- user and workflow owner
- current workaround
- trigger and final output
- actors, handoffs, systems, data, and decisions
- exceptions and failure recovery
- volume, timing, cost, quality, and risk baselines
- incentives, politics, adoption, and authority
- downstream consequences

Do not fire a generic questionnaire. Ask one concrete question at a time, prioritizing the gap that most changes the next decision. Read `../fde-os/references/interaction-rules.md` when conducting dialogue.

## Phase 3: Observe representative cases

Whenever authorized, trace real cases from trigger to completion. For each step capture:

- actor and owner
- input and source
- system or communication channel
- action and decision
- output and destination
- handling and waiting time
- exception, failure, escalation, and workaround
- evidence pointer and confidence

Compare stated and observed process. Preserve disagreements rather than averaging them into a fictional workflow.

## Phase 4: Exception sweep

Explicitly seek:

- missing, duplicate, malformed, conflicting, or ambiguous inputs
- undocumented formats and attachments
- unavailable people or systems
- urgent overrides and policy exceptions
- permission failures and manual re-entry
- informal approvals and shadow systems
- knowledge concentrated in one person
- downstream corrections and rework

A discovery that documents only the happy path is incomplete.

## Phase 5: Synthesis

Update the dossier and supporting artifacts with:

- discovery summary
- stakeholder and authority changes
- system and data inventories
- stated versus observed process
- exceptions, workarounds, and knowledge dependencies
- baseline evidence and metric gaps
- contradictions, assumptions, and unknowns
- evidence registry

Use claim labels from the artifact contract. Never convert stakeholder estimates into measured baselines.

## Exit gate

Set readiness to `discovery-grounded` only when representative evidence covers the workflow boundary, material actors and systems, important exceptions, and the remaining gaps are explicit.

## Handoff

End with:

- dossier and evidence paths
- representative cases observed
- critical exceptions
- disputed or unknown items
- readiness verdict
- next valid skill: `/fde-map`

If evidence remains too weak, give the smallest next discovery action rather than advancing.