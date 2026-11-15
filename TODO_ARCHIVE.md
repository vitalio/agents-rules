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
