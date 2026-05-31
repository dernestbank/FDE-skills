---
name: fde-map
description: Convert discovery evidence into current-state workflow, system, data, decision, responsibility, exception, and bottleneck maps. Use after discovery or when the user asks to document how work currently flows. Not for proposing the future-state solution; use fde-prioritize and fde-design after the map is accepted.
argument-hint: "[engagement path, workflow evidence, or map type]"
---

# Map the Current Operating Reality

## Outcome

Produce an evidence-linked current-state operating model and advance readiness toward `mapped`.

## Preconditions

- canonical engagement dossier exists;
- workflow boundary is coherent;
- representative evidence exists or its absence is explicit.

When discovery evidence is insufficient, route back to `/fde-discover` rather than filling gaps with plausible process steps.

## Mapping flow

### 1. Normalize evidence

Create stable identifiers for actors, roles, systems, data objects, workflow steps, decisions, controls, exceptions, and evidence items.

### 2. Build the current-state workflow

Every step must contain:

- stable ID and sequence
- name and purpose
- owner and performer
- trigger or predecessor
- inputs and outputs
- system and channel
- action and decision
- control and approval
- handling time, waiting time, volume, and frequency when known
- failure modes, exceptions, workarounds, and rework
- evidence references
- confidence and dispute status

### 3. Build complementary views

- **System map:** applications, spreadsheets, files, messaging, databases, vendors, and manual channels.
- **Data map:** origin, format, transformation, system of record, owner, sensitivity, access, retention, and destination.
- **Decision map:** decision owner, required evidence, deterministic rules, judgment, authority, confidence, and escalation.
- **Responsibility map:** sponsor, accountable owner, performer, approver, technical owner, security/compliance owner, and affected users.
- **Exception map:** trigger, detection, current response, owner, impact, frequency, and recovery.

### 4. Analyze the map

Identify:

- queue and handoff delays
- re-entry and duplication
- rework loops
- control gaps
- knowledge concentration
- unavailable or stale data
- system-boundary failures
- high-cost judgment points
- steps that exist only because of an upstream defect

Do not recommend a specific AI architecture yet.

### 5. Review

For Standard or Deep engagements, independently review the map for evidence gaps and process contradictions. Use the workflow researcher prompt asset for extraction verification and the process challenger for hidden simplification opportunities, but keep opportunity recommendations out of the current-state map.

## Durable outputs

Update:

- dossier Current-state understanding
- `artifacts/workflow-current.json`
- `artifacts/systems.json`
- `artifacts/data-sources.json`
- `artifacts/exceptions.json`
- evidence registry, risks, assumptions, and disputes

When visual output is useful, generate Mermaid, BPMN-like text, or a platform-native diagram from the structured map; the JSON remains canonical.

## Exit gate

Set readiness to `mapped` only when the current-state model is traceable to evidence, material exceptions are represented, and disputed or unknown steps are visible.

## Handoff

End with:

- map paths
- highest-confidence bottlenecks
- critical evidence gaps
- disputed workflow areas
- readiness verdict
- next valid skill: `/fde-prioritize`