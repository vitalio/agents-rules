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
