# agents_rules

**Standard catalog of composable AI agent engineering rules (`rules/`) and presets (`presets/`) for [`agents_bundle`](https://github.com/vitalio/agents_bundle).**

## Usage in `.agents_bundle`

```text
preset vitalio/agents_rules:workflow
rule vitalio/agents_rules:vcs/git
rule vitalio/agents_rules:release/semver
rule vitalio/agents_rules:release/single-file-build
rule vitalio/agents_rules:stack/python-cli py_min=3.9
```

## Structure

- `presets/*.preset` — composable rule presets (`core`, `workflow`, `default`, `python-tool`) using `preset ...` and `rule ...` directives.
- `rules/core/*.md` — VCS- and language-agnostic workflow rules (`start`, `secrets`, `plan`, `edit`, `diff-review`, `external`, `end`, `lang`, `unix-philosophy`).
- `rules/vcs/*.md` — version control rules (`git`, `cvs`).
- `rules/release/*.md` — release & build rules (`semver`, `single-file-build`).
- `rules/stack/*.md` — stack-specific invariants (`python-cli`).

## License

[MIT](LICENSE) © 2026 [vitalio](https://github.com/vitalio)
