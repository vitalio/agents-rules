# Description: macOS & BSD userland compatibility (BSD vs GNU flags and filesystem conventions)
- macOS & BSD userland rules: Account for macOS BSD userland differences in
  shell commands and scripts (avoid GNU-only flags such as `sed -i` without an
  extension argument, `readlink -f`, or `grep -P`).
