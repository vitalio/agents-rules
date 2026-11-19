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
