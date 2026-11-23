# 🎯 [NEXT] L2: Update adapters and documentation for renamed CLIs (todo, context, run)

- Rename `agents/adapters/todo_md.bundle` and `agents/adapters/todo_md/{work,backlog}.md` to `agents/adapters/todo-md.bundle` and `agents/adapters/todo-md/{work,backlog}.md` per `todo_flow:D8` (`docs/adr/0004-ecosystem-rename-and-cutover.md`).
- Update `agents/adapters/todo-md.bundle` to support qualified `vitalio.todo_md.*` and short `todo_md.*` upstream variables and load `adapters/todo-md/{work,backlog}`.
- Update `agents/adapters/todo-md/{work,backlog}.md`, `README.md`, and `AGENTS.md` examples to reference the renamed `todo`, `context`, and `run` CLIs (`todo <ID> | context | run`, `context --list`, `context role=law | run`).
- Acceptance criteria: all rule and bundle files under `agents/` start with `# Description:`, follow ~80-column prose wrapping, and contain no stale `todo_md`/`agents_bundle`/`run_block` CLI invocation examples.
