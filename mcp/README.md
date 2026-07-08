# FDE OS MCP Integration

The skills are usable without an MCP server. MCP is the optional execution layer for durable project state, enterprise connectors, evaluation runs, human approvals, and deployment operations.

## Current status

`server-config.example.json` is a non-active example. Do not rename it to an active host configuration until an `fde_os_mcp` package or equivalent server exists and has been tested.

## Planned tool domains

- projects and engagement artifacts
- stakeholder and interview records
- workflow and exception maps
- opportunity scoring
- architecture and tool contracts
- evaluation datasets and runs
- human-review queues
- deployment stages, incidents, and rollback
- metrics, ROI, and reports

## Tool contract requirements

Every write-capable tool must declare:

- required role
- read or write classification
- target system and data class
- reversibility
- approval requirement
- idempotency behavior
- audit requirement
- rate and cost limits

Tool availability never grants authority. Skills must still apply engagement scope, least privilege, human approval, and readiness gates.

## Recommended rollout

1. Implement read-only project and artifact tools.
2. Add schema validation and audit traces.
3. Add bounded project-document writes.
4. Add human-review tools.
5. Add external-system writes only after security and evaluation gates.
6. Add deployment controls last.

See `platforms/chatgpt/mcp-tool-contract.md` for cross-platform design guidance.