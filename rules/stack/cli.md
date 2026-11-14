# Description: CLI tool hygiene (-h/--help exits 0 doing nothing, stdout vs stderr separation)
- CLI interface rules: Every CLI command/flag must be documented in
  `-h`/`--help`, which prints usage to `stdout` and exits `0` without side
  effects, and kept in sync with `README.md` in the same commit. Write primary
  results to `stdout` and errors/warnings to `stderr`.
