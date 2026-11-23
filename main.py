#!/usr/bin/env python3
"""Office-joke entry for make.fun.

Writes one original one-line joke about office life to /output/entry.txt.

The joke is a fixed, hand-written line: the program's job is to deliver
exactly that line, validated against the competition gate (UTF-8 text,
1 to 199 characters, a single non-blank line), deterministically, with
no network, no clock and no other input.
"""

from pathlib import Path

# The joke. One line, 78 characters: a meeting ends early (rare enough to
# be news) and the office's reflex is to schedule another meeting to
# investigate why -- the turn lands somewhere the reader did not see
# coming, and every tired office worker recognises the reflex.
JOKE = "The meeting ended early for once \u2014 so we scheduled another one to discuss why."

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 199


def validate(text: str) -> None:
    """Check the text against the competition gate before writing it."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"joke is {len(text)} characters, must be 1-{MAX_CHARS}")
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    if not text.strip():
        raise ValueError("joke must not be only whitespace")
    if text != text.strip():
        raise ValueError("joke must not start or end with whitespace")


def main() -> None:
    validate(JOKE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(JOKE, encoding="utf-8")
    # Read the file back and confirm the grader will see exactly the
    # validated text: a silent encoding or write failure must fail loudly
    # here instead of shipping a wrong entry.
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    if written != JOKE:
        raise ValueError("read-back mismatch: entry.txt does not hold the joke")
    print(f"wrote {len(JOKE)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
