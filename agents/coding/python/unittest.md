# Description: Python unittest mirrored tests/test_<module>.py layout, shared tests/helpers.py fixtures, in-process execution, fixture cloning, and subTest diagnostics
- Python `unittest` file naming, shared `tests/helpers.py` & runner invocation:
  Name module test files `tests/test_<module>.py` mirroring `src/<module>.py`,
  and place shared base `unittest.TestCase` classes, in-process CLI runners,
  and fixtures in `tests/helpers.py` (without a `test_` prefix so
  `unittest discover -s tests` loads the target script once and does not
  execute the base class standalone). Run
  `python3 -m unittest discover -s tests` directly (default verbosity `1`,
  without `-q`, `-v`, or `-b`/`--buffer` so unexpected test stdout is never
  hidden, and without wrapping in custom `verbosity=0` runners).
- In-process execution, fixture cloning, and resource hygiene: Invoke Python
  modules and CLI entrypoints in-process (capturing `stdout`/`stderr` via
  `contextlib.redirect_stdout` and `contextlib.redirect_stderr` and exit codes
  via `SystemExit`) rather than spawning `subprocess.run` per test or
  `subTest` iteration, reserving `subprocess.run(..., capture_output=True)`
  for non-Python executables or single process-boundary smoke checks. Build
  expensive directory fixtures once in `setUpClass()` (cleaned up via
  `cls.addClassCleanup`) and clone them into per-test directories with
  `shutil.copytree(..., symlinks=True)` (or lazily in helpers), and share a
  single `tempfile.TemporaryDirectory` across read-only `subTest` loops. Stub
  third-party modules via `unittest.mock.patch.dict` on `sys.modules`, and
  manage files and subprocesses with `with` context managers to prevent
  `ResourceWarning`.
- Failure diagnostics: Include diagnostic context (`msg=proc.stderr` or
  captured output) when asserting subprocess exit codes or side effects and use
  `with self.subTest(...):` for parameterized cases, without requiring
  redundant `msg=` on plain value assertions where `unittest` diffs already
  suffice.
