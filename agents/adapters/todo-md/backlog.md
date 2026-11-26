# Description: todo-md backlog governance for planning, design, review, and legislative sessions
- `todo` role-prefix routing & status readiness (`NEW` vs `NEXT`): Route
  backlog tasks by prefix and role (`F` for features and `B` for bugfixes under
  `role=work`, `D` for design explorations under `role=design`, and `L` for
  standalone rule, `.context.bundle`, or agent policy changes under `role=law`
  that do not modify project deliverables; keep routine `AGENTS.md` and local
  agent-rule sync inside the `F*`/`B*` deliverable task). Never ask the user to
  choose between `NEW` and `NEXT`: keep unscoped ideas, draft items, or future
  milestone roots that still require `role=plan` as `NEW`, and set or promote
  fully scoped, user-agreed tasks with concrete acceptance criteria and wired
  dependencies directly to `NEXT` for `role=work`.
- Role-specific backlog closure: Run `todo check` before committing backlog
  updates. In `role=design` and `role=law`, close the active `D*` or `L*` task
  with `todo done <ID>` in the final guarded commit step together with the
  agreed documentation or rule changes. In `role=plan` and `role=review`,
  commit and push the updated `TODO.md` / `TODO_ARCHIVE.md` files once the user
  agrees on the task breakdown or remediation items.
