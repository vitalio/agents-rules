# Description: Cross-repository task decomposition and one-way dependency boundaries
- Owning-repository backlog scope: Record detailed implementation tasks,
  acceptance criteria, and code-level context in the backlog of the repository
  that owns the target files, never in an unrelated or coordinating repository.
- Orchestrator parent tracking: When an initiative spans multiple
  repositories, record a parent task in the coordinating repository's backlog
  that links every child repository task as a dependency and tracks overall
  integration and sequencing.
- One-way dependency boundaries: Keep cross-repository dependency edges
  confined to the coordinating repository; standalone child repositories must
  remain self-contained without dependency references to sibling or parent
  repositories.
- Cross-repository execution order: Complete and verify prerequisite child
  repository tasks before advancing or closing dependent downstream tasks or
  the coordinating parent task.
