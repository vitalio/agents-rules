# 🎯 [NEXT] L6: Refine adapters/todo-md and collab/multi-repo for post-add ID wiring and orchestrator boundaries

- In `agents/adapters/todo-md/backlog.md`, instruct agents never to run `todo ids` before `todo add` to guess future task IDs: create tasks via `todo add` first, then wire `--depends` between newly created tasks (or from an orchestrator parent task to `<project>:<ID>`) using the actual assigned IDs printed by `todo add`.
- In `agents/collab/multi-repo.md` (`vitalio/agents-rules:orchestrator`), codify cross-repository inspection and mutation boundaries: resolve managed project paths from workspace registry context (reading target files and each child project's `AGENTS.md` in a single batched step) and never mutate child repository source or documentation files directly from an orchestrator session (record tasks in the owning child repository's backlog instead).

# ⚪ [NEW] L5: Document operating roles and bundle parameters in README.md

- Add a concise reference of the 5 operating roles (`design`, `plan`, `work`, `review`, `law`) and key bundle configuration parameters (`os`, `vcs`, `py_min`, `single_file_build`) in `README.md` while preserving the dynamic discovery invariant (no static file inventories).
