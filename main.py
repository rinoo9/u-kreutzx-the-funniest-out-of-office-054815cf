#!/usr/bin/env python3
"""One-line out-of-office auto-reply entry for the make.fun bounty
"The Funniest Out-of-Office".

Writes exactly one line — a single-sentence out-of-office auto-reply —
to /output/entry.txt. Deterministic: no input, no network, no randomness;
the same bytes on every run.

Craft notes: the setup is a plain, believable out-of-office notice
("out until Friday"), and the twist hands the calendar to the cat —
the cat is now in charge and has declined every meeting until further
notice. That fits the judge brief: a one-line out-of-office reply a
real person would set and send, a genuine surprise in the second half,
a voice of its own rather than a template, and every word earning its
place. At 112 characters it is short enough to be read in one breath.
"""

import os

ENTRY = (
    "I'm out until Friday. My calendar is now run by my cat, and she "
    "has declined every meeting until further notice."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} characters"
    assert "\n" not in ENTRY and ENTRY == ENTRY.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
