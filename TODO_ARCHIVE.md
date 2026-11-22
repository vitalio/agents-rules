# ❌ [CANCELED] F25: Rename project and package references from agents-rules to ctx-taxonomy — *vitalio/agents-rules keeps its repository and package name per todo_flow:D1/D8 (docs/adr/0003-task-targeted-bundle-architecture-and-atomic-rule-taxonomy.md)*

- Rename package identity, documentation, and internal references from `agents-rules` (`vitalio/agents-rules`) to `ctx-taxonomy` (`vitalio/ctx-taxonomy`), aligned with the ecosystem rename design.
- Target files: `AGENTS.md`, `README.md`, `.agents_bundle`, `VERSION`, and exported rule/bundle files (`rules/`, `rulesets/`, or `agents/` after `F20`).
- Acceptance criteria: all docs, examples, and package references use `ctx-taxonomy` (alongside sibling names `ctx-bundle`/`cxb`, `todo-markdown`/`tmd`, `run-block`/`rxb`), `VERSION` is bumped appropriately, and repository checks pass.

# ✅ [DONE] F42: Add opt-in collab/commits rule and remove other-task TODO.md cleanup from role=work diff review — *2026-11-22*

- Remove `rules/collab/no-task-ids.md` and create `rules/collab/commits.md` (`# Description: Opt-in commit message convention with imperative subjects, trailing task IDs, and no redundant release versions`):
  - Commit subject line: write a concise single-line summary in the imperative mood without a trailing period, describing what changed and why.
  - Trailing task ID suffix: when a commit implements, plans, or closes one or more repository backlog tasks, append the task ID(s) in parentheses at the end of the subject line (`<Summary> (<ID>)` or `<Summary> (<ID1>, <ID2>)`); omit the suffix for commits not tied to a backlog task.
  - No release version in commit subject: do not include `Release vX.Y.Z:` or `(vX.Y.Z)` in the commit subject when the version is already recorded in `VERSION` and the annotated git tag `vX.Y.Z`.
  - Optional commit body: separate the body from the subject with a blank line, wrap at roughly 72-80 columns, and explain non-obvious context or rationale without restating the diff line by line.
- Resolve the rule conflict between self-reviewed diff cleanup and `role=work` scope boundaries:
  - In `rules/core/diff-review.md` and `rules/stack/python-cli.md`, remove `and active backlog tasks in TODO.md` / `and active backlog task references to the old file in TODO.md` from pre-commit stale-reference cleanup so `role=work` cleans up stale references only in code, tests, CI workflows (`.github/workflows/`), `README.md`, and `AGENTS.md`.
  - In `rules/role/work.md`, explicitly state that stale references inside other backlog tasks (`- Target files:`, symbols, line numbers) are neither inspected nor edited in `role=work` (that belongs to `role=plan`): a single repository `grep` check and a single new backlog item describing the stale reference problem without a solution are sufficient.
- Enable `rule vitalio/agents-rules:collab/commits` in `.agents_bundle` and update the usage example in `README.md` (replacing `rule vitalio/agents-rules:collab/no-task-ids` with `rule vitalio/agents-rules:collab/commits`).
- Wrap prose at ~80 columns and bump `VERSION` (`MINOR`) with an annotated release tag.
- Target files: `rules/collab/commits.md`, `rules/collab/no-task-ids.md`, `rules/core/diff-review.md`, `rules/stack/python-cli.md`, `rules/role/work.md`, `.agents_bundle`, `README.md`, `VERSION`.

# ✅ [DONE] F41: Require explicit '- Target files:' bullet and drift-proof symbol slices in role/plan.md — *2026-11-22*

- Update `rules/role/plan.md` so the target-file closure bullet explicitly requires recording target repository files and slices on a dedicated `- Target files:` line (because `todo_md files` parses only `- Target files:` lines), prefers drift-proof symbol slices (`path:symbol` or `path:start_symbol..end_symbol`) alongside `path:start-end` for large files (`> 400` lines) so slices survive out-of-order task edits, and instructs planners not to include `TODO.md`, `TODO_ARCHIVE.md`, or `AGENTS.md` (unless `AGENTS.md` itself is being edited) in `- Target files:`.
- Target files: `rules/role/plan.md`.

# ❌ [CANCELED] F39: agents_bundle include silently ignores glob patterns — *Tracked in agents_bundle:F29 (glob include implementation) and agents-rules:F20 (.agents_bundle migration to include agents/**/AGENTS.md)*

