# Description: Python syntax verification via ast.parse and AST-based programmatic test file slicing
- Python syntax verification: Verify Python source and test files with
  `ast.parse` before running tests or committing.
- Programmatic AST slicing: When splitting an existing large Python module or
  test file across multiple files, slice functions or methods programmatically
  on disk using `ast.parse()` (`node.lineno`..`node.end_lineno`) rather than
  re-emitting large code bodies in chat output, and update CI workflows
  (`.github/workflows/`) in the same change.
