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
