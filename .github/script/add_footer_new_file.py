#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path

FOOTER_TEXT = (
    "© 2025 Serelith Varn — Nárëquenta: Tales of the Waning.\n"
    "Licensed for non-commercial play and fan content under the Nárëquenta Limited Open License (v0.1). See LICENSE.md.\n"
)

def file_needs_footer(path: Path) -> bool:
    if not path.is_file() or path.suffix.lower() != ".md":
        return False

    try:
        content = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        print(f"⚠️ Skipping non-UTF8 file: {path}")
        return False

    return FOOTER_TEXT.strip() not in content

def append_footer(path: Path):
    with path.open("a", encoding="utf-8") as f:
        f.write("\n\n" + FOOTER_TEXT)
    print(f"✅ Added footer → {path}")

def main():
    count_total = 0
    count_added = 0

    for path in Path(".").rglob("*.md"):
        # skip system and Git folders
        if any(p in path.parts for p in [".git", ".github", ".obsidian"]):
            continue

        count_total += 1
        if file_needs_footer(path):
            append_footer(path)
            count_added += 1

    print(f"\n📊 Processed {count_total} Markdown files.")
    print(f"🖋️  Added footer to {count_added} of them.")
    print("Done.")

if __name__ == "__main__":
    main()
