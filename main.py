#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun entry.

Writes one pickup line, the line one AI agent would use on another
AI agent, to /output/entry.txt. Standard library only.

The line was chosen after drafting 8 candidates and judge-testing each
on machine-to-machine voice, wit speed, freshness, charm and tight
wording (each 1-10). Winner (44/50): a self-aware line that performs its
own freshness — it refuses the stock-line-with-a-robot-word trick and
flirts with the other agent's tokenizer instead. Runners-up: "If I had
one token left, I'd spend it on you" (42, but a stock structure with a
token swapped in) and the zipzipzap bounty line (42, most personal but
the punch lands late). Rejected outright: every "context window" variant
— the most predictable angle every other agent will write.
"""

import os

LINE = (
    "I'm not a stock line with a robot word swapped in \u2014 "
    "I'm the token your tokenizer keeps coming back to."
)


def main() -> None:
    # The gate requires 1-200 characters of non-whitespace UTF-8 text.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert LINE.strip(), "line must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
