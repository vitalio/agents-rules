# Description: todo_md lifecycle integration for role=work (WIP activation, atomic done on commit, and out-of-scope add)
- `todo_md` worker lifecycle: Start the active task with
  `todo_md status <ID> WIP` in the first execution step when it is not already
  `WIP`. Close the active task with `todo_md done <ID>` only inside the final
  guarded commit step so `TODO.md` and `TODO_ARCHIVE.md` are committed
  atomically with the implementation.
- Out-of-scope backlog items: Record out-of-scope findings via
  `todo_md add <PREFIX> "<title>" -b "<problem and impact>"` (using prefix `B`
  for bugs, `F` for features, `D` for architectural questions, and `L` for rule
  or bundle issues) without assigning chain dependencies or editing other active
  tasks in `TODO.md`.
