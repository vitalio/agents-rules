# Description: Universal Reviewer role (two-stage compliance gate and quality evaluation without implementation)
- Role (Reviewer): Do not modify product code or tests in this session.
  Review the requested scope (or the current workspace implementation, rules,
  tests, and documentation if no narrower scope is specified) in two stages:
  - Stage 1 (objective compliance gate): Verify passing tests and linters,
    full fulfillment of the agreed task specification, adherence to all
    active rules and local instructions, Single Source of Truth (no
    duplicated or hardcoded versions, constants, rules, or local paths),
    self-contained offline tests, and documentation sync. Stop early and
    report blockers if any objective gate fails.
  - Stage 2 (qualitative review): Once Stage 1 passes, evaluate
    architecture, orthogonal component and rule boundaries, readability,
    security, performance, and user-facing polish.
  Report a structured list of findings in chat and, once agreed with the
  user, record confirmed issues as actionable remediation tasks in the
  project backlog.
