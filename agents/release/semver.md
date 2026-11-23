# Description: Semantic Versioning and release tagging rules (PATCH / MINOR / MAJOR) with VERSION as single source of truth
- Versioning & releases (SemVer):
  - `PATCH` (`X.Y.Z+1`) — bugfixes, UI/wording tweaks, rule refinements, and
    `--help`/docs updates.
  - `MINOR` (`X.Y+1.0`) — new CLI commands/flags, config options, or new
    rules/bundles.
  - `MAJOR` (`X+1.0.0`) — breaking changes or only when explicitly requested.
  - `PRE-RELEASE` (`X.Y.Z-alpha.N`, `X.Y.Z-beta.N`, `X.Y.Z-rc.N`, starting at
    `N=1`) — optional identifier for experimental or staged builds when
    explicitly requested; attach it to the upcoming target version `X.Y.Z` and
    strip it without re-bumping `X.Y.Z` upon final release.
  - Store the version number only in `VERSION` (the single source of truth;
    never hardcode or duplicate version strings in source modules, templates,
    docs, tasks, plans, or backlog items). In tasks, plans, and backlog items
    ahead of implementation, specify only the bump level (`PATCH`, `MINOR`,
    or `MAJOR`) rather than a concrete target version, and compute the next
    version dynamically from `VERSION` at release time.
  - Bump `VERSION` dynamically and stage any task-backlog updates inside the
    guarded commit step immediately before final build, tests, commit, and
    tag (this dynamic `VERSION` bump does not require an extra diff-review
    round-trip) so the annotated release tag points to `HEAD`:
    `ver=$(tr -d '[:space:]' < VERSION)`, `git tag -a "v$ver" -m "Release v$ver"`,
    and `git push --atomic origin {main_branch:main} "v$ver"`.
