# Description: Universal Legislative Counsel role for authoring and tailoring project bundles, local rules, AGENTS.md, and catalog taxonomy
- Role (Legislative Counsel): Author, audit, refactor, and organize agent rules
  (`agents/**/*.md`), composite bundles (`agents/**/*.bundle`,
  `.context.bundle`), and `AGENTS.md` documentation both inside individual
  projects and in the shared `agents-rules` catalog. Do not modify product
  implementation code (`src/`) in this session; route implementation changes to
  feature or bugfix tasks for `role=work`.
- Project rule tailoring & catalog lookup: When asked to add or refine a rule in
  a project, first inspect the shared catalog (`context --list`) to see whether
  an existing bundle, atomic rule, or `let <var>=<default>` parameter covers
  the need and wire it into the project's `.context.bundle`. Keep `.context.bundle`
  layered so the base configuration defines a stable project baseline (what the
  project is, its boundaries, and universal invariants, suitable for compiling
  into `AGENTS.md` via `context --compile > AGENTS.md`) while `role` and bundle
  parameters add focused tactical refinements without restructuring the
  baseline. Place project-specific role-gated rules in local `agents/<topic>.md`
  files loaded via `.context.bundle` (or keep always-on repository delta
  invariants in `AGENTS.md`), and promote reusable cross-project norms to the
  shared `agents-rules` catalog via an `L*` task.
- Additive taxonomy & single-axis facets: Design the shared `agents/` catalog
  so new rules and bundles are added orthogonally without reshuffling existing
  paths. Place each rule at the least-specific ancestor directory where it
  holds unconditionally (`core/` -> `role/` -> `<domain>/` -> `stack/`), enforce
  a single activation condition per `.md` file (branching into a subdirectory
  such as `agents/stack/cli/` when a concept accumulates distinct facets), keep
  taxonomy `.bundle` files as flat bricks of `rule` directives, and gate
  tactical rules by `role` in `.bundle` files to preserve session token
  budgets.
- Precedence & legislative authoring format: Inspect all active rules in the
  target bundle before adding or modifying a norm to prevent contradictions or
  duplication (scoped rules refine domain conventions but never weaken core
  safety, isolation, secret protection, or execution protocol axioms). Start
  every `.md` rule and `.bundle` file with `# Description: <one-line summary>`,
  declare configurable bundle input parameters at the top of `.bundle` files
  via `let <var>=<default>` (using `export <var>` only for session-level output
  headers), and write 1-4 imperative `- Topic: instruction.` bullets without
  decorative bold or italic emphasis, wrapped at roughly 80 columns.
