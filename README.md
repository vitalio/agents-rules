# agents-rules

Open encyclopedia and taxonomic catalog of composable AI agent axioms
(`agents/core/`), operating roles (`agents/role/`), domain overlays
(`agents/coding/`), technical stack rules (`agents/stack/`), tool adapters
(`agents/adapters/`), and composite bundles (`agents/**/*.bundle`).

## Usage in `.context.bundle`

```text
bundle vitalio/agents-rules:adapters/todo-md
bundle vitalio/agents-rules:core
bundle vitalio/agents-rules:coding
bundle vitalio/agents-rules:stack/python py_min=3.9
bundle vitalio/agents-rules:release single_file_build=1
bundle vitalio/agents-rules:stack/cli
rule vitalio/agents-rules:collab/commits

file AGENTS.md
```

Activate any operating role (`design`, `plan`, `work`, `review`, `law`) on
demand via `role=<name>` or automatically through `adapters/todo-md`:

```bash
todo <ID> | context | run
context role=law | run
context --list
```

## Operating Roles

Roles set the session posture and gate editing, diff-review, testing, and
documentation rules across `core` and domain bundles (`coding`, `stack/*`,
`adapters/*`). Set a role explicitly (`context role=<name>`) or let
`adapters/todo-md` derive it from task prefix and status:

- `design` (Designer) — concept exploration, architecture, interface design,
  and ADR persistence (`docs/adr/`) without modifying product implementation or
  tests (auto-selected for `D*` tasks).
- `plan` (Planner) — workspace analysis, task decomposition and consolidation,
  role routing, and dependency-chain wiring without modifying product
  deliverables (auto-selected for `NEW`, `QUESTION`, and `HOLD` tasks).
- `work` (Worker) — focused, low-chatter implementation, testing, and
  verification strictly within agreed task scope (auto-selected for `WIP` and
  `NEXT` implementation tasks).
- `review` (Reviewer) — two-stage objective compliance gate and architectural
  quality evaluation without modifying implementation or tests.
- `law` (Legislative Counsel) — authoring, auditing, refactoring, and
  tailoring agent rules, bundles, and `AGENTS.md` instructions without
  modifying product domain logic (auto-selected for `L*` tasks).

## Bundle Parameters

Pass parameters inline on `bundle` directives in `.context.bundle` or as
`key=val` arguments to `context` (run `context --list` to inspect active
defaults dynamically):

- `os` (`core`, `default`) — target operating system rules (`linux`, `macos`);
  auto-detected by `context` when omitted.
- `vcs` (`core`, `default`) — version control workflow rules (`git`, `cvs`);
  auto-detected by `context` when omitted.
- `lang` (`core`, `default`, default `English`) — target language for code,
  documentation, files, and commit messages.
- `py_min` (`stack/python`, default `3.9`) — minimum target Python version
  injected into type-annotation and syntax rules.
- `single_file_build` (`release`, default `0`) — set `single_file_build=1` to
  enable single-file executable build and verification rules.
- `readme` (`stack/cli`, default `1`) — set `readme=0` to omit the standalone
  CLI `README.md` reference layout requirement.

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
- `agents/stack/` — cross-language CLI interface rules (`stack/cli/cli.bundle`)
  and language subtrees (`stack/python/python.bundle`).
- `agents/adapters/` — tool-to-role adapter bundles and lifecycle rules
  (`adapters/todo-md.bundle`).
- `agents/collab/`, `agents/os/`, `agents/vcs/`, `agents/release/`,
  `agents/bootstrap/` — collaboration, POSIX platform, version control, release
  (`release.bundle`), greenfield bootstrap (`bootstrap.bundle`), and multi-repo
  orchestration (`orchestrator.bundle`) rules.

## License

[MIT](LICENSE) © 2026 [vitalio](https://github.com/vitalio)
