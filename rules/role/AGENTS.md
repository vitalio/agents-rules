# `rules/role/` — Universal Agent Operating Roles

Rules in `rules/role/` define session-level operating postures (`audit`, `plan`) activated via `role=<name>`:
- Never hardcode specific file names, programming languages, or external CLI tools inside a role.
- Let the role define the agent's objective and posture, delegating domain-specific artifact checks to the active rules and `AGENTS.md` files in the workspace.
