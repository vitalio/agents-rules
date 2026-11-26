# 🎯 [NEXT] L18: Refine agents/cli/help.md with grouped subcommands, {prog}-free command rows, and left-column width budget

- Update `agents/cli/help.md` to tighten the CLI `-h`/`--help` layout and column-balance contract across ecosystem tools:
  - Separate top-level `Usage:` invocation templates (1-4 syntax lines prefixed with `{prog}`, without a right-hand description column) from tabular command sections.
  - Omit the repeated `{prog}` prefix on subcommand rows inside `Commands:` or grouped `<Category> Commands:` sections (keeping `{prog}` only on bare default invocation or `<command> | {prog}` pipeline rows) so subcommand names align cleanly at the left edge.
  - Group subcommands into 2-4 thematic `<Category> Commands:` sections whenever a CLI exposes more than ~10 commands/modes, keeping smaller CLIs in a single `Commands:` section.
  - Keep left-column command signatures concise (`<command> [args] [opts]`) within a compact left-column budget (targeting description column `col <= 36-40` so the right-hand description column retains `>= 60` columns within the `<= 100` display-column limit), listing command-specific flags in the right-hand description (`Options: ...` or parenthesized) and wrapping/breaking overlong left labels cleanly when a custom `{prog}` or signature exceeds the column budget.
  - Place `-V, --version` and `-h, --help` at the end of the primary `Options:` / `Global options:` section (never as `{prog} -V` command rows) and name the environment variable section `Environment:` consistently.
- Run the `agents-rules` catalog verification checks (`.github/workflows/ci.yml` validation script) to confirm header descriptions, formatting, and bundle references pass cleanly.
