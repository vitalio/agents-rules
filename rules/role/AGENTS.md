# `rules/role/` — Universal Agent Operating Roles

- Scope: Session-level operating postures activated on demand via
  `role=<name>`.
- Invariants: A role defines the agent's objective, stance, and boundaries for
  the session (for example, designing, planning, working, or reviewing)
  without hardcoding domain-specific file names, languages, or external CLI
  tools.
- Composition: Roles must compose orthogonally with whatever domain rules and
  tool instructions are active in the workspace.
