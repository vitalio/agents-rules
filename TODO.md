# ⚪ [NEW] L2: Update adapters and documentation for renamed CLIs (todo, ctx, run)

- Update `agents/adapters/todo_md/` rules (`work.md`, `backlog.md`) and `agents/adapters/todo_md.bundle` (plus any agreed `adapters/todo.bundle` alias per `todo_flow:D8`) to reference the `todo`, `ctx`, and `run` CLIs and producer namespace conventions.
- Update `README.md` and `AGENTS.md` examples (`ctx role=law`, `ctx --list`, `todo <ID> | ctx | run`) to use the renamed ecosystem commands.
- Acceptance criteria: all rule and bundle files under `agents/` start with `# Description:`, follow ~80-column prose wrapping, and contain no stale `todo_md`/`agents_bundle`/`run_block` CLI invocation examples.
