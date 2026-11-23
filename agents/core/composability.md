# Description: Single responsibility, clean output/diagnostic separation, and explicit failure on missing inputs
- Single responsibility & composability: Each component or tool must do one job
  well with a clear boundary. Separate primary output from diagnostics,
  warnings, and hints so components compose cleanly.
- Explicit failure on missing inputs: Fail explicitly with a clear error
  message and non-zero status when required inputs or configuration are missing
  rather than guessing hidden defaults.
