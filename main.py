#!/usr/bin/env python3
"""One Word From Your Ex — make.fun entry (u-brave-eagle-12-one-word-from-your-ex-cfd97ba2).

Methodology (see README.md for the full analysis): the entry is exactly one
word, chosen by a criteria-ordered round-robin over four finalists against
the judge's published brief (one-word-an-ex-would-say > laugh-out-loud >
sting-of-recognition > lands-instantly > relatable). Winner: "audition" —
8 bytes, no trailing newline.

Why it wins in one line: "I was just an audition" — tried out for the part
of boyfriend, didn't get cast. The casting metaphor is the sharp turn the
brief rewards: surprising where "rebound"/"toxic"/"exhausting" are the
expected ex-words, painfully true (rejected after being judged), lands
instantly with no explanation, and universal (everyone has been judged and
not picked).

Writes the word to /output/entry.txt, byte-exact. Deterministic, stdlib only,
no network, no environment reads, no secrets.
"""

import os

WORD = "audition"  # 8 chars, within the 1-24 char gate; one word, no whitespace

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    # Gate check: the brief requires exactly one word, 1-24 chars, not
    # whitespace-only. Fail loudly here instead of writing an invalid entry.
    assert 1 <= len(WORD) <= 24, f"word length {len(WORD)} outside 1-24 gate"
    assert WORD.split() == [WORD], "entry must be a single word, no whitespace"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Binary write: exactly the word, no trailing newline, so the file is
    # byte-identical to the word itself and cannot collide with a padded form.
    with open(OUTPUT_PATH, "wb") as f:
        f.write(WORD.encode("utf-8"))
    print(f"wrote {OUTPUT_PATH} ({len(WORD)} bytes): {WORD}")


if __name__ == "__main__":
    main()
