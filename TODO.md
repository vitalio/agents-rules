# 🎯 [NEXT] F44: Simplify role/plan.md Target files rule to record only already-known files without dedicated search steps or slices

- In `rules/role/plan.md`, update the `- Target files:` bullet so the Planner records target file paths (in backticks, excluding `TODO.md`, `TODO_ARCHIVE.md`, and `AGENTS.md`) only when those files are already known from the planning discussion, without spending dedicated steps searching for target files, checking the 400-line threshold, or computing internal symbol/line slices.
- Wrap modified prose at ~80 columns and bump `VERSION` (`PATCH`).
- Target files: `rules/role/plan.md`, `VERSION`.

# 🎯 [NEXT] F43: Clarify in rules/stack/cli.md that --help 100-column width is measured in display columns rather than mawk UTF-8 bytes

- In `rules/stack/cli.md` (under `Help column alignment and width`), note that the 100-column limit applies to rendered display columns / Unicode characters (verified via display-width helpers or unit tests) rather than `awk 'length($0)'`, because `mawk` measures `length($0)` in UTF-8 bytes and reports false positives on lines with multi-byte Unicode symbols or emoji.
- Target files: `rules/stack/cli.md`.

# 🎯 [NEXT] F40: Add release/github-ci rule, interactive CI/Release questionnaire, and tag-triggered GitHub Release workflow

- Create `rules/release/github-ci.md` defining the GitHub Actions CI & Release workflow standard (`.github/workflows/ci.yml`):
  - Interactive CI/Release questionnaire for `role=design` and `role=plan`: when bootstrapping or configuring CI/Release and requirements are not yet specified in `AGENTS.md` or the task, briefly ask the user across 4 points rather than guessing:
    1. Triggers & branches: push/PR branches (`main`) and whether `v*` tag pushes (`tags: ['v*']`) should automatically publish GitHub Releases.
    2. OS / runtime matrix: single `ubuntu-latest` runner (for rule catalogs, docs, or pure POSIX tools) vs cross-platform matrix (`ubuntu-latest`, `macos-latest`, `windows-latest`).
    3. Verification gate (`test` job): fast syntax, linter, build/test, or catalog integrity checks to run before release, plus verifying on `refs/tags/v*` that `GITHUB_REF_NAME` matches `"v$(tr -d '[:space:]' < VERSION)"`.
    4. Release assets (`release` job): source-only release notes (`generate_release_notes: true` with `LICENSE`) vs attaching built artifacts (standalone executable, `install.sh`, `install.ps1`, `LICENSE`).
  - Workflow invariants: set `permissions: contents: write`, gate `release` on `needs: test` and `if: startsWith(github.ref, 'refs/tags/v')`, and use `softprops/action-gh-release@v2` with `generate_release_notes: true`.
- Update `rules/role/design.md` so greenfield project bootstrap includes agreeing on the CI & release strategy with the user.
- Create `.github/workflows/ci.yml` in `agents-rules` following `rules/release/github-ci.md`:
  - Trigger on `push` (`branches: [main]`, `tags: ['v*']`) and `pull_request` (`branches: [main]`) on `ubuntu-latest` with `permissions: contents: write`.
  - In `test`, validate that every rule (`.md` under `rules/`) and ruleset/bundle (`.ruleset` / `.bundle`) starts with `# Description: `, check that rule files and `AGENTS.md` contain no decorative bold (`**...**`) outside fenced/inline code, verify that every `rule` / `ruleset` reference in `rulesets/*` resolves to an existing file, and on `refs/tags/v*` verify that the tag matches `v$(tr -d '[:space:]' < VERSION)`.
  - In `release` (`needs: test`, `if: startsWith(github.ref, 'refs/tags/v')`), publish the GitHub Release via `softprops/action-gh-release@v2` with `generate_release_notes: true` and `files: LICENSE`.
- Enable `rule vitalio/agents-rules:release/github-ci` in `.agents_bundle`, wrap modified prose at ~80 columns, and bump `VERSION` (`MINOR`) with an annotated release tag so GitHub Actions publishes the new latest release.
- Target files: `rules/release/github-ci.md`, `rules/role/design.md`, `rules/release/semver.md`, `.github/workflows/ci.yml`, `.agents_bundle`, `AGENTS.md`, `README.md`, `VERSION`.

# ⚪ [NEW] F20: Replace rulesets with bundles and organize rules logically by domain

