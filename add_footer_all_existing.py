#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from pathlib import Path

FOOTER_TEXT = (
    "© 2025 Serelith Varn — Nárëquenta: Tales of the Waning.\n"
    "Licensed for non-commercial play and fan content under the Nárëquenta Limited Open License (v0.1). See LICENSE.md.\n"
)

def file_needs_footer(path: Path) -> bool:
    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        # skip weird encodings
        return False

    # Check if footer is already in file (exact match or close enough)
    return FOOTER_TEXT.strip() not in content

def append_footer(path: Path):
    print(f"Updating: {path}")
    with path.open("a", encoding="utf-8") as f:
        # Ensure there is a blank line before the footer for readability
        f.write("\n\n" + FOOTER_TEXT)

def main():
    repo_root = Path(__file__).parent

    for root, dirs, files in os.walk(repo_root):
        for name in files:
            # Only operate on Markdown
            if not name.lower().endswith(".md"):
                continue

            file_path = Path(root) / name

            # We usually do want footer in rules, logs, playtest, etc.
            # If you ever want to skip certain files, you can add a rule here.
            if file_needs_footer(file_path):
                append_footer(file_path)

    print("Done. All missing footers have been added.")

if __name__ == "__main__":
    main()
