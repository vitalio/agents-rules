# `agents-rules` — Encyclopedia Philosophy & Taxonomic Rules

`agents-rules` is a tool-agnostic encyclopedia of composable axioms,
operational rules, and roles for AI agents.

## Taxonomic Design Principles

- Place each rule at the highest level of abstraction where it holds
  unconditionally: universal domain-agnostic axioms in `rules/core/`,
  session-level operating postures in `rules/role/`, communication boundaries
  in `rules/collab/`, and environment/stack specifics in `rules/os/`,
  `rules/vcs/`, `rules/stack/`, or `rules/release/`.
- Never list directory contents or specific file inventories inside
  `AGENTS.md` or `README.md` (directory trees and rule catalogs are inspected
  dynamically via filesystem and bundler tools).
- Keep rules decoupled from external tools: never reference specific
  third-party or sibling CLI utilities inside general rules or roles.

## Authoring Format

- Start every rule, ruleset, or bundle file with
  `# Description: <one-line summary>` (lines starting with `#` and
  `<!-- ... -->` comments are stripped during bundle assembly).
- Do not use decorative bold or italic Markdown emphasis in rule files or
  `AGENTS.md`; use plain `- Topic: instruction.` bullets and single backticks
  (`` `...` ``) around literal commands, paths, and identifiers.
- Aim to wrap prose in text and Markdown files at roughly 80 characters per
  line for readability in terminal editors (`vim`).
- In `.agents_bundle`, `.bundle`, and `.ruleset` files, single-line
  `[if ...] <directive>` needs no closing tag; for multi-line
  `[if ...] ... [/if]` blocks, indent nested lines by 4 spaces per level.
- Parameterize configurable values with `{var:default}` placeholders.
