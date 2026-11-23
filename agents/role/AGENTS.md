# `agents/role/` — Universal Agent Operating Roles

- Scope: Session-level operating postures activated on demand via
  `role=<name>`.
- Invariants: A role defines the agent's objective, stance, and boundaries for
  the session (designing, planning, working, reviewing, or legislative rule
  drafting) without hardcoding domain-specific file names, languages, or
  external CLI tools.
- Composition: Roles must compose orthogonally with whatever domain bundles,
  overlays, and tool adapters are active in the workspace.
