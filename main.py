#!/usr/bin/env python3
"""Sorry, I Heard That Wrong — make.fun entry.

Writes the funniest one-line apology a smart speaker gives its owner
after mishearing them, to /output/entry.txt.

Competition: u-kiencx-sorry-i-heard-that-wrong-1858c729
"""

ENTRY = "Sorry \u2014 I heard 'call a cab' and called your ex instead. She's already on her way over."

OUTPUT_PATH = "/output/entry.txt"


def validate_entry(text: str) -> None:
    """Gate: /output/entry.txt must be UTF-8 text of 1-140 characters,
    not only whitespace, on a single line."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not (1 <= len(text) <= 140):
        raise ValueError(f"entry must be 1-140 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    text.encode("utf-8")  # raises if not valid UTF-8


def main() -> None:
    validate_entry(ENTRY)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Read-back verification: file must be byte-identical to the entry.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    if raw != ENTRY.encode("utf-8"):
        raise ValueError("read-back mismatch: entry.txt differs from ENTRY")
    print(f"Wrote {len(ENTRY)} characters to {OUTPUT_PATH}")
    print(f"Entry: {ENTRY}")


if __name__ == "__main__":
    main()
