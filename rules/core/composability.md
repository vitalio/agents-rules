# Description: Single responsibility, code structure discipline, clean output/diagnostic separation, and explicit failure on missing inputs
- Single responsibility & composability: Each module or tool must do one job
  well with a clear boundary. Separate primary output from diagnostics,
  warnings, and hints so components compose cleanly. Fail explicitly with a
  clear error message and non-zero status when required inputs or
  configuration are missing rather than guessing hidden defaults.
- Modular cohesion & layering: Keep each source module focused on a single
  responsibility at roughly 300-800 lines, and split any module that exceeds
  about 1000 lines or mixes architectural layers. Separate pure data/parsing
  and domain/graph algorithms from terminal rendering and CLI or I/O
  dispatch.
- Focused functions & canonical algorithms: Keep each function at a single
  level of abstraction, and implement each domain invariant with one
  canonical algorithm that every caller reuses rather than parallel
  implementations.
