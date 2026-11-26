# Description: CLI -h/--help hygiene (Usage templates, grouped {prog}-free Commands, left-column width budget, and <=100 display columns)
- CLI `-h`/`--help` contract: Document every CLI command and flag in
  `-h`/`--help`, which prints usage to `stdout` and exits `0` without side
  effects.
- Structured `-h`/`--help` sections & grouped commands: Separate top-level
  `Usage:` invocation templates (1-4 syntax lines prefixed with `{prog}`,
  without a right-hand description column) from tabular command and option
  sections. Omit the repeated `{prog}` prefix on subcommand rows inside
  `Commands:` or grouped `<Category> Commands:` sections (keeping `{prog}` only
  on bare default invocation or `<command> | {prog}` pipeline rows) so
  subcommand names align cleanly at the left edge. Group subcommands into 2-4
  thematic `<Category> Commands:` sections whenever a CLI exposes more than ~10
  commands or modes, keeping smaller CLIs in a single `Commands:` section. In
  `Options:`, show all short/long forms, argument placeholders, defaults, and
  notable side effects (such as Git commits or network calls), place
  `-V, --version` and `-h, --help` at the end of the primary `Options:` /
  `Global options:` section (never as `{prog} -V` command rows), and name the
  environment variable section `Environment:` consistently.
- Left-column width budget & unified cross-section alignment: Keep left-column
  command signatures concise (`<command> [args] [opts]`) within a compact
  left-column budget (targeting description column `col <= 36-40` so the
  right-hand description column retains `>= 60` columns within the `<= 100`
  display-column limit), listing command-specific flags in the right-hand
  description (`Options: ...` or parenthesized) and wrapping or breaking
  overlong left labels cleanly when a custom `{prog}` or signature exceeds the
  column budget. Align the description column at the same column across all
  tabular sections (`Commands:` / `<Category> Commands:`, `Options:`,
  `Environment:`) so descriptions never jump horizontally between sections, and
  start wrapped continuation lines at that same column. When templates contain
  a `{prog}` placeholder, measure the rendered program name length (not the
  placeholder length) when computing column widths and continuation indents.
  Keep every `--help` line at most 100 display columns wide (wrapping prose at
  roughly 80 columns), and measure rendered Unicode display columns in unit
  tests rather than `awk 'length($0)'` (which counts UTF-8 bytes in `mawk`).
