# `agents-rules` — Encyclopedia Philosophy & Taxonomic Rules

`agents-rules` is a tool-agnostic encyclopedia of composable axioms,
operational rules, roles, language/interface bundles, and adapters for AI
agents. Universal workflow, locale, Git, legislative authoring
(`agents/role/law.md`), and release rules are loaded via `.context.bundle`.

## Taxonomic Design Principles

- Canonical package root: `agents/` is the single package directory for all
  exported atomic rules (`.md`) and composite bundles (`.bundle`), organized by
  logical domain subtrees. When tracked in `TODO.md`, any creation,
  modification, reorganization, or deletion of files under `agents/`,
  `.context.bundle`, or `AGENTS.md` uses the `L*` task prefix under `role=law`.
- Flat bundle bricks & core-first ordering: Keep domain `.bundle` files in
  `agents-rules` as flat bricks composed directly of atomic `rule` directives
  (no nested `bundle` inside `.bundle`, except `agents/default.bundle` as a
  thin package-shorthand alias for `core` and
  `agents/bootstrap/bootstrap.bundle` as a standalone greenfield entrypoint
  before `.context.bundle` exists) so projects compose orthogonal bundles at
  depth 1 from their root `.context.bundle`. Place
  `bundle vitalio/agents-rules:core` first in `.context.bundle` (before
  `lang/*`, `cli`, `adapters/*`, and `release` bundles).
- Abstraction promotion & category boundaries (least-specific ancestor): Place
  each rule at the highest level of the tree where it holds unconditionally:
  - `agents/core/` — universal axioms, modular architecture and canonical
    test-suite invariants, and editing/diff-review rules completely independent
    of OS, VCS, programming language, and external CLI tools.
  - `agents/role/` — unified session-level operating postures (`design`,
    `plan`, `work`, `review`, `law`) activated via `role=<name>`, free of
    hardcoded programming languages or external CLI tools.
  - `agents/lang/` — language- and runtime-specific subtrees
    (`agents/lang/python/`, and future language bundles such as
    `agents/lang/js/`).
  - `agents/cli/` — command-line interface contracts (`-h`/`--help` hygiene
    and standalone CLI `README.md` reference layout).
  - `agents/adapters/` — tool-specific variable mappings and lifecycle rules
    (`agents/adapters/<tool>.bundle` and `agents/adapters/<tool>/*.md`),
    keeping general rules and roles decoupled from specific external CLIs.
  - `agents/collab/`, `agents/os/`, `agents/vcs/`, `agents/release/`,
    `agents/bootstrap/` — communication boundaries and opt-in repository
    conventions (`collab/commits.md`, `collab/docs.md`), POSIX OS specifics,
    version control, release workflows, and greenfield repository scaffolding.
- Composable role postures & role gating: Gate role-specific architecture,
  testing, mutation, and diff-review rules by `role` inside `.bundle` files
  (`if role=work,law`, `if role=work,review`, `if role=work,design,review`,
  etc.), keeping each operating role consolidated in a single file under
  `agents/role/<role>.md`.
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
  spans, forbid nested `bundle` directives inside flat domain bundles, leave no
  unreferenced `.md` rule files under `agents/`, resolve all referenced `rule`,
  `bundle`, and `file` targets across `agents/**/*.bundle` and
  `.context.bundle` (including chained `if`/`else` guards and all target files
  of parameterized rules), and declare `let <var>=<default>` in every `.bundle`
  for all `{var:default}` placeholders used by its rules.
- Dynamic discovery & scoped cross-layer catalog audit: Never list directory
  contents or static file inventories inside `AGENTS.md` or `README.md`
  (inspect the rule catalog dynamically via `context --list` and
  `context --tree`). Before proposing or editing any rule or bundle in
  `agents/`, apply a strict taxonomic self-check: (1) verify that `core/` and
  `role/` remain free of specific programming languages or external CLI tool
  names (language specifics belong under `lang/<language>/`, CLI interface
  contracts under `cli/`, tool bindings under `adapters/`, and norms specific
  to the `agents-rules` catalog itself belong here in `AGENTS.md`); (2) use
  `context --list` to scan rule descriptions and batch-read related rules along
  the affected vertical hierarchy (`core/` <-> `role/` <-> target `lang/*`,
  `cli/`, or `adapters/*` subtree) to eliminate cross-layer contradictions or
  duplication without dumping unrelated subtrees into context; (3) keep
  role-invariant rules contiguous ahead of `if role=...` blocks in `.bundle`
  files for prompt-cache prefix invariance; and (4) repeat full audit passes
  across modified and neighboring rules/bundles until a pass converges with
  zero remaining leaks, overlaps, or boundary violations.
