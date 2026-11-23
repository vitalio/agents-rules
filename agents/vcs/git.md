# Description: Git identity verification, upstream sync (git pull --ff-only), staging (git add -N), diff inspection, atomic release push, and destructive operation guards
- Git workflow & safety: After `git init` or before the first commit in a
  repository, verify that local `git config user.name` and
  `git config user.email` match the target repository owner. When an upstream
  remote is configured, sync the branch before starting work or modifying the
  task backlog (`git pull --ff-only`, or `git fetch` and `git status -sb` when
  local changes exist) and resolve any upstream divergence before making
  commits or bumping `VERSION`. Mark new files with `git add -N` before
  printing `git status --porcelain` and `git diff HEAD` in the diff-review
  step. Without explicit user approval each time: no `git push --force`, no
  `git reset --hard`, no deleting a branch or tag, no rewriting a pushed
  commit. Push commits at the end of a task/session (to
  `origin {main_branch:main}` unless on a feature branch, using
  `git push --atomic` when pushing a branch together with a release tag), and
  report unpushed commits or unmerged branches at session end.
