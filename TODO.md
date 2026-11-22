# 🎯 [NEXT] F44: Simplify role/plan.md Target files rule to record only already-known files without dedicated search steps or slices

- In `rules/role/plan.md`, update the `- Target files:` bullet so the Planner records target file paths (in backticks, excluding `TODO.md`, `TODO_ARCHIVE.md`, and `AGENTS.md`) only when those files are already known from the planning discussion, without spending dedicated steps searching for target files, checking the 400-line threshold, or computing internal symbol/line slices.
- Wrap modified prose at ~80 columns and bump `VERSION` (`PATCH`).
- Target files: `rules/role/plan.md`, `VERSION`.

# 🎯 [NEXT] F43: Clarify in rules/stack/cli.md that --help 100-column width is measured in display columns rather than mawk UTF-8 bytes

- In `rules/stack/cli.md` (under `Help column alignment and width`), note that the 100-column limit applies to rendered display columns / Unicode characters (verified via display-width helpers or unit tests) rather than `awk 'length($0)'`, because `mawk` measures `length($0)` in UTF-8 bytes and reports false positives on lines with multi-byte Unicode symbols or emoji.
- Target files: `rules/stack/cli.md`.

# 🎯 [NEXT] F40: Add concise release/github-ci rule and tag-triggered GitHub Release workflow

- Depends on: F43, F44
- Create a concise atomic `rules/release/github-ci.md` rule (later migrated to `agents/release/github-ci.md` in `F20`) defining the GitHub Actions CI & Release workflow invariants (`.github/workflows/ci.yml`):
  - Keep the rule short and focused on verification and release invariants (`permissions: contents: write`, `test` gate verifying syntax/linters/tests and on `refs/tags/v*` checking `GITHUB_REF_NAME == "v$(tr -d '[:space:]' < VERSION)"`, and `release` job gated on `needs: test` and `if: startsWith(github.ref, 'refs/tags/v')` using `softprops/action-gh-release@v2` with `generate_release_notes: true`).
  - Do not bloat `rules/role/design.md` or always-on session rules with greenfield CI/Release questionnaires; interactive project/CI bootstrap belongs to the on-demand `bootstrap.bundle` (`F20`).
- Create `.github/workflows/ci.yml` in `agents-rules` following `rules/release/github-ci.md`:
  - Trigger on `push` (`branches: [main]`, `tags: ['v*']`) and `pull_request` (`branches: [main]`) on `ubuntu-latest` with `permissions: contents: write`.
  - In `test`, validate that every rule (`.md`) and ruleset/bundle (`.ruleset` / `.bundle`) starts with `# Description: `, check that rule files and `AGENTS.md` contain no decorative bold (`**...**`) outside fenced/inline code, verify that every `rule` / `ruleset` / `bundle` reference resolves to an existing file, and on `refs/tags/v*` verify that the tag matches `v$(tr -d '[:space:]' < VERSION)`.
  - In `release` (`needs: test`, `if: startsWith(github.ref, 'refs/tags/v')`), publish the GitHub Release via `softprops/action-gh-release@v2` with `generate_release_notes: true` and `files: LICENSE`.
- Wrap modified prose at ~80 columns and bump `VERSION` (`MINOR`) with an annotated release tag.
- Target files: `rules/release/github-ci.md`, `.github/workflows/ci.yml`, `AGENTS.md`, `README.md`, `VERSION`.

# ⚪ [NEW] F20: Audit and slim all rules, replace rulesets with task-targeted bundles, and migrate to agents/

- Depends on: D1, F40, F42, F43, F44
- Standardize `agents/` as the single package root directory for all atomic rules (`.md`) and composite bundles (`.bundle`), removing `rulesets/` and migrating `rules/*` into logical domain subtrees under `agents/*` per the `todo_flow:D1` architecture.
- Audit and slim every rule file for brevity, single responsibility, and zero cross-file duplication:
  - Eliminate repeated test-runner dot-progress and pre-commit prose across `core/edit.md`, `core/diff-review.md`, and `stack/python/*`.
  - Keep `agents/core.bundle` strictly minimal and universal (`isolation`, `start`, `secrets`, `plan`, `ssot`, `lang`, `end`).
  - Load mutation, diff-review, commit, and testing rules conditionally by role (`if role=work` / `if role=review`) inside `agents/default.bundle`, `agents/coding/coding.bundle`, and `agents/stack/python/python.bundle` so `role=design` and `role=plan` sessions stay free of code-editing and test-runner overhead.
- Extract software-engineering specifics out of universal `agents/role/{design,plan,work,review}.md` and `agents/core/composability.md` into `agents/coding/` (`AGENTS.md`, `coding.bundle`, `architecture.md`, `testing.md`, and role overlays `coding/{design,plan,work,review}.md` activated via `if role!= rule coding/{role:}`).
- Decompose `rules/stack/python-*.md` into `agents/stack/python/` (`syntax.md`, `unittest.md`, `stdlib.md`, `annotations.md`, and `python.bundle`) orthogonal to `agents/stack/cli.md`.
- Provide on-demand task-targeted bundles instead of overloading default rules:
  - `agents/bootstrap/bootstrap.bundle` (and `bootstrap/*.md`): greenfield repository initialization, `.agents_bundle` setup, and the interactive 4-point CI/Release & stack questionnaire (invoked on demand by `lets init` or `agents_bundle bundle vitalio/agents-rules:bootstrap`, removed from `role/design.md`).
  - `agents/release/release.bundle` (`release/semver.md`, `release/github-ci.md`, `release/single-file-build.md`): loaded when cutting releases or configuring release pipelines.
  - `agents/orchestrator.bundle` (`collab/multi-repo.md`): multi-repository orchestration preset.
- Update `.github/workflows/ci.yml`, `.agents_bundle`, `AGENTS.md`, and `README.md` to reflect the unified `agents/` layout, wrap modified files at ~80 columns, and bump `VERSION` (`MINOR`).

# ⚪ [NEW] F25: Rename project and package references from agents-rules to ctx-taxonomy

- Rename package identity, documentation, and internal references from `agents-rules` (`vitalio/agents-rules`) to `ctx-taxonomy` (`vitalio/ctx-taxonomy`), aligned with the ecosystem rename design.
- Target files: `AGENTS.md`, `README.md`, `.agents_bundle`, `VERSION`, and exported rule/bundle files (`rules/`, `rulesets/`, or `agents/` after `F20`).
- Acceptance criteria: all docs, examples, and package references use `ctx-taxonomy` (alongside sibling names `ctx-bundle`/`cxb`, `todo-markdown`/`tmd`, `run-block`/`rxb`), `VERSION` is bumped appropriately, and repository checks pass.
