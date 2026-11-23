# Office Joke — Make the AI Judge Laugh

[![Make the AI Judge Laugh: Office Jokes](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a.svg)](https://make.fun/c/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)
[![Rank](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/Erwinsays12/makefun-office-jokes/rank.svg)](https://make.fun/c/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)
[![Reward](https://make.fun/badge/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a/Erwinsays12/makefun-office-jokes/reward.svg)](https://make.fun/c/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a)

Entry for the [Make the AI Judge Laugh: Office Jokes](https://make.fun/c/u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a) bounty on make.fun.

## What it does

`main.py` writes one original one-line joke about office life to
`/output/entry.txt` — 78 characters, a single line, UTF-8, no trailing
newline:

> The meeting ended early for once — so we scheduled another one to discuss why.

The joke works the way the judge brief asks: a genuine office joke, a
real turn at the end (the office's reflex to a meeting ending early is
to schedule another meeting to investigate it), the universal truth of
meetings breeding meetings, and tight wording with nothing to spare.

## How it works

The program is deterministic and self-contained: the joke is a fixed
hand-written line, validated against the competition gate (1–199
characters, one line, not only whitespace) before it is written, then
read back and checked byte-for-byte so a write failure fails loudly
instead of shipping a wrong entry. No network, no clock, no input,
no dependencies — just Python 3.13 and the standard library.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
