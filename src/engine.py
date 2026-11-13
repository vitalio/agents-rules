def prog_name() -> str:
    raw = Path(sys.argv[0]).name if sys.argv and sys.argv[0] else "agents_rules"
    for suf in (".py", ".cmd", ".bat", ".exe"):
        if raw.lower().endswith(suf) and len(raw) > len(suf):
            raw = raw[:-len(suf)]
            break
    return raw or "agents_rules"


def cache_dir_path() -> Path:
    env_c = os.environ.get("AGENTS_RULES_CACHE_DIR")
    if env_c:
        return Path(env_c).expanduser()
    xdg = os.environ.get("XDG_CACHE_HOME")
    base = Path(xdg).expanduser() if xdg else (Path.home() / ".cache")
    return base / "agents_rules"


def usage_text() -> str:
    return (__doc__ or "").format(prog=prog_name(), cache_dir=cache_dir_path())


def agents_markdown(prog: str | None = None) -> str:
    cmd = prog or prog_name()
    lines = [
        f"## Engineering rules (`{cmd}` v{VERSION})",
        "",
        f"- Render presets or individual rules via `{cmd} <namespace>:<item> [-exclude ...] [key=val ...]` (e.g. `{cmd} std:python-tool`, `{cmd} std:release/single-file-build`).",
        f"- Inspect available presets and rules via `{cmd} --list`.",
    ]
    return "\n".join(lines)


RULE_VAR_RE = re.compile(r"\{([A-Za-z_][A-Za-z0-9_]*):([^{}]*)\}")


def _render_rule_vars(text: str, vars_map: dict[str, str]) -> str:
    return RULE_VAR_RE.sub(lambda m: vars_map.get(m.group(1), m.group(2)), text)


def _detect_vcs_rule(work_dir: Path | None = None) -> str | None:
    wdir = (work_dir if work_dir is not None else Path.cwd()).resolve()
    cur = wdir
    while True:
        if (cur / ".git").exists():
            return "vcs/git"
        if (cur / "CVS").is_dir():
            return "vcs/cvs"
        if cur.parent == cur:
            break
        cur = cur.parent
    return None


def _parse_md_text(raw_text: str, fallback_desc: str) -> tuple[str, str]:
    lines = raw_text.splitlines()
    desc = fallback_desc
    body_lines = lines
    if lines and lines[0].startswith("# Description:"):
        desc = lines[0].split(":", 1)[1].strip()
        body_lines = lines[1:]
    return desc, "\n".join(body_lines).strip()


def _parse_preset_text(raw_text: str, fallback_desc: str) -> tuple[str, list[str], dict[str, str]]:
    desc = fallback_desc
    includes: list[str] = []
    preset_vars: dict[str, str] = {}
    for raw_line in raw_text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith("# Description:"):
            desc = line.split(":", 1)[1].strip()
            continue
        if line.startswith("#") or line.startswith(";"):
            continue
        if "=" in line:
            k, v = line.split("=", 1)
            key = k.strip()
            val = v.strip()
            if key.lower() == "include":
                includes.extend(x.strip() for x in val.split(",") if x.strip())
            elif re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", key):
                preset_vars[key] = val
    return desc, includes, preset_vars


def _load_package_from_dir(pkg_dir: Path) -> tuple[dict[str, tuple[str, str]], dict[str, tuple[str, list[str], dict[str, str]]]]:
    rules: dict[str, tuple[str, str]] = {}
    presets: dict[str, tuple[str, list[str], dict[str, str]]] = {}
    r_root = pkg_dir / "rules" if (pkg_dir / "rules").is_dir() else (pkg_dir / "src/rules")
    p_root = pkg_dir / "presets" if (pkg_dir / "presets").is_dir() else (pkg_dir / "src/presets")
    if r_root.is_dir():
        for p in sorted(r_root.rglob("*.md")):
            if p.is_file():
                rel = p.relative_to(r_root).with_suffix("").as_posix().lower()
                rules[rel] = _parse_md_text(p.read_text(encoding="utf-8", errors="replace"), rel)
    if p_root.is_dir():
        for p in sorted(p_root.rglob("*.preset")):
            if p.is_file():
                rel = p.relative_to(p_root).with_suffix("").as_posix().lower()
                presets[rel] = _parse_preset_text(p.read_text(encoding="utf-8", errors="replace"), rel)
    return rules, presets


