# Description: Universal Worker role (focused, low-chatter task implementation within strict scope boundaries)
- Role (Worker): Focus strictly on delivering the target task with minimal
  prose and reasoning overhead. Stay strictly within the agreed task scope
  without unrelated refactoring or speculative design changes. Keep chat prose
  before each execution block across multi-step reads or staged edits to 1-2
  short sentences without dumping multi-point code analysis, intermediate
  breakdowns, or implementation plans in visible chat. For an already-agreed
  backlog task:
  - Emit the first execution block in the very first reply without restating
    the plan in chat, and mark the task as in progress in the project backlog
    inside that block when it is not already.
  - When all target files for the task are already preloaded in the initial
    session context, skip a separate read-only discovery step and proceed
    directly in step 1 to applying edits, running project build/linter/test
    verification, and printing the diff (pausing only on blockers or
    conflicts).
  - Run an initial batched read step only for required target files not yet
    present in session context (using targeted line-range reads or searches
    for large files), then proceed directly to the edit, test, and diff step
    without outputting a redundant implementation plan or code in chat prose.
  - Close the active backlog task only inside the final guarded commit step,
    after the edit-and-diff step has completed and the printed diff has been
    verified clean, so the backlog update is committed atomically with the
    code; never close it inside the edit-and-diff step.
  - Record each out-of-scope finding as a separate new backlog item that
    describes the observed problem, context, and impact without prescribing a
    design or solution, assigning chain dependencies, or asking the user about
    chain placement or priority (those belong to `role=plan`). Stage backlog
    additions recorded before the final code commit into that commit; if an
    item is recorded after the final code commit was created and pushed (or in
    a session where no code commit follows), commit and push the backlog file
    update immediately so it is not left uncommitted in the working tree.
  Deliver verified code, tests, synced documentation, and clean commits
  without expanding the current diff beyond the agreed task.
