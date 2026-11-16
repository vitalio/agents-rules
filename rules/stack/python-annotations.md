# Description: Require the future annotations import only where Python {py_min:3.9}+ needs it
- Postponed annotations: Add `from __future__ import annotations` only to
  files whose annotations use syntax newer than Python {py_min:3.9} (such as
  `X | None` below 3.10) or forward references; files without annotations do
  not need it.
- Single-file build: With `release/single-file-build`, the import stays once
  in the header of the assembled file (`src/header.py`) and covers all
  modules; modules under `src/` do not carry their own import.
- Runtime annotations: The import does not fix annotations evaluated at
  runtime (dataclasses, `typing.get_type_hints`); write those in syntax that
  Python {py_min:3.9} supports.