- Observed in session s228 with `agents_bundle` 0.15.0: `include rules/**/AGENTS.md`, `include rules/*/AGENTS.md`, and `include rules/**/*.md` exit with rc=0 and emit no fragments and no warning, while `include rules/core/AGENTS.md` emits the file as expected.
- Context: `F32` needs every scoped category `AGENTS.md` preloaded, so `.agents_bundle` currently lists `rules/core/AGENTS.md` and `rules/role/AGENTS.md` explicitly; a new category `AGENTS.md` is silently missing from every session until someone adds a line by hand.
- Impact: context that the author believes is preloaded is absent without any signal, and the failure is invisible in the bundle output.

# ✅ [DONE] F5: Wrap prose at ~80 columns across all remaining rule files — *2026-11-21*

- Depends on: F31, F32, F34
- Wrap long lines (>80 chars) across all remaining rule files in `rules/` (`rules/collab/*.md`, `rules/core/*.md`, `rules/os/*.md`, `rules/release/*.md`, `rules/role/*.md`, `rules/stack/*.md`, `rules/vcs/*.md`) to ~80 characters per line and bump `VERSION` for a PATCH release.

# ✅ [DONE] F32: Add session isolation rule, forbid AI trailers, refine plan/work role protocols, and preload AGENTS.md via include globs — *2026-11-21, Added session isolation and AI attribution rules, refined plan/work/design/review roles, expanded code structure axioms, and preloaded scoped AGENTS.md files*

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

# ✅ [DONE] D1: Design composable role extensions and domain overlays — *2026-11-21, Designed composable role overlays (agents/coding/*) and orthogonal agents/stack/python/* subtree*

- Depends on: F16, F9
- Explore separating universal domain-agnostic role postures in `agents/role/` (cognitive stance, artifact permissions, and handoff contracts) from domain-specific role overlays (such as `agents/coding/design.md`, `agents/coding/plan.md`, `agents/coding/work.md`, and `agents/coding/review.md`) activated automatically via `[if role=...]` inside domain bundles.
- Define how projects compose base roles with one or more domain overlays without duplicating rules or leaking software-engineering assumptions into universal roles, feeding into `F20`.
- Apply orthogonal facet decomposition (`AGENTS.md`): separate cross-language interface contracts (`cli.md`) from language subtrees (`python/syntax.md`, `python/unittest.md`, `python/stdlib.md`, `python/annotations.md`, plus a default `python.bundle` preset) so projects never rely on hybrid filenames like `python-cli.md`.

- Promote universal modular code and test architecture rules (module cohesion, ~300-800 line module budget, layered separation between parsing/domain/rendering/CLI, single canonical domain algorithms, and mirrored `tests/test_<module>.py` organization) to `core/composability.md` (or the `coding/` domain overlay), keeping `python/unittest.md` focused strictly on Python `unittest` mechanics (`unittest discover -s tests`, `tests/helpers.py`, `ast.parse()`).

# ❌ [CANCELED] F36: Clarify worker task-closing step and out-of-scope backlog recording in rules/role/work.md — *Consolidated into F32*

- In `rules/role/work.md`, clarify the task completion and out-of-scope backlog recording protocol for `role=work`:
  - Close the active backlog task only inside the final commit step (after the edit-and-diff step has completed and the printed diff has been verified clean), never inside the edit-and-diff step before diff verification.
  - When recording an out-of-scope finding as a new backlog item, describe the observed problem, context, and impact without prescribing a design/solution, assigning chain dependencies, or asking the user about chain placement or priority (which belong to `role=plan`).
  - Stage backlog additions recorded before the final code commit into that commit; if an out-of-scope item is recorded after the final code commit is already created/pushed (or in a session where no code commit follows), commit and push the backlog file update immediately so it is not left uncommitted in the working tree.
- Wrap prose in `rules/role/work.md` at ~80 columns without decorative bold/italic markup, and bump `VERSION` for a PATCH release.

# ❌ [CANCELED] F35: Preload root AGENTS.md and scoped rules/**/AGENTS.md via include in .agents_bundle — *Consolidated into F32*

- In `.agents_bundle`, replace `$ cat AGENTS.md` with declarative `include AGENTS.md` and `include rules/**/AGENTS.md` directives so root `AGENTS.md` and all scoped category `AGENTS.md` files (`rules/core/AGENTS.md`, `rules/role/AGENTS.md`, and any future category `AGENTS.md` files) are preloaded as discrete `include` bundle fragments in every session.
- Wrap long prose lines in `rules/core/AGENTS.md` at ~80 columns to match `AGENTS.md` and `rules/role/AGENTS.md`.

