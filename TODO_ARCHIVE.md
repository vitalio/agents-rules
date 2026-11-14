# ✅ [DONE] F1: Bootstrap .agents_bundle and TODO.md and refine semver/todo_md release rules — *2026-11-14*

- Add .agents_bundle and initialize TODO.md / TODO_ARCHIVE.md in agents-rules.
- Require staging task-backlog updates (--no-commit) before the release commit so release tags point to HEAD.
- Clarify PATCH and MINOR criteria for rule/ruleset/bundle changes in rules/release/semver.md.

# ✅ [DONE] F2: Move tool bundles to tool repositories and remove --agents from stack/cli rule — *2026-11-14*

# ✅ [DONE] F3: Align core/plan and role/execute for pre-agreed backlog tasks — *2026-11-14, Aligned core/plan, role/execute, and core/start for pre-agreed backlog tasks*

- Update `rules/core/plan.md` so high-level plan + waiting for user agreement is required when task scope is not yet agreed, and explicitly forbid emitting a plan and file modifications (or code dumps) in the same message.
- Update `rules/role/execute.md` so that for an already-agreed backlog task, after batched file inspection the agent proceeds directly to the edit/test/diff step without outputting a redundant implementation plan or code in chat prose (pausing only on blockers or conflicts).
- Update `rules/core/start.md` so uncommitted changes limited to project task-backlog files do not block starting an execution session on the queued task.
