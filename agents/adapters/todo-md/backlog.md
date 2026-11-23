# Description: todo-md backlog governance for planning, design, review, and legislative sessions
- `todo` task prefix & status readiness contract (`NEW` vs `NEXT`): Classify
  backlog tasks by prefix (`F` for features, `B` for bugfixes, `D` for design
  explorations under `role=design`, and `L` for standalone rule,
  `.context.bundle`, or agent policy changes under `role=law` that do not
  modify product logic; keep routine `AGENTS.md` and embedded
  `agents/<tool>.md` sync inside the `F*`/`B*` implementation task). Never ask
  the user to choose between `NEW` and `NEXT`: `NEW` (default on `todo add`) is
  for unscoped ideas, draft items, or future milestone roots that still require
  planning (`role=plan`), whereas `NEXT` (`todo add --next`, `todo next <ID>`,
  or `todo edit <ID> --next`) is for fully scoped, user-agreed tasks with
  concrete acceptance criteria and dependencies ready for execution
  (`role=work`). When a planning, design, or review session finalizes and
  agrees on a task's scope, set or promote it directly to `NEXT` (or keep it
  `NEW` when recording an unscoped placeholder).
- Post-add ID wiring & dependency precedence: Create tasks via `todo add` first
  and wire `--depends` in both directions using the actual assigned IDs
  returned by `todo add` (using `todo add -q` when capturing the raw `<ID>`
  into a shell variable via `id=$(todo add -q ...)`, since default `todo add`
  prints `"todo: added <ID> ([<STATUS>]) to TODO.md"`, and never guessing
  future IDs beforehand). Because `,` binds tighter than `->`, never splice a
  sequential stage `A -> B` inside a comma list (`X, A -> B, Y` parses as
  `(X, A) -> (B, Y)`); separate sequential stages from parallel branches with
  `;` (`X, Y; A -> B`), and run `todo check` before committing backlog updates.
- Role-specific backlog closure: In `role=design` and `role=law`, close the
  active `D*` or `L*` task with `todo done <ID>` in the final guarded commit
  step together with the agreed documentation or rule changes. In `role=plan`
  and `role=review`, commit and push the updated `TODO.md` / `TODO_ARCHIVE.md`
  files once the user agrees on the task breakdown or remediation items.
