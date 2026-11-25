# Description: Cross-repository discovery, task decomposition, ADR and mutation boundaries, and one-way dependency rules
- Two-phase child-repository discovery: When a target or child repository's
  file tree is not yet present in session context, never guess internal file or
  rule paths — inspect the child repository's file tree, `<repo_dir>/AGENTS.md`,
  and active backlog in the first batched discovery step before reading
  specific internal files in the follow-up step.
- Owning-repository backlog, ADR & mutation boundary: Never mutate child
  repository files directly from an orchestrator session — record tasks in the
  owning child repository's backlog instead. Keep detailed task specifications,
  acceptance criteria, and file-level context in the backlog of the repository
  that owns the target files, never in an unrelated or coordinating repository.
  Keep single-repository ADRs inside that owning child repository's `docs/adr/`
  so it remains self-contained, and place cross-repository ADRs covering
  inter-project protocols or orchestration standards in the coordinating
  orchestrator repository's `docs/adr/`.
- Orchestrator parent tracking & one-way dependency boundaries: When an
  initiative spans multiple repositories, record a parent task in the
  coordinating repository's backlog that links target child tasks and tracks
  overall integration and sequencing. Keep cross-repository dependency edges
  confined to the coordinating repository (standalone child repositories must
  remain self-contained without dependency references to sibling or parent
  repositories), and keep intra-project dependency chains inside the child
  repository's own backlog (referencing only the target child milestone in the
  orchestrator task rather than duplicating intra-project sequential edges
  inside cross-repository dependency lists).
- Cross-repository execution order: Complete and verify prerequisite child
  repository tasks before advancing or closing dependent downstream tasks or
  the coordinating parent task.
