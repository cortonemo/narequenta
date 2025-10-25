#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path

FOOTER_TEXT = (
    "© 2025 Serelith Varn — Nárëquenta: Tales of the Waning.\n"
    "Licensed for non-commercial play and fan content under the Nárëquenta Limited Open License (v0.1). See LICENSE.md.\n"
)

EXCLUDED_FILES = {"README.md", "LICENSE.md"}
EXCLUDED_DIRS = {".git", ".github", ".obsidian"}

def file_needs_footer(path: Path) -> bool:
    """Check if file should get a footer appended."""
    if not path.is_file() or path.suffix.lower() != ".md":
        return False

    if path.name in EXCLUDED_FILES:
        return False

    if any(part in EXCLUDED_DIRS for part in path.parts):
        return False

    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        print(f"⚠️  Skipping non-UTF8 file: {path}")
        return False

    return FOOTER_TEXT.strip() not in content

def append_footer(path: Path):
    """Append footer to the file."""
    with path.open("a", encoding="utf-8") as f:
        f.write("\n\n" + FOOTER_TEXT)
    print(f"✅ Added footer → {path}")

def main():
    count_total = 0
    count_added = 0

    for path in Path(".").rglob("*.md"):
        if file_needs_footer(path):
            append_footer(path)
            count_added += 1
        count_total += 1

    print(f"\n📊 Processed {count_total} Markdown files.")
    print(f"🖋️  Added footer to {count_added} of them.")
    print("✅ Done.")

if __name__ == "__main__":
    main()
