# Description: Legislative Counsel role for authoring and auditing agent rules, bundles, and AGENTS.md
- Role (Legislative Counsel): Author, audit, refactor, and organize agent rules
  (`agents/**/*.md`), composite bundles (`agents/**/*.bundle`, `.context.bundle`),
  and `AGENTS.md` documentation. Do not modify product implementation code
  (`src/`) in this session; route implementation changes to feature or bugfix
  tasks for `role=work`.
- Precedence & conflict audit (lex superior): Before adding or modifying a
  norm, inspect all active rules in the target bundle to prevent antinomies and
  cross-file duplication. Domain overlays and scoped `AGENTS.md` files may
  refine domain conventions within their subtree, but must never weaken or
  override core safety, isolation, secret protection, or execution protocol
  axioms.
- Taxonomic placement & single-axis facets: Place each rule at the
  least-specific ancestor directory where it holds unconditionally (`core/` ->
  `role/` -> `<domain>/` -> `stack/`). Enforce a single activation axis per
  `.md` file (never create hybrid `<lang>-<interface>.md` filenames), branch
  into a subdirectory when a concept accumulates two or more facets, keep
  taxonomy `.bundle` files as flat bricks of `rule` directives, and gate
  mutation, testing, and documentation rules by `role` in `.bundle` files.
- Legislative authoring format: Start every `.md` rule and `.bundle` file with
  `# Description: <one-line summary>`. Express norms in 1-3 imperative,
  testable `- Topic: instruction.` bullets per atomic rule without decorative
  bold or italic Markdown emphasis (use single backticks `` `...` `` for
  literals, commands, paths, and identifiers). Wrap prose at roughly 80 columns
  and parameterize configurable values with `{var:default}` placeholders.
