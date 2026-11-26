# Description: Responsibility split between README.md, AGENTS.md, and docs/adr/, progressive disclosure, and documentation sync
- Documentation split (`README.md` vs `AGENTS.md`): Separate the external or
  human-facing project reference from internal agent instructions. Use
  `README.md` for purpose, architecture or public interfaces, installation or
  entry points, configuration, and usage examples. Keep `AGENTS.md` a concise
  internal guide covering repository-specific delta knowledge an agent cannot
  infer from the file tree: component boundaries, cross-file invariants,
  negative constraints, and verification steps. Never duplicate `README.md`
  tutorials, marketing prose, or full reference tables inside `AGENTS.md`.
- `README.md` progressive disclosure: Open `README.md` with a one-line purpose
  tagline and a concise high-level overview (plus a section or directory map in
  multi-component repositories) without dumping low-level protocol grammars,
  edge cases, or exhaustive environment tables into the introduction. Present
  primary entry points or scenario-grouped usage examples before deep reference
  sections or internal specifications, and honor any project-specific
  documentation conventions defined in `AGENTS.md`.
- Architecture Decision Records (`docs/adr/`): When a design decision involves
  complex protocols, trade-offs, or multi-component rationale too detailed for
  `AGENTS.md`, record a concise ADR in `docs/adr/NNNN-<slug>.md` (context,
  decision, rejected alternatives, consequences) rather than inflating
  `AGENTS.md`, and reference relevant `docs/adr/*.md` paths in backticks in
  downstream task descriptions.
- Documentation sync: Keep project documentation (`README.md`, `AGENTS.md`,
  `docs/adr/`), user-facing specifications, and agent rules in sync within the
  same change when modifying behavior, options, or rules.
