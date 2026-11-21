# 🎯 [NEXT] F32: Add session isolation rule, forbid AI trailers, refine plan/work role protocols, and preload AGENTS.md via include globs

- Add `rules/core/isolation.md` (`# Description: Host-chat session isolation and external platform tool boundary`) and include `rule core/isolation` as the first entry in `rulesets/core.ruleset` (before `rule core/start`) so every bundle begins by scoping the active session to the bundle rules and workspace `AGENTS.md` files and instructing the agent not to apply any host-chat persona/domain context or invoke built-in host platform tools (such as external knowledge-base or web search) unless explicitly requested by the user.
- Update `rules/collab/external.md` (`Clean external text & two-step external changes`) to forbid adding AI co-author trailers (such as `Co-Authored-By:`), agent attribution lines (such as `Generated with...`), or tool signatures to commit messages, MR/PR descriptions, comments, or files.
- Update `rules/role/plan.md` (`Role (Planner)`):
  - Require bidirectional dependency-chain integration whenever adding or refining tasks (wiring both upstream prerequisites on the new task and downstream dependents/closing roots or milestone waves that touch the same target files or build on the capability, so tasks are not left as unintended standalone items).
  - Specify that while long-term `NEW` backlog tasks reference file paths and key symbol names in backticks (avoiding brittle line numbers across unrelated commits), once the user agrees to promote a task to `NEXT`, the planner records exact `path:start-end` line ranges in backticks for any inspected files that exceed single-file bundle size budgets so a subsequent `role=work` session bundle preloads those slices directly.
  - Scope each `role=plan` session to an atomic planning goal: once the agreed task updates, dependency edges, and priorities are persisted, committed, and pushed in `TODO*.md`, end the planning session immediately without asking which task to work on next or spawning another task session.
- Update `rules/role/work.md` (`Role (Worker)`):
  - Clarify that the active backlog task is closed only inside the final commit step (after the edit-and-diff step has completed and the printed diff has been verified clean), never inside the edit-and-diff step before diff verification.
  - When recording an out-of-scope finding as a new backlog item, describe the observed problem, context, and impact without prescribing a design/solution, assigning chain dependencies, or asking the user about chain placement or priority (which belong to `role=plan`).
  - Stage backlog additions recorded before the final code commit into that commit; if an out-of-scope item is recorded after the final code commit is already created/pushed (or in a session where no code commit follows), commit and push the backlog file update immediately so it is not left uncommitted in the working tree.
- In `.agents_bundle`, replace `$ cat AGENTS.md` with declarative `include AGENTS.md` and `include rules/**/AGENTS.md` directives so root `AGENTS.md` and all scoped category `AGENTS.md` files (`rules/core/AGENTS.md`, `rules/role/AGENTS.md`, and any future category `AGENTS.md` files) are preloaded as discrete `include` bundle fragments in every session.
- Wrap prose in `rules/core/isolation.md`, `rules/collab/external.md`, `rules/role/plan.md`, `rules/role/work.md`, and `rules/core/AGENTS.md` at ~80 columns without decorative bold/italic markup, and bump `VERSION` for a PATCH release.

# 🎯 [NEXT] F5: Wrap prose at ~80 columns across all remaining rule files

- Depends on: F31, F32, F34
- Wrap long lines (>80 chars) across all remaining rule files in `rules/` (`rules/collab/*.md`, `rules/core/*.md`, `rules/os/*.md`, `rules/release/*.md`, `rules/role/*.md`, `rules/stack/*.md`, `rules/vcs/*.md`) to ~80 characters per line and bump `VERSION` for a PATCH release.

# ⚪ [NEW] D1: Design composable role extensions and domain overlays

- Depends on: F16, F9
- Explore separating universal domain-agnostic role postures in `agents/role/` (cognitive stance, artifact permissions, and handoff contracts) from domain-specific role overlays (such as `agents/coding/design.md`, `agents/coding/plan.md`, `agents/coding/work.md`, and `agents/coding/review.md`) activated automatically via `[if role=...]` inside domain bundles.
- Define how projects compose base roles with one or more domain overlays without duplicating rules or leaking software-engineering assumptions into universal roles, feeding into `F20`.
- Apply orthogonal facet decomposition (`AGENTS.md`): separate cross-language interface contracts (`cli.md`) from language subtrees (`python/syntax.md`, `python/unittest.md`, `python/stdlib.md`, `python/annotations.md`, plus a default `python.bundle` preset) so projects never rely on hybrid filenames like `python-cli.md`.

# ⚪ [NEW] F20: Replace rulesets with bundles and organize rules logically by domain

- Depends on: D1
- Standardize `agents/` as the single package root directory for all rules (`.md`) and bundles (`.bundle`), migrating `rulesets/core.ruleset`, `rulesets/default.ruleset`, and `rules/` into a logical domain-based layout under `agents/` (incorporating composable domain role overlays designed in `D1`, after `agents_bundle` supports the `agents/` layout).
- Decompose `rules/stack/python-cli.md`, `rules/stack/python-stdlib.md`, and `rules/stack/python-annotations.md` into a nested `agents/stack/python/` (or `agents/python/`) subtree (`syntax.md`, `unittest.md`, `stdlib.md`, `annotations.md`, and `python.bundle`) orthogonal to `cli.md`.
- Update `.agents_bundle` (`include agents/**/AGENTS.md`), `AGENTS.md`, and `README.md` to reflect the unified `agents/` rule/bundle layout, and release a new MINOR version.

# ⚪ [NEW] F25: Rename project and package references from agents-rules to ctx-taxonomy

- Rename package identity, documentation, and internal references from `agents-rules` (`vitalio/agents-rules`) to `ctx-taxonomy` (`vitalio/ctx-taxonomy`), aligned with the ecosystem rename design.
- Target files: `AGENTS.md`, `README.md`, `.agents_bundle`, `VERSION`, and exported rule/bundle files (`rules/`, `rulesets/`, or `agents/` after `F20`).
- Acceptance criteria: all docs, examples, and package references use `ctx-taxonomy` (alongside sibling names `ctx-bundle`/`cxb`, `todo-markdown`/`tmd`, `run-block`/`rxb`), `VERSION` is bumped appropriately, and repository checks pass.
