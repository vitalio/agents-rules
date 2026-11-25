# Description: Two-step self-reviewed diff before commit, explicit pre-commit diff audit, and fail-fast guarded commit steps
- Self-reviewed diff before commit: An edit step never commits — it applies
  changes, runs project verification checks inside the same step, and prints
  the working status and full diff.
  - Explicit pre-commit diff audit: After the full diff is printed, before
    emitting a commit block, write a concise hunk-by-hunk audit in chat
    verifying the printed diff against three gates: (1) task completeness —
    every bullet, requirement, and wording detail in the task specification is
    fulfilled; (2) project & rule invariants — all active rules and
    `AGENTS.md` requirements (including documentation sync and required
    previews) are satisfied; and (3) hunk accuracy — each modified block is
    free of copy-paste errors, formatting glitches, broken line continuations,
    unused content, or stale references across the repository.
  - Strict separation of fix steps and commit steps: If the diff audit reveals
    any defect (even a one-line typo, spacing glitch, or missing doc sync),
    emit a dedicated fix-and-diff step (`edit + verification + full diff`)
    without committing, and re-audit the new diff. Once the printed diff passes
    all three gates with zero defects, emit the commit step immediately in that
    reply without asking the user for confirmation.
- Guarded commit steps (no file edits): A step that commits or publishes
  changes must never modify target deliverable or rule files (only task-backlog
  closure and dynamic release-version bumps are permitted). Enable fail-fast
  mode and
  re-run project verification checks immediately before the commit command so
  any failure aborts execution before committing.
