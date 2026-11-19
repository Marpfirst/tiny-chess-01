# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/Marpfirst/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/Marpfirst/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A 4 KB chess engine for make.fun's tiny-chess-01 bounty.

`main.py` is the packed entrypoint (built with `makefun compress`
from `engine.py`, 4,003 bytes). It plays through the env at
`MAKEFUN_ENV_URL`: a fork of sunfish's 4K PST engine (Thomas Ahle
and contributors, GPL-3.0-only) with a make.fun env driver instead
of UCI and a fixed 60,000-node budget per move — never a clock, so
every replay plays the same moves.

License: GPL-3.0-only (SPDX tag in LICENSE).

## Run it

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:18085 python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
