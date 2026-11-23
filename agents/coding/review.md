# Description: Software engineering Reviewer overlay (module layering, offline test isolation, and resource hygiene checks)
- Code & test audit: Verify that changes respect module layering and line-count
  cohesion, cover edge cases and error paths with offline unit tests named by
  domain behavior (no task-ID test names), clean up temporary files and
  subprocesses without resource leaks, and leave no dead code or stale symbol
  references across code, tests, CI workflows, or documentation.
