# Cross-Platform Tool Adaptation

The skill contract is platform-neutral. Adapt tool names without changing authority or evidence requirements.

## Capability categories

### Blocking stakeholder question
Use the host's interactive question mechanism when available. Fall back to one concise question in chat when unavailable.

### File discovery and reading
Use native search before broad full-file reads. Prefer targeted sections and preserve file/line provenance when possible.

### Task tracking
For Standard and Deep work, use the host's task or plan view to expose meaningful outcomes. Do not simulate low-level tool-call lists in chat.

### Isolated specialist work
Use subagents, tasks, or isolated delegated contexts. If unavailable, run serial independent reviews with clean prompt boundaries.

### External systems
Use MCP, actions, connectors, or native integration tools. Tool availability does not imply authorization.

### Deterministic execution
Use shell or Python for schema validation, scoring, health checks, metrics, redaction, and artifact generation when available.

## Host examples

### Claude Code
- skills: `skills/<name>/SKILL.md`
- questions: `AskUserQuestion`
- specialists: task/subagent dispatch
- external tools: MCP
- hooks: plugin hooks

### ChatGPT / Codex-style hosts
- skills: Agent Skills directories where supported
- questions: native user-input mechanism or chat
- specialists: delegated agent/context when available
- external tools: Apps SDK/MCP/actions/connectors
- deterministic controls: backend services and schema validation

### Cursor, Copilot, Cline, OpenCode, and similar hosts
Use their native skill/plugin conversion or source installation. Preserve skill-local references and do not flatten every reference into a global instruction file.

## Permission rule

Map tool names, never weaken policy. A production write that requires approval in one host requires approval in every host.