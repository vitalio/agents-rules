# `agents-rules` — Encyclopedia Philosophy & Taxonomic Rules

`agents-rules` is a tool-agnostic encyclopedia of composable axioms,
operational rules, roles, and adapters for AI agents. Universal workflow,
language, Git, legislative authoring (`agents/role/law.md`), and release rules
are loaded via `.context.bundle`.

## Taxonomic Design Principles

- Canonical package root: `agents/` is the single package directory for all
  exported atomic rules (`.md`) and composite bundles (`.bundle`), organized by
  logical domain subtrees. When tracked in `TODO.md`, any creation,
  modification, reorganization, or deletion of files under `agents/`,
  `.context.bundle`, or `AGENTS.md` uses the `L*` task prefix under `role=law`.
- Flat bundle bricks & adapter-first ordering: Keep domain `.bundle` files in
  `agents-rules` as flat bricks composed directly of atomic `rule` directives
  (no nested `bundle` inside `.bundle`, except `agents/default.bundle` as a
  thin package-shorthand alias for `core` and
  `agents/bootstrap/bootstrap.bundle` as a standalone greenfield entrypoint
  before `.context.bundle` exists) so projects compose orthogonal bundles at
  depth 1 from their root `.context.bundle`. Because `.context.bundle`
  evaluates top-down, place upstream adapter bundles that compute and `export`
  session variables (`adapters/todo-md` exporting `role` and `task`) first,
  before `core` and domain bundles that gate rules on `if role=...`.
- Abstraction promotion & category boundaries (least-specific ancestor): Place
  each rule at the highest level of the tree where it holds unconditionally:
  - `agents/core/` — universal domain-agnostic axioms completely independent of
    OS, VCS, subject domain, and external tools.
  - `agents/role/` — universal session-level operating postures (`design`,
    `plan`, `work`, `review`, `law`) activated via `role=<name>`, free of
    hardcoded domain assumptions, languages, or external CLI tools.
  - `agents/coding/` — software-engineering domain root: language-agnostic
    architecture, test-suite invariants, and additive role overlays
    (`coding/{design,plan,work,review}.md`), plus technical subtrees for
    interface contracts (`agents/coding/cli/`) and languages/runtimes
    (`agents/coding/python/`).
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
- CI catalog verification gate (`.github/workflows/ci.yml`): Every change to
  `agents/`, `.context.bundle`, or `AGENTS.md` must pass the CI validation
  script verifying that all `.md` and `.bundle` files under `agents/` start
  with `# Description: <summary>`, contain no decorative `**` outside code
  spans, resolve all referenced `rule`, `bundle`, and `file` targets across
  `agents/**/*.bundle` and `.context.bundle` (including chained `if`/`else`
  guards and all target files of parameterized rules), and declare
  `let <var>=<default>` in every `.bundle` for all `{var:default}` placeholders
  used by its rules.
- Dynamic discovery & scoped cross-layer catalog audit: Never list directory
  contents or static file inventories inside `AGENTS.md` or `README.md`
  (inspect the rule catalog dynamically via `context --list` and
  `context --tree`). Before proposing or editing any rule or bundle in
  `agents/`, apply a strict taxonomic self-check: (1) verify that `core/` and
  `role/` remain strictly domain-agnostic (software-engineering, code, and test
  specifics belong under `coding/` and `coding/*`, while norms specific to the
  `agents-rules` catalog itself belong here in `AGENTS.md`); (2) use
  `context --list` to scan rule descriptions and batch-read related rules along
  the affected vertical hierarchy (`core/` <-> `role/` <-> `coding/` <->
  target `coding/*` or `adapters/*` subtree) to eliminate cross-layer
  contradictions or duplication without dumping unrelated subtrees into
  context; (3) keep role-invariant rules contiguous ahead of `if role=...`
  blocks in `.bundle` files for prompt-cache prefix invariance; and (4) repeat
  full audit passes across modified and neighboring rules/bundles until a pass
  converges with zero remaining leaks, overlaps, or domain-boundary violations.
