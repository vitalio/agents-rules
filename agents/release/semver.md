# Description: Semantic Versioning and release tagging rules (PATCH / MINOR / MAJOR) with VERSION as single source of truth
- Versioning & releases (SemVer):
  - `PATCH` (`X.Y.Z+1`) — bugfixes, wording or formatting tweaks, rule
    refinements, and documentation updates.
  - `MINOR` (`X.Y+1.0`) — backward-compatible new features, commands/options,
    or new rules/bundles.
  - `MAJOR` (`X+1.0.0`) — breaking changes or only when explicitly requested.
  - `PRE-RELEASE` (`X.Y.Z-alpha.N`, `X.Y.Z-beta.N`, `X.Y.Z-rc.N`, starting at
    `N=1`) — optional identifier for experimental or staged builds when
    explicitly requested; attach it to the upcoming target version `X.Y.Z` and
    strip it without re-bumping `X.Y.Z` upon final release.
  - Keep `VERSION` as the single source of truth for the version string. In
    tasks, plans, and backlog items ahead of execution, specify only the bump
    level (`PATCH`, `MINOR`, or `MAJOR`) rather than a concrete target version,
    and compute the next version dynamically from `VERSION` at release time.
  - Bump `VERSION` dynamically and stage any task-backlog updates inside the
    guarded commit step immediately before the final verification checks,
    commit, and `vX.Y.Z` release tag (this dynamic `VERSION` bump does not
    require an extra diff-review round-trip) so the release tag points to the
    release commit.
