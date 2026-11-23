# Description: Session start priority, instruction self-audit, and date formatting ({chat_date_fmt:DD/MM/YYYY})
- Start priority, instruction self-audit & dates: Uncommitted local work (other
  than changes limited to project task-backlog files) or an active
  build/pipeline takes precedence over unrelated tasks — ask what to do first.
  On session start, silently check all active rules, tool instructions,
  and `AGENTS.md` sections in context for contradictions or conflicts with
  current workspace state; if any conflict or ambiguity is found, warn the
  user immediately before proceeding. Format dates to the user in chat as
  `{chat_date_fmt:DD/MM/YYYY}`; in files, commits, headers, and logs always
  use UTC with ISO `YYYY-MM-DD` (or `YYYY-MM-DD HH:MM UTC` /
  `YYYY-MM-DDTHH:MM:SSZ` when time is included).
