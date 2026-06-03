# FDE Engagement Artifact Contract

## Canonical location

`docs/fde/engagements/<engagement-slug>/ENGAGEMENT.md`

Supporting structured artifacts:

`docs/fde/engagements/<engagement-slug>/artifacts/`

## Required frontmatter

```yaml
artifact_contract: fde-engagement/v1
artifact_readiness: intake
engagement_id: fde-<stable-id>
organization: <name-or-confidential-label>
workflow: <one coherent outcome>
owner: <responsible human role or unknown>
scope_tier: lightweight | standard | deep
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
```

Optional fields:

```yaml
confidentiality: public | internal | confidential | restricted
jurisdictions: []
source_engagement: null
supersedes: null
```

## Required sections

1. Goal capsule
2. Scope boundaries
3. Stakeholders and authority
4. Evidence registry
5. Current-state understanding
6. Exceptions and failure modes
7. Baseline and success metrics
8. Opportunity decisions
9. Future-state operating model
10. Architecture and integrations
11. Human authority and escalation
12. Evaluation contract and results
13. Deployment and operating model
14. Risks, assumptions, disputes, and unknowns
15. Decision log
16. Next gate

Sections may be compact or marked `Not yet established` at early readiness states. Do not fabricate content to make the dossier look complete.

## Claim labels

Use one of these labels for material claims:

- `MEASURED`
- `OBSERVED`
- `DOCUMENTED`
- `STAKEHOLDER_REPORTED`
- `ESTIMATED`
- `ASSUMED`
- `DISPUTED`
- `UNKNOWN`

Each material claim should include a source or explain why no source exists.

## Evidence registry fields

- evidence ID
- type
- source
- date or time window
- owner or custodian
- scope
- sensitivity
- reliability notes
- artifact path or external reference

## Decision record fields

- decision ID
- date
- owner
- decision
- alternatives considered
- evidence
- assumptions
- risks
- consequences
- reversal trigger
- status

## Resume rules

1. Search for an obvious matching dossier before creating another.
2. Preserve approved decisions and provenance.
3. Append or version changes; do not silently overwrite disputed or approved material.
4. Reassess readiness when evidence changes.
5. If the user requests a new coherent outcome, create a separate dossier and link it under surrounding work.

## Artifact readiness

- `intake`: charter and authority established
- `discovery-grounded`: representative workflow evidence collected
- `mapped`: current-state operating model documented
- `prioritized`: pilot selected with risk-adjusted reasoning
- `design-ready`: future-state design and reviews recorded
- `evaluation-ready`: evaluation evidence meets the design gate
- `deployment-ready`: production rollout, controls, ownership, and rollback approved
- `operational`: production evidence and improvement cadence exist

## Supporting filenames

Recommended files under `artifacts/`:

- `stakeholders.json`
- `systems.json`
- `data-sources.json`
- `observation-log.json`
- `workflow-current.json`
- `exceptions.json`
- `opportunities.json`
- `workflow-future.json`
- `solution-design.json`
- `tool-contracts.json`
- `evaluation-plan.json`
- `evaluation-report.json`
- `deployment-plan.json`
- `risk-register.json`
- `decision-log.json`
- `metrics.json`
- `incident-log.json`

The dossier summarizes and links these files; it does not duplicate every field.