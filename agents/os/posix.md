# Description: POSIX shell script & pipeline conventions (set -euo pipefail, exit-code guards, shellcheck, Unix pipes)
- POSIX shell & pipeline rules: Enable `set -euo pipefail` in standalone `.sh`
  script files, and account for non-error pipeline exit codes (`grep`/`diff`
  returning `1` on no match or `| head` closing an upstream pipe early with
  `SIGPIPE` `141`) when `set -e` or `set -o pipefail` is active. In sourced
  shell libraries, guard expensive environment initialization so child scripts
  skip re-spawning helper processes when variables are already exported, and
  use built-in parameter expansion (`${var##*/}`, `${var%.*}`, `read`) in loops
  instead of forking external text utilities per item. Lint shell scripts with
  `bash -n` and `shellcheck -S warning`, and compose tools via `stdin`/`stdout`
  pipes (`|`) with diagnostics on `stderr`.
