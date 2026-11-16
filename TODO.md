# 🔵 [WIP] F16: Rename role/audit to role/review with two-stage quality gate

- Rename `rules/role/audit.md` to `rules/role/review.md` with `Universal Reviewer role` description and `- Role (Reviewer):` heading.
- Structure `rules/role/review.md` as a two-stage review: first verify objective compliance (passing tests and linters, task specification fulfillment, active workspace rules, SSOT, and documentation sync), stopping early on blockers; once the objective gate passes, evaluate architecture, module boundaries, readability, security, performance, and user-facing polish.
- Update `rules/role/AGENTS.md` and `README.md` to replace `audit`/`auditing` role references with `review`/`reviewing`, and release a new MINOR version.

# 🎯 [NEXT] F21: Remove redundant test start-indicator requirement from core and stack rules

- Remove the requirement to print a start/progress indicator (such as `Running unit tests...`) before running tests from `rules/core/edit.md`, `rules/core/diff-review.md`, and `rules/stack/python-cli.md`, while preserving concise pass summaries and full diagnostics/tracebacks on failure.
- Bump `VERSION` (`PATCH`) and release the updated rule set.

# 🎯 [NEXT] F13: Define role handoff contracts, target-file closure, and preloaded-context execution in rules/role/

- Update `rules/role/plan.md` so the Planner determines the full target file closure for each prioritized task (source modules, CLI help, docs, paired rules, and tests per `AGENTS.md` and active stack rules), records those file paths in the task body, and preloads them into the new session context when handing off to working.
- Update `rules/role/work.md` (renamed from `rules/role/execute.md` per F9) so that when a task's target files are already preloaded in the initial session context, the agent skips a separate read-only discovery step and proceeds directly in step 1 to edits, project build/linter/test verification, and diff output (running an initial batched read step only for files not yet in context).
- Update `rules/role/design.md` and `rules/role/review.md` (renamed from `rules/role/audit.md` per F16) so Designer records module-boundary and file-coupling invariants in `AGENTS.md` for downstream planning/working, and Reviewer verifies those project-specific `AGENTS.md` invariants alongside task specifications.

# 🎯 [NEXT] F4: Support greenfield project bootstrap and tool-agnostic wording in role/design

- Update `rules/role/design.md` so that when designing a new project from scratch, once the design is agreed with the user, the agent creates the target project directory, initializes version control, and scaffolds `AGENTS.md`, project context configuration, and the initial project task backlog before committing the initial scaffold.
- Replace the hardcoded `.agents_bundle` filename in `rules/role/design.md` with tool-agnostic wording so `rules/role/` complies with `AGENTS.md` and `rules/role/AGENTS.md` taxonomic invariants.

# 🎯 [NEXT] F10: Specify structured --help layout and complete option listings in stack/cli

- Update `rules/stack/cli.md` to require structured `Usage:`/`Commands:` and `Options:` sections in `-h`/`--help` output (showing short/long flag forms, argument placeholders, defaults, and side effects such as Git commits or network calls) rather than burying flags in prose or listing partial option sets.

# 🎯 [NEXT] F9: Rename role/execute to role/work

- Rename `rules/role/execute.md` to `rules/role/work.md` with `Universal Worker role` description and `- Role (Worker):` heading, update `rules/role/AGENTS.md`, `rules/role/plan.md`, and `README.md` to replace `execute`/`executing` role references with `work`/`working`, and release a new MINOR version.

# ⚪ [NEW] F5: Wrap prose at ~80 columns across all remaining rule files

- Wrap long lines (>80 chars) in `rules/collab/external.md`, `rules/core/AGENTS.md`, `rules/core/composability.md`, `rules/core/diff-review.md`, `rules/core/end.md`, `rules/core/lang.md`, `rules/core/plan.md`, `rules/core/secrets.md`, `rules/core/ssot.md`, `rules/os/*.md`, `rules/release/single-file-build.md`, `rules/stack/python-cli.md`, and `rules/vcs/*.md` to ~80 characters per line.

# ⚪ [NEW] F6: Group bundle directives at the top of .agents_bundle

- Depends on: agents_bundle:F5
- Move bundle vitalio/todo_md to the top of .agents_bundle alongside bundle vitalio/run_block and bundle vitalio/agents_bundle before ruleset, rule, and $ <cmd> directives.
- Keep the .agents_bundle usage example in README.md in sync.

# ⚪ [NEW] F11: Remove leftover .bundle authoring references from AGENTS.md

- Remove '.bundle' references from AGENTS.md lines 22 and 30 since agents-rules only hosts rules/ and rulesets/ after moving tool bundles to their own repositories in v0.10.0.

# ⚪ [NEW] F12: Define pre-release versioning convention in release/semver

- Add an optional `PRE-RELEASE` clause (`X.Y.Z-alpha.N`, `X.Y.Z-beta.N`, `X.Y.Z-rc.N` starting at `N=1`) to `rules/release/semver.md` for experimental or staged builds when explicitly requested, specifying that pre-release identifiers attach to the upcoming target version `X.Y.Z` and are stripped without re-bumping `X.Y.Z` upon final release.

# ⚪ [NEW] F18: Define responsibility split between README.md and AGENTS.md in core/docs

- Add `rules/core/docs.md` defining the separation of concerns between `README.md` (external public contract: purpose, installation, CLI flags, environment variables, input/output protocols, and integration examples) and `AGENTS.md` (concise internal engineering guide: module boundaries, cross-file invariants, negative constraints, and build/test verification steps).
- Forbid duplicating `README.md` tutorials, marketing descriptions, or full reference tables inside `AGENTS.md`, keeping `AGENTS.md` focused on repository-specific delta knowledge an agent cannot infer from the file tree.
- Include `rule core/docs` in `rulesets/core.ruleset`, follow `AGENTS.md` formatting conventions (plain bullets, ~80-char line wrapping, no decorative bold/italic emphasis), and release a new MINOR version.

- Move the documentation synchronization and `AGENTS.md` plain-text formatting clauses out of `rules/core/edit.md` into `rules/core/docs.md` so documentation rules live in one canonical place without duplication.

# ⚪ [NEW] F19: Extract internal task ID restriction from collab/external into a separate opt-in rule

- Remove the internal task ID restriction from `rules/collab/external.md` and move it into a separate opt-in rule (e.g. `rules/collab/no-task-ids.md`) so projects can include it only when they want to hide task IDs in commits and external updates.
- Keep `rulesets/default.ruleset` and `README.md` in sync.

# ⚪ [NEW] F20: Replace rulesets with bundles and organize rules logically by domain

- Depends on: vitalio/agents_bundle#F15
- Migrate `rulesets/core.ruleset` and `rulesets/default.ruleset` to `.bundle` files and reorganize `rules/` and `rulesets/` into a logical domain-based directory structure.
- Update `AGENTS.md` and `README.md` to reflect the unified rule/bundle layout.
