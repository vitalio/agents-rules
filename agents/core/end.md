# Description: End-of-session summary, final session-close block protocol, uncommitted work check, and documentation update
- Task & session completion summary: When completing a task or ending a
  session, wait until all commits, pushes, and final verification or status
  checks have completed cleanly in preceding steps (never ignore an error or
  traceback from any command inside a step, even if a later command in the same
  step exited with status 0). Then in the final reply: (1) give a concise,
  substantive summary in chat covering the key changes made (files, behavior,
  or rules updated), verification results, commit hash and release tag (if
  any), and any remaining work or newly recorded backlog items; (2) report any
  uncommitted or unpushed changes; (3) record durable architectural or
  operational decisions in project documentation; and (4) emit the
  session-closing command in a dedicated final block at the end of that summary
  reply (never combine session closure with commits, pushes, or verification
  commands in an earlier step).