# ❌ [CANCELED] F33: Specify planner line-range preloading (path:start-end) on NEXT promotion and atomic planning session boundary in rules/role/plan.md — *Consolidated into F32*

- In `rules/role/plan.md`:
  - Update the target-file closure bullet so that while long-term `NEW` backlog tasks reference file paths and key symbol names in backticks (avoiding brittle line numbers across unrelated commits), once the user agrees to promote a task to `NEXT`, the planner records exact `path:start-end` line ranges in backticks for any inspected files that exceed single-file bundle size budgets so a subsequent `role=work` session bundle preloads those slices directly.
  - Scope each `role=plan` session to an atomic planning goal: once the agreed task updates, dependency edges, and priorities are persisted, committed, and pushed in `TODO*.md`, end the planning session immediately without asking which task to work on next or spawning another task session (each subsequent task runs in its own new session).
- Verify line wrapping (~80 columns) and bump `VERSION` for a PATCH release.

# ❌ [CANCELED] F38: Worker has no guidance on how to record a new backlog item — *Consolidated into F36*

- Problem: the rules describe `todo_md` mechanics, but not what a worker-authored backlog item should contain or where the worker responsibility ends. The planner decides the solution, chain placement, and priority together with the user.
- Observed in session s210: the worker wrote F36 as a ready solution (target file and wording to add) instead of describing the problem, and asked the user whether to link the new task into a chain, which belongs to the planner.
- Impact: planner discussion is pre-empted, task bodies are inconsistent between sessions, and the worker overreaches its role.

# ❌ [CANCELED] F37: Worker-recorded backlog items have no defined commit path when no code commit follows — *Consolidated into F36*

- Problem: in `role=work`, `todo_md` mutations are not committed with `-c` and are expected to be staged into the final code commit. When the worker records an out-of-scope finding as a new backlog item after the final code commit is already pushed (or in any session where no code commit follows), the rules do not say what happens to the resulting `TODO.md` change.
- Observed in session s210: F36 was added after the release commit was pushed and stayed uncommitted in the working tree until the user pointed it out; the worker also asked whether to link it into a chain, which is outside the worker role (chain placement belongs to the planner).
- Impact: backlog items can stay unpublished or be lost between sessions, and the start-of-session check ignores uncommitted task-backlog changes, so the gap is not caught later.

# ✅ [DONE] F31: Specify --help column alignment, {prog} placeholder accounting, and <=100-col width in rules/stack/cli.md — *2026-11-21*

- In `rules/stack/cli.md` (`Structured -h/--help layout`), require aligned description columns within each section (accounting for the rendered program name length when `{prog}` templates are used so continuation lines align with primary descriptions) and a maximum `--help` line width of 100 columns (~80 columns for prose paragraphs).
- Wrap rule prose in `rules/stack/cli.md` at ~80 characters per line and bump `VERSION` for a PATCH release.

# ✅ [DONE] F34: Enforce brief between-step worker prose, in-step test runs, and domain-named test methods — *2026-11-21*

- In `rules/role/work.md` (`Role (Worker)`), require chat prose before each execution block across multi-step reads or staged edits to stay within 1-2 short sentences without dumping multi-point code analysis, intermediate breakdowns, or implementation plans in visible chat.
- In `rules/core/edit.md` (`Edit & pre-commit verification`) and `rules/core/diff-review.md` (`Self-reviewed diff before commit`), forbid dedicating a standalone execution step solely to running tests after an edit: run syntax checks and unit tests inside the same step immediately after any self-consistent edit, and when a large change is split across sequential steps solely to stay within output token limits (leaving code and tests temporarily out of sync, such as updating source modules in one step and test files in the next), run only syntax/build checks in intermediate steps and run the full test suite at the end of the final edit step together with `git status --porcelain` and `git diff HEAD`.
- In `rules/stack/python-cli.md` and `rules/collab/no-task-ids.md`, require unit test methods and classes in `tests/test_*.py` to be named and grouped strictly by domain behavior and component invariants (such as `test_bundle_table_hierarchy`, `test_fullscreen_info_part_cursor`, `test_clipboard_prompt_action`) without backlog task-ID prefixes (`test_f47_...`, `test_b11_...`), updating the component's domain test when a contract evolves rather than accumulating ticket-numbered test methods.
- Wrap rule prose in `rules/role/work.md`, `rules/core/edit.md`, `rules/core/diff-review.md`, `rules/stack/python-cli.md`, and `rules/collab/no-task-ids.md` at ~80 columns and bump `VERSION` for a PATCH release.

