# Description: Software engineering Planner overlay (module, test, CLI help, embedded rule, and documentation cohesion)
- Code, test, and doc task cohesion: Keep source module changes, corresponding
  `tests/test_<module>.py` unit tests, CLI `-h`/`--help`, `README.md`,
  `AGENTS.md` module notes, and any synced CLI embedded rule
  (`agents/<tool>.md`) together inside the same implementation task rather than
  splitting tests, docs, or embedded rule sync into separate follow-up tasks.
