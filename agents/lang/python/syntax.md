# Description: Python syntax verification via ast.parse and AST-based module slicing
- Python syntax verification & AST slicing: Verify modified Python source and
  test files with `ast.parse` before running tests or committing. When
  splitting a large Python module or test file across multiple files, slice
  functions or classes programmatically on disk via `ast.parse`
  (`node.lineno`..`node.end_lineno`) rather than re-emitting large code bodies
  in chat output.
