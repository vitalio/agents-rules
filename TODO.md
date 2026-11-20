# 🎯 [NEXT] F31: Specify --help column alignment, {prog} placeholder accounting, and <=100-col width in rules/stack/cli.md

- In `rules/stack/cli.md` (`Structured -h/--help layout`), require aligned description columns within each section (accounting for the rendered program name length when `{prog}` templates are used so continuation lines align with primary descriptions) and a maximum `--help` line width of 100 columns (~80 columns for prose paragraphs).
- Wrap rule prose in `rules/stack/cli.md` at ~80 characters per line and bump `VERSION` for a PATCH release.

# ⚪ [NEW] F5: Wrap prose at ~80 columns across all remaining rule files

- Wrap long lines (>80 chars) in `rules/collab/external.md`, `rules/core/AGENTS.md`, `rules/core/composability.md`, `rules/core/diff-review.md`, `rules/core/end.md`, `rules/core/lang.md`, `rules/core/plan.md`, `rules/core/secrets.md`, `rules/core/ssot.md`, `rules/os/*.md`, `rules/release/single-file-build.md`, `rules/stack/python-cli.md`, `rules/stack/python-stdlib.md`, `rules/stack/python-annotations.md`, and `rules/vcs/*.md` to ~80 characters per line.

# ⚪ [NEW] D1: Design composable role extensions and domain overlays

- Depends on: F16, F9
- Explore separating universal domain-agnostic role postures in `agents/role/` (cognitive stance, artifact permissions, and handoff contracts) from domain-specific role overlays (such as `agents/coding/design.md`, `agents/coding/plan.md`, `agents/coding/work.md`, and `agents/coding/review.md`) activated automatically via `[if role=...]` inside domain bundles.
- Define how projects compose base roles with one or more domain overlays without duplicating rules or leaking software-engineering assumptions into universal roles, feeding into `F20`.
- Apply orthogonal facet decomposition (`AGENTS.md`): separate cross-language interface contracts (`cli.md`) from language subtrees (`python/syntax.md`, `python/unittest.md`, `python/stdlib.md`, `python/annotations.md`, plus a default `python.bundle` preset) so projects never rely on hybrid filenames like `python-cli.md`.

# ⚪ [NEW] F20: Replace rulesets with bundles and organize rules logically by domain

- Depends on: D1
- Standardize `agents/` as the single package root directory for all rules (`.md`) and bundles (`.bundle`), migrating `rulesets/core.ruleset`, `rulesets/default.ruleset`, and `rules/` into a logical domain-based layout under `agents/` (incorporating composable domain role overlays designed in `D1`, after `agents_bundle` supports the `agents/` layout).
- Decompose `rules/stack/python-cli.md`, `rules/stack/python-stdlib.md`, and `rules/stack/python-annotations.md` into a nested `agents/stack/python/` (or `agents/python/`) subtree (`syntax.md`, `unittest.md`, `stdlib.md`, `annotations.md`, and `python.bundle`) orthogonal to `cli.md`.
- Update `AGENTS.md` and `README.md` to reflect the unified `agents/` rule/bundle layout, and release a new MINOR version.

# ⚪ [NEW] F25: Rename project and package references from agents-rules to ctx-taxonomy

- Role: plan
- Rename package identity, documentation, and internal references from `agents-rules` (`vitalio/agents-rules`) to `ctx-taxonomy` (`vitalio/ctx-taxonomy`), aligned with the ecosystem rename design.
- Target files: `AGENTS.md`, `README.md`, `.agents_bundle`, `VERSION`, and exported rule/bundle files (`rules/`, `rulesets/`, or `agents/` after `F20`).
- Acceptance criteria: all docs, examples, and package references use `ctx-taxonomy` (alongside sibling names `ctx-bundle`/`cxb`, `todo-markdown`/`tmd`, `run-block`/`rxb`), `VERSION` is bumped appropriately, and repository checks pass.
