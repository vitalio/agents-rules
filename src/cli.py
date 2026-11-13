def parse_version_from_source(source: str) -> str | None:
    m = re.search(r'^VERSION\s*=\s*["\x27]([^"\x27]+)["\x27]', source, flags=re.MULTILINE)
    return m.group(1) if m else None


def version_tuple(v: str) -> tuple[int, ...]:
    return tuple(int(p) for p in re.split(r"[^0-9]+", v) if p)


def fetch_remote_script(url: str | None = None) -> str:
    target_url = url or os.environ.get("AGENTS_RULES_UPDATE_URL") or DEFAULT_UPDATE_URL
    if target_url.startswith(("http://", "https://")) and "?" not in target_url:
        target_url = f"{target_url}?t={int(time.time())}"
    req = urllib.request.Request(
        target_url,
        headers={"User-Agent": f"agents_rules/{VERSION}", "Cache-Control": "no-cache"},
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        data = resp.read().decode("utf-8")
    if REPO_MARKER not in data:
        raise ValueError("downloaded file does not contain expected repository marker")
    ast.parse(data)
    return data


def cmd_check_update(url: str | None = None) -> int:
    prog = prog_name()
    try:
        remote_src = fetch_remote_script(url)
    except Exception as exc:
        sys.stderr.write(f"{prog}: failed to check for updates: {exc}\n")
        return 1
    remote_ver = parse_version_from_source(remote_src) or "unknown"
    if version_tuple(remote_ver) > version_tuple(VERSION):
        sys.stdout.write(f"{prog}: update available: {VERSION} -> {remote_ver} (run '{prog} --update')\n")
    else:
        sys.stdout.write(f"{prog} {VERSION} is up to date (remote: {remote_ver}).\n")
    return 0


def cmd_update(force: bool = False, url: str | None = None) -> int:
    prog = prog_name()
    dest = Path(__file__).resolve()
    try:
        remote_src = fetch_remote_script(url)
    except Exception as exc:
        sys.stderr.write(f"{prog}: update failed: {exc}\n")
        return 1
    remote_ver = parse_version_from_source(remote_src) or "unknown"
    if not force and version_tuple(remote_ver) <= version_tuple(VERSION):
        sys.stdout.write(f"{prog} {VERSION} is already up to date.\n")
        return 0
    try:
        tmp_fd, tmp_name = tempfile.mkstemp(prefix=f".{dest.name}.", dir=str(dest.parent))
        try:
            with os.fdopen(tmp_fd, "w", encoding="utf-8") as f:
                f.write(remote_src)
            os.chmod(tmp_name, 0o755)
            os.replace(tmp_name, dest)
        except Exception:
            if os.path.exists(tmp_name):
                os.unlink(tmp_name)
            raise
    except Exception as exc:
        sys.stderr.write(f"{prog}: could not write updated binary to {dest}: {exc}\n")
        return 1
    sys.stdout.write(f"{prog}: updated {VERSION} -> {remote_ver} ({dest})\n")
    return 0


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    prog = prog_name()
    if "-h" in args or "--help" in args:
        sys.stdout.write(usage_text())
        return 0
    if "-V" in args or "--version" in args:
        sys.stdout.write(f"{prog} {VERSION}\n")
        return 0
    if "--agents" in args:
        sys.stdout.write(agents_markdown(prog) + "\n")
        return 0
    if not args:
        sys.stderr.write(usage_text())
        return 2
    if args[0] in ("--list", "-l"):
        if len(args) > 2:
            raise SystemExit(f"{prog}: usage: {prog} --list [package]")
        return cmd_list(args[1] if len(args) == 2 else "std")
    if args[0] == "--update-cache":
        return cmd_update_cache()
    if args[0] == "--check-update":
        return cmd_check_update()
    if args[0] in ("--update", "--self-update"):
        return cmd_update(force="--force" in args[1:])

    refresh = False
    targets: list[str] = []
    excludes: list[str] = []
    cli_vars: dict[str, str] = {}
    for a in args:
        if a == "--refresh":
            refresh = True
        elif a.startswith("--"):
            raise SystemExit(f"{prog}: unknown option: {a}")
        elif "=" in a and not a.startswith("-"):
            k, v = a.split("=", 1)
            k_clean = k.strip()
            if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", k_clean):
                raise SystemExit(f"{prog}: invalid variable name {k_clean!r} in {a!r}")
            cli_vars[k_clean] = v.strip()
        elif a.startswith("-") and len(a) > 1:
            excludes.append(a[1:])
        else:
            targets.append(a)

    if len(targets) != 1:
        raise SystemExit(f"{prog}: expected exactly 1 <package>:<target> argument (got {len(targets)})")
    out = render_target(targets[0], excludes=excludes, cli_vars=cli_vars, refresh=refresh)
    if out:
        sys.stdout.write(out + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