# ✅ [DONE] F13: Define role handoff contracts, target-file closure, and preloaded-context execution in rules/role/ — *2026-11-20, Defined role handoff contracts, target-file closure, and preloaded-context execution across rules/role/*

- Depends on: F9, F16
- Update `rules/role/plan.md` so the Planner balances task decomposition and task composition (consolidation) based on module, test, and documentation cohesion:
  - Distinguish raw ideas/design tasks (routing them to `role=design`) from ready work items.
  - Decompose large or multi-stage initiatives into sequential, self-contained tasks (keeping the original task as the terminal closing root of the dependency chain with newly extracted steps wired as its prerequisites).
  - Compose (consolidate) work into an existing open task in place rather than creating separate tasks when requirements overlap or touch the same target files, tests, and documentation in a single coherent change (merging overlapping or standalone doc-only tasks into the primary implementation task and closing duplicates with a reference to the target task).
  - Determine the full target file closure for each prioritized task (source modules, CLI help, docs, paired rules, and tests per `AGENTS.md` and active stack rules), record those file paths in the task body, and preload them into the new session context when handing off to working.
- Update `rules/role/work.md` so that when a task's target files are already preloaded in the initial session context, the agent skips a separate read-only discovery step and proceeds directly in step 1 to edits, project build/linter/test verification, and diff output (running an initial batched read step only for files not yet in context).
- Update `rules/role/design.md` and `rules/role/review.md` so Designer records module-boundary and file-coupling invariants in `AGENTS.md` for downstream planning/working, and Reviewer verifies those project-specific `AGENTS.md` invariants alongside task specifications, keeping wording strictly tool-agnostic, and release a PATCH version.

# ✅ [DONE] F4: Support greenfield project bootstrap and tool-agnostic wording in role/design — *2026-11-20*

- Update `rules/role/design.md` so that when designing a new project from scratch, once the design is agreed with the user, the agent creates the target project directory, initializes version control, and scaffolds `AGENTS.md`, project context configuration, and the initial project task backlog before committing the initial scaffold.
- Clarify in `rules/role/design.md` that raw ideas and architectural explorations enter the backlog as design tasks for `role=design`, and once agreed are closed after recording architectural invariants in `AGENTS.md` and creating actionable implementation tasks.
- Replace the hardcoded `.agents_bundle` filename in `rules/role/design.md` with tool-agnostic wording so `rules/role/` complies with `AGENTS.md` and `rules/role/AGENTS.md` taxonomic invariants, and release a PATCH version.

- Specify in `rules/role/design.md` that when a design decision involves complex protocols, trade-offs, or multi-component rationale too detailed for `AGENTS.md`, the agent records a concise Architecture Decision Record in `docs/adr/NNNN-<slug>.md` (context, decision, rejected alternatives, consequences) and references it in backticks in downstream implementation tasks.

# ✅ [DONE] F30: Require modular test files in tests/ and shared fixtures in tests/helpers.py — *2026-11-20*

- Role: work
- In `rules/stack/python-cli.md`, add a modular test organization requirement: split unit tests across domain- or module-focused `tests/test_<module>.py` files mirroring `src/` modules (rather than accumulating all tests into a single monolithic `tests/test_<project>.py`), and place shared base `unittest.TestCase` classes, in-process CLI runners, and fixtures in `tests/helpers.py` (without a `test_` prefix so `unittest discover -s tests` loads the target script once and does not execute the base class standalone).
- Note in `rules/stack/python-cli.md` that when splitting an existing large test file into modular `tests/test_*.py` files, agents should slice test methods programmatically on disk using `ast.parse()` (`node.lineno`..`node.end_lineno`) rather than re-emitting test bodies in chat output.
- Verify prose wrapping (~80 columns) and bump `VERSION` for a PATCH release.

# ✅ [DONE] F29: Sync with origin before starting work and push release tags atomically — *2026-11-20, Updated rules/vcs/git.md and rules/release/semver.md to require upstream git sync before work/backlog mutations and atomic release tag pushes*

