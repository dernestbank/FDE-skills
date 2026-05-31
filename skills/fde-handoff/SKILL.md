---
name: fde-handoff
description: Create or resume a compact, source-linked handoff for another session, engineer, consultant, or agent. Use before context loss, team transfer, a phase change, or when separating independently planned work. Not for replacing the canonical engagement dossier.
argument-hint: "[engagement path or resume source] [destination path optional]"
---

# FDE Handoff

## Purpose

Preserve enough verified context to resume without reconstructing the engagement from chat history.

The handoff is a transport envelope, not the source of truth. Link canonical artifacts rather than copying them wholesale.

## Create mode

Write a handoff containing:

- engagement and dossier path
- current readiness and scope tier
- current coherent work unit
- objective and non-goals
- settled decisions and owners
- evidence and artifact paths
- completed work
- unresolved questions, disputes, and risks
- blocking findings and approvals
- active implementation or evaluation state
- next valid action and recommended skill
- commands or checks required to resume
- warnings about credentials, local state, or uncommitted changes

Default location:

`docs/fde/handoffs/<timestamp>-<engagement-slug>.md`

Use a user-provided destination when requested.

## Resume mode

1. Read the handoff.
2. Verify linked canonical artifacts still exist.
3. Check whether readiness, decisions, or project state have changed.
4. Summarize the current state and stale assumptions.
5. Continue with the named next skill or explain why a different prerequisite is now required.

## Rules

- Do not promote handoff summaries over newer canonical artifacts.
- Do not include secrets or sensitive raw evidence.
- Mark unverified local state.
- Preserve exact paths, IDs, versions, and owner roles where material.
- One handoff should represent one coherent current work unit.

## Completion

Return the handoff path, readiness, next skill, blocking issue, and any stale or missing linked artifact.