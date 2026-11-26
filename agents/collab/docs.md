# Description: Opt-in repository documentation structure (README.md vs AGENTS.md split, progressive disclosure, and docs/adr/)
- Documentation split (`README.md` vs `AGENTS.md`): Separate human-facing
  project reference from internal agent instructions. Use `README.md` for
  purpose, architecture or public interfaces, installation or entry points,
  configuration, and usage examples. Keep `AGENTS.md` a concise internal guide
  covering repository-specific delta knowledge an agent cannot infer from the
  file tree (component boundaries, cross-file invariants, negative constraints,
  and verification steps), never duplicating `README.md` tutorials or reference
  tables inside `AGENTS.md`.
- `README.md` progressive disclosure: Open `README.md` with a one-line purpose
  tagline and a concise high-level overview (plus a directory map in
  multi-component repositories) before presenting primary entry points or
  scenario-grouped usage examples and deeper reference sections.
- Architecture Decision Records (`docs/adr/`): When a design decision involves
  complex protocols, trade-offs, or multi-component rationale too detailed for
  `AGENTS.md`, record a concise ADR in `docs/adr/NNNN-<slug>.md` (context,
  decision, rejected alternatives, consequences) and reference relevant
  `docs/adr/*.md` paths in backticks in downstream tasks.
