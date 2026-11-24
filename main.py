#!/usr/bin/env python3
"""One-line robot vacuum excuse entry for the make.fun bounty
"The Robot Vacuum's Best Excuse".

Writes exactly one line — the funniest excuse a robot vacuum gives for
missing a spot — to /output/entry.txt. Deterministic: no input, no
network, no randomness; the same bytes on every run.
"""

import os

EXCUSE = (
    "My map marked that dust bunny as a protected landmark, "
    "so I cleaned around it out of respect."
)


def main() -> None:
    assert 1 <= len(EXCUSE) <= 140, f"excuse is {len(EXCUSE)} characters"
    assert "\n" not in EXCUSE and EXCUSE == EXCUSE.strip()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
