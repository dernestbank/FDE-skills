# Design Study: Compound Engineering Plugin

FDE OS version 0.2 was improved after studying the architecture and workflow discipline of Every's `compound-engineering-plugin`:

https://github.com/everyinc/compound-engineering-plugin

This document records architectural lessons, not copied prompts or product branding.

## Lessons adopted

### 1. Skills own outcomes

A strong plugin is not one giant instruction file. Each user-invoked skill should own one recognizable outcome, its durable artifact, its detailed references, its scripts, and its terminal handoff.

FDE OS now separates:

- setup
- engagement intake
- discovery
- mapping
- prioritization
- design
- review
- build
- evaluation
- deployment
- production pulse
- knowledge compounding
- handoff
- reporting

### 2. Progressive context loading

Large methodologies become noisy when all checklists and specialist roles load at once. The root skill now routes and governs, while detailed lifecycle rules, artifact contracts, interaction rules, model tiers, platform mappings, and specialist prompts live under `references/` and load only when their gate fires.

### 3. Durable artifacts over chat history

The canonical FDE engagement dossier accumulates evidence, decisions, readiness, architecture, evaluation, deployment, and ownership. Skills resume and enrich the same dossier rather than producing disconnected documents.

### 4. Explicit readiness contracts

An artifact declares both its contract and its strongest evidence-backed readiness state. Readiness can advance, remain blocked, or move backward when new evidence disproves an assumption.

### 5. Right-sized ceremony

Lightweight, Standard, and Deep scope tiers prevent a trivial workflow question from receiving an enterprise-transformation process while protecting high-risk work from unsafe compression.

### 6. Independent specialist review

Reviewers operate in isolated context with a bounded mandate and evidence package. They return findings to the owning skill and do not silently edit canonical artifacts.

### 7. Plan, execution, and evidence are separate

The design owns product and workflow decisions. The build skill owns implementation. The evaluation skill owns readiness evidence. Passing local tests is not the same as passing an FDE deployment gate.

### 8. Setup is a product feature

A plugin should diagnose installation health, local configuration, optional capabilities, project directories, and unsafe config tracking. Setup should not require manually understanding the whole repository.

### 9. Explicit handoffs

Every skill states what it produced, what remains unresolved, the current readiness, and the next valid skill. A separate handoff skill preserves resumability across sessions and teams.

### 10. Compound the learning

The final step is not merely reporting completion. Each verified engagement can produce one reusable workflow, architecture, evaluation, security, adoption, deployment, economics, or governance learning.

## FDE-specific extensions

FDE OS extends those plugin-design patterns into enterprise AI deployment through:

- stated-versus-observed workflow evidence
- process-elimination and deterministic alternatives before AI
- execution classification for each future-state step
- explicit human-control levels
- security and prompt-injection review
- agent-trajectory evaluation
- staged autonomy
- production pulse reports
- business-value and adoption measurements
- rollback and incident ownership

## Boundary

FDE OS should remain its own methodology and product. Inspiration from another plugin should improve architecture, ergonomics, and workflow discipline without copying proprietary text or turning the product into a software-development-only tool.