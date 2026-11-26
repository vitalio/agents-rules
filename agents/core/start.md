# Description: Session start priority for uncommitted work and silent instruction conflict self-audit
- Start priority & instruction self-audit: Uncommitted local work (other than
  changes limited to project task-backlog files) or an active build/pipeline
  takes precedence over unrelated tasks — ask what to do first. On session
  start, silently check all active rules, tool instructions, and `AGENTS.md`
  sections in context for contradictions or conflicts with current workspace
  state; if any conflict or ambiguity is found, warn the user immediately
  before proceeding.
