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

# ⚪ [NEW] F20: Audit and slim all rules, add role=law and adapters/todo_md, drop Windows support, and migrate to agents/

- Depends on: D1, F40, F42, F43, F44
- Implement the full rule audit, deduplication, role gating, and `agents/` package migration per `todo_flow` `docs/adr/0003-task-targeted-bundle-architecture-and-atomic-rule-taxonomy.md`:
  - Standardize `agents/` as the single package root directory for all atomic rules (`.md`) and composite bundles (`.bundle`), removing `rulesets/` and `rules/` and using the unified 4-space indented `.bundle` syntax (`bundle`, `rule`, `file`, `cmd`, `prompt`, `let`, `export`, `if` / `else if` / `else`).
  - Drop Windows support: delete `os/windows.md`, remove `if os=windows` from `agents/default.bundle`, and remove `install.ps1` from `agents/release/single-file-build.md`.
  - Keep all `.bundle` files in `agents-rules` as flat bricks of `rule` directives (no nested `bundle` inside `.bundle`): `agents/core.bundle` (with `default.bundle` as legacy alias) contains universal axioms (`isolation`, `start`, `secrets`, `plan`, `ssot`, `composability`, `lang lang=English`, `end`, `collab/external`), POSIX `os/{linux,macos}`, `vcs/{git,cvs}`, `if role!= -> rule role/{role:} + export role`, and role-gated `core/edit`, `core/diff-review`, and `core/docs`.
  - Add `agents/role/law.md` (`role=law`, Legislative Counsel for `L*` rule, bundle, and `AGENTS.md` tasks: precedence/conflict audit, least-specific ancestor placement, orthogonal single-axis facets, imperative testable bullets, `# Description:` header, no decorative bold/italic, ~80-col wrapping, and `{var:default}` parameterization).
  - Gate mutation, diff-review, docs, and testing rules by role inside `agents/default.bundle` (`if role!= -> rule role/{role:} + export role`, `if role=work,law -> rule core/edit + rule core/diff-review`, `if role=work,design,review,law -> rule core/docs`), removing duplicated test-runner dot-progress paragraphs from `core/edit.md` and `core/diff-review.md`.
  - Extract software-engineering specifics into `agents/coding/` (`AGENTS.md`, `coding.bundle`, `architecture.md` gated on `if role=work,design,review`, `testing.md` gated on `if role=work,review` as the single canonical rule for `tests/test_<module>.py` and dot-progress runner execution, and role overlays `coding/{design,plan,work,review}.md`).
  - Decompose `rules/stack/python-*.md` into `agents/stack/python/` (`AGENTS.md`, `syntax.md`, `unittest.md`, `stdlib.md`, `annotations.md`, and `python.bundle` gated on `if role=work,review`) orthogonal to `agents/stack/cli.md`.
  - Add `agents/adapters/todo_md.bundle` and `agents/adapters/todo_md/{work,backlog}.md` mapping `todo_md.role`, `todo_md.prefix` (`D -> design`, `L -> law`), and `todo_md.status` (`WIP,NEXT -> work`, `NEW,QUESTION,HOLD -> plan`) to `role` and exporting `role`, `task`, and `title`.
  - Add on-demand scenario bundles: `agents/bootstrap/bootstrap.bundle` (`bootstrap/scaffold.md`, `bootstrap/questionnaire.md`), `agents/release/release.bundle` (`release/semver.md`, `release/github-ci.md`, conditional `release/single-file-build.md`), and `agents/orchestrator.bundle` (`collab/multi-repo.md`).
- Update `.github/workflows/ci.yml`, `.ctx.bundle` / `.agents_bundle`, `AGENTS.md`, and `README.md`, wrap modified files at ~80 columns, and bump `VERSION` (`MINOR`).
