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

- Expand `rules/core/composability.md` with universal software engineering code structure principles: modular cohesion and file-size discipline (keeping source modules under `src/` focused on a single responsibility at roughly 300-800 lines and splitting modules that exceed ~1000 lines or mix architectural layers), layered separation of concerns (separating pure data/parsing and domain/graph algorithms from TTY/ANSI rendering and CLI/I/O dispatch), focused functions at a single level of abstraction, and a single canonical algorithm per domain invariant rather than parallel implementations.

- Align `rules/role/{design,plan,work,review}.md` with `todo_flow:D6` (`docs/adr/0002-context-bundle-protocol-and-self-contained-producers.md`) so role definitions in `agents-rules` are completely self-sufficient once `todo_md.bundle` and its role-specific `prompt Mode: ...` lines are removed.

# 🎯 [NEXT] F5: Wrap prose at ~80 columns across all remaining rule files

- Depends on: F31, F32, F34
- Wrap long lines (>80 chars) across all remaining rule files in `rules/` (`rules/collab/*.md`, `rules/core/*.md`, `rules/os/*.md`, `rules/release/*.md`, `rules/role/*.md`, `rules/stack/*.md`, `rules/vcs/*.md`) to ~80 characters per line and bump `VERSION` for a PATCH release.

# ⚪ [NEW] F20: Replace rulesets with bundles and organize rules logically by domain

- Depends on: D1
- Standardize `agents/` as the single package root directory for all rules (`.md`) and bundles (`.bundle`), migrating `rulesets/core.ruleset` -> `agents/core.bundle`, `rulesets/default.ruleset` -> `agents/default.bundle`, `rulesets/orchestrator.ruleset` -> `agents/orchestrator.bundle`, and `rules/*` into `agents/*` (after `agents_bundle` supports the `agents/` layout and unified `.bundle` resolution).
- Extract software-engineering specifics out of universal `agents/role/{design,plan,work,review}.md` and `agents/core/composability.md` into the `agents/coding/` domain subtree (`agents/coding/AGENTS.md`, `agents/coding/coding.bundle`, `agents/coding/architecture.md`, `agents/coding/testing.md`, and additive role overlays `agents/coding/{design,plan,work,review}.md` activated via `[if role!=] rule coding/{role:}` in `agents/coding/coding.bundle`):
  - Keep base `agents/role/{design,plan,work,review}.md` strictly domain-agnostic (cognitive stance, artifact modification boundaries, target-file closure and `path:start-end` slice handoffs, two-stage review gate, and backlog lifecycle).
  - Place modular code structure rules (~300-800 line module budget under `src/`, splitting modules >1000 lines or mixing layers, layered separation between parsing/domain/rendering/CLI, single-abstraction-level functions, and a single canonical algorithm per domain invariant) in `agents/coding/architecture.md`.
  - Place language-agnostic test architecture rules (modular `tests/test_<module>.*` mirroring source modules, domain-behavior test naming without task-ID prefixes, offline/stubbed network isolation, temporary-directory filesystem isolation, and in-step test runs with live `.` progress indicators) in `agents/coding/testing.md`.
  - Place software-engineering role constraints (`src/` and `tests/` modification prohibition in `design`/`plan`/`review`, `docs/adr/NNNN-<slug>.md` and greenfield repo bootstrap in `design`, full code/CLI/doc/test target-file closure in `plan`, in-step and guarded-commit linter/test verification in `work`, and Stage 1 test/linter/doc compliance plus Stage 2 architecture/security/performance review in `review`) in `agents/coding/{design,plan,work,review}.md`.
- Decompose `rules/stack/python-cli.md`, `rules/stack/python-stdlib.md`, and `rules/stack/python-annotations.md` into an orthogonal `agents/stack/python/` subtree separate from `agents/stack/cli.md`:
  - `agents/stack/python/syntax.md` (`ast.parse` syntax verification).
  - `agents/stack/python/unittest.md` (strictly Python `unittest` mechanics: `python3 -m unittest discover -s tests` at default verbosity `1` without `-q`/`-v`/`-b`, shared base classes and fixtures in `tests/helpers.py` without `test_` prefix, `contextlib.redirect_stdout`/`redirect_stderr` output capture and `with` resource hygiene, `msg=proc.stderr` and `self.subTest(...)` failure diagnostics, `tempfile.TemporaryDirectory`, and programmatic test splitting via `ast.parse()` `node.lineno`..`node.end_lineno`).
  - `agents/stack/python/stdlib.md` (opt-in Python 3 standard-library-only invariant).
  - `agents/stack/python/annotations.md` (opt-in `from __future__ import annotations` for `{py_min:3.9}` and `src/header.py`).
  - `agents/stack/python/python.bundle` (default Python preset loading `rule stack/python/syntax` and `rule stack/python/unittest`).
- Update `.agents_bundle` (`include AGENTS.md` and `include agents/**/AGENTS.md`), `AGENTS.md`, and `README.md` to reflect the unified `agents/` rule/bundle layout, wrap all modified files at ~80 columns, and bump `VERSION` for a MINOR release.

# ⚪ [NEW] F25: Rename project and package references from agents-rules to ctx-taxonomy

- Rename package identity, documentation, and internal references from `agents-rules` (`vitalio/agents-rules`) to `ctx-taxonomy` (`vitalio/ctx-taxonomy`), aligned with the ecosystem rename design.
- Target files: `AGENTS.md`, `README.md`, `.agents_bundle`, `VERSION`, and exported rule/bundle files (`rules/`, `rulesets/`, or `agents/` after `F20`).
- Acceptance criteria: all docs, examples, and package references use `ctx-taxonomy` (alongside sibling names `ctx-bundle`/`cxb`, `todo-markdown`/`tmd`, `run-block`/`rxb`), `VERSION` is bumped appropriately, and repository checks pass.
