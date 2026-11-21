# `agents-rules` — Encyclopedia Philosophy & Taxonomic Rules

`agents-rules` is a tool-agnostic encyclopedia of composable axioms,
operational rules, and roles for AI agents. Universal workflow, language, Git,
and SemVer rules are loaded via `.agents_bundle`.

## Taxonomic Design Principles

- Canonical package root: `agents/` is the canonical package directory for
  all exported atomic rules (`.md`) and composite bundles (`.bundle`),
  organized by logical domain subtrees (replacing the legacy top-level
  `rules/` and `rulesets/` split tracked in `F20`).
- Abstraction promotion (least-specific ancestor): Place each rule at the
  highest level of the tree where it holds unconditionally: universal
  domain-agnostic axioms in `core/`, session-level operating postures in
  `role/`, domain-specific invariants and role overlays in domain subtrees
  (such as `coding/`), communication boundaries in `collab/`, and
  environment, stack, or release specifics in `os/`, `vcs/`, `stack/`, or
  `release/`.
- Composable role postures and domain overlays: Keep base roles in `role/`
  strictly domain-agnostic (cognitive stance, artifact permissions, context
  handoff contracts, and backlog lifecycle without software-engineering
  assumptions). Express domain-specific role constraints as additive overlay
  rules (`<domain>/<role>.md`) activated automatically via
  `[if role!=] rule <domain>/{role:}` inside `<domain>/<domain>.bundle` so
  base roles compose cleanly with one or more domain bundles without
  duplicating role protocols.
- Orthogonal facets (single axis of activation): Each leaf rule file (`.md`)
  must depend on a single activation condition. Never cross-multiply
  independent axes into hybrid filenames (such as `<language>-<interface>.md`);
  keep cross-language interface contracts (e.g. `cli.md`) separate from
  language or runtime rules (`python/...`) so projects compose them freely.
- Arbitrary-depth subtree branching: Whenever a domain, language, or subsystem
  accumulates two or more distinct facets with different activation triggers
  (such as language syntax, a specific test framework like `unittest`, stdlib
  restrictions, or type annotations), branch into a subdirectory
  (`<axis>/<domain>/.../<facet>.md`) rather than flat sibling files with
  hyphenated prefixes (`<domain>-*.md`). Continue nesting deeper whenever a
  child concept branches along its own axis of choice.
- Scoped category `AGENTS.md`: Place a concise `AGENTS.md` inside any category
  or domain directory whose inclusion boundaries or decomposition axes are not
  self-evident from directory names alone.
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
