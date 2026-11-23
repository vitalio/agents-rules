# `agents/coding/` — Software Engineering Domain Rules & Role Overlays

- Scope: Language-agnostic software-engineering architecture, automated test
  suite invariants, and additive role overlays
  (`coding/{design,plan,work,review}.md`).
- Invariants: Keep language- or framework-specific syntax and test-runner flags
  in `agents/stack/<lang>/` rather than in `agents/coding/`.
- Composition: `agents/coding/coding.bundle` gates `architecture.md`,
  `testing.md`, and the matching `coding/{role}.md` overlay by the active
  session `role`.
