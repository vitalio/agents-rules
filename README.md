# agents-rules

Open encyclopedia and taxonomic catalog of composable AI agent axioms
(`agents/core/`), operating roles (`agents/role/`), domain overlays
(`agents/coding/`), technical stack rules (`agents/stack/`), tool adapters
(`agents/adapters/`), and composite bundles (`agents/**/*.bundle`).

## Usage in `.ctx.bundle` / `.agents_bundle`

```text
bundle vitalio/agents-rules:core
bundle vitalio/agents-rules:adapters/todo_md
bundle vitalio/agents-rules:coding
bundle vitalio/agents-rules:stack/python py_min=3.9
bundle vitalio/agents-rules:release single_file_build=1
rule vitalio/agents-rules:collab/commits
rule vitalio/agents-rules:stack/cli

file AGENTS.md
```

Activate any operating role (`design`, `plan`, `work`, `review`, `law`) on
demand via `role=<name>` or automatically through `adapters/todo_md`:

```bash
agents_bundle role=law
agents_bundle --list
```

## Taxonomic Structure

- `agents/core.bundle` (`agents/default.bundle`) — foundational flat bundle of
  universal axioms, POSIX OS (`linux`, `macos`) and VCS (`git`, `cvs`) rules,
  active base role posture, and role-gated editing, diff-review, and
  documentation rules.
- `agents/core/` — universal domain-, OS-, and VCS-agnostic axioms.
- `agents/role/` — domain-agnostic operating roles (`design`, `plan`, `work`,
  `review`, `law`) activated via `role=<name>`.
- `agents/coding/` — software-engineering architecture, test-suite invariants,
  and additive role overlays (`coding.bundle`).
- `agents/stack/` — cross-language interface rules (`cli.md`) and language
  subtrees (`stack/python/python.bundle`).
- `agents/adapters/` — tool-to-role adapter bundles and lifecycle rules
  (`adapters/todo_md.bundle`).
- `agents/collab/`, `agents/os/`, `agents/vcs/`, `agents/release/`,
  `agents/bootstrap/` — collaboration, POSIX platform, version control, release
  (`release.bundle`), greenfield bootstrap (`bootstrap.bundle`), and multi-repo
  orchestration (`orchestrator.bundle`) rules.

## License

[MIT](LICENSE) © 2026 [vitalio](https://github.com/vitalio)
