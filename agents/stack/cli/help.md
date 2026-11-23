# Description: CLI -h/--help hygiene (Usage/Commands/Options layout, unified cross-section column alignment, stdout vs stderr, and <=100 display columns)
- CLI interface & stream separation: Document every CLI command and flag in
  `-h`/`--help`, which prints usage to `stdout` and exits `0` without side
  effects, and keep it in sync with project documentation in the same commit.
  Write primary command output to `stdout` and diagnostics, warnings, or errors
  to `stderr`.
- Structured `-h`/`--help` sections: Format help output with explicit `Usage:`,
  `Commands:` (when subcommands exist), and `Options:` sections (plus optional
  reference sections such as `Environment:`) rather than burying flags in prose
  or listing partial option sets. For every option and flag, show all
  short/long forms, argument placeholders, defaults, and any notable side
  effects (such as Git commits or network calls).
- Unified cross-section column alignment and width: Align the description
  column at the same column across all tabular sections in `-h`/`--help`
  (`Usage:`, `Commands:`, `Options:`, `Environment:`) so the right-hand
  description column never jumps horizontally between sections, and start
  wrapped continuation lines at that same column. When usage or option
  templates contain a `{prog}` placeholder, measure the rendered program name
  length (not the placeholder length) when computing the shared column and
  continuation indent. Keep every `--help` line at most 100 display columns
  wide (wrapping prose at roughly 80 columns); measure rendered Unicode display
  columns in unit tests rather than `awk 'length($0)'`, because `mawk` counts
  UTF-8 bytes and reports false positives on multi-byte symbols.
