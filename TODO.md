# 🎯 [NEXT] L3: Define README.md progressive-disclosure and CLI reference formatting rules

- Decide taxonomic placement in role=law per AGENTS.md abstraction-promotion rules: universal progressive-disclosure README conventions (one-line tagline, concise overview without low-level protocol dumps in the intro, scenario-grouped Quick Start instead of monolithic command dumps) in agents/core/docs.md vs CLI-specific reference layout (Quick Installation, scenario-based Quick Start, and structured Commands / Options / Environment reference tables synced with -h/--help) in agents/stack/cli.md (or a dedicated rule file).
- Keep all rule files under agents/ starting with '# Description:', plain '- Topic: instruction.' bullets, and ~80-column prose wrapping.
- Run context --update-cache after pushing so downstream repositories pick up the updated rules.

# 🎯 [NEXT] L2: Update adapters and documentation for renamed CLIs (todo, context, run)

- Rename `agents/adapters/todo_md.bundle` and `agents/adapters/todo_md/{work,backlog}.md` to `agents/adapters/todo-md.bundle` and `agents/adapters/todo-md/{work,backlog}.md` per `todo_flow:D8` (`docs/adr/0004-ecosystem-rename-and-cutover.md`).
- Update `agents/adapters/todo-md.bundle` to support qualified `vitalio.todo_md.*` and short `todo_md.*` upstream variables and load `adapters/todo-md/{work,backlog}`.
- Update `agents/adapters/todo-md/{work,backlog}.md`, `README.md`, and `AGENTS.md` examples to reference the renamed `todo`, `context`, and `run` CLIs (`todo <ID> | context | run`, `context --list`, `context role=law | run`).
- After pushing `origin/main`, run `context --update-cache` and update `bundle vitalio/agents-rules:adapters/todo-md` across workspace `.context.bundle` files so subsequent sessions resolve the renamed adapter immediately.
- Acceptance criteria: all rule and bundle files under `agents/` start with `# Description:`, follow ~80-column prose wrapping, and contain no stale `todo_md`/`agents_bundle`/`run_block` CLI invocation examples.
