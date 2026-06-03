# Stakeholder Interaction Rules

Use these rules during discovery, scoping, design decisions, and approval gates.

## Question discipline

1. Ask one decision-bearing question at a time during interactive discovery.
2. Use a single-select menu when the stakeholder is choosing one direction, priority, or next step.
3. Use multi-select only for compatible sets such as constraints, goals, or non-goals.
4. Use open-ended questions for narrative evidence, lived workflow details, incentives, or unfamiliar territory.
5. Make open questions concrete enough to elicit examples, not opinions alone.
6. Do not repeat settled questions. Read the dossier and current conversation first.
7. When the user cannot evaluate the question because they lack domain knowledge, map the decision surface before asking them to choose.

## Evidence probes

Prefer questions such as:

- Walk me through the last real case from trigger to completion.
- Show me where the record changes systems or owners.
- What happened the last time this failed?
- Which exceptions are not in the SOP?
- What information does an experienced employee notice that a new employee misses?
- What would make the proposed system unsafe to trust?
- Which metric would prove that this change helped rather than merely moved work elsewhere?

Avoid broad prompts such as `Tell me about the process` when a more concrete probe is possible.

## Pressure test

Before converging, examine only the gaps that materially exist:

- Is the problem evidenced or merely asserted?
- Is the affected user and workflow owner clear?
- Is the current workaround known?
- Is the proposed outcome independently valuable and testable?
- Are incentives and adoption costs visible?
- Is there a non-AI or process-only alternative?
- Could improvement in one step create a downstream bottleneck?
- Are high-risk exceptions represented?

Raise gaps progressively; do not dump a generic questionnaire.

## Synthesis and confirmation

Before writing a material artifact or advancing readiness:

1. summarize the proposed understanding;
2. state important assumptions and disputed items;
3. identify the consequence of the chosen direction;
4. ask for confirmation only when the decision requires stakeholder authority;
5. proceed without ceremonial approval when the user has already clearly authorized the bounded work.

## Audience adaptation

- Executives: outcome, evidence, economics, risk, ownership, decision.
- Workflow users: daily behavior, workload, authority, exceptions, training.
- Engineers: contracts, architecture, failure handling, verification, operations.
- Security/legal/compliance: data, permissions, retention, trust boundaries, auditability, residual risk.

## No false consensus

When stakeholder accounts conflict, preserve the conflict and its provenance. Do not average incompatible process descriptions into a clean but fictional workflow.