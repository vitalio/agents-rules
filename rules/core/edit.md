# Description: Unique anchor verification, atomic in-memory validation, plain-text agent rules, documentation sync, and pre-commit checks
- Edit & pre-commit verification: When editing files programmatically, verify
  that each search anchor occurs uniquely (`count == 1`), prefer targeted
  `text.replace(old, new, 1)` patches over rewriting entire files as a single
  literal, validate all search anchors and syntax in memory before writing any
  file to disk (so a failed check leaves the working tree untouched), and avoid
  raw multiline strings that could break chat Markdown fences. Aim to wrap
  prose in text and Markdown files at roughly 80 characters per line for
  readability in terminal editors. Keep project documentation (`README.md`,
  `AGENTS.md`), user-facing help, and agent instructions in sync within the
  same change when modifying behavior, options, or rules. In agent instructions
  (`AGENTS.md` and rule files), do not use decorative bold or italic Markdown
  emphasis — use plain bullet lists and single backticks (`` `...` ``) for
  literal commands, paths, and identifiers. Before committing, always run
  syntax/linter checks and the local unit test suite: print a brief
  start/progress indicator before running tests, emit a single concise summary
  line when all tests pass (avoiding verbose per-test output across large
  suites), and display full diagnostics and tracebacks only on test failure.
