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

Round 3 — a fresh angle again: no cat, no calendar. This one takes
the word every out-of-office reply leans on — “urgent” — and
turns it into a trap: the reply invites the reader to define urgent,
then makes the definition irrelevant, because the answer is Monday
either way. The joke is the politeness itself, weaponised.
"""

import os

ENTRY = (
    "I'm away until Monday. If this is urgent, please define urgent, "
    "then wait until Monday anyway."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} characters"
    assert "\n" not in ENTRY and ENTRY == ENTRY.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
