# Description: Software engineering Worker overlay (paired tests, build/linter verification, and rule escalation via L* tasks)
- Code & test delivery: Deliver every feature or bugfix together with offline
  unit tests covering the changed behavior, passing syntax and linter checks,
  and synced `--help` and documentation in the same commit. When a rule gap or
  conflict is discovered during implementation, record an `L*` backlog task
  rather than modifying rule files ad hoc inside a code task.
