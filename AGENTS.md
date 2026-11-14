# `agents-rules` — Encyclopedia Taxonomy & Authoring Rules

`agents-rules` is an open, tool-agnostic encyclopedia of composable axioms, operational rules, and roles for AI agents.

## Taxonomic Hierarchy & Boundaries

- `rules/core/` — Kingdom: universal, domain-agnostic axioms (epistemology, SSOT/DRY, scoped `AGENTS.md` hierarchy, composability, atomic edits, self-reviewed diffs, secrets, language, session lifecycle). Never put OS-, VCS-, language-, or tool-specific names here.
- `rules/role/` — Operating roles (`audit`, `plan`) activated on demand (e.g. `role=audit`, `role=plan`). Keep roles universal so they compose naturally with any domain or tool.
- `rules/collab/` — External communication and two-step external changes (`external`).
- `rules/os/`, `rules/vcs/`, `rules/stack/`, `rules/release/` — Environment, version control, technical stack, and release pipeline rules.
- `presets/` & `includes/` — Composable rule presets (`core`, `default`) and reusable bundle fragments.

## Authoring Invariants

- Start every rule/preset/include file with `# Description: <one-line summary>`.
- Keep each rule atomic (1–3 concise bullets), free of hardcoded tool versions, and parameterized with `{var:default}` where appropriate.
- Keep `README.md` and subfolder `AGENTS.md` files in sync when adding or renaming rules or presets.
