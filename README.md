# agents-rules

**Standard catalog of composable AI agent engineering rules (`rules/`), presets (`presets/`), and bundle includes (`includes/`).**

## Usage in `.agents_bundle`

```text
preset vitalio/agents-rules:default
[if os=linux] rule vitalio/agents-rules:os/linux
[if os=macos] rule vitalio/agents-rules:os/macos
[if os=windows] rule vitalio/agents-rules:os/windows
rule vitalio/agents-rules:vcs/git
rule vitalio/agents-rules:release/semver
rule vitalio/agents-rules:release/single-file-build
rule vitalio/agents-rules:stack/cli
rule vitalio/agents-rules:stack/python-cli py_min=3.9
```

## Structure

- `presets/*.preset` — composable presets (`core`, `default`) using built-in variables (`os`, `vcs`) and `[if ...]` conditions.
- `includes/*.bundle` — reusable `.agents_bundle` fragments with conditional `$ <cmd>` and `prompt` directives.
- `rules/core/*.md` — pure OS-, VCS-, and language-agnostic workflow principles (`start`, `secrets`, `plan`, `edit`, `diff-review`, `end`, `lang`, `composability`).
- `rules/os/*.md` — platform-specific rules (`linux`, `macos`, `windows`).
- `rules/vcs/*.md` — version control rules (`git`, `cvs`).
- `rules/stack/*.md` — interface and language stack rules (`cli`, `python-cli`).
- `rules/release/*.md` — versioning and packaging rules (`semver`, `single-file-build`).
- `rules/collab/*.md` — collaboration and external communication rules (`external`).

## License

[MIT](LICENSE) © 2026 [vitalio](https://github.com/vitalio)
