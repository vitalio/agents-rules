# Description: CLI tool hygiene (-h/--help layout, stdout vs stderr separation, and <=100 display-column width)
- CLI interface rules: Every CLI command and flag must be documented in
  `-h`/`--help`, which prints usage to `stdout` and exits `0` without side
  effects, and kept in sync with `README.md` in the same commit. Write primary
  results to `stdout` and errors/warnings to `stderr`.
- Structured `-h`/`--help` layout: Format help output with explicit `Usage:`,
  `Commands:` (when subcommands exist), and `Options:` sections rather than
  burying flags in prose or listing partial option sets. For every option and
  flag, show all short/long forms, argument placeholders, defaults, and any
  notable side effects (such as Git commits or network calls).
- Help column alignment and width: Align the description column within each
  section (`Commands:`, `Options:`) so every description starts at the same
  column, and start wrapped continuation lines at that same column. When usage
  or option templates contain a `{prog}` placeholder, measure the rendered
  program name length (not the placeholder length) when computing the column
  and the continuation indent. Keep every `--help` line at most 100 columns
  wide (wrapping prose paragraphs at roughly 80 columns); the 100-column limit
  applies to rendered display columns / Unicode characters (verified via
  display-width helpers or unit tests) rather than `awk 'length($0)'`, because
  `mawk` measures `length($0)` in UTF-8 bytes and reports false positives on
  multi-byte Unicode symbols.
