# Description: Modular code cohesion, pragmatic ~300-800 line guideline, layered architecture, and canonical algorithms
- Modular cohesion & layering: Keep each source module focused on a single
  responsibility at roughly 300-800 lines, and split a module that exceeds
  about 1000 lines when it mixes distinct responsibilities or architectural
  layers. Treat the ~300-800 / ~1000-line guideline as a pragmatic
  recommendation rather than a hard line-count cap: never artificially relocate
  cohesive helpers across modules just to keep `wc -l` under 1000. Separate
  pure data/parsing and domain/graph algorithms from terminal rendering and CLI
  or I/O dispatch.
- Focused functions & canonical algorithms: Keep each function at a single
  level of abstraction, and implement each domain invariant with one canonical
  algorithm that every caller reuses rather than parallel implementations.