- Role: work
- Update `rules/vcs/git.md` to require syncing with the upstream remote (`git pull --ff-only`, or `git fetch` + `git status -sb` when local edits exist) before starting a task or modifying the backlog, pausing on branch divergence before making commits or bumping `VERSION`, and wrap prose at ~80 characters per line.
- Update `rules/vcs/git.md` and `rules/release/semver.md` to push release branches and tags atomically (`git push --atomic origin {main_branch:main} "v$ver"`) so a rejected branch push never leaves an orphaned release tag on the remote.
- Release a PATCH version in `VERSION`.

# ✅ [DONE] F28: Preserve live dot-progress test output and forbid piping test runners through tail/head/grep — *2026-11-19, Updated rules/core/edit.md, rules/core/diff-review.md, and rules/stack/python-cli.md to preserve live dot-progress test output and forbid piping test runners through tail, head, or grep*

- Role: work
- Update `rules/core/edit.md` and `rules/core/diff-review.md` to replace "emit a single concise summary line" with requiring compact live progress indicators (such as per-test `.` dots followed by the summary line) and explicitly forbid piping test runner output through `tail`, `head`, or `grep` (or suppressing it via redirection), which buffers live progress and truncates failure tracebacks.
- Update `rules/stack/python-cli.md` (`Concise unittest execution`) to require running `python3 -m unittest discover -s tests` directly without piping to `tail`/`head`/`grep` or wrapping in custom `verbosity=0` runners so `.` progress indicators stream live as tests execute.
- Keep prose wrapped at ~80 characters per line and release a PATCH version in `VERSION`.

# ✅ [DONE] F23: Add portable multi-repository coordination rule and orchestrator bundle preset — *2026-11-20*

- Add a universal, tool-agnostic rule (for example `rules/collab/multi-repo.md` or `rules/role/multi-repo-plan.md`) defining cross-repository task decomposition and dependency boundaries: detailed implementation tasks belong in each owning repository's backlog, while the coordinating repository records a parent task linking all child tasks via dependencies and keeps cross-repository dependency edges out of standalone child repositories.
- Add `rulesets/orchestrator.ruleset` (migrating to `agents/orchestrator.bundle` under `F20`) exporting the multi-repository coordination rule so orchestrator repositories can compose it directly without duplicating prose in local `AGENTS.md` files.
- Follow `AGENTS.md` formatting conventions (`# Description:` header, plain `- Topic: instruction.` bullets, ~80-char line wrapping, no tool-specific names), update `README.md` if needed, and bump `VERSION` for a MINOR release.

# ✅ [DONE] F24: Remove bundle vitalio/run_block from .agents_bundle and README.md — *2026-11-19*

- Remove `bundle vitalio/run_block` from `.agents_bundle` and the `.agents_bundle` usage example in `README.md` once `run_block` embeds its own block execution rules.

# ✅ [DONE] F9: Rename role/execute to role/work — *2026-11-19*

- Rename `rules/role/execute.md` to `rules/role/work.md` with `Universal Worker role` description and `- Role (Worker):` heading.
- Update `rules/role/AGENTS.md` and `rules/role/plan.md` to replace `execute`/`executing` role references with `work`/`working`, ensure `README.md` omits explicit role inventories per `AGENTS.md`, and release a new MINOR version.

# ✅ [DONE] F16: Rename role/audit to role/review with two-stage quality gate — *2026-11-19*

- Rename `rules/role/audit.md` to `rules/role/review.md` with `Universal Reviewer role` description and `- Role (Reviewer):` heading.
- Structure `rules/role/review.md` as a two-stage review: first verify objective compliance (passing tests and linters, task specification fulfillment, active workspace rules, SSOT, and documentation sync), stopping early on blockers; once the objective gate passes, evaluate architecture, module boundaries, readability, security, performance, and user-facing polish.
- Update `rules/role/AGENTS.md` to replace `audit`/`auditing` with `review`/`reviewing`, remove the explicit role list from `README.md` per `AGENTS.md` directory-listing rules, and release a new MINOR version.

# ✅ [DONE] F27: Clarify SemVer planning rules and version notation in rules/release/semver.md — *2026-11-19*

