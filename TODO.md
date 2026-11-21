# 🎯 [NEXT] F35: Preload root AGENTS.md and scoped rules/**/AGENTS.md via include in .agents_bundle

- In `.agents_bundle`, replace `$ cat AGENTS.md` with declarative `include AGENTS.md` and `include rules/**/AGENTS.md` directives so root `AGENTS.md` and all scoped category `AGENTS.md` files (`rules/core/AGENTS.md`, `rules/role/AGENTS.md`, and any future category `AGENTS.md` files) are preloaded as discrete `include` bundle fragments in every session.
- Wrap long prose lines in `rules/core/AGENTS.md` at ~80 columns to match `AGENTS.md` and `rules/role/AGENTS.md`.

# 🎯 [NEXT] F33: Specify planner line-range preloading (path:start-end) for large inspected files when promoting a task to NEXT in rules/role/plan.md

- In `rules/role/plan.md`, update the target-file closure bullet so that while long-term `NEW` backlog tasks reference file paths and key symbol names in backticks (avoiding brittle line numbers across unrelated commits), once the user agrees to promote a task to `NEXT` or take it into `role=work` next, the planner records exact `path:start-end` line ranges in backticks for any inspected files that exceed single-file bundle size budgets so the initial `role=work` bundle preloads those slices directly.
- Verify line wrapping (~80 columns) and update `README.md` or `VERSION` if needed.

# 🎯 [NEXT] F32: Add host-chat session isolation rule (rules/core/isolation.md) and forbid AI attribution trailers in rules/collab/external.md

- Add `rules/core/isolation.md` (`# Description: Host-chat session isolation and external platform tool boundary`) and include `rule core/isolation` as the first entry in `rulesets/core.ruleset` (before `rule core/start`) so every bundle begins by scoping the active session to the bundle rules and workspace `AGENTS.md` files and instructing the agent not to apply any host-chat persona/domain context or invoke built-in host platform tools (such as external knowledge-base or web search) unless explicitly requested by the user.
- Update `rules/collab/external.md` (`Clean external text & two-step external changes`) to forbid adding AI co-author trailers (such as `Co-Authored-By:`), agent attribution lines (such as `Generated with...`), or tool signatures to commit messages, MR/PR descriptions, comments, or files.
- Update `rules/role/plan.md` (`Role (Planner)`) to require bidirectional dependency-chain integration whenever adding or refining tasks (wiring both upstream prerequisites on the new task and downstream dependents/closing roots or milestone waves that touch the same target files or build on the capability, so tasks are not left as unintended standalone items).
- Wrap prose in `rules/core/isolation.md`, `rules/collab/external.md`, and `rules/role/plan.md` at ~80 columns without decorative bold/italic markup, and bump `VERSION` for a PATCH release.

# 🎯 [NEXT] F5: Wrap prose at ~80 columns across all remaining rule files

- Depends on: F31, F32, F33, F34, F35
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

# ⚪ [NEW] F36: Worker closes the task in the edit step, before the diff is verified clean

- Problem: the rules say `todo_md done` is run before the final commit in `role=work`, but do not say in which step. In session s210 it was run in the edit-and-diff step, before the self-review of the diff was finished.
- Impact: if the diff had turned out unclean, the task would already be archived as DONE with unfinished implementation and would need a reopen; until the commit, the working tree also shows a closed task with no matching implementation commit.

# ⚪ [NEW] F37: Worker-recorded backlog items have no defined commit path when no code commit follows

- Problem: in `role=work`, `todo_md` mutations are not committed with `-c` and are expected to be staged into the final code commit. When the worker records an out-of-scope finding as a new backlog item after the final code commit is already pushed (or in any session where no code commit follows), the rules do not say what happens to the resulting `TODO.md` change.
- Observed in session s210: F36 was added after the release commit was pushed and stayed uncommitted in the working tree until the user pointed it out; the worker also asked whether to link it into a chain, which is outside the worker role (chain placement belongs to the planner).
- Impact: backlog items can stay unpublished or be lost between sessions, and the start-of-session check ignores uncommitted task-backlog changes, so the gap is not caught later.

# ⚪ [NEW] F38: Worker has no guidance on how to record a new backlog item

- Problem: the rules describe `todo_md` mechanics, but not what a worker-authored backlog item should contain or where the worker responsibility ends. The planner decides the solution, chain placement, and priority together with the user.
- Observed in session s210: the worker wrote F36 as a ready solution (target file and wording to add) instead of describing the problem, and asked the user whether to link the new task into a chain, which belongs to the planner.
- Impact: planner discussion is pre-empted, task bodies are inconsistent between sessions, and the worker overreaches its role.
