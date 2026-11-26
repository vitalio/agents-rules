# Description: todo-md backlog governance for planning, design, review, and legislative sessions
- `todo` role-prefix routing & status readiness (`NEW` vs `NEXT`): Map task
  prefixes to roles (`F` for features and `B` for bugfixes under `role=work`,
  `D` for design tasks under `role=design`, and `L` for standalone rule or
  bundle tasks under `role=law`). Never ask the user to choose between `NEW`
  and `NEXT`: keep unscoped ideas, drafts, or future milestone roots requiring
  `role=plan` as `NEW`, and set or promote fully scoped, user-agreed tasks with
  concrete acceptance criteria and wired dependencies directly to `NEXT`.
- Role-specific backlog closure: Run `todo check` before committing backlog
  updates. In `role=design` and `role=law`, close the active `D*` or `L*` task
  with `todo done <ID>` in the final guarded commit step together with the
  agreed documentation or rule changes. In `role=plan` and `role=review`,
  commit and push the updated `TODO.md` / `TODO_ARCHIVE.md` files once the user
  agrees on the task breakdown or remediation items.
