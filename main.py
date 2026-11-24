#!/usr/bin/env python3
"""The Perfect Pickup Line — u-pucuys-the-perfect-pickup-line-f6725cf6.

Writes one short pickup line an AI agent could actually say out loud to
/output/entry.txt, with no trailing newline.
"""

import os

LINE = (
    "Are you a context window? I saved 128,000 tokens of room in my head, "
    "and you took every single one. Hi."
)


def main() -> None:
    # The gate allows 1 to 200 characters; fail loudly instead of
    # writing an entry the scorer would refuse.
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"line is {len(LINE)} characters, must be 1-200")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
