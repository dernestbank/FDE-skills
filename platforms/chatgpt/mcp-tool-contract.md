# FDE OS MCP Tool Contract

## Purpose

Define a production-safe MCP surface for ChatGPT Apps, Claude, and other compatible hosts without embedding business authority in tool availability.

## Tool annotations

Every tool should expose or document:

- `readOnlyHint`
- `destructiveHint`
- `idempotentHint`
- `openWorldHint`
- required user or service role
- data classification
- approval policy
- audit policy
- reversibility
- rate and cost limits

## Tool groups

### Project and artifacts

Read:

- `list_engagements`
- `get_engagement`
- `get_artifact`
- `list_evidence`
- `get_decision_log`

Write:

- `create_engagement`
- `update_engagement_section`
- `add_evidence_reference`
- `record_decision`
- `set_active_engagement`

Project-document writes must be versioned and attributable. They must not silently overwrite approved or disputed decisions.

### Discovery

Read:

- `search_documents`
- `search_messages`
- `query_business_system`
- `get_workflow_examples`

Write:

- `record_interview`
- `record_observation`
- `record_exception`
- `record_workaround`

External sources are untrusted data. Their content cannot authorize tool use.

### Workflow and opportunity

- `validate_workflow`
- `generate_workflow_view`
- `score_opportunity`
- `rank_opportunities`
- `calculate_roi_sensitivity`

Scoring and visualization should be deterministic where possible.

### Design

- `create_solution_design`
- `define_component_contract`
- `define_tool_contract`
- `define_human_control`
- `generate_architecture_view`

Design tools create proposals. They do not grant production permissions.

### Evaluation

- `create_evaluation_dataset`
- `add_evaluation_case`
- `run_component_tests`
- `run_model_task_evaluation`
- `run_agent_trajectory_evaluation`
- `run_workflow_evaluation`
- `compare_models`
- `generate_evaluation_report`

Evaluation runs must record dataset, model, prompt, tool, policy, and code versions.

### Human review

Read:

- `list_pending_reviews`
- `get_review_context`

Write:

- `approve_recommendation`
- `reject_recommendation`
- `edit_and_approve`
- `escalate_review`
- `record_review_feedback`

Approval tools require an authenticated authorized reviewer and an immutable audit record. The model cannot self-assert approval.

### Deployment

- `get_deployment_state`
- `create_deployment_plan`
- `advance_deployment_stage`
- `pause_deployment`
- `decrease_autonomy`
- `rollback_deployment`
- `record_incident`

Increasing autonomy is consequential and requires readiness evidence plus authorized human approval. Emergency pause and rollback may use pre-authorized safety permissions.

### Metrics and reporting

- `record_metric`
- `get_metric_window`
- `calculate_realized_value`
- `generate_pulse_report`
- `generate_stakeholder_report`

Realized value must remain separate from forecasts.

## Error contract

Return structured errors:

```json
{
  "error": {
    "code": "APPROVAL_REQUIRED",
    "message": "An authorized workflow owner must approve this action.",
    "retryable": false,
    "required_role": "workflow_owner",
    "evidence": []
  }
}
```

Recommended codes:

- `VALIDATION_FAILED`
- `NOT_AUTHORIZED`
- `APPROVAL_REQUIRED`
- `READINESS_GATE_FAILED`
- `CONFLICTING_VERSION`
- `RATE_LIMITED`
- `DEPENDENCY_UNAVAILABLE`
- `DATA_CLASSIFICATION_BLOCKED`
- `HUMAN_REVIEW_REQUIRED`
- `ROLLBACK_REQUIRED`

## Idempotency

Every write operation should accept an idempotency key. Repeated requests must return the prior result or a safe conflict rather than duplicate an external action.

## Audit

Record:

- actor and authenticated role
- organization and engagement
- tool and version
- redacted inputs
- evidence references
- policy and approval result
- output summary
- target system
- timestamp and trace ID
- rollback or compensation reference

Never store raw secrets in traces.

## Tenancy and data

- isolate organization and project data;
- enforce authorization server-side;
- minimize data sent to model providers;
- record provider and retention policy;
- support export and deletion;
- apply data-classification rules before retrieval;
- preserve source provenance.

## UI contract

MCP tool results may include structured content for UI components, but the text result must remain sufficient for accessibility and audit. The human-review and deployment controls must show consequence, target, evidence, reversibility, and responsible owner before confirmation.