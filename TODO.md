# 🎯 [NEXT] L20: Add agents/cli/lifecycle.md standardizing --update [--check | --force], --uninstall [--purge], and install.sh

- Bump: `MINOR`
- Create `agents/cli/lifecycle.md` (`# Description: Standalone CLI self-update (--update [--check | --force]), uninstallation (--uninstall [--purge]), and install.sh lifecycle contract`) defining the ecosystem CLI lifecycle conventions:
  - Unified self-update command/flag (`--update [--check | --force]` or `update [--check | --force]`): fold update checking into `--check` and force-reinstall into `--force` without separate `--check-update` / `check-update` commands or `--self-update` aliases; verify the downloaded script's `# <repo>-repo: <owner>/<repo>` marker and syntax before atomically replacing the binary via a sibling temp file (`0755`, `os.replace`); support overriding the remote URL via `<TOOL>_UPDATE_URL`.
  - Safe uninstallation (`--uninstall [--purge]` or `uninstall [--purge]`): verify repository marker ownership before unlinking the installed binary (never deleting a source checkout or foreign binary); remove package caches or preserve user state by default and delete state directories only when `--purge` is passed.
  - Standalone `install.sh` contract: support `-h|--help`, `--name CMD`, `--dir DIR`, `-y|--yes`, and `--uninstall [--purge]`, detect command conflicts in `PATH`, and install from a sibling built executable or `<TOOL>_UPDATE_URL`.
- Wire `rule cli/lifecycle` into `agents/cli/cli.bundle` (controlled by `let lifecycle=1` under `if role=work,design,review`, keeping `agents/cli/help.md` strictly focused on `-h`/`--help` layout and alignment).
- Update `AGENTS.md` and `README.md` if needed and verify the CI catalog validation script in `.github/workflows/ci.yml` passes.
