# 🎯 [NEXT] F24: Remove bundle vitalio/run_block from .agents_bundle and README.md

- Remove `bundle vitalio/run_block` from `.agents_bundle` and the `.agents_bundle` usage example in `README.md` once `run_block` embeds its own block execution rules.

# 🎯 [NEXT] F23: Add portable multi-repository coordination rule and orchestrator bundle preset

- Add a universal, tool-agnostic rule (for example `rules/collab/multi-repo.md` or `rules/role/multi-repo-plan.md`) defining cross-repository task decomposition and dependency boundaries: detailed implementation tasks belong in each owning repository's backlog, while the coordinating repository records a parent task linking all child tasks via dependencies and keeps cross-repository dependency edges out of standalone child repositories.
- Add `rulesets/orchestrator.ruleset` (migrating to `agents/orchestrator.bundle` under `F20`) exporting the multi-repository coordination rule so orchestrator repositories can compose it directly without duplicating prose in local `AGENTS.md` files.
- Follow `AGENTS.md` formatting conventions (`# Description:` header, plain `- Topic: instruction.` bullets, ~80-char line wrapping, no tool-specific names), update `README.md` if needed, and bump `VERSION` for a MINOR release.

# 🎯 [NEXT] F4: Support greenfield project bootstrap and tool-agnostic wording in role/design

- Update `rules/role/design.md` so that when designing a new project from scratch, once the design is agreed with the user, the agent creates the target project directory, initializes version control, and scaffolds `AGENTS.md`, project context configuration, and the initial project task backlog before committing the initial scaffold.
- Clarify in `rules/role/design.md` that raw ideas and architectural explorations enter the backlog as design tasks for `role=design`, and once agreed are closed after recording architectural invariants in `AGENTS.md` and creating actionable implementation tasks.
- Replace the hardcoded `.agents_bundle` filename in `rules/role/design.md` with tool-agnostic wording so `rules/role/` complies with `AGENTS.md` and `rules/role/AGENTS.md` taxonomic invariants, and release a PATCH version.

- Specify in `rules/role/design.md` that when a design decision involves complex protocols, trade-offs, or multi-component rationale too detailed for `AGENTS.md`, the agent records a concise Architecture Decision Record in `docs/adr/NNNN-<slug>.md` (context, decision, rejected alternatives, consequences) and references it in backticks in downstream implementation tasks.

# 🎯 [NEXT] F13: Define role handoff contracts, target-file closure, and preloaded-context execution in rules/role/

- Depends on: F9, F16
- Update `rules/role/plan.md` so the Planner distinguishes raw ideas/design tasks (routing them to `role=design`) from ready work items, determines the full target file closure for each prioritized task (source modules, CLI help, docs, paired rules, and tests per `AGENTS.md` and active stack rules), records those file paths in the task body, and preloads them into the new session context when handing off to working.
- Update `rules/role/work.md` so that when a task's target files are already preloaded in the initial session context, the agent skips a separate read-only discovery step and proceeds directly in step 1 to edits, project build/linter/test verification, and diff output (running an initial batched read step only for files not yet in context).
- Update `rules/role/design.md` and `rules/role/review.md` so Designer records module-boundary and file-coupling invariants in `AGENTS.md` for downstream planning/working, and Reviewer verifies those project-specific `AGENTS.md` invariants alongside task specifications, keeping wording strictly tool-agnostic, and release a PATCH version.

# ⚪ [NEW] F5: Wrap prose at ~80 columns across all remaining rule files

- Wrap long lines (>80 chars) in `rules/collab/external.md`, `rules/core/AGENTS.md`, `rules/core/composability.md`, `rules/core/diff-review.md`, `rules/core/end.md`, `rules/core/lang.md`, `rules/core/plan.md`, `rules/core/secrets.md`, `rules/core/ssot.md`, `rules/os/*.md`, `rules/release/single-file-build.md`, `rules/stack/python-cli.md`, `rules/stack/python-stdlib.md`, `rules/stack/python-annotations.md`, and `rules/vcs/*.md` to ~80 characters per line.

# ⚪ [NEW] D1: Design composable role extensions and domain overlays

- Depends on: F16, F9
- Explore separating universal domain-agnostic role postures in `agents/role/` (cognitive stance, artifact permissions, and handoff contracts) from domain-specific role overlays (such as `agents/coding/design.md`, `agents/coding/plan.md`, `agents/coding/work.md`, and `agents/coding/review.md`) activated automatically via `[if role=...]` inside domain bundles.
- Define how projects compose base roles with one or more domain overlays without duplicating rules or leaking software-engineering assumptions into universal roles, feeding into `F20`.

# ⚪ [NEW] F20: Replace rulesets with bundles and organize rules logically by domain

- Depends on: D1
- Standardize `agents/` as the single package root directory for all rules (`.md`) and bundles (`.bundle`), migrating `rulesets/core.ruleset`, `rulesets/default.ruleset`, and `rules/` into a logical domain-based layout under `agents/` (incorporating composable domain role overlays designed in `D1`, after `agents_bundle` supports the `agents/` layout).
- Update `AGENTS.md` and `README.md` to reflect the unified `agents/` rule/bundle layout, and release a new MINOR version.

# ⚪ [NEW] F25: Rename project and package references from agents-rules to ctx-taxonomy

- Role: plan
- Rename package identity, documentation, and internal references from `agents-rules` (`vitalio/agents-rules`) to `ctx-taxonomy` (`vitalio/ctx-taxonomy`), aligned with the ecosystem rename design.
- Target files: `AGENTS.md`, `README.md`, `.agents_bundle`, `VERSION`, and exported rule/bundle files (`rules/`, `rulesets/`, or `agents/` after `F20`).
- Acceptance criteria: all docs, examples, and package references use `ctx-taxonomy` (alongside sibling names `ctx-bundle`/`cxb`, `todo-markdown`/`tmd`, `run-block`/`rxb`), `VERSION` is bumped appropriately, and repository checks pass.