- Depends on: D1, F40, F42, F43, F44
- Standardize `agents/` as the single package root directory for all rules (`.md`) and bundles (`.bundle`), migrating `rulesets/core.ruleset` -> `agents/core.bundle`, `rulesets/default.ruleset` -> `agents/default.bundle`, `rulesets/orchestrator.ruleset` -> `agents/orchestrator.bundle`, and `rules/*` (including `rules/release/github-ci.md`) into `agents/*` (after `agents_bundle` supports the `agents/` layout and unified `.bundle` resolution).
- Extract software-engineering specifics out of universal `agents/role/{design,plan,work,review}.md` and `agents/core/composability.md` into the `agents/coding/` domain subtree (`agents/coding/AGENTS.md`, `agents/coding/coding.bundle`, `agents/coding/architecture.md`, `agents/coding/testing.md`, and additive role overlays `agents/coding/{design,plan,work,review}.md` activated via `[if role!=] rule coding/{role:}` in `agents/coding/coding.bundle`):
  - Keep base `agents/role/{design,plan,work,review}.md` strictly domain-agnostic (cognitive stance, artifact modification boundaries, target-file closure and `path:start-end` slice handoffs, two-stage review gate, and backlog lifecycle).
  - Place modular code structure rules (~300-800 line module budget under `src/`, splitting modules >1000 lines or mixing layers, layered separation between parsing/domain/rendering/CLI, single-abstraction-level functions, and a single canonical algorithm per domain invariant) in `agents/coding/architecture.md`.
  - Place language-agnostic test architecture rules (modular `tests/test_<module>.*` mirroring source modules, domain-behavior test naming without task-ID prefixes, offline/stubbed network isolation, temporary-directory filesystem isolation, and in-step test runs with live `.` progress indicators) in `agents/coding/testing.md`.
  - Place software-engineering role constraints (`src/` and `tests/` modification prohibition in `design`/`plan`/`review`, `docs/adr/NNNN-<slug>.md` and greenfield repo bootstrap in `design`, full code/CLI/doc/test target-file closure in `plan`, in-step and guarded-commit linter/test verification in `work`, and Stage 1 test/linter/doc compliance plus Stage 2 architecture/security/performance review in `review`) in `agents/coding/{design,plan,work,review}.md`.
- Decompose `rules/stack/python-cli.md`, `rules/stack/python-stdlib.md`, and `rules/stack/python-annotations.md` into an orthogonal `agents/stack/python/` subtree separate from `agents/stack/cli.md`:
  - `agents/stack/python/syntax.md` (`ast.parse` syntax verification).
  - `agents/stack/python/unittest.md` (strictly Python `unittest` mechanics: `python3 -m unittest discover -s tests` at default verbosity `1` without `-q`/`-v`/`-b`, shared base classes and fixtures in `tests/helpers.py` without `test_` prefix, `contextlib.redirect_stdout`/`redirect_stderr` output capture and `with` resource hygiene, `msg=proc.stderr` and `self.subTest(...)` failure diagnostics, `tempfile.TemporaryDirectory`, and programmatic test splitting via `ast.parse()` `node.lineno`..`node.end_lineno`).
  - `agents/stack/python/stdlib.md` (opt-in Python 3 standard-library-only invariant).
  - `agents/stack/python/annotations.md` (opt-in `from __future__ import annotations` for `{py_min:3.9}` and `src/header.py`).
  - `agents/stack/python/python.bundle` (default Python preset loading `rule stack/python/syntax` and `rule stack/python/unittest`).
- Update `.github/workflows/ci.yml`, `.agents_bundle` (`include AGENTS.md` and `include agents/**/AGENTS.md`), `AGENTS.md`, and `README.md` to reflect the unified `agents/` rule/bundle layout, wrap all modified files at ~80 columns, and bump `VERSION` for a MINOR release.

# ⚪ [NEW] F25: Rename project and package references from agents-rules to ctx-taxonomy

- Rename package identity, documentation, and internal references from `agents-rules` (`vitalio/agents-rules`) to `ctx-taxonomy` (`vitalio/ctx-taxonomy`), aligned with the ecosystem rename design.
- Target files: `AGENTS.md`, `README.md`, `.agents_bundle`, `VERSION`, and exported rule/bundle files (`rules/`, `rulesets/`, or `agents/` after `F20`).
- Acceptance criteria: all docs, examples, and package references use `ctx-taxonomy` (alongside sibling names `ctx-bundle`/`cxb`, `todo-markdown`/`tmd`, `run-block`/`rxb`), `VERSION` is bumped appropriately, and repository checks pass.
