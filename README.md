# agents_rules

**Standard catalog of composable AI agent engineering rules (`rules/`) and presets (`presets/`) for [`agents_bundle`](https://github.com/vitalio/agents_bundle).**

## Usage in `.agents_bundle`

```text
preset vitalio/agents_rules:workflow
rule vitalio/agents_rules:os/auto
rule vitalio/agents_rules:vcs/git
rule vitalio/agents_rules:release/semver
rule vitalio/agents_rules:release/single-file-build
rule vitalio/agents_rules:stack/cli
rule vitalio/agents_rules:stack/python-cli py_min=3.9
```

## Structure

- `presets/*.preset` — composable presets (`core`, `workflow`, `default`, `python-tool`).
- `rules/core/*.md` — pure OS-, VCS-, and language-agnostic workflow principles (`start`, `secrets`, `plan`, `edit`, `diff-review`, `end`, `lang`, `composability`).
- `rules/os/*.md` — platform-specific rules (`linux`, `macos`, `windows`, plus `os/auto`).
- `rules/vcs/*.md` — version control rules (`git`, `cvs`, plus `vcs/auto`).
- `rules/stack/*.md` — interface and language stack rules (`cli`, `python-cli`).
- `rules/release/*.md` — versioning and packaging rules (`semver`, `single-file-build`).
- `rules/collab/*.md` — collaboration and external communication rules (`external`).

## License

[MIT](LICENSE) © 2026 [vitalio](https://github.com/vitalio)
