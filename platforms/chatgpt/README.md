# ChatGPT Packaging for FDE OS

FDE OS has two practical ChatGPT distribution paths. Choose one per GPT experience rather than mixing incompatible integration modes.

## Path A: Custom GPT

Best for:

- early distribution
- guided FDE methodology
- uploaded playbooks and templates
- a small number of REST actions
- single-user or lightweight project workflows

Package:

- `system-instructions.md` as the core instruction source
- selected skill/reference files as Knowledge
- `openapi.example.yaml` adapted to the deployed backend
- OAuth or API-key authentication appropriate to the action

Use Actions when the GPT needs to call a conventional REST API. Keep project state and authorization in the backend, not only in the conversation.

A GPT configured with external Actions should not also be designed as a ChatGPT App in the same surface. Maintain separate releases when both experiences are needed.

## Path B: ChatGPT App

Best for:

- production multi-project FDE work
- durable project state
- rich workflow maps and evaluation dashboards
- human-review queues
- OAuth and role-based access
- MCP tools and resources
- staged deployment controls

Recommended architecture:

```text
ChatGPT
  -> FDE OS MCP server
       -> project/artifact service
       -> enterprise connectors
       -> evaluation workers
       -> human-review service
       -> deployment/metrics service
  -> Apps SDK UI components
       -> project dashboard
       -> workflow map
       -> opportunity matrix
       -> evaluation dashboard
       -> approval queue
       -> deployment control panel
```

Use the Apps SDK for interactive UI and MCP for tools/resources. Keep authority, tenancy, audit, and readiness gates server-side.

## Shared rules

Both packages must preserve:

- one canonical engagement dossier
- explicit project readiness
- evidence and claim labels
- least-privilege tools
- human approval for consequential actions
- read/write tool classification
- audit traces and provenance
- evaluation before autonomy
- rollback and ownership before production

## Suggested release sequence

1. Ship a no-backend Custom GPT using instructions and Knowledge.
2. Add read-only Actions for project and artifact retrieval.
3. Add bounded project-document writes with authentication.
4. Build the MCP server and migrate production workflows to a ChatGPT App.
5. Add rich review, evaluation, and deployment interfaces.

## Files

- `system-instructions.md` — compact ChatGPT instruction layer
- `openapi.example.yaml` — starter REST action schema
- `mcp-tool-contract.md` — production MCP design contract

Review current OpenAI documentation before publishing because product configuration and review requirements may change.