# 🎯 [NEXT] F10: Specify structured --help layout and complete option listings in stack/cli

- Update `rules/stack/cli.md` to require structured `Usage:`/`Commands:` and `Options:` sections in `-h`/`--help` output (showing short/long flag forms, argument placeholders, defaults, and side effects such as Git commits or network calls) rather than burying flags in prose or listing partial option sets.

# 🎯 [NEXT] F9: Rename role/execute to role/work

- Rename `rules/role/execute.md` to `rules/role/work.md` with `Universal Worker role` description and `- Role (Worker):` heading, update `rules/role/AGENTS.md`, `rules/role/plan.md`, and `README.md` to replace `execute`/`executing` role references with `work`/`working`, and release a new MINOR version.

# ⚪ [NEW] F4: Decouple role/design from hardcoded .agents_bundle filename

- Remove the hardcoded `.agents_bundle` reference from `rules/role/design.md` in favor of tool-agnostic wording so `rules/role/` complies with `AGENTS.md` and `rules/role/AGENTS.md` taxonomic invariants.

# ⚪ [NEW] F5: Wrap prose at ~80 columns across all remaining rule files

- Wrap long lines (>80 chars) in `rules/collab/external.md`, `rules/core/AGENTS.md`, `rules/core/composability.md`, `rules/core/diff-review.md`, `rules/core/end.md`, `rules/core/lang.md`, `rules/core/plan.md`, `rules/core/secrets.md`, `rules/core/ssot.md`, `rules/os/*.md`, `rules/release/single-file-build.md`, `rules/stack/python-cli.md`, and `rules/vcs/*.md` to ~80 characters per line.

# ⚪ [NEW] F6: Group bundle directives at the top of .agents_bundle

- Move bundle vitalio/todo_md to the top of .agents_bundle alongside bundle vitalio/run_block and bundle vitalio/agents_bundle before ruleset, rule, and $ <cmd> directives.

# ⚪ [NEW] F7: Verify completed task specification compliance in role/audit

- Update rules/role/audit.md so that when auditing a completed task or commit, the auditor verifies that the implementation, tests, and documentation fulfill all requirements of the task specification alongside all active workspace rules.
