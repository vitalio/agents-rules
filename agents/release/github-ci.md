# Description: GitHub Actions CI & tag-triggered GitHub Release workflow invariants (.github/workflows/ci.yml)
- CI verification gate (`.github/workflows/ci.yml`): Trigger on `push` to
  `main` and `v*` tags and `pull_request` to `main` on `ubuntu-latest` with
  `permissions: contents: write`. In the `test` job, run fast syntax/linter
  checks and the unit test suite, and on `refs/tags/v*` verify that the pushed
  tag matches `VERSION`
  (`GITHUB_REF_NAME == "v$(tr -d '[:space:]' < VERSION)"`).
- Tag-triggered GitHub Release job: Gate the `release` job on `needs: test` and
  `if: startsWith(github.ref, 'refs/tags/v')`, publishing the GitHub Release
  via `softprops/action-gh-release@v2` with `generate_release_notes: true` and
  attaching the project's distributable release artifacts.
