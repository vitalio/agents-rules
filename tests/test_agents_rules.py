#!/usr/bin/env python3
"""Tests for agents_rules."""
from __future__ import annotations

import importlib.machinery
import importlib.util
import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "agents_rules"
BUILD_PY = ROOT / "build.py"
INSTALL_SH = ROOT / "install.sh"


def load_module():
    loader = importlib.machinery.SourceFileLoader("agents_rules", str(SCRIPT))
    spec = importlib.util.spec_from_loader("agents_rules", loader)
    mod = importlib.util.module_from_spec(spec)
    loader.exec_module(mod)
    return mod


class TestAgentsRules(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="ar_test_"))
        os.environ["AGENTS_RULES_CACHE_DIR"] = str(self.tmp / "cache")
        self.mod = load_module()

    def tearDown(self):
        os.environ.pop("AGENTS_RULES_CACHE_DIR", None)
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_build_check_help_and_version(self):
        rb = subprocess.run(["python3", str(BUILD_PY), "--check"], capture_output=True, text=True, check=False)
        self.assertEqual(rb.returncode, 0, rb.stderr)
        rh = subprocess.run([str(SCRIPT), "-h"], capture_output=True, text=True, check=False)
        self.assertEqual(rh.returncode, 0)
        self.assertIn("Usage:", rh.stdout)
        rv = subprocess.run([str(SCRIPT), "--version"], capture_output=True, text=True, check=False)
        self.assertEqual(rv.returncode, 0)
        ver = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
        self.assertEqual(rv.stdout.strip(), f"agents_rules {ver}")

    def test_mandatory_prefix_enforced(self):
        r = subprocess.run([str(SCRIPT), "python-tool"], capture_output=True, text=True, check=False)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("missing namespace prefix", r.stderr)

    def test_std_presets_exclusions_and_variables(self):
        out = self.mod.render_target("std:python-tool", excludes=["-core/external"], cli_vars={"lang": "Russian", "py_min": "3.12"})
        self.assertIn("Unix philosophy & composability:", out)
        self.assertIn("in **Russian**", out)
        self.assertIn("Python 3.12+ compatibility", out)
        self.assertNotIn("Clean external text & two-step external changes:", out)

    def test_local_file_and_remote_package_clone(self):
        # Local rule file
        local_md = self.tmp / "custom.md"
        local_md.write_text("# Description: Custom rule\n- **Custom:** Always greet {who:world}.\n", encoding="utf-8")
        out_local = self.mod.render_target(str(local_md), cli_vars={"who": "Alice"})
        self.assertEqual(out_local.strip(), "- **Custom:** Always greet Alice.")

        # Remote git package (local bare/work repo cloned via file:// URL)
        pkg_repo = self.tmp / "ext_pkg"
        (pkg_repo / "presets").mkdir(parents=True)
        (pkg_repo / "rules/sec").mkdir(parents=True)
        (pkg_repo / "rules/sec/tokens.md").write_text("# Description: Token rule\n- **Tokens:** Rotate every {days:30} days.\n", encoding="utf-8")
        (pkg_repo / "presets/strict.preset").write_text("# Description: Strict preset\ninclude = sec/tokens\ndays = 7\n", encoding="utf-8")
        subprocess.run(["git", "-C", str(pkg_repo), "init", "-q"], check=True)
        subprocess.run(["git", "-C", str(pkg_repo), "config", "user.email", "t@example.com"], check=True)
        subprocess.run(["git", "-C", str(pkg_repo), "config", "user.name", "Test"], check=True)
        subprocess.run(["git", "-C", str(pkg_repo), "add", "."], check=True)
        subprocess.run(["git", "-C", str(pkg_repo), "commit", "-q", "-m", "init"], check=True)

        # Preset default days=7 overrides rule default days=30, and CLI days=1 overrides preset
        out_pkg = self.mod.render_target(f"{pkg_repo}:strict")
        self.assertIn("Rotate every 7 days.", out_pkg)
        out_cli = self.mod.render_target(f"{pkg_repo}:strict", cli_vars={"days": "1"})
        self.assertIn("Rotate every 1 days.", out_cli)

    def test_list_and_install_sh(self):
        rl = subprocess.run([str(SCRIPT), "--list"], capture_output=True, text=True, check=False)
        self.assertEqual(rl.returncode, 0)
        self.assertIn("std:python-tool", rl.stdout)
        self.assertIn("std:core/unix-philosophy", rl.stdout)

        bin_dir = self.tmp / "bin"
        bin_dir.mkdir()
        ri = subprocess.run(["sh", str(INSTALL_SH), "--dir", str(bin_dir), "--yes"], capture_output=True, text=True, check=False)
        self.assertEqual(ri.returncode, 0, ri.stderr)
        self.assertTrue((bin_dir / "agents_rules").is_file())


if __name__ == "__main__":
    unittest.main()
