# agents-rules

Open encyclopedia and taxonomic catalog of composable AI agent axioms
(`agents/core/`), operating roles (`agents/role/`), domain overlays
and technical stack subtrees (`agents/coding/`), tool adapters
(`agents/adapters/`), and composite bundles (`agents/**/*.bundle`).

## Usage in `.context.bundle`

```text
bundle vitalio/agents-rules:core
bundle vitalio/agents-rules:coding
bundle vitalio/agents-rules:coding/python py_min=3.9
bundle vitalio/agents-rules:coding/cli
bundle vitalio/agents-rules:adapters/todo-md
bundle vitalio/agents-rules:release single_file_build=1
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
documentation rules across `core` and domain bundles (`coding`, `coding/*`,
`adapters/*`). Set a role explicitly (`context role=<name>`) or let
`adapters/todo-md` derive it from task prefix and status:

- `design` (Designer) — concept exploration, architecture, interface design,
  and ADR persistence (`docs/adr/`) without modifying project deliverables
  (auto-selected for `D*` tasks and `bootstrap`).
- `plan` (Planner) — workspace analysis, backlog triage, task decomposition and
  consolidation, role routing, and dependency-chain wiring without modifying
  project deliverables (auto-selected for `NEW`, `QUESTION`, and `HOLD` tasks,
  and for piped backlog views such as `todo | context | run`).
- `work` (Worker) — focused, low-chatter task delivery and verification
  strictly within agreed task scope (auto-selected for `WIP` and `NEXT`
  deliverable tasks).
- `review` (Reviewer) — two-stage objective compliance gate and qualitative
  evaluation without modifying project deliverables.
- `law` (Legislative Counsel) — authoring, auditing, refactoring, and
  tailoring agent rules, bundles, and `AGENTS.md` instructions without
  modifying project deliverables (auto-selected for `L*` tasks).

## Bundle Parameters

Pass parameters inline on `bundle` directives in `.context.bundle` or as
`key=val` arguments to `context` (run `context --list` to inspect active
defaults dynamically):

- `os` (`core`, `default`) — target operating system rules (`linux`, `macos`);
  auto-detected by `context` when omitted.
- `vcs` (`core`, `default`) — version control workflow rules (`git`, `cvs`);
  auto-detected by `context` when omitted.
- `lang` (`core`, `default`, default `English`) — target language for code,
  commands, comments, output strings, project files, documentation, and commit
  messages.
- `chat_lang` (`core`, `default`, default `the language the user writes in`) —
  target language for chat prose to the user.
- `chat_date_fmt` (`core`, `default`, default `DD/MM/YYYY`) — date format used
  when formatting dates to the user in chat.
- `py_min` (`coding/python`, default `3.9`) — minimum target Python version
  injected into type-annotation and syntax rules.
- `stdlib_only` (`coding/python`, default `1`) — set `stdlib_only=0` to omit
  the standard-library-only dependency constraint.
- `single_file_build` (`release`, default `0`) — set `single_file_build=1` to
  enable single-file executable build and verification rules.
- `readme` (`coding/cli`, default `1`) — set `readme=0` to omit the standalone
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
  and additive role overlays (`coding.bundle`), plus CLI interface rules
  (`coding/cli/cli.bundle`) and language subtrees
  (`coding/python/python.bundle`).
- `agents/adapters/` — tool-to-role adapter bundles and lifecycle rules
  (`adapters/todo-md.bundle`).
- `agents/collab/`, `agents/os/`, `agents/vcs/`, `agents/release/`,
  `agents/bootstrap/` — collaboration, POSIX platform, version control, release
  (`release.bundle`), greenfield bootstrap (`bootstrap.bundle`), and multi-repo
  orchestration (`orchestrator.bundle`) rules.

## License

[MIT](LICENSE) © 2026 [vitalio](https://github.com/vitalio)
