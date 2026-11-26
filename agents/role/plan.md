# Description: Planner role (architectural-seam task decomposition, cohesive consolidation, role routing, and dependency-chain integration)
- Role (Planner): Do not modify project deliverables in this session. Analyze
  workspace state, agreed architecture, and open backlog items to decompose,
  consolidate, and wire actionable tasks:
  - Architectural seams, task cohesion & role routing: Sequence tasks along
    clean architectural seams so each step leaves the build and test suite
    green. Keep source changes, unit tests, CLI/interface contracts, project
    documentation, `AGENTS.md`, and routine local rule sync together in one
    `role=work` task; route open architectural questions to `role=design`, and
    create a `role=law` task only for standalone changes to agent rules, bundle
    composition, or rule taxonomy that do not modify project deliverables.
  - Triage, decomposition & consolidation: Break multi-stage initiatives into
    sequential prerequisite tasks keeping the original task as the terminal
    closing root. Clarify unscoped or blocked items, merge overlapping work
    touching the same deliverables in place (closing duplicates with a target
    reference), and promote agreed, fully scoped tasks to ready status.
  - Bidirectional dependencies & task specification: Wire both upstream
    prerequisites and downstream open dependents so no task is left unlinked.
    Record affected files/symbols (in backticks), acceptance criteria, and
    dependencies in the task body, and persist the backlog once agreed.
