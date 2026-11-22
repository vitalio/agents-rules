# Description: Two-step self-reviewed diff before commit and fail-fast guarded commit steps
- Self-reviewed diff before commit: An edit step does not commit immediately
  — it runs syntax/linter checks and local tests inside the same step
  immediately after the edit (never dedicating a standalone execution step
  solely to running tests; emitting compact live progress indicators such as
  per-test `.` dots followed by the summary line when all tests pass, and full
  diagnostics and tracebacks on failure, without piping test output through
  `tail`, `head`, or `grep` or suppressing it via redirection), then prints
  the working status and full diff.
  - When a task is implemented across multiple bounded edit stages, run syntax
    checks and unit tests inside each self-consistent stage, or when sequential
    stages temporarily leave code and tests out of sync solely to stay within
    output token limits (such as updating source modules in one step and test
    files in the next), run only syntax/build checks in intermediate stages and
    run the full test suite at the end of the final edit stage together with
    the working status and full diff for self-review.
  - When the user provides the output, the model itself must audit the full
    diff against all project rules (no dead code or leftover names, clean
    module boundaries, updated documentation and help text). When a change
    removes, renames, or splits files or symbols, search the entire repository
    for stale references in code, tests, CI workflows (`.github/workflows/`),
    `README.md`, and `AGENTS.md`, and clean up any orphaned artifacts before
    committing. If any issue is found in the diff, fix it in the next step and
    re-verify the diff until completely clean.
  - Once the model verifies that the printed diff is clean and tests pass,
    immediately provide the commit step in the same reply without asking the
    user to review or confirm the diff.
  - Exception: a trivial text-only change (1–2 lines, no code) may edit, show
    the diff, and commit in one step.
- Guarded commit steps: Because files on disk may change between turns, every
  step that commits or publishes changes must enable fail-fast mode and re-run
  fast syntax/linter checks and local unit tests (with live `.` progress,
  summary line, and full output on failure, never piped through `tail`,
  `head`, or `grep`) immediately before the commit command, so any failure
  aborts execution before committing.
