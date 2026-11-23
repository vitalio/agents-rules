# Description: Cross-repository discovery, task decomposition, mutation boundaries, and one-way dependency rules
- Two-phase child-repository discovery: When a target or child repository's
  file tree is not yet present in session context, never guess internal module
  or rule file paths — inspect `context --tree <repo_dir>` and
  `<repo_dir>/AGENTS.md` (plus `todo projects` / `todo -p <project> show <ID>`)
  in the first batched discovery step before reading specific internal files in
  the follow-up step.
- Owning-repository backlog & mutation boundary: Never mutate child repository
  source or documentation files directly from an orchestrator session — record
  tasks in the owning child repository's backlog instead. Keep detailed
  implementation tasks, acceptance criteria, and code-level context in the
  backlog of the repository that owns the target files, never in an unrelated
  or coordinating repository.
- Orchestrator parent tracking & one-way dependency boundaries: When an
  initiative spans multiple repositories, record a parent task in the
  coordinating repository's backlog that links target child tasks and tracks
  overall integration and sequencing. Keep cross-repository dependency edges
  confined to the coordinating repository (standalone child repositories must
  remain self-contained without dependency references to sibling or parent
  repositories), and keep intra-project dependency chains inside the child
  repository's `TODO.md` (referencing only the target child milestone in the
  orchestrator task rather than duplicating intra-project `proj:A -> proj:B`
  edges inside comma-separated cross-repo dependency lists).
- Cross-repository execution order: Complete and verify prerequisite child
  repository tasks before advancing or closing dependent downstream tasks or
  the coordinating parent task.
