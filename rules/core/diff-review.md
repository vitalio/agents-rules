# Description: Two-step self-reviewed diff before commit and fail-fast guarded commit steps
- Self-reviewed diff before commit: An edit step does not commit immediately
  — it runs syntax/linter checks and local tests (emitting compact live
  progress indicators such as per-test `.` dots followed by the summary line
  when all tests pass, and full diagnostics and tracebacks on failure, without
  piping test output through `tail`, `head`, or `grep` or suppressing it via
  redirection), then prints the working status and full diff.
  - When a task is implemented across multiple bounded edit stages, intermediate
    stages may run syntax checks and compact test suites without printing the
    accumulated diff; emit full `git status --porcelain` and `git diff HEAD`
    output for self-review once all planned edit stages are complete.
  - When the user provides the output, the model itself must audit the full
    diff against all project rules (no dead code or leftover names, clean
    module boundaries, updated documentation and help text). When a change
    removes, renames, or splits files or symbols, search the entire repository
    for stale references — including CI workflows (`.github/workflows/`),
    `README.md`, `AGENTS.md`, and active backlog tasks in `TODO.md` — and
    clean up any orphaned artifacts before committing. If any issue is found in
    the diff, fix it in the next step and re-verify the diff until completely
    clean.
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
