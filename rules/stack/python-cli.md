# Description: Python CLI engineering invariants: ast.parse syntax check and offline unittest suite
- Python CLI engineering invariants: Verify Python syntax with `ast.parse`
  and cover every CLI flag and behavior with offline unit tests
  (`tests/test_*.py`).
- Offline tests: Tests never touch the network; third-party clients (such as
  `boto3`) are replaced by stubs in tests (`unittest.mock.patch.dict` on
  `sys.modules`).
- Concise `unittest` execution: Run `python3 -m unittest discover -s tests`
  (default verbosity `1`, without `-q`, `-v`, or `-b`/`--buffer` so unexpected
  test stdout is never hidden); `unittest` emits compact `.` progress
  indicators per test on a single line followed by the summary when all tests
  pass, and prints full failure details and tracebacks whenever any test fails.
- Unit test output and resource hygiene: In `tests/test_*.py`, capture
  expected CLI `stdout`/`stderr` (`contextlib.redirect_stdout`,
  `redirect_stderr`, or `subprocess.run(..., capture_output=True)`); code
  under test that writes to `stderr` must be captured with
  `contextlib.redirect_stderr` so the progress line stays clean; manage
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
