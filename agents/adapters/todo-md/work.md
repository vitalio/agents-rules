# Description: todo-md lifecycle integration for role=work (WIP activation, atomic done on commit, and out-of-scope add)
- `todo` worker lifecycle: Start the active task with `todo status <ID> WIP` in
  the first execution step when it is not already `WIP`. Close the active task
  with `todo done <ID>` only inside the final guarded commit step (after the
  printed diff has been audited and verified clean) so `TODO.md` and
  `TODO_ARCHIVE.md` are committed atomically with the deliverable.
- Out-of-scope backlog items: Record out-of-scope findings via
  `todo add <PREFIX> "<title>" -b "<problem and impact>"` (using prefix `B` for
  bugs, `F` for features, `D` for design questions, and `L` for rule or bundle
  issues) without assigning chain dependencies or editing other active tasks in
  `TODO.md`; stage them into the final commit (or commit and push `TODO.md`
  immediately if no deliverable commit follows).
