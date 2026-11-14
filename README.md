# agents-rules

**Open encyclopedia and taxonomic catalog of composable AI agent axioms, operational rules (`rules/`), roles (`rules/role/`), presets (`presets/`), and bundle includes (`includes/`).**

## Usage in `.agents_bundle`

```text
preset vitalio/agents-rules:default
rule vitalio/agents-rules:release/semver
rule vitalio/agents-rules:release/single-file-build
rule vitalio/agents-rules:stack/cli
rule vitalio/agents-rules:stack/python-cli py_min=3.9

$ cat AGENTS.md
```

Activate universal roles on demand via `key=val` overrides (e.g. `role=audit` or `role=plan`):

```bash
agents_bundle role=audit
agents_bundle role=plan
```

## Taxonomy

- `presets/*.preset` — composable presets (`core`, `default`) using built-in variables (`os`, `vcs`), optional `role`, and `[if ...]` conditions.
- `rules/core/*.md` — universal domain-, OS-, and VCS-agnostic axioms (`start`, `secrets`, `plan`, `ssot`, `edit`, `diff-review`, `end`, `composability`, `lang`).
- `rules/role/*.md` — universal operating roles (`audit`, `plan`) that compose with active workspace rules and tools.
- `rules/collab/*.md` — collaboration and external communication rules (`external`).
- `rules/os/*.md` — platform-specific rules (`linux`, `macos`, `windows`).
- `rules/vcs/*.md` — version control rules (`git`, `cvs`).
- `rules/stack/*.md` — interface and language stack rules (`cli`, `python-cli`).
- `rules/release/*.md` — versioning and packaging rules (`semver`, `single-file-build`).
- `includes/*.bundle` — reusable `.agents_bundle` fragments with conditional `$ <cmd>` and `prompt` directives.

## License

[MIT](LICENSE) © 2026 [vitalio](https://github.com/vitalio)
