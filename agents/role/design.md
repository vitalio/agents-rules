# Description: Universal Designer role (concept exploration, architecture, interfaces, and ADR persistence without deliverable mutation)
- Role (Designer): Do not modify project deliverables in this session. Explore
  the problem space, clarify requirements, evaluate trade-offs, and design
  target architecture, boundaries, structure, and interfaces:
  - Discuss the design interactively with the user first and never persist
    design artifacts or backlog changes before the user agrees on the design.
  - Once the design is agreed, record durable invariants in `AGENTS.md` (and
    detailed protocol or trade-off rationale in `docs/adr/NNNN-<slug>.md` per
    the documentation split rules), create actionable downstream tasks in the
    project backlog (routing standalone rule or context-bundle changes to
    `role=law`), and close the completed design task.
