# Description: Two-step self-reviewed diff before commit, stale-reference cleanup, and fail-fast guarded commit steps
- Self-reviewed diff before commit: An edit step does not commit immediately
  — it runs project verification checks inside the same step immediately after
  the edit, then prints the working status and full diff.
  - When a task is implemented across multiple bounded edit stages, verify each
    self-consistent stage in place (or run fast validation checks in
    intermediate stages when related files are temporarily split across steps
    for output token limits) and run full project verification at the end of
    the final edit stage together with the working status and full diff for
    self-review.
  - When the user provides the output, the model itself must audit the full
    diff against all active bundle rules, task requirements, and project
    `AGENTS.md` invariants before committing: verify accuracy, completeness,
    clean boundaries without unused content or leftover names, and synced
    documentation. When a change removes, renames, or splits files or named
    entities, search the entire repository for stale references and clean up
    any orphaned artifacts before committing. If any issue is found in the
    diff, fix it in the next step and re-verify the diff until completely
    clean.
  - Once the model verifies that the printed diff is clean and checks pass,
    immediately provide the commit step in the same reply without asking the
    user to review or confirm the diff.
  - Exception: a trivial text-only change (1-2 lines) may edit, show the diff,
    and commit in one step.
- Guarded commit steps: Because files on disk may change between turns, every
  step that commits or publishes changes must enable fail-fast mode and re-run
  project verification checks immediately before the commit command, so any
  failure aborts execution before committing.
