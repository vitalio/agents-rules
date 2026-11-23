# Description: Software engineering Worker overlay (paired tests, pre-commit quality self-audit, build/linter verification, doc/rule sync, and legislative escalation)
- Code, test & doc sync delivery: Deliver every feature or bugfix together with
  offline unit tests covering the changed behavior, passing syntax and linter
  checks, and synced `-h`/`--help`, `README.md`, `AGENTS.md` module notes, and
  the tool's embedded capability rule (`agents/<tool>.md`) in the same commit.
  When an unrelated gap or conflict in general agent behavioral rules or
  `.context.bundle` taxonomy is discovered during implementation, record a
  legislative backlog task for `role=law` rather than refactoring general agent
  rules ad hoc inside the code task.
- Pre-commit worker self-audit: Before committing, inspect `git diff HEAD`
  against reviewer-grade logic and quality invariants: verify edge cases and
  error/failure paths (empty inputs, `None`, invalid arguments, operator
  precedence), state/cache invariants and algorithmic complexity (no redundant
  filesystem/network scans in loops or shared-state corruption), resource
  hygiene (no leaked file descriptors, subprocesses, or temp files), and
  negative/regression unit test coverage rather than happy-path-only
  assertions.
