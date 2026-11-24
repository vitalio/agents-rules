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
- Flat bundle bricks & adapter-first ordering: Keep domain `.bundle` files in
  `agents-rules` as flat bricks composed directly of atomic `rule` directives
  (no nested `bundle` inside `.bundle`, except `agents/default.bundle` as a
  thin package-shorthand alias for `core`) so projects compose orthogonal
  bundles at depth 1 from their root `.context.bundle`. Because `.context.bundle`
  evaluates top-down, place upstream adapter bundles that compute and `export`
  session variables (`adapters/todo-md` exporting `role` and `task`) first,
  before `core` and domain/stack bundles that gate rules on `if role=...`.
- Abstraction promotion & category boundaries (least-specific ancestor): Place
  each rule at the highest level of the tree where it holds unconditionally:
  - `agents/core/` — universal axioms completely independent of OS, VCS,
    programming language, and external tools.
  - `agents/role/` — session-level operating postures (`design`, `plan`,
    `work`, `review`, `law`) activated via `role=<name>`, free of hardcoded
    domain file paths, languages, or external CLI tools.
  - `agents/coding/` — language-agnostic software-engineering architecture,
    test-suite invariants, and additive role overlays
    (`coding/{design,plan,work,review}.md`).
  - `agents/stack/` — cross-language interface contracts (`agents/stack/cli/`)
    and language/runtime subtrees (`agents/stack/python/`).
  - `agents/adapters/` — tool-specific variable mappings and lifecycle rules
    (`agents/adapters/<tool>.bundle` and `agents/adapters/<tool>/*.md`),
    keeping general rules and roles decoupled from specific external CLIs.
  - `agents/collab/`, `agents/os/`, `agents/vcs/`, `agents/release/`,
    `agents/bootstrap/` — communication boundaries, POSIX OS specifics, version
    control, release workflows, and greenfield repository scaffolding.
- Composable role postures & role gating: Gate mutation, diff-review,
  documentation, and testing rules by `role` inside `.bundle` files
  (`if role=work,law`, `if role=work,review`, etc.), and express
  domain-specific role constraints as additive overlay rules
  (`<domain>/<role>.md`) activated via `if role=...` inside
  `<domain>/<domain>.bundle`.
- Orthogonal facets & subtree branching: Each leaf rule file (`.md`) must
  depend on a single activation condition. Never cross-multiply independent
  axes into hybrid filenames (such as `<language>-<interface>.md`). Whenever a
  concept accumulates two or more distinct facets, branch into a subdirectory
  rather than flat hyphen-prefixed sibling files (avoid naming leaf rule files
  `README.md` or `readme.md`, which the bundler reserves for directory
  documentation).
- Dynamic discovery: Never list directory contents or specific file inventories
  inside `AGENTS.md` or `README.md` (directory trees and rule catalogs are
  inspected dynamically via filesystem and bundler tools).
