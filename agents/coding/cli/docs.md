# Description: Standalone CLI README.md layout (Quick Installation, scenario-grouped Quick Start, and structured Commands/Options/Environment reference tables)
- Standalone CLI `README.md` structure: Follow progressive disclosure from
  `core/docs` with four canonical sections after the title, one-line tagline,
  and concise 3-5 line overview: `Quick Installation`, scenario-grouped
  `Quick Start`, and exhaustive `Commands`, `Options`, and `Environment`
  reference tables in the second half of the document.
- Scenario-grouped `Quick Start`: Organize `Quick Start` as a sequence of
  short, task-oriented blocks (2-4 commands per code block) preceded by a
  one-line scenario heading (from the simplest default invocation to common
  workflows) rather than a single monolithic dump of every CLI subcommand and
  flag.
- CLI reference tables: Place `Commands`, `Options`, and `Environment` (plus
  exit codes or I/O protocol specifications when relevant) after `Quick Start`,
  covering every command signature, flag, default value, and environment
  variable exposed by `-h`/`--help`.
