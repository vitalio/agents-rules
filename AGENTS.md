# `agents-rules` — Encyclopedia Philosophy & Taxonomic Rules

`agents-rules` is a tool-agnostic encyclopedia of composable axioms,
operational rules, roles, and adapters for AI agents. Universal workflow,
language, Git, legislative authoring (`agents/role/law.md`), and release rules
are loaded via `.context.bundle`.

## Taxonomic Design Principles

- Canonical package root: `agents/` is the single package directory for all
  exported atomic rules (`.md`) and composite bundles (`.bundle`), organized by
  logical domain subtrees. Any creation, modification, reorganization, or
  deletion of files under `agents/`, `.context.bundle`, or `AGENTS.md` is
  tracked as an `L*` task under `role=law`.
- Flat bundle bricks: Keep all `.bundle` files in `agents-rules` as flat bricks
  composed directly of atomic `rule` directives (no nested `bundle` inside
  `.bundle`) so projects compose orthogonal bundles at depth 1 from their root
  `.context.bundle`.
- Abstraction promotion (least-specific ancestor): Place each rule at the
  highest level of the tree where it holds unconditionally: universal
  domain-agnostic axioms in `agents/core/`, session-level operating postures in
  `agents/role/`, domain-specific invariants and role overlays in domain
  subtrees (`agents/coding/`), tool-to-role bindings in `agents/adapters/`,
  communication boundaries in `agents/collab/`, and environment, stack,
  bootstrap, or release specifics in `agents/os/`, `agents/vcs/`,
  `agents/stack/`, `agents/bootstrap/`, or `agents/release/`.
- Composable role postures, role gating, and domain overlays: Keep base roles
  in `agents/role/` (`design`, `plan`, `work`, `review`, `law`) strictly
  domain-agnostic. Gate mutation, diff-review, documentation, and testing rules
  by `role` inside `.bundle` files (`if role=work,law`, `if role=work,review`,
  etc.), and express domain-specific role constraints as additive overlay rules
  (`<domain>/<role>.md`) activated via `if role=...` inside
  `<domain>/<domain>.bundle`.
- Orthogonal facets & subtree branching: Each leaf rule file (`.md`) must
  depend on a single activation condition. Never cross-multiply independent
  axes into hybrid filenames (such as `<language>-<interface>.md`); keep
  cross-language interface contracts (`agents/stack/cli/`) separate from
  language subtrees (`agents/stack/python/`). Whenever a concept accumulates
  two or more distinct facets, branch into a subdirectory rather than flat
  hyphen-prefixed sibling files (avoid naming leaf rule files `README.md` or
  `readme.md`, which the bundler reserves for directory documentation).
- Scoped category `AGENTS.md`: Place a concise `AGENTS.md` inside any category
  or domain directory whose inclusion boundaries or decomposition axes are not
  self-evident from directory names alone.
- Never list directory contents or specific file inventories inside `AGENTS.md`
  or `README.md` (directory trees and rule catalogs are inspected dynamically
  via filesystem and bundler tools).
- Keep general rules and roles decoupled from specific external CLI tools;
  isolate tool-specific variable mappings and lifecycle rules inside
  `agents/adapters/<tool>.bundle` and `agents/adapters/<tool>/*.md`.
