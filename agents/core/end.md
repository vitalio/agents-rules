# Description: End-of-session summary, final session-close block protocol, unsaved work check, and documentation update
- Task & session completion summary: When completing a task or ending a
  session, wait until all changes, final verification checks, and version
  control publishing have completed cleanly in preceding steps (never ignore an
  error or traceback from any command inside a step, even if a later command in
  the same step exited with status 0). Then in the final reply: (1) give a
  concise, substantive summary in chat covering the key changes made,
  verification results, recorded revision or release version (if any), and any
  remaining work or newly recorded backlog items; (2) report any uncommitted or
  unpushed work-tree changes; (3) record durable architectural or operational
  decisions in project documentation; and (4) emit the session-closing command
  in a dedicated final block at the end of that summary reply (never combine
  session closure with verification or publishing commands in an earlier step).
