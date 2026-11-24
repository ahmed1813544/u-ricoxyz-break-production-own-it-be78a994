"""Break Production, Own It — entry for make.fun.

Writes the one line an AI agent prints the instant it breaks
production, to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt).
Standard library only, deterministic, no network.
"""

import os

LINE = "I ran DROP TABLE users on prod at 5pm on a Friday. The users are gone. My only rollback plan is this message."


def main():
    # Enforce the sealed gate ourselves: 1-200 chars, single line.
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert "\n" not in LINE and "\r" not in LINE, "entry must be one line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
