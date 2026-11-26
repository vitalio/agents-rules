# Description: Python unittest mirrored tests/test_<module>.py layout, shared tests/helpers.py fixtures, in-process execution, fixture cloning, and bounded diagnostics
- Python `unittest` layout & runner: Name test files `tests/test_<module>.py`
  mirroring `src/<module>.py`, place shared base `unittest.TestCase` classes,
  in-process CLI runners, and fixtures in `tests/helpers.py` (no `test_`
  prefix), and run `python3 -m unittest discover -s tests` at default verbosity
  `1` (without `-q`, `-v`, `-b`/`--buffer`, or custom `verbosity=0` wrappers).
- Python in-process capture, fixtures & resource hygiene: Capture in-process
  CLI `stdout`/`stderr` via `contextlib.redirect_stdout`/`redirect_stderr` and
  exit codes via `SystemExit` (reserving `subprocess.run(..., capture_output=True)`
  for non-Python binaries or single process-boundary smoke tests). Use
  `setUpClass()` with `cls.addClassCleanup` and
  `shutil.copytree(..., symlinks=True)` for cloned directory fixtures,
  `tempfile.TemporaryDirectory` for shared read-only `subTest` loops,
  `unittest.mock.patch.dict` on `sys.modules` for third-party stubs, and `with`
  context managers for files and subprocesses to prevent `ResourceWarning`.
- Subprocess, `subTest` & bounded `safe_repr` diagnostics: Override
  `unittest.case.safe_repr` in `tests/helpers.py` to default `short=True`
  (`lambda obj, short=True: unittest.util.safe_repr(obj, short=short)`) so
  failed `assertIn` and `assertNotIn` calls truncate large container
  representations instead of dumping entire files or buffers with
  `short=False`. When checking for a snippet inside a large source file or
  buffer, prefer `self.assertEqual(src.count(needle), 1)` or slice the target
  function or block rather than calling `assertIn(needle, full_text)`. Pass
  `msg=proc.stderr` (or captured output) on subprocess assertions and wrap
  parameterized checks in `with self.subTest(...):` (omitting redundant `msg=`
  on plain value assertions).
