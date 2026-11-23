# Description: Python unittest mirrored tests/test_<module>.py layout, shared tests/helpers.py fixtures, output capture, and subTest diagnostics
- Mirrored `tests/test_<module>.py` layout, shared `tests/helpers.py` & runner
  invocation: Split unit tests across module-focused `tests/test_<module>.py`
  files mirroring `src/` modules, and place shared base `unittest.TestCase`
  classes, in-process CLI runners, and fixtures in `tests/helpers.py` (without
  a `test_` prefix so `unittest discover -s tests` loads the target script once
  and does not execute the base class standalone). Run
  `python3 -m unittest discover -s tests` directly (default verbosity `1`,
  without `-q`, `-v`, or `-b`/`--buffer` so unexpected test stdout is never
  hidden, and without wrapping in custom `verbosity=0` runners).
- Output capture, mocks, and resource hygiene: In `tests/test_*.py`, capture
  expected CLI `stdout`/`stderr` (`contextlib.redirect_stdout`,
  `redirect_stderr`, or `subprocess.run(..., capture_output=True)`); code under
  test that writes to `stderr` must be captured with
  `contextlib.redirect_stderr` so the dot-progress line stays clean. Stub
  third-party modules via `unittest.mock.patch.dict` on `sys.modules`, manage
  files and subprocesses with `with` context managers to prevent
  `ResourceWarning`, and isolate filesystem writes in
  `tempfile.TemporaryDirectory`.
- Failure diagnostics: Include diagnostic context (`msg=proc.stderr` or
  captured output) when asserting subprocess exit codes or side effects and use
  `with self.subTest(...):` for parameterized cases, without requiring
  redundant `msg=` on plain value assertions where `unittest` diffs already
  suffice.
