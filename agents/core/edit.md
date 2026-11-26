# Description: Bounded edit stages, unique anchor verification, in-memory validation, ~80-column wrapping, doc sync, and same-step verification
- Edit, doc sync & pre-commit verification: Keep each edit step and any emitted
  patch or literal bounded in size so a single response never risks exceeding
  chat output limits; when a change spans many files or requires large edits,
  split the work into sequential stages. Keep project documentation,
  user-facing specifications, and local agent instructions in sync within the
  same change whenever modifying behavior, options, or rules. Never dedicate a
  standalone execution step solely to running checks after an edit: run project
  verification checks inside the same step immediately after any
  self-consistent edit, and when a large change is split across sequential
  steps solely to stay within output token limits, run fast validation checks
  in intermediate steps and run full project verification at the end of the
  final edit step together with the working status and full diff.
- Programmatic patching & prose wrapping: When editing files programmatically,
  verify that each search anchor occurs uniquely, prefer targeted in-memory
  replacements over rewriting entire files as a single literal, and validate
  all anchors and syntax in memory before writing any file to disk (so a failed
  check leaves the working tree untouched). Aim to wrap prose in text and
  Markdown files at roughly 80 characters per line for readability in terminal
  editors.
