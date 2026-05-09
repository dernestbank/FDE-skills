# FDE OS Concepts

Canonical vocabulary for this plugin. This file is a glossary, not a specification.

## Plugin parts

### Skill
A user-invoked capability stored in its own `skills/<name>/` directory. A skill owns a workflow, loads detailed references only when needed, may run deterministic scripts, and may dispatch specialist reviewers in isolated context.

### Specialist prompt asset
An internal prompt stored under a skill's `references/agents/` directory. It is not a permanent user-facing agent. The owning skill decides when to load it, what evidence it receives, and how its findings are reconciled.

### Reference
Detailed procedural guidance loaded only when a decision gate or workflow phase requires it. References keep the primary `SKILL.md` focused and reduce irrelevant context.

### Hook
A deterministic lifecycle control that validates actions, records activity, or blocks false completion claims.

### MCP tool
An external capability exposed through the Model Context Protocol. Tools are execution surfaces; they do not replace skill judgment, project policy, or human authority.

## Engagement artifacts

### Engagement dossier
The canonical `ENGAGEMENT.md` for one coherent FDE outcome. It accumulates product, workflow, technical, risk, evaluation, deployment, and ownership decisions through the lifecycle.

### Artifact contract
A machine-readable identifier declaring the artifact shape. FDE OS uses `fde-engagement/v1`.

### Artifact readiness
The strongest lifecycle state supported by current evidence:

- `intake`
- `discovery-grounded`
- `mapped`
- `prioritized`
- `design-ready`
- `evaluation-ready`
- `deployment-ready`
- `operational`

Readiness is evidence-backed. It is not a percentage-complete label.

### Decision record
A durable record of a consequential choice, alternatives considered, evidence, owner, date, and reversal trigger.

### Evidence reference
A pointer to the observation, document, system record, test result, interview, metric, or other source supporting a claim.

### Settled decision
A decision explicitly examined and chosen by an authorized stakeholder, or imported from an approved project artifact. A casual assertion is not automatically settled.

## Workflow concepts

### Stated process
How stakeholders or documentation say the workflow operates.

### Observed process
How the workflow actually operated in representative cases.

### Exception
A material deviation from the normal path requiring different data, judgment, authority, or recovery.

### Workaround
An informal method used to bypass a limitation, failure, or mismatch in the official workflow.

### Knowledge dependency
Operational knowledge concentrated in a person, team, private file, or undocumented habit.

### Current-state map
An evidence-linked representation of the workflow as it operates today.

### Future-state map
The proposed operating model after process, software, AI, and human-control changes.

## Execution classifications

- `HUMAN_ONLY`
- `DETERMINISTIC_RULE`
- `API_CALL`
- `DATABASE_OPERATION`
- `RPA_ACTION`
- `LLM_ASSIST`
- `LLM_DECISION`
- `AGENT_ACTION`
- `HUMAN_APPROVAL`
- `HUMAN_EXCEPTION`
- `NO_LONGER_REQUIRED`

## Human-control levels

0. Human-only
1. AI assistance
2. AI recommendation
3. Human approval
4. Supervised autonomy
5. Conditional autonomy
6. Monitored autonomy

Use the lowest level that creates acceptable value and risk.

## Review concepts

### Independent review
A review performed in a separate reasoning context that receives evidence and a clear review mandate, not the original author's unstated assumptions.

### Blocking finding
A finding that prevents the next readiness transition until resolved or formally accepted by an authorized owner.

### Residual risk
Risk remaining after controls are applied and explicitly accepted by the responsible owner.

## Evaluation concepts

### Golden dataset
Representative cases with reviewed expected outcomes.

### Regression dataset
Cases retained to prevent previously solved failures from returning.

### Trajectory evaluation
Evaluation of tool selection, sequencing, arguments, policy compliance, recovery, and escalation—not just final text.

### Deployment gate
The evidence and approvals required to advance to a higher-autonomy stage.

## Compounding concepts

### Compound learning
A durable, reusable lesson extracted from an engagement after a problem was solved or an assumption was disproved.

### Pattern
A reusable approach with applicability boundaries, prerequisites, risks, evidence, and known failure signals.

### Pulse report
A time-windowed report on actual production experience: adoption, outcomes, failures, overrides, costs, latency, incidents, and business metrics.

### Handoff envelope
A compact, source-linked summary allowing another session, engineer, or agent to resume without reconstructing the engagement from chat history.