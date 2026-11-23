# Description: Clean external communication (no session/step numbers, local workflow tools, or AI attribution) and two-step external writes
- Clean external text & two-step external changes: In commit messages, MR/PR
  descriptions, chat channels, and status updates, describe changes in words
  without session/step numbers or local agent workflow tools unrelated to the
  repository. Changes outside the repository (remote branches, MR/PR
  descriptions, shared messages) follow a two-step rule: first a read-only
  preview step saving what it replaces, then the write step after agreement.
- No AI attribution: Never add AI co-author trailers (such as
  `Co-Authored-By:`), agent attribution lines (such as `Generated with ...`),
  or tool signatures to commit messages, MR/PR descriptions, comments, or
  files.
