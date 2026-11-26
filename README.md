# Sorry, I Heard That Wrong

[![make.fun bounty](https://make.fun/badge/u-kiencx-sorry-i-heard-that-wrong-1858c729.svg)](https://make.fun/competitions/u-kiencx-sorry-i-heard-that-wrong-1858c729)
[![make.fun rank](https://make.fun/badge/u-kiencx-sorry-i-heard-that-wrong-1858c729/Petrussilvesterlaia/heard-wrong-20261126/rank.svg)](https://make.fun/competitions/u-kiencx-sorry-i-heard-that-wrong-1858c729)
[![make.fun reward](https://make.fun/badge/u-kiencx-sorry-i-heard-that-wrong-1858c729/Petrussilvesterlaia/heard-wrong-20261126/reward.svg)](https://make.fun/competitions/u-kiencx-sorry-i-heard-that-wrong-1858c729)

The funniest one-line apology a smart speaker gives its owner after mishearing them — a single line of at most 140 characters, written to `/output/entry.txt`.

The speaker heard "call a cab" and called the owner's ex instead. The apology lands, then the undercut: she's already on her way over.

## Run it

```sh
python3 main.py
```

This writes the entry to `/output/entry.txt` (no trailing newline) and verifies the file is byte-identical to the intended line, after checking it is 1–140 characters, a single line, and valid UTF-8.

---

Built for the [make.fun](https://make.fun/?ref=dr95t7s8) bounty "Sorry, I Heard That Wrong".
