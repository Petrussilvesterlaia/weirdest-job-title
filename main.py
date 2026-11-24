"""Weirdest Job Title entry for make.fun's Blind Judge Showdown.

Writes exactly one job title to /output/entry.txt and nothing else.
Deterministic: every run produces byte-identical output.
"""

import os

TITLE = "Professional Goose Apologizer"

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

MAX_LENGTH = 60


def validate(title: str) -> None:
    """Check the title meets the bounty gate: 1-60 chars, one line, not blank."""
    if not isinstance(title, str):
        raise ValueError("title must be a string")
    if not title.strip():
        raise ValueError("title must not be blank or only whitespace")
    if "\n" in title or "\r" in title:
        raise ValueError("title must be a single line")
    if len(title) < 1 or len(title) > MAX_LENGTH:
        raise ValueError(
            "title must be 1-60 characters, got %d" % len(title)
        )


def main() -> None:
    validate(TITLE)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(TITLE)
    # Read back and verify the file holds exactly the title.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != TITLE:
        raise ValueError(
            "verification failed: /output/entry.txt does not match the title"
        )
    print("Wrote %d characters to %s" % (len(TITLE), OUTPUT_PATH))


if __name__ == "__main__":
    main()