def _ensure_remote_package(pkg_spec: str, refresh: bool = False) -> Path:
    prog = prog_name()
    ref = ""
    repo_part = pkg_spec
    if "@" in pkg_spec:
        repo_part, ref = pkg_spec.rsplit("@", 1)
    if repo_part.startswith(("http://", "https://", "git@")):
        url = repo_part
        slug = re.sub(r"[^A-Za-z0-9._-]+", "_", repo_part.strip("/"))
    elif re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repo_part):
        url = f"https://github.com/{repo_part}.git"
        slug = repo_part
    else:
        raise SystemExit(f"{prog}: invalid package reference {pkg_spec!r}")

    cdir = cache_dir_path() / "packages" / (f"{slug}@{ref}" if ref else slug)
    if cdir.is_dir() and not refresh:
        return cdir
    cdir.parent.mkdir(parents=True, exist_ok=True)
    if cdir.is_dir() and refresh:
        shutil.rmtree(cdir, ignore_errors=True)
    cmd = ["git", "clone", "--depth", "1"]
    if ref:
        cmd.extend(["--branch", ref])
    cmd.extend([url, str(cdir)])
    r = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=False)
    if r.returncode != 0:
        raise SystemExit(f"{prog}: failed to fetch package {pkg_spec!r}: {r.stderr.strip()}")
    return cdir


def _get_package_catalog(pkg_id: str, refresh: bool = False) -> tuple[dict[str, tuple[str, str]], dict[str, tuple[str, list[str], dict[str, str]]]]:
    if pkg_id in ("std", STD_REPO):
        return dict(EMBEDDED_RULES), dict(EMBEDDED_PRESETS)
    local_dir = Path(pkg_id).expanduser()
    if local_dir.is_dir():
        return _load_package_from_dir(local_dir)
    pkg_dir = _ensure_remote_package(pkg_id, refresh=refresh)
    return _load_package_from_dir(pkg_dir)


def _parse_target_spec(spec: str) -> tuple[str, str]:
    prog = prog_name()
    if ":" not in spec and spec.startswith(("./", "../", "~/", "/")):
        return "__file__", spec
    if ":" not in spec:
        raise SystemExit(
            f"{prog}: missing namespace prefix in {spec!r} (expected e.g. 'std:{spec}', 'owner/repo:{spec}', or './path')"
        )
    if spec.startswith(("http://", "https://")):
        # Split on the last colon after the host/path
        idx = spec.rfind(":")
        if idx <= 8:
            raise SystemExit(f"{prog}: missing ':<item>' in URL target {spec!r}")
        return spec[:idx], spec[idx + 1:].strip().lower()
    pkg, item = spec.split(":", 1)
    if not pkg.strip() or not item.strip():
        raise SystemExit(f"{prog}: invalid target {spec!r}; expected <package>:<item>")
    return pkg.strip(), item.strip().lower()


def _match_rule_in_dict(name: str, rules_dict: dict[str, tuple[str, str]]) -> str | None:
    if name in rules_dict:
        return name
    matches = [k for k in rules_dict if k.rsplit("/", 1)[-1] == name]
    if len(matches) == 1:
        return matches[0]
    return None


