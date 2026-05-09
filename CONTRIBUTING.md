# Contributing to FDE OS

## Contribution principles

- Preserve evidence-before-autonomy behavior.
- Give each user-invoked skill one clear outcome and terminal handoff.
- Put detailed rubrics and specialist prompts in skill-local `references/` rather than enlarging the root router.
- Add deterministic validation where model judgment is unnecessary.
- Separate product/design decisions, implementation progress, evaluation evidence, and deployment authority.
- Keep schemas backward compatible or document migrations.
- Distinguish methodology changes from domain-specific playbooks.
- Avoid vendor-specific assumptions in the core unless implemented as optional adapters.
- Do not add active root-level `agents/` or `commands/`; version 0.1 files are archived under `legacy/`.
- Capture verified reusable lessons with `/fde-compound` after material work.

## Adding a skill

A new skill is warranted when the user can recognize and request a distinct outcome.

Required:

1. `skills/<skill-name>/SKILL.md`
2. YAML frontmatter with matching `name`
3. description containing both when to use and when not to use
4. clear preconditions
5. durable output contract
6. readiness or gate behavior when applicable
7. terminal handoff
8. positive and adversarial routing cases
9. documentation in `docs/skills/README.md`

If the change is only a checklist, rubric, platform variant, or specialist review role, add a gated reference to the owning skill instead.

## Specialist prompts

Specialist prompt assets:

- live under the owning skill's `references/agents/` directory;
- receive bounded evidence and mandate;
- return findings without editing canonical artifacts;
- preserve an independent verdict before reconciliation;
- use task-shape model tiers rather than hard-coded model brands.

## Pull request checklist

- [ ] Purpose and affected lifecycle phase are documented.
- [ ] Skill scope is coherent and not duplicated.
- [ ] New or changed artifacts have schemas or validation where appropriate.
- [ ] Security, privacy, human-control, and adoption implications were reviewed.
- [ ] Read/write and approval semantics are explicit for tools.
- [ ] Positive, negative, and adversarial tests were added.
- [ ] Setup and health checks still pass.
- [ ] Python scripts compile.
- [ ] JSON/YAML configuration parses.
- [ ] Plugin and marketplace versions agree.
- [ ] Documentation and changelog were updated.
- [ ] No machine-local settings, audit data, or credentials are committed.
- [ ] A compound-learning candidate was considered.
