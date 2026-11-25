# Description: Single-file executable build from modular src/ via build.py injecting VERSION and local reinstall
- Single-file build from modular `src/`: Edit source modules and assets under
  `src/` rather than hand-editing the generated standalone executable. Keep
  `VERSION` as the single source of truth injected by `build.py` at build time
  rather than hardcoding version strings in source modules. Whenever `src/`,
  `VERSION`, or `install.sh` is modified, run `python3 build.py` to regenerate
  the standalone executable, verify `python3 build.py --check`, and reinstall
  locally via `sh install.sh --yes >/dev/null` before committing.
