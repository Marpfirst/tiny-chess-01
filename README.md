# tiny-chess-01

A 4 KB chess engine for make.fun's tiny-chess-01 bounty.

`main.py` is the packed entrypoint (built with `makefun compress`
from `engine.py`, 2,834 bytes). It plays through the env at
`MAKEFUN_ENV_URL`: alpha-beta search with quiescence, a transposition
table and killer moves, to a fixed node budget per move — never a
clock, so every replay plays the same moves.

License: MIT.
