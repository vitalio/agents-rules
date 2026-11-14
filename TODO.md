# 🎯 [NEXT] F3: Align core/plan and role/execute for pre-agreed backlog tasks

- Update `rules/core/plan.md` so high-level plan + waiting for user agreement is required when task scope is not yet agreed, and explicitly forbid emitting a plan and file modifications (or code dumps) in the same message.
- Update `rules/role/execute.md` so that for an already-agreed backlog task, after batched file inspection the agent proceeds directly to the edit/test/diff step without outputting a redundant implementation plan or code in chat prose (pausing only on blockers or conflicts).
- Update `rules/core/start.md` so uncommitted changes limited to project task-backlog files do not block starting an execution session on the queued task.

# ⚪ [NEW] F4: Decouple role/design from hardcoded .agents_bundle filename

- Remove the hardcoded `.agents_bundle` reference from `rules/role/design.md` in favor of tool-agnostic wording so `rules/role/` complies with `AGENTS.md` and `rules/role/AGENTS.md` taxonomic invariants.

# ⚪ [NEW] F5: Wrap prose at ~80 columns across all remaining rule files

- Wrap long lines (>80 chars) in `rules/collab/external.md`, `rules/core/AGENTS.md`, `rules/core/composability.md`, `rules/core/diff-review.md`, `rules/core/end.md`, `rules/core/lang.md`, `rules/core/plan.md`, `rules/core/secrets.md`, `rules/core/ssot.md`, `rules/os/*.md`, `rules/release/single-file-build.md`, `rules/stack/python-cli.md`, and `rules/vcs/*.md` to ~80 characters per line.

# ⚪ [NEW] F6: Group bundle directives at the top of .agents_bundle

- Move bundle vitalio/todo_md to the top of .agents_bundle alongside bundle vitalio/run_block and bundle vitalio/agents_bundle before ruleset, rule, and $ <cmd> directives.
