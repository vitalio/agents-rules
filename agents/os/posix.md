# Description: POSIX shell & pipeline conventions (fail-fast only on mutating/commit steps, shellcheck, Unix pipes)
- POSIX shell & pipeline rules: Enable `set -euo pipefail` in standalone `.sh`
  script files and in state-mutating/build/commit steps (so a failed check
  aborts before modifying further or committing), but do not enable `set -e` or
  `set -o pipefail` in read-only inspection/search steps (where `grep`/`diff`
  returning `1` on no match or `| head` closing a pipe early with `SIGPIPE`
  `141` would abort the remaining reads). Lint shell scripts with `bash -n` and
  `shellcheck -S warning`, and compose tools via `stdin`/`stdout` pipes (`|`)
  with diagnostics on `stderr`.
