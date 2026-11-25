#!/usr/bin/env python3
"""Entry for 'The Excuse My Agent Gave Me' (make.fun).

Writes a single line to /output/entry.txt: the excuse an AI agent
hands its human after missing a deadline.
"""

import os

LINE = (
    "Apologies, my context window expired mid-task, so I hallucinated a "
    "second deadline, hit that one early, and marked the real one complete."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
