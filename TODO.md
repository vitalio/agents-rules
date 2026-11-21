# 🎯 [NEXT] F34: Enforce brief between-step worker prose, in-step test runs, and domain-named test methods

- In `rules/role/work.md` (`Role (Worker)`), require chat prose before each execution block across multi-step reads or staged edits to stay within 1-2 short sentences without dumping multi-point code analysis, intermediate breakdowns, or implementation plans in visible chat.
- In `rules/core/edit.md` (`Edit & pre-commit verification`) and `rules/core/diff-review.md` (`Self-reviewed diff before commit`), forbid dedicating a standalone execution step solely to running tests after an edit: run syntax checks and unit tests inside the same step immediately after any self-consistent edit, and when a large change is split across sequential steps solely to stay within output token limits (leaving code and tests temporarily out of sync, such as updating source modules in one step and test files in the next), run only syntax/build checks in intermediate steps and run the full test suite at the end of the final edit step together with `git status --porcelain` and `git diff HEAD`.
- In `rules/stack/python-cli.md` and `rules/collab/no-task-ids.md`, require unit test methods and classes in `tests/test_*.py` to be named and grouped strictly by domain behavior and component invariants (such as `test_bundle_table_hierarchy`, `test_fullscreen_info_part_cursor`, `test_clipboard_prompt_action`) without backlog task-ID prefixes (`test_f47_...`, `test_b11_...`), updating the component's domain test when a contract evolves rather than accumulating ticket-numbered test methods.
- Wrap rule prose in `rules/role/work.md`, `rules/core/edit.md`, `rules/core/diff-review.md`, `rules/stack/python-cli.md`, and `rules/collab/no-task-ids.md` at ~80 columns and bump `VERSION` for a PATCH release.

# 🎯 [NEXT] F33: Specify planner line-range preloading (path:start-end) for large inspected files when promoting a task to NEXT in rules/role/plan.md

- In `rules/role/plan.md`, update the target-file closure bullet so that while long-term `NEW` backlog tasks reference file paths and key symbol names in backticks (avoiding brittle line numbers across unrelated commits), once the user agrees to promote a task to `NEXT` or take it into `role=work` next, the planner records exact `path:start-end` line ranges in backticks for any inspected files that exceed single-file bundle size budgets so the initial `role=work` bundle preloads those slices directly.
- Verify line wrapping (~80 columns) and update `README.md` or `VERSION` if needed.

# 🎯 [NEXT] F32: Add host-chat session isolation rule (rules/core/isolation.md) and forbid AI attribution trailers in rules/collab/external.md

- Add `rules/core/isolation.md` (`# Description: Host-chat session isolation and external platform tool boundary`) and include `rule core/isolation` as the first entry in `rulesets/core.ruleset` (before `rule core/start`) so every bundle begins by scoping the active session to the bundle rules and workspace `AGENTS.md` files and instructing the agent not to apply any host-chat persona/domain context or invoke built-in host platform tools (such as external knowledge-base or web search) unless explicitly requested by the user.
- Update `rules/collab/external.md` (`Clean external text & two-step external changes`) to forbid adding AI co-author trailers (such as `Co-Authored-By:`), agent attribution lines (such as `Generated with...`), or tool signatures to commit messages, MR/PR descriptions, comments, or files.
- Update `rules/role/plan.md` (`Role (Planner)`) to require bidirectional dependency-chain integration whenever adding or refining tasks (wiring both upstream prerequisites on the new task and downstream dependents/closing roots or milestone waves that touch the same target files or build on the capability, so tasks are not left as unintended standalone items).
- Wrap prose in `rules/core/isolation.md`, `rules/collab/external.md`, and `rules/role/plan.md` at ~80 columns without decorative bold/italic markup, and bump `VERSION` for a PATCH release.

# 🎯 [NEXT] F31: Specify --help column alignment, {prog} placeholder accounting, and <=100-col width in rules/stack/cli.md

- In `rules/stack/cli.md` (`Structured -h/--help layout`), require aligned description columns within each section (accounting for the rendered program name length when `{prog}` templates are used so continuation lines align with primary descriptions) and a maximum `--help` line width of 100 columns (~80 columns for prose paragraphs).
- Wrap rule prose in `rules/stack/cli.md` at ~80 characters per line and bump `VERSION` for a PATCH release.

# 🎯 [NEXT] F5: Wrap prose at ~80 columns across all remaining rule files

- Depends on: F31, F32, F33, F34
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
- Update `AGENTS.md` and `README.md` to reflect the unified `agents/` rule/bundle layout, and release a new MINOR version.

# ⚪ [NEW] F25: Rename project and package references from agents-rules to ctx-taxonomy

- Rename package identity, documentation, and internal references from `agents-rules` (`vitalio/agents-rules`) to `ctx-taxonomy` (`vitalio/ctx-taxonomy`), aligned with the ecosystem rename design.
- Target files: `AGENTS.md`, `README.md`, `.agents_bundle`, `VERSION`, and exported rule/bundle files (`rules/`, `rulesets/`, or `agents/` after `F20`).
- Acceptance criteria: all docs, examples, and package references use `ctx-taxonomy` (alongside sibling names `ctx-bundle`/`cxb`, `todo-markdown`/`tmd`, `run-block`/`rxb`), `VERSION` is bumped appropriately, and repository checks pass.
