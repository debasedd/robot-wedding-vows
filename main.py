#!/usr/bin/env python3
"""One-Line Robot Wedding Vows — writes one line to /output/entry.txt.

The line is one line of wedding vows for a robot couple, kept in the
shape of a real vow — sickness and health — but translated into machine
states, airplane mode and low-power mode, and closed with the turn:
"until a factory reset do us part." The joke lands in the last few words,
where the most permanent promise in the ceremony meets the one button
that erases everything.
"""

import os

LINE = "I promise to love you in sickness and in health, in airplane mode and in low-power mode, until a factory reset do us part."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
