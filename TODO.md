# 🎯 [NEXT] L9: Codify ADR ownership boundary between orchestrator and child repositories in agents/collab/multi-repo.md

- In `agents/collab/multi-repo.md` (under `Owning-repository backlog & mutation boundary` / `Orchestrator parent tracking & one-way dependency boundaries`), explicitly codify the two-tier `docs/adr/` ownership boundary alongside `TODO.md` ownership:
  - Repository-scoped ADRs (`<repo>/docs/adr/NNNN-<slug>.md`) covering a single repository's internal module architecture, data structures, CLI/TUI behavior, or state machines live inside that owning child repository's `docs/adr/` so the repository remains self-contained.
  - Cross-repository / ecosystem ADRs covering inter-project protocols, pipeline contracts, and orchestration standards live in the coordinating orchestrator repository's `docs/adr/`.
- Keep `agents/collab/multi-repo.md` starting with `# Description:`, free of decorative bold/italic markup, and wrapped at ~80 columns, and bump `VERSION` (`PATCH`).
