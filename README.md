# agents-rules

Open encyclopedia and taxonomic catalog of composable AI agent axioms
(`rules/core/`), operational rules (`rules/`), roles (`rules/role/`), and
rulesets (`rulesets/`).

## Usage in `.agents_bundle`

```text
bundle vitalio/agents_bundle
bundle vitalio/todo_md

ruleset vitalio/agents-rules:default
rule vitalio/agents-rules:collab/no-task-ids
rule vitalio/agents-rules:release/semver
rule vitalio/agents-rules:release/single-file-build
rule vitalio/agents-rules:stack/cli
rule vitalio/agents-rules:stack/python-cli
rule vitalio/agents-rules:stack/python-stdlib
rule vitalio/agents-rules:stack/python-annotations py_min=3.9

$ cat AGENTS.md
```

Activate any role from `rules/role/` on demand via `role=<name>`:

```bash
agents_bundle role=<name>
agents_bundle --list
```

## Taxonomic Structure

- `rulesets/` — composable rulesets (`core`, `default`) using built-in
  variables (`os`, `vcs`), optional `role`, and `[if ...]` conditions.
- `rules/core/` — universal domain-, OS-, and VCS-agnostic axioms.
- `rules/role/` — universal session operating roles activated via
  `role=<name>`.
- `rules/collab/` — collaboration and external communication rules.
- `rules/os/`, `rules/vcs/`, `rules/stack/`, `rules/release/` — platform,
  version control, technical stack, and release rules.

## License

[MIT](LICENSE) © 2026 [vitalio](https://github.com/vitalio)