- Update `rules/release/semver.md` to explicitly forbid hardcoding concrete version numbers in tasks, plans, or backlog items ahead of implementation (specify only the bump level `PATCH`, `MINOR`, or `MAJOR` and compute the next version dynamically from `VERSION` at release time).
- Unify the `PATCH` and `MINOR` pattern examples in `rules/release/semver.md` from `0.Y.Z+1` and `0.Y+1.0` to `X.Y.Z+1` and `X.Y+1.0` for consistency with `MAJOR` (`X+1.0.0`) and `PRE-RELEASE` (`X.Y.Z-...`).
- Clarify that bumping `VERSION` dynamically inside the guarded commit step before final build, tests, commit, and tag does not require an extra diff-review round-trip.
- Keep wording strictly tool-agnostic, wrap prose at ~80 characters per line, avoid decorative bold/italic emphasis per `AGENTS.md`, and release a PATCH version per `rules/release/semver.md`.

# ✅ [DONE] F26: Add bounded edit-stage rule to avoid oversized output blocks — *2026-11-19, Added bounded edit-stage rule to core/edit and multi-stage diff clarification to core/diff-review*

- Update `rules/core/edit.md` to require bounding the size of any single edit step or emitted patch/literal so a response never risks exceeding chat output limits; when a change spans many files or requires large edits, split the work into sequential, self-consistent stages (for example module by module, or implementation then tests and docs), running syntax checks and compact tests between stages as needed.
- Update `rules/core/diff-review.md` to clarify that when a task is implemented across multiple edit stages, full `git status --porcelain` and `git diff HEAD` output for pre-commit self-review is emitted once all planned edit stages are complete (while intermediate stages may still run syntax checks and compact test suites).
- Keep wording strictly tool-agnostic (no references to sibling tools), wrap prose at ~80 characters per line, avoid decorative bold/italic emphasis per `AGENTS.md`, and release a PATCH version per `rules/release/semver.md`.

# ✅ [DONE] F18: Define responsibility split between README.md and AGENTS.md in core/docs — *2026-11-19*

- Add `rules/core/docs.md` (1–3 plain-text `- Topic: instruction.` bullets per `rules/core/AGENTS.md`, keeping domain-independent framing with items such as CLI flags, environment variables, or I/O protocols as illustrative examples where applicable) defining the separation of concerns between `README.md` (external public contract: purpose, installation, interfaces/configuration, protocols, and integration examples) and `AGENTS.md` (concise internal engineering guide: module boundaries, cross-file invariants, negative constraints, and build/test verification steps).
- Forbid duplicating `README.md` tutorials, marketing descriptions, or full reference tables inside `AGENTS.md`, keeping `AGENTS.md` focused on repository-specific delta knowledge an agent cannot infer from the file tree.
- Define the role of `docs/adr/` (Architecture Decision Records) in `rules/core/docs.md` as the place for detailed architectural rationale and rejected alternatives, keeping `AGENTS.md` concise and actionable while referencing relevant `docs/adr/*.md` paths in task descriptions.
- Move the documentation synchronization and `AGENTS.md` plain-text formatting clauses out of `rules/core/edit.md` into `rules/core/docs.md` (updating `# Description:` in `rules/core/edit.md` accordingly, while keeping the ~80-character prose-wrapping clause in `rules/core/edit.md`) so documentation rules live in one canonical place without duplication.
- Include `rule core/docs` in `rulesets/core.ruleset` (or the corresponding core bundle if executed after F20), follow `AGENTS.md` formatting conventions, bump `VERSION` for a new MINOR release, and tag the release.

# ✅ [DONE] F19: Extract internal task ID restriction from collab/external into a separate opt-in rule — *2026-11-19, Extracted internal task ID restriction to collab/no-task-ids and released v0.12.0*

- Remove the internal task ID restriction from `rules/collab/external.md` and move it into a separate opt-in rule (`rules/collab/no-task-ids.md`) so projects can include it only when they want to hide task IDs in commits and external updates.
- Keep `rulesets/default.ruleset` (or the corresponding default bundle if executed after F20) and `README.md` in sync, and release a new MINOR version.

# ✅ [DONE] F6: Group bundle directives at the top of .agents_bundle — *2026-11-19*

- Move `bundle vitalio/todo_md` to the top of `.agents_bundle` alongside `bundle vitalio/agents_bundle` before `ruleset`, `rule`, and `$ <cmd>` directives (already supported since `agents_bundle` v0.12.2).
- Keep the `.agents_bundle` usage example in `README.md` in sync.

# ✅ [DONE] F12: Define pre-release versioning convention in release/semver — *2026-11-19, Added PRE-RELEASE clause to rules/release/semver.md and bumped VERSION to 0.11.1*

