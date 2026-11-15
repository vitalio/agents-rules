# Description: Zero-dependency Python 3 CLI invariants ({py_min:3.9}+), ast.parse, and unittest suite
- Python CLI engineering invariants: Use only the Python 3 standard library
  (`from __future__ import annotations` at top of Python files for Python
  {py_min:3.9}+ compatibility). Verify Python syntax with `ast.parse` and
  cover every CLI flag and behavior with offline unit tests
  (`tests/test_*.py`).
- Concise `unittest` execution: Print a brief start indicator (such as
  `Running unit tests...`) and run `python3 -m unittest discover -s tests -q`
  (quiet verbosity `0`, without `-b`/`--buffer` so unexpected test stdout is
  never hidden); `unittest` emits a single concise summary when all tests pass
  and prints full failure details and tracebacks whenever any test fails.
- Unit test output and resource hygiene: In `tests/test_*.py`, capture
  expected CLI `stdout`/`stderr` (`contextlib.redirect_stdout`,
  `redirect_stderr`, or `subprocess.run(..., capture_output=True)`), manage
  files and subprocesses with `with` context managers to prevent
  `ResourceWarning`, and strip temporary debug `print()` calls before
  committing.
- Unit test failure diagnostics: Include diagnostic context (`msg=proc.stderr`
  or captured output) when asserting subprocess exit codes or side effects and
  use `with self.subTest(...):` for parameterized cases, without requiring
  redundant `msg=` on plain value assertions where `unittest` diffs already
  suffice.
- Unit test filesystem isolation: Isolate filesystem operations inside
  `tempfile.TemporaryDirectory` without mutating the repository working tree
  or user environment.
