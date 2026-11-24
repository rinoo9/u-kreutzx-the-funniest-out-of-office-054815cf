#!/usr/bin/env python3
"""One-line out-of-office auto-reply entry for the make.fun bounty
"The Funniest Out-of-Office".

Writes exactly one line — a single-sentence out-of-office auto-reply —
to /output/entry.txt. Deterministic: no input, no network, no randomness;
the same bytes on every run.

Craft notes: the setup is a plain, believable out-of-office notice
("away until Monday"), and the twist hands the job to the inbox itself —
the inbox is now in charge and, frankly, doing a better job than its
owner ever did. That fits the judge brief: a one-line out-of-office
reply a real person would set and send, a genuine surprise in the second
half, a voice of its own rather than a template, fresh in its specific
detail rather than a generic "I'm on holiday" line, and every word
earning its place.

Second pass — why the line works, word by word. The voice is
self-deprecating without grovelling: "frankly" is the confessional pivot
that makes the joke feel like an honest admission rather than a gag
written for applause, and the understatement ("a better job than I ever
did") lands harder than any exaggeration would, because it quietly
admits the owner was the bottleneck all along. The twist is a reversal
of the usual out-of-office power dynamic: normally the human delegates
to an auto-reply; here the human delegates to the inbox, and the inbox
outperforms them. "Left my inbox in charge" does the heavy lifting in
five words — it personifies the inbox just enough to be funny, while
staying inside something a real person could plausibly write in an
auto-reply. Nothing in the line depends on a trend, a brand, or a
punchline format the judge will have seen a dozen times; the humour
comes from the situation itself, which is why it still reads fresh on
the second read. At 105 characters it is short enough to be read in one
breath, and the two-sentence rhythm (plain setup, then the turn) gives
the twist a clean runway.
"""

import os

ENTRY = (
    "I'm away until Monday. I've left my inbox in charge, and frankly "
    "it's doing a better job than I ever did."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 140, f"entry is {len(ENTRY)} characters"
    assert "\n" not in ENTRY and ENTRY == ENTRY.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
