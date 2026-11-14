# Description: Semantic Versioning and release tagging rules (PATCH / MINOR / MAJOR) with VERSION as single source of truth
- Versioning & releases (SemVer):
  - `PATCH` (`0.Y.Z+1`) — bugfixes, UI tweaks, and `--agents`/`--help`/docs updates.
  - `MINOR` (`0.Y+1.0`) — new CLI commands/flags or config options.
  - `MAJOR` (`X+1.0.0`) — breaking changes or only when explicitly requested.
  - Store the version number only in `VERSION` (the single source of truth; never hardcode or duplicate version strings in source modules, templates, or docs). Bump `VERSION` dynamically in the guarded commit step (immediately before final build, tests, commit, and tag) rather than during earlier edit steps, then push to `origin {main_branch:main}` with an annotated release tag (`ver=$(tr -d '[:space:]' < VERSION) && git tag -a "v$ver" -m "Release v$ver" && git push origin {main_branch:main} "v$ver"`).
