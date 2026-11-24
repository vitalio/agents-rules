# 🎯 [NEXT] L9: Codify ADR ownership boundary between orchestrator and child repositories in agents/collab/multi-repo.md

- In `agents/collab/multi-repo.md` (under `Owning-repository backlog & mutation boundary` / `Orchestrator parent tracking & one-way dependency boundaries`), explicitly codify the two-tier `docs/adr/` ownership boundary alongside `TODO.md` ownership:
  - Repository-scoped ADRs (`<repo>/docs/adr/NNNN-<slug>.md`) covering a single repository's internal module architecture, data structures, CLI/TUI behavior, or state machines live inside that owning child repository's `docs/adr/` so the repository remains self-contained.
  - Cross-repository / ecosystem ADRs covering inter-project protocols, pipeline contracts, and orchestration standards live in the coordinating orchestrator repository's `docs/adr/`.
- Keep `agents/collab/multi-repo.md` starting with `# Description:`, free of decorative bold/italic markup, and wrapped at ~80 columns, and bump `VERSION` (`PATCH`).

# 🎯 [NEXT] L13: Stratify core.bundle into role-invariant and role-gated lifecycle blocks and place core first in .context.bundle

- Depends on: L9
- Bump: `PATCH`
- Reorder `agents/core.bundle` into two lifecycle-ordered blocks so all role-invariant axioms and host/VCS rules form a contiguous cacheable prefix before role-gated rules:
  - Block 1 (role-invariant session framing, investigation axioms, environment & closure): `core/isolation` -> `core/secrets` -> `core/lang` -> `core/start` -> `core/plan` -> `core/ssot` -> `core/composability` -> `if os=linux` (`os/linux`) / `if os=macos` (`os/macos`) -> `if vcs=git` (`vcs/git`) / `if vcs=cvs` (`vcs/cvs`) -> `collab/external` -> `core/end`.
  - Block 2 (role-gated posture, execution & documentation): `if role!=` (`rule role/{role:}` + `export role`) -> `if role=work,law` (`core/edit` -> `core/diff-review`) -> `if role=work,design,review,law` (`core/docs`).
- In `agents/adapters/todo-md.bundle`, include `rule vitalio/todo-md` unconditionally so the canonical `todo` CLI rule is always loaded in Layer 1 (even in standalone `context role=<role> | run` sessions without a `todo |` pipe, while deduplicating by `vitalio/todo-md:todo` when piped), and trim `agents/adapters/todo-md/backlog.md` to role-specific prefix routing (`F`/`B`/`D`/`L`), `NEW` vs `NEXT` readiness, and role-specific closure without duplicating `todo add -q` or `,`/`->`/`;` CLI syntax owned by `vitalio/todo-md`.
- After two-pass `export` resolution, `rule <owner>/<repo>` shorthand, and rule stratification land in `context-bundle`, remove the obsolete "place before core in .context.bundle" requirement from `agents/adapters/todo-md.bundle`, `agents/role/law.md`, and `AGENTS.md`, and place `bundle vitalio/agents-rules:core` first (before domain/stack bundles and `bundle vitalio/agents-rules:adapters/todo-md`) in `.context.bundle` and `README.md` examples.
