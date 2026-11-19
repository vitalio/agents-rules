# Description: Semantic Versioning and release tagging rules (PATCH / MINOR / MAJOR) with VERSION as single source of truth
- Versioning & releases (SemVer):
  - `PATCH` (`0.Y.Z+1`) — bugfixes, UI/wording tweaks, rule refinements, and
    `--help`/docs updates.
  - `MINOR` (`0.Y+1.0`) — new CLI commands/flags, config options, or new
    rules/rulesets/bundles.
  - `MAJOR` (`X+1.0.0`) — breaking changes or only when explicitly requested.
  - `PRE-RELEASE` (`X.Y.Z-alpha.N`, `X.Y.Z-beta.N`, `X.Y.Z-rc.N`, starting at
    `N=1`) — optional identifier for experimental or staged builds when
    explicitly requested; attach it to the upcoming target version `X.Y.Z` and
    strip it without re-bumping `X.Y.Z` upon final release.
  - Store the version number only in `VERSION` (the single source of truth;
    never hardcode or duplicate version strings in source modules, templates,
    or docs). Bump `VERSION` dynamically and stage any task-backlog updates in
    the guarded commit step immediately before final build, tests, commit, and
    tag so the annotated release tag points to `HEAD` (`ver=$(tr -d '[:space:]' < VERSION) && git tag -a "v$ver" -m "Release v$ver" && git push origin {main_branch:main} "v$ver"`).
