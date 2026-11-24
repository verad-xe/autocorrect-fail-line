#!/usr/bin/env python3
"""Funniest Autocorrect Fail — entry program.

Writes exactly one line, a funny autocorrect fail and nothing else,
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

The line is an anniversary text in which autocorrect splits the
compound word "butterflies" into "butter knives":

    Happy anniversary, honey! Six years of marriage and I still get
    butter knives every time you walk into the room

It reads as a real autocorrect slip — autocorrect famously breaks
compound words apart — the intended word is obvious from the romantic
context, and the wrong words are specific and surprising: instead of
butterflies in the stomach, the sender gets cutlery. The joke lands on
first read with no explanation.
"""

import os
import sys

LINE = (
    "Happy anniversary, honey! Six years of marriage and I still get "
    "butter knives every time you walk into the room"
)

# Gate limits from the bounty requirements (RULES.txt, "The gate"):
# entry.txt must be UTF-8 text of 1 to 199 characters, not only white space.
MIN_CHARS = 1
MAX_CHARS = 199


def main() -> int:
    line = LINE

    # Gate self-check: one line, inside the length limits.
    assert isinstance(line, str), "the entry line must be text"
    assert MIN_CHARS <= len(line) <= MAX_CHARS, (
        f"entry must be {MIN_CHARS} to {MAX_CHARS} characters, "
        f"got {len(line)}"
    )
    assert line.strip(), "entry must not be only white space"
    assert line == line.strip(), "entry must have no surrounding space"
    assert "\n" not in line and "\r" not in line, "entry must be one line"
    assert "\t" not in line, "entry must not contain a tab"
    assert "  " not in line, "entry must not contain a double space"
    # Plain ASCII, so the character count and the byte count agree and
    # the gate's 1-to-199-character rule cannot be tripped by encoding.
    assert line.isascii(), "entry must be plain ASCII"
    # The slip must be visible in the line: the wrong words are there.
    assert "butter knives" in line, "the autocorrect slip must be in the line"

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)

    # Verify what was written: read it back and re-check the gate.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == line, "entry.txt does not hold exactly the line"
    assert MIN_CHARS <= len(written) <= MAX_CHARS
    assert written.strip() and "\n" not in written
    return 0


if __name__ == "__main__":
    sys.exit(main())
