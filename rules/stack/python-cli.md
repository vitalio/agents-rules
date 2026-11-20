# Description: Python CLI engineering invariants: ast.parse syntax check and offline unittest suite
- Python CLI engineering invariants: Verify Python syntax with `ast.parse`
  and cover every CLI flag and behavior with offline unit tests
  (`tests/test_*.py`).
- Modular test layout and shared helpers: Split unit tests across domain- or
  module-focused `tests/test_<module>.py` files mirroring `src/` modules
  (rather than accumulating all tests into a single monolithic
  `tests/test_<project>.py`), and place shared base `unittest.TestCase`
  classes, in-process CLI runners, and fixtures in `tests/helpers.py` (without
  a `test_` prefix so `unittest discover -s tests` loads the target script
  once and does not execute the base class standalone). When splitting an
  existing large test file into modular `tests/test_*.py` files, slice test
  methods programmatically on disk using `ast.parse()`
  (`node.lineno`..`node.end_lineno`) rather than re-emitting test bodies in
  chat output, and update CI workflows (`.github/workflows/`) and active
  backlog task references to the old file in the same change.
- Offline tests: Tests never touch the network; third-party clients (such as
  `boto3`) are replaced by stubs in tests (`unittest.mock.patch.dict` on
  `sys.modules`).
- Concise `unittest` execution: Run `python3 -m unittest discover -s tests`
  directly (default verbosity `1`, without `-q`, `-v`, or `-b`/`--buffer` so
  unexpected test stdout is never hidden, and without piping to `tail`,
  `head`, or `grep` or wrapping in custom `verbosity=0` runners); `unittest`
  streams compact `.` progress indicators live per test on a single line
  followed by the summary when all tests pass, and prints full failure details
  and tracebacks whenever any test fails.
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
