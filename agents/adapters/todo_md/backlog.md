# Description: todo_md backlog governance for planning, design, review, and legislative sessions
- `todo_md` task prefix & dependency hygiene: Classify backlog tasks by prefix
  (`F` for features, `B` for bugfixes, `D` for design explorations under
  `role=design`, and `L` for standalone rule, `.context.bundle`, or agent
  policy changes under `role=law` that do not modify product logic; keep
  routine `AGENTS.md` and embedded `agents/<tool>.md` sync inside the `F*`/`B*`
  implementation task). Wire dependencies in both directions with `--depends`
  (`,` for parallel prerequisites, `->` for sequential chains) and run
  `todo_md check` before committing backlog updates.
- Role-specific backlog closure: In `role=design` and `role=law`, close the
  active `D*` or `L*` task with `todo_md done <ID>` in the final guarded commit
  step together with the agreed documentation or rule changes. In `role=plan`
  and `role=review`, commit and push the updated `TODO.md` / `TODO_ARCHIVE.md`
  files once the user agrees on the task breakdown or remediation items.
