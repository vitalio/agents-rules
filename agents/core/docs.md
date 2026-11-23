# Description: Responsibility split between README.md, AGENTS.md, and docs/adr/, progressive disclosure, and documentation sync
- Documentation split (`README.md` vs `AGENTS.md`): Separate the external or
  human-facing project reference from internal agent instructions. Use
  `README.md` for purpose, architecture or public interfaces, installation or
  entry points, configuration, and usage examples. Keep `AGENTS.md` a concise
  internal guide covering repository-specific delta knowledge an agent cannot
  infer from the file tree: module boundaries, cross-file invariants, negative
  constraints, and verification steps. Never duplicate `README.md` tutorials,
  marketing prose, or full reference tables inside `AGENTS.md`.
- `README.md` progressive disclosure: Open `README.md` with a one-line purpose
  tagline and a concise high-level overview (plus a section or directory map in
  multi-component repositories) without dumping low-level protocol grammars,
  parser edge cases, or exhaustive environment tables into the introduction.
  Present primary entry points or scenario-grouped usage examples before deep
  reference sections or internal specifications, and honor any project-specific
  `README.md` and subdirectory `README.md` conventions defined in `AGENTS.md`.
- Architecture Decision Records (`docs/adr/`): Record detailed architectural
  rationale and rejected alternatives in `docs/adr/` rather than inflating
  `AGENTS.md`. Keep `AGENTS.md` concise and actionable, and reference relevant
  `docs/adr/*.md` paths in task descriptions when context or trade-offs matter.
- Documentation sync: Keep project documentation (`README.md`, subdirectory
  `README.md` indexes, `AGENTS.md`), user-facing help or interface
  specifications, and agent rules in sync within the same commit when modifying
  behavior, options, or rules.
