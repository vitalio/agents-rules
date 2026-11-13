#!/usr/bin/env python3
# agents_rules-repo: vitalio/agents_rules
"""Usage:
  {prog} <target> [-exclude ...] [key=val ...]   Render a preset or rule to stdout
    Targets:
      std:<preset|rule>            Built-in catalog (e.g. std:python-tool, std:vcs/git)
      <owner>/<repo>[@ref]:<item>  GitHub repository package (auto-cached in {cache_dir})
      ./<path> | ~/<path>          Local .preset or .md rule file on disk
  {prog} --list | -l [package]     List presets and atomic rules in std (or cached packages)
  {prog} --update-cache            Refresh cached remote rule packages in {cache_dir}
  {prog} --agents                  Print Markdown instructions for AI agents
  {prog} --update [--force]        Self-update {prog} from GitHub (vitalio/agents_rules)
  {prog} --check-update            Check if a newer version is available
  {prog} -V | --version            Print version and exit 0
  {prog} -h | --help               Print this usage and exit 0
"""
from __future__ import annotations

if __doc__ is None:
    raise SystemExit("missing usage documentation")

import ast
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.request
from pathlib import Path

VERSION = "0.1.0"
REPO_MARKER = "agents_rules-repo: vitalio/agents_rules"
DEFAULT_UPDATE_URL = "https://raw.githubusercontent.com/vitalio/agents_rules/main/agents_rules"
STD_REPO = "vitalio/agents_rules"