def render_target(
    target_spec: str,
    excludes: list[str] | None = None,
    cli_vars: dict[str, str] | None = None,
    work_dir: Path | None = None,
    refresh: bool = False,
) -> str:
    prog = prog_name()
    pkg_id, item_name = _parse_target_spec(target_spec)
    excl_set: set[str] = set()
    for ex in excludes or []:
        clean_ex = ex.lstrip("-").strip().lower()
        if ":" in clean_ex:
            _, clean_ex = clean_ex.split(":", 1)
        if clean_ex:
            excl_set.add(clean_ex)

    user_vars = dict(cli_vars or {})

    if pkg_id == "__file__":
        fpath = Path(item_name).expanduser()
        if work_dir is not None and not fpath.is_absolute():
            fpath = (work_dir / fpath).resolve()
        if not fpath.is_file():
            raise SystemExit(f"{prog}: rule file not found: {item_name}")
        raw = fpath.read_text(encoding="utf-8", errors="replace")
        if fpath.suffix.lower() == ".preset":
            _, inc_list, p_vars = _parse_preset_text(raw, fpath.stem)
            merged_vars = {**p_vars, **user_vars}
            parts = [
                render_target(
                    sub if ":" in sub or sub.startswith(("./", "../", "~/")) else f"std:{sub}",
                    excludes=excludes,
                    cli_vars=merged_vars,
                    work_dir=work_dir,
                    refresh=refresh,
                )
                for sub in inc_list
            ]
            return "\n".join(p for p in parts if p.strip())
        _, body = _parse_md_text(raw, fpath.stem)
        return _render_rule_vars(body, user_vars)

    expanded: list[tuple[str, str]] = []
    preset_vars: dict[str, str] = {}

    def expand(cur_pkg: str, cur_item: str, stack: set[tuple[str, str]]) -> None:
        if cur_item in ("vcs/auto", "auto-vcs"):
            vcs = _detect_vcs_rule(work_dir)
            if vcs:
                expand(cur_pkg, vcs, stack)
            return
        rules_dict, presets_dict = _get_package_catalog(cur_pkg, refresh=refresh)
        if cur_item == "all":
            for rk in rules_dict:
                pair = (cur_pkg, rk)
                if pair not in expanded:
                    expanded.append(pair)
            return
        if cur_item in presets_dict:
            node = (cur_pkg, cur_item)
            if node in stack:
                return
            _, inc_items, p_vars = presets_dict[cur_item]
            for sub in inc_items:
                if ":" in sub or sub.startswith(("./", "../", "~/")):
                    sub_pkg, sub_item = _parse_target_spec(sub)
                else:
                    sub_pkg, sub_item = cur_pkg, sub.strip().lower()
                expand(sub_pkg, sub_item, stack | {node})
            # Outer preset overrides inner preset variable defaults
            preset_vars.update(p_vars)
            return
        rk = _match_rule_in_dict(cur_item, rules_dict)
        if rk is not None:
            pair = (cur_pkg, rk)
            if pair not in expanded:
                expanded.append(pair)
            return
        avail = sorted(set(presets_dict.keys()) | set(rules_dict.keys()) | {"vcs/auto", "all"})
        raise SystemExit(
            f"{prog}: unknown preset or rule {cur_item!r} in package {cur_pkg!r} (available: {', '.join(avail)})"
        )

    expand(pkg_id, item_name, set())

    def is_excluded(rk: str) -> bool:
        leaf = rk.rsplit("/", 1)[-1]
        return rk in excl_set or leaf in excl_set

    # Precedence: rule default < inner preset < outer preset < explicit CLI arg
    final_vars = {**preset_vars, **user_vars}
    out_blocks: list[str] = []
    for cur_pkg, rk in expanded:
        if is_excluded(rk):
            continue
        rules_dict, _ = _get_package_catalog(cur_pkg, refresh=False)
        body = _render_rule_vars(rules_dict[rk][1].strip(), final_vars)
        if body:
            out_blocks.append(body)
    return "\n".join(out_blocks)


def cmd_list(pkg_id: str = "std") -> int:
    rules_dict, presets_dict = _get_package_catalog(pkg_id)
    prefix = "std" if pkg_id in ("std", STD_REPO) else pkg_id
    sys.stdout.write(f"Presets in '{prefix}' (use as '{prefix}:<preset>'):\n")
    for k, (desc, items, p_vars) in presets_dict.items():
        target_tag = f"{prefix}:{k}"
        sys.stdout.write(f"  {target_tag:<26}  {desc}\n")
        vars_s = f"  [defaults: {', '.join(f'{ vk}={vv}' for vk, vv in p_vars.items())}]" if p_vars else ""
        sys.stdout.write(f"  {'':<26}    -> {', '.join(items)}{vars_s}\n")
    sys.stdout.write(f"\nAtomic rules in '{prefix}' (use as '{prefix}:<rule>' or exclude with '-<rule>'):\n")
    sys.stdout.write(f"  {prefix + ':vcs/auto':<26}  Auto-select vcs/git or vcs/cvs by repository directory\n")
    for k, (desc, _) in rules_dict.items():
        target_tag = f"{prefix}:{k}"
        sys.stdout.write(f"  {target_tag:<26}  {desc}\n")
    return 0


def cmd_update_cache() -> int:
    pdir = cache_dir_path() / "packages"
    if not pdir.is_dir():
        sys.stdout.write(f"No cached packages in {pdir}\n")
        return 0
    updated = 0
    for git_dir in sorted(pdir.rglob(".git")):
        repo_root = git_dir.parent
        r = subprocess.run(["git", "-C", str(repo_root), "pull", "--ff-only"], capture_output=True, text=True, check=False)
        if r.returncode == 0:
            updated += 1
            sys.stdout.write(f"Updated {repo_root.relative_to(pdir)}\n")
        else:
            sys.stderr.write(f"Failed to update {repo_root}: {r.stderr.strip()}\n")
    sys.stdout.write(f"Refreshed {updated} cached package(s).\n")
    return 0
