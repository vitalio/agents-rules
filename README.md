# agents_rules

**Composable AI agent engineering rules and presets with namespace & GitHub package support.**

`agents_rules` is a zero-dependency Python 3 CLI following the Unix philosophy: it renders
namespaced engineering rules and presets (`std:...`, `<owner>/<repo>:...`, or `./path`) to `stdout`
with `{var:default}` variable overrides and `-<rule>` exclusions.

## Usage

```bash
agents_rules std:python-tool
agents_rules std:workflow -core/external lang=Russian
agents_rules std:release/single-file-build
agents_rules vitalio/agents_rules:python-tool
agents_rules --list
```

## License

[MIT](LICENSE) © 2026 [vitalio](https://github.com/vitalio)
