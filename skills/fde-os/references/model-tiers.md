# Model and Subagent Tiers

Use task shape rather than provider names.

## Extraction tier

Use for bounded retrieval, quotation, classification, schema filling, and evidence indexing where creativity is undesirable.

Expected behavior:
- quote or extract with provenance
- avoid recommendations
- stay within explicit source bounds
- return compact structured results

## Generation tier

Use for synthesis, workflow decomposition, architecture options, test generation, and stakeholder-facing drafts where judgment is needed but evidence remains bounded.

Expected behavior:
- distinguish evidence from inference
- expose alternatives and tradeoffs
- follow output contracts
- avoid silently deciding matters owned by stakeholders

## Ceiling tier

Use for high-risk architecture, cross-functional synthesis, adversarial review, ambiguous strategic decisions, or reconciliation of conflicting specialist findings.

Expected behavior:
- reason across business and technical constraints
- pressure-test assumptions
- identify second-order effects
- preserve uncertainty and dissent

## Degradation rules

If the host cannot select models per dispatch:

1. keep the same role and evidence boundaries;
2. reduce the number and breadth of parallel tasks;
3. prefer deterministic scripts for extraction and validation;
4. independently verify high-risk findings;
5. never claim that model diversity exists when all reviews used the same model/context.

If the host has no subagent primitive, run specialist reviews serially with clearly separated prompts and evidence packages. Preserve independent verdicts before reconciliation.

## Dispatch contract

Every specialist dispatch must include:

- engagement and readiness state
- bounded question
- evidence paths or excerpts
- excluded decisions
- required output shape
- claim-label policy
- severity or confidence scale
- instruction not to edit canonical artifacts

Return only the specialist result and evidence pointers. The owning skill performs synthesis.