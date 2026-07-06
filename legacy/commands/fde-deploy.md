# /fde-deploy

Plan or advance a controlled deployment stage.

## Procedure

1. Review the approved evaluation and unresolved conditions.
2. Select the lowest safe deployment stage.
3. Define entry criteria, exit criteria, permitted actions, approver, metrics, and rollback triggers.
4. Verify monitoring, escalation, support, training, security approval, and rollback readiness.
5. Advance only when the responsible owner approves.
6. Record the deployment decision and version.

Default stages:

`HISTORICAL_REPLAY -> SANDBOX -> SHADOW -> RECOMMENDATION -> APPROVAL -> BOUNDED_AUTONOMY -> CONDITIONAL_AUTONOMY -> MONITORED_PRODUCTION`
