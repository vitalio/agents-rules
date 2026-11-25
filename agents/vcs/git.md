# Description: Git identity verification, upstream sync (git pull --ff-only), explicit-path staging, atomic release push, and destructive-op guards
- Git identity & upstream sync: After `git init` or before the first commit in
  a repository, verify that local `git config user.name` and
  `git config user.email` match the target repository owner. When an upstream
  remote is configured, sync the branch before starting work or modifying the
  task backlog (`git pull --ff-only`, or `git fetch` and `git status -sb` when
  local changes exist) and resolve any upstream divergence before committing.
- Explicit-path staging & diff inspection: Mark new files with `git add -N`
  before printing `git status --porcelain` and `git diff HEAD` in the
  diff-review step. Stage and commit only explicit target file paths
  (`git add <file>...` or `git commit <file>... -m ...`) — never run
  `git add -A`, `git add .`, `git add -u`, or `git commit -a`, so unrelated or
  concurrent work-tree changes are never swept into a commit by mistake.
- Destructive-operation guards & atomic push: Never run `git push --force`,
  `git reset --hard`, delete a branch or tag, or rewrite a pushed commit
  without explicit user approval each time. Push commits at the end of a task
  or session (to `origin main` unless on a feature branch; when tagging a
  release, create an annotated tag `git tag -a "v$ver" -m "Release v$ver"` and
  push branch and tag together via `git push --atomic origin main "v$ver"`).
