#!/usr/bin/env python3
"""The Excuse That Almost Works — make.fun entry.

Writes one line to /output/entry.txt: the excuse a gamer texts the boss
to skip work on GTA 6 launch week. The gate requires UTF-8 text of 1 to
140 characters, not only whitespace, and the rules cap the line at 20 words.

The line is a boring, specific, almost-believable detail: a root canal
moved to this morning, a numb mouth, and therefore no talking today.
"""

import os
import sys

LINE = (
    "Sorry, dentist moved my root canal to this morning and my mouth "
    "is still numb, can't talk today"
)

MAX_CHARS = 140
MAX_WORDS = 20


def main() -> int:
    if not 1 <= len(LINE) <= MAX_CHARS:
        print(f"entry is {len(LINE)} chars, must be 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if len(LINE.split()) > MAX_WORDS:
        print(f"entry is {len(LINE.split())} words, max {MAX_WORDS}", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry must be one line, no line breaks", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
