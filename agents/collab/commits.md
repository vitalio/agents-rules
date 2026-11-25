# Description: Opt-in commit message convention with imperative subjects, trailing task IDs, and no redundant release versions
- Commit subject line: Write a concise single-line summary in the imperative
  mood without a trailing period, describing what changed and why.
- Trailing task ID suffix: When a commit implements, plans, or closes one or
  more repository backlog tasks, append the task ID(s) in parentheses at the
  end of the subject line (`<Summary> (<ID>)` or `<Summary> (<ID1>, <ID2>)`);
  omit the suffix for commits not tied to a backlog task.
- No release version in commit subject: Do not include `Release vX.Y.Z:` or
  `(vX.Y.Z)` in the commit subject when the version is already recorded in
  `VERSION` and the annotated git tag `vX.Y.Z`.
- Optional commit body: Separate the body from the subject with a blank line,
  wrap at roughly 72-80 columns, and explain non-obvious context or rationale
  without restating the diff line by line.
