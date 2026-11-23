# Description: Two-step self-reviewed diff before commit, stale-reference cleanup, and fail-fast guarded commit steps
- Self-reviewed diff before commit: An edit step does not commit immediately
  — it runs project syntax/linter checks and local verification inside the same
  step immediately after the edit, then prints the working status and full
  diff.
  - When a task is implemented across multiple bounded edit stages, verify each
    self-consistent stage in place (or run syntax/build checks in intermediate
    stages when code and tests are temporarily split across steps for output
    token limits) and run full verification at the end of the final edit stage
    together with the working status and full diff for self-review.
  - When the user provides the output, the model itself must audit the full
    diff against all project rules and reviewer-grade logic and quality
    invariants before committing: verify edge cases and error/failure paths
    (null/empty inputs, invalid arguments, operator precedence), state/cache
    invariants and algorithmic complexity (no redundant filesystem/network
    scans in loops or shared-state corruption), resource hygiene (no leaked
    file descriptors, subprocesses, or temp files), negative/regression unit
    test coverage rather than happy-path-only assertions, clean boundaries
    without dead code or leftover names, and updated documentation and
    user-facing help or interface specifications. When a change removes,
    renames, or splits files or symbols, search the entire repository for stale
    references in code, tests, CI/build configurations, `README.md`, and
    `AGENTS.md`, and clean up any orphaned artifacts before committing. If any
    issue is found in the diff, fix it in the next step and
    re-verify the diff until completely clean.
  - Once the model verifies that the printed diff is clean and checks pass,
    immediately provide the commit step in the same reply without asking the
    user to review or confirm the diff.
  - Exception: a trivial text-only change (1-2 lines, no code) may edit, show
    the diff, and commit in one step.
- Guarded commit steps: Because files on disk may change between turns, every
  step that commits or publishes changes must enable fail-fast mode and re-run
  fast syntax/linter checks and local unit tests immediately before the commit
  command, so any failure aborts execution before committing.