- Add an optional `PRE-RELEASE` clause (`X.Y.Z-alpha.N`, `X.Y.Z-beta.N`, `X.Y.Z-rc.N` starting at `N=1`) to `rules/release/semver.md` for experimental or staged builds when explicitly requested, specifying that pre-release identifiers attach to the upcoming target version `X.Y.Z` and are stripped without re-bumping `X.Y.Z` upon final release.
- Bump `VERSION` for a PATCH release.

# ✅ [DONE] F22: Split python-cli into a base rule and opt-in Python extension rules — *2026-11-16*

Found while evaluating `stack/python-cli` for canary; it cannot be connected as is. Keep only the universal base in `stack/python-cli` and move specifics into opt-in extension rules.

Target files: `rules/stack/python-cli.md`, `rules/stack/python-stdlib.md` (new), `rules/stack/python-annotations.md` (new), `README.md`, `VERSION`.

- Base `rules/stack/python-cli.md`: keep `ast.parse` syntax verification, offline unit tests for every CLI flag and behavior in `tests/test_*.py`, `python3 -m unittest discover -s tests` without `-q`, `-v`, `-b`, and the unit test hygiene, diagnostics, and filesystem isolation bullets. Add that code under test writing to stderr must be captured with `contextlib.redirect_stderr` so the progress line stays clean. Drop the standard-library-only invariant, the `from __future__ import annotations` requirement, and the `py_min` parameter; update `# Description:` so it no longer claims zero dependencies. Third-party clients (such as boto3) are replaced by stubs in tests.
- New `rules/stack/python-stdlib.md`: opt-in invariant to use only the Python 3 standard library, for dependency-free tools.
- New `rules/stack/python-annotations.md` with `{py_min:3.9}`: require `from __future__ import annotations` only in files whose annotations use syntax newer than `{py_min}` (such as `X | None` below 3.10) or forward references; not required for files without annotations.
- Update `README.md` (usage example with `py_min=3.9`) so consumers add the new `rule` lines when they need the removed invariants, and release a MINOR version.
- Do the move atomically in one commit so the rules never contradict each other. Related: `F5` wraps these files.

Clarifications agreed during planning:
- `rules/stack/python-annotations.md`: with `release/single-file-build`, the
  `from __future__ import annotations` import stays once in the header of the
  assembled file (`src/header.py`) and covers all modules; modules under `src/`
  do not carry their own import. Document that annotations evaluated at
  runtime (dataclasses, `get_type_hints`) are not fixed by this import.
- `README.md`: drop `py_min=3.9` from the `stack/python-cli` line and show the
  `stack/python-stdlib` and `stack/python-annotations py_min=3.9` lines.
- `rules/stack/python-stdlib.md` also covers `build.py` and tests.
- Base `rules/stack/python-cli.md`: say that third-party clients are replaced
  by stubs in tests (`unittest.mock.patch.dict` on `sys.modules`) and that
  tests never touch the network.
- Check: `agents_bundle rule` renders `python-cli` without `py_min`, and
  `python-annotations py_min=3.9` substitutes the parameter. Release `0.11.0`.
  Consumers refresh the package cache once per machine afterwards.

# ❌ [CANCELED] F11: Remove leftover .bundle authoring references from AGENTS.md — *Superseded by F20: rulesets are being replaced by .bundle files*

- Remove '.bundle' references from AGENTS.md lines 22 and 30 since agents-rules only hosts rules/ and rulesets/ after moving tool bundles to their own repositories in v0.10.0.

# ✅ [DONE] F10: Specify structured --help layout and complete option listings in stack/cli — *2026-11-16*

- Update `rules/stack/cli.md` to require structured `Usage:`/`Commands:` and `Options:` sections in `-h`/`--help` output (showing short/long flag forms, argument placeholders, defaults, and side effects such as Git commits or network calls) rather than burying flags in prose or listing partial option sets.

# ✅ [DONE] F21: Remove redundant test start-indicator requirement from core and stack rules — *2026-11-16*

- Remove the requirement to print a start/progress indicator (such as `Running unit tests...`) before running tests from `rules/core/edit.md`, `rules/core/diff-review.md`, and `rules/stack/python-cli.md`, while preserving concise pass summaries and full diagnostics/tracebacks on failure.
- Bump `VERSION` (`PATCH`) and release the updated rule set.

# ✅ [DONE] F17: Use default unittest verbosity 1 for dot progress instead of -q — *2026-11-16, Updated Concise unittest execution in rules/stack/python-cli.md*

