# Description: Responsibility split between README.md, AGENTS.md, and docs/adr/, plus documentation sync
- Documentation split (`README.md` vs `AGENTS.md`): Separate the external
  public contract from internal engineering guidance. Use `README.md` for
  purpose, installation, public interfaces and configuration (such as CLI
  flags, environment variables, or I/O protocols), and integration examples.
  Keep `AGENTS.md` a concise internal guide covering only repository-specific
  delta knowledge an agent cannot infer from the file tree: module boundaries,
  cross-file invariants, negative constraints, and build/test verification
  steps. Never duplicate `README.md` tutorials, marketing descriptions, or full
  reference tables inside `AGENTS.md`.
- Architecture Decision Records (`docs/adr/`): Record detailed architectural
  rationale and rejected alternatives in `docs/adr/` rather than inflating
  `AGENTS.md`. Keep `AGENTS.md` concise and actionable, and reference relevant
  `docs/adr/*.md` paths in task descriptions when context or trade-offs matter.
- Documentation sync: Keep project documentation (`README.md`, `AGENTS.md`),
  user-facing help, and agent instructions in sync within the same change when
  modifying behavior, options, or rules.
