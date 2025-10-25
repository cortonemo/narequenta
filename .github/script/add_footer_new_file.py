#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import sys

FOOTER_TEXT = (
    "© 2025 Serelith Varn — Nárëquenta: Tales of the Waning.\n"
    "Licensed for non-commercial play and fan content under the Nárëquenta Limited Open License (v0.1). See LICENSE.md.\n"
)

def file_needs_footer(path: Path) -> bool:
    if not path.exists():
        print(f"Error: {path} does not exist.")
        return False

    if not path.is_file():
        print(f"Error: {path} is not a file.")
        return False

    if path.suffix.lower() != ".md":
        print(f"Skipped: {path} (not a Markdown file)")
        return False

    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        print(f"Warning: {path} has non-utf8 encoding, skipping.")
        return False

    return FOOTER_TEXT.strip() not in content

def append_footer(path: Path):
    print(f"Adding footer to: {path}")
    with path.open("a", encoding="utf-8") as f:
        f.write("\n\n" + FOOTER_TEXT)

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python add_footer_new_file.py path/to/file.md")
        sys.exit(1)

    target_path = Path(sys.argv[1])

    if file_needs_footer(target_path):
        append_footer(target_path)
    else:
        print("Footer already present or file skipped.")

if __name__ == "__main__":
    main()
