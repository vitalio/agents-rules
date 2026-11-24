# Description: Git identity verification, upstream sync (git pull --ff-only), staging (git add -N), diff inspection, atomic release push, and destructive operation guards
- Git workflow & safety: After `git init` or before the first commit in a
  repository, verify that local `git config user.name` and
  `git config user.email` match the target repository owner. When an upstream
  remote is configured, sync the branch before starting work or modifying the
  task backlog (`git pull --ff-only`, or `git fetch` and `git status -sb` when
  local changes exist) and resolve any upstream divergence before making
  commits or bumping `VERSION`. Mark new files with `git add -N` before
  printing `git status --porcelain` and `git diff HEAD` in the diff-review
  step. Stage and commit only explicit target file paths (`git add <file>...`
  or `git commit <file>... -m ...`) — never run `git add -A`, `git add .`,
  `git add -u`, or `git commit -a`, so unrelated or concurrent work-tree
  changes are never swept into a commit by mistake. Without explicit user
  approval each time: no `git push --force`, no
  `git reset --hard`, no deleting a branch or tag, no rewriting a pushed
  commit. Push commits at the end of a task/session (to `origin main` unless
  on a feature branch; when tagging a release, create an annotated tag
  `git tag -a "v$ver" -m "Release v$ver"` and push branch and tag together via
  `git push --atomic origin main "v$ver"`), and report unpushed commits or
  unmerged branches at session end.
