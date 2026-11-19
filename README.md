# tiny-chess-01

A 4 KB chess engine for make.fun's tiny-chess-01 bounty.

`main.py` is the packed entrypoint (built with `makefun compress`
from `engine.py`, 4,003 bytes). It plays through the env at
`MAKEFUN_ENV_URL`: a fork of sunfish's 4K PST engine (Thomas Ahle
and contributors, GPL-3.0-only) with a make.fun env driver instead
of UCI and a fixed 60,000-node budget per move — never a clock, so
every replay plays the same moves.

License: GPL-3.0-only (SPDX tag in LICENSE).
