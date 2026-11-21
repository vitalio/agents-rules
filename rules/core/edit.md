# Description: Bounded edit stages, unique anchor verification, atomic validation, line wrapping, and pre-commit checks
- Edit & pre-commit verification: Keep each edit step and any emitted patch or
  literal bounded in size so a single response never risks exceeding chat
  output limits; when a change spans many files or requires large edits, split
  the work into sequential stages (such as module by module, or implementation
  followed by tests and documentation). Never dedicate a standalone execution
  step solely to running tests after an edit: run syntax checks and unit tests
  inside the same step immediately after any self-consistent edit, and when a
  large change is split across sequential steps solely to stay within output
  token limits (leaving code and tests temporarily out of sync, such as
  updating source modules in one step and test files in the next), run only
  syntax/build checks in intermediate steps and run the full test suite at the
  end of the final edit step together with the working status and full diff.
  When editing files programmatically, verify that each search anchor occurs
  uniquely (`count == 1`), prefer targeted `text.replace(old, new, 1)` patches
  over rewriting entire files as a single literal, validate all search anchors
  and syntax in memory before writing any file to disk (so a failed check
  leaves the working tree untouched), and avoid raw multiline strings that
  could break chat Markdown fences. Aim to wrap prose in text and Markdown
  files at roughly 80 characters per line for readability in terminal editors.
  Before committing, always run syntax/linter checks and the local unit test
  suite: emit compact live progress indicators (such as per-test `.` dots
  followed by the summary line) when all tests pass (avoiding verbose per-test
  names across large suites), display full diagnostics and tracebacks on test
  failure, and never pipe test runner output through `tail`, `head`, or `grep`
  or suppress it via redirection (which buffers live progress and truncates
  failure tracebacks).
