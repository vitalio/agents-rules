# 🎯 [NEXT] L20: Add agents/cli/lifecycle.md standardizing --update [--check | --force], --uninstall [--purge], and install.sh

- Bump: `MINOR`
- Create `agents/cli/lifecycle.md` (`# Description: Standalone CLI self-update (--update [--check | --force]), uninstallation (--uninstall [--purge]), and install.sh lifecycle contract`) defining the ecosystem CLI lifecycle conventions:
  - Unified self-update command/flag (`--update [--check | --force]` or `update [--check | --force]`): fold update checking into `--check` and force-reinstall into `--force` without separate `--check-update` / `check-update` commands or `--self-update` aliases; verify the downloaded script's `# <repo>-repo: <owner>/<repo>` marker and syntax before atomically replacing the binary via a sibling temp file (`0755`, `os.replace`); support overriding the remote URL via `<TOOL>_UPDATE_URL`.
  - Safe uninstallation (`--uninstall [--purge]` or `uninstall [--purge]`): verify repository marker ownership before unlinking the installed binary (never deleting a source checkout or foreign binary); remove package caches or preserve user state by default and delete state directories only when `--purge` is passed.
  - Standalone `install.sh` contract: support `-h|--help`, `--name CMD`, `--dir DIR`, `-y|--yes`, and `--uninstall [--purge]`, detect command conflicts in `PATH`, and install from a sibling built executable or `<TOOL>_UPDATE_URL`.
- Wire `rule cli/lifecycle` into `agents/cli/cli.bundle` (controlled by `let lifecycle=1` under `if role=work,design,review`, keeping `agents/cli/help.md` strictly focused on `-h`/`--help` layout and alignment).
- Update `AGENTS.md` and `README.md` if needed and verify the CI catalog validation script in `.github/workflows/ci.yml` passes.

# 🎯 [NEXT] L21: Update adapters/todo-md for REVIEW status role mapping and todo --<cmd> CLI contract

- Depends on: L20
- Bump: `MINOR`
- In `agents/adapters/todo-md.bundle`, map `else if todo_md.status=REVIEW` to `let role=review` so `todo REVIEW -B | context | run` and `todo <ID> -B | context | run` on `🔎 [REVIEW]` tasks automatically activate `role=review`.
- In `agents/adapters/todo-md/work.md` and `agents/adapters/todo-md/backlog.md`, update all `todo` command references to the `--<cmd>` contract (`todo --status <ID> WIP`, `todo --done <ID>`, `todo --add <PREFIX> "<title>" ...`, `todo --edit <ID> ...`, `todo --promote <ID>`, `todo --check`) and document the `WIP -> REVIEW -> DONE` handoff (`role=work` runs `todo --done <ID>` to transition code tasks to `🔎 [REVIEW]`; `role=review` runs `todo --done <ID>` or `todo --done REVIEW` to archive verified tasks as `✅ [DONE]`, or `todo --promote <ID>` + `todo --append <ID>` when returning findings).
- Update `README.md` examples if needed and verify CI validation passes.
