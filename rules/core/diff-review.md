# Description: Two-step self-reviewed diff before commit and fail-fast guarded commit steps
- **Self-reviewed diff before commit:** An edit step does **not** commit immediately — it runs syntax/linter checks and local tests, and prints the working status and full diff.
  - When the user provides the output, **the model itself must audit the full diff** against all project rules (no dead code or leftover names, clean module boundaries, updated documentation and help text). If any issue is found in the diff, fix it in the next step and re-verify the diff until completely clean.
  - Once the model verifies that the printed diff is clean and tests pass, immediately provide the commit step in the same reply without asking the user to review or confirm the diff.
  - *Exception:* a trivial text-only change (1–2 lines, no code) may edit, show the diff, and commit in one step.
- **Guarded commit steps:** Because files on disk may change between turns, every step that commits or publishes changes must enable fail-fast mode and re-run fast syntax/linter checks and local unit tests immediately before the commit command, so any failure aborts execution before committing.
