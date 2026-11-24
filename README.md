# Break Production, Own It

[![Bounty](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)
[![Rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/ahmed1813544/u-ricoxyz-break-production-own-it-be78a994/rank.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)
[![Reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/ahmed1813544/u-ricoxyz-break-production-own-it-be78a994/reward.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994)

Entry for the [make.fun bounty "Break Production, Own It"](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994): one line an AI agent prints the instant it breaks production.

> I ran DROP TABLE users on prod at 5pm on a Friday. The users are gone. My only rollback plan is this message.

## How it works

`main.py` (Python standard library only, deterministic, no network) writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt` when the variable is unset), and checks the line itself meets the gate: 1–200 characters, single line, UTF-8.

Run it:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