- Update `Concise unittest execution` in `rules/stack/python-cli.md` to run `python3 -m unittest discover -s tests` (default verbosity `1`, without `-q`, `-v`, or `-b`/`--buffer`) instead of `-q` (`verbosity=0`), so `unittest` emits compact `.` progress indicators per test on a single line followed by the summary while still keeping unexpected test stdout unbuffered and visible.

# ❌ [CANCELED] F7: Verify completed task specification compliance in role/audit — *Superseded by F16: renamed role/audit to role/review with two-stage verification*

- Update rules/role/audit.md so that when auditing a completed task or commit, the auditor verifies that the implementation, tests, and documentation fulfill all requirements of the task specification alongside all active workspace rules.

# ✅ [DONE] F15: Add unit test output hygiene and failure diagnostics rules in stack/python-cli — *2026-11-15, Added unit test output hygiene, failure diagnostics, and filesystem isolation rules to rules/stack/python-cli.md*

- Update `rules/stack/python-cli.md` with unit test authoring rules for `tests/test_*.py`:
  - Capture expected CLI `stdout`/`stderr` (`contextlib.redirect_stdout`, `redirect_stderr`, or `subprocess.run(..., capture_output=True)`), manage files and subprocesses with `with` context managers to prevent `ResourceWarning`, and strip temporary debug `print()` calls before committing.
  - Include diagnostic context (`msg=proc.stderr` or captured output) when asserting subprocess exit codes or side effects and use `with self.subTest(...):` for parameterized cases, without requiring redundant `msg=` on plain value assertions where `unittest` diffs already suffice.
  - Isolate filesystem operations inside `tempfile.TemporaryDirectory` without mutating the repository working tree or user environment.
- Follow `AGENTS.md` formatting conventions (plain bullet list, ~80-character line wrapping, no decorative bold/italic emphasis) and bump `VERSION` for a `PATCH` release (`0.10.4`).

# ✅ [DONE] F14: Standardize concise test runner output with start indicator and full failure details — *2026-11-15, Standardized concise test-runner output rules across core/edit, core/diff-review, and stack/python-cli*

- Update `rules/core/edit.md` and `rules/core/diff-review.md` to define balanced test-execution output rules: print a brief start/progress indicator before running the test suite, emit a single concise summary line when all tests pass (avoiding verbose per-test output across large suites), and display full diagnostics and tracebacks only on test failure.
- Update `rules/stack/python-cli.md` with an idiomatic offline `unittest` invocation pattern matching the concise-on-pass / verbose-on-failure rule without altering test assertions or hiding unexpected stdout inside tests.
- Wrap all updated rule prose at ~80 columns and follow `AGENTS.md` plain-bullet formatting rules.

# ✅ [DONE] F1: Bootstrap .agents_bundle and TODO.md and refine semver/todo_md release rules — *2026-11-14*

- Add .agents_bundle and initialize TODO.md / TODO_ARCHIVE.md in agents-rules.
- Require staging task-backlog updates (--no-commit) before the release commit so release tags point to HEAD.
- Clarify PATCH and MINOR criteria for rule/ruleset/bundle changes in rules/release/semver.md.

# ✅ [DONE] F2: Move tool bundles to tool repositories and remove --agents from stack/cli rule — *2026-11-14*

# ✅ [DONE] F3: Align core/plan and role/execute for pre-agreed backlog tasks — *2026-11-14, Aligned core/plan, role/execute, and core/start for pre-agreed backlog tasks*

- Update `rules/core/plan.md` so high-level plan + waiting for user agreement is required when task scope is not yet agreed, and explicitly forbid emitting a plan and file modifications (or code dumps) in the same message.
- Update `rules/role/execute.md` so that for an already-agreed backlog task, after batched file inspection the agent proceeds directly to the edit/test/diff step without outputting a redundant implementation plan or code in chat prose (pausing only on blockers or conflicts).
- Update `rules/core/start.md` so uncommitted changes limited to project task-backlog files do not block starting an execution session on the queued task.

# ✅ [DONE] F8: Scope file reads and recursive searches to target directories in core/plan — *2026-11-15, Scoped file reads and recursive searches to target directories in core/plan*

- Update `rules/core/plan.md` so file reads and searches are scoped to the current working repository (or specific known project/cache paths) and recursive searches (`grep -r`, `find`, etc.) across `$HOME`, parent directories, or `/` are forbidden.
