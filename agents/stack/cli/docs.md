# Description: Standalone CLI README.md layout (Quick Installation, scenario-grouped Quick Start, and structured Commands/Options/Environment reference tables)
- Standalone CLI `README.md` flow: Structure `README.md` for standalone CLI
  tools in progressive-disclosure order: title and one-line tagline, concise
  3-5 line overview (without dumping wire-protocol headers, parser edge cases,
  or environment variable tables into the intro), `Quick Installation`,
  scenario-grouped `Quick Start`, and detailed reference sections in the second
  half of the document.
- Scenario-grouped `Quick Start`: Organize `Quick Start` as a sequence of short,
  task-oriented blocks (2-4 commands per code block) preceded by a one-line
  scenario heading (from the simplest default invocation to common workflows)
  rather than a single monolithic dump of every CLI subcommand and flag.
- Structured CLI reference tables: Place exhaustive `Commands`, `Options`, and
  `Environment` (plus exit codes or I/O protocol specifications when relevant)
  reference tables after `Quick Start`, and keep every command signature, flag,
  default value, and environment variable in sync with `-h`/`--help` in the
  same commit.
