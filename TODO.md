# 🎯 [NEXT] F5: Wrap prose at ~80 columns across all remaining rule files

- Depends on: F31, F32, F34
- Wrap long lines (>80 chars) across all remaining rule files in `rules/` (`rules/collab/*.md`, `rules/core/*.md`, `rules/os/*.md`, `rules/release/*.md`, `rules/role/*.md`, `rules/stack/*.md`, `rules/vcs/*.md`) to ~80 characters per line and bump `VERSION` for a PATCH release.

# ⚪ [NEW] F20: Replace rulesets with bundles and organize rules logically by domain

- Depends on: D1
- Standardize `agents/` as the single package root directory for all rules (`.md`) and bundles (`.bundle`), migrating `rulesets/core.ruleset` -> `agents/core.bundle`, `rulesets/default.ruleset` -> `agents/default.bundle`, `rulesets/orchestrator.ruleset` -> `agents/orchestrator.bundle`, and `rules/*` into `agents/*` (after `agents_bundle` supports the `agents/` layout and unified `.bundle` resolution).
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
- Update `.agents_bundle` (`include AGENTS.md` and `include agents/**/AGENTS.md`), `AGENTS.md`, and `README.md` to reflect the unified `agents/` rule/bundle layout, wrap all modified files at ~80 columns, and bump `VERSION` for a MINOR release.

# ⚪ [NEW] F25: Rename project and package references from agents-rules to ctx-taxonomy

- Rename package identity, documentation, and internal references from `agents-rules` (`vitalio/agents-rules`) to `ctx-taxonomy` (`vitalio/ctx-taxonomy`), aligned with the ecosystem rename design.
- Target files: `AGENTS.md`, `README.md`, `.agents_bundle`, `VERSION`, and exported rule/bundle files (`rules/`, `rulesets/`, or `agents/` after `F20`).
- Acceptance criteria: all docs, examples, and package references use `ctx-taxonomy` (alongside sibling names `ctx-bundle`/`cxb`, `todo-markdown`/`tmd`, `run-block`/`rxb`), `VERSION` is bumped appropriately, and repository checks pass.

# ⚪ [NEW] F39: agents_bundle include silently ignores glob patterns

- Observed in session s228 with `agents_bundle` 0.15.0: `include rules/**/AGENTS.md`, `include rules/*/AGENTS.md`, and `include rules/**/*.md` exit with rc=0 and emit no fragments and no warning, while `include rules/core/AGENTS.md` emits the file as expected.
- Context: `F32` needs every scoped category `AGENTS.md` preloaded, so `.agents_bundle` currently lists `rules/core/AGENTS.md` and `rules/role/AGENTS.md` explicitly; a new category `AGENTS.md` is silently missing from every session until someone adds a line by hand.
- Impact: context that the author believes is preloaded is absent without any signal, and the failure is invisible in the bundle output.
