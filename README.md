# tiny4k

A chess engine entry for the make.fun competition **tiny-chess-01** ("Build the
strongest chess engine in 4 KB of Python").

- `main.py` (4,094 bytes) is the packed entrypoint: an lzma payload plus its
  unpacker, as the kit's `makefun compress` tool produces.
- The readable source it was packed from is kept beside this repository during
  development (`engine_src.py`, not committed; it does not fit the snapshot cap).

## What it is

The engine is a stripped, minified fork of the classic sunfish MTD-bi alphabeta
search with piece-square tables, running at a fixed 50,000-node budget per move,
wrapped in a driver for the competition's env HTTP protocol:

- parses the env's FEN into sunfish's 120-char mover-oriented board,
- replays only unseen moves from each `/game` poll (incremental state),
- handles white- and black-side orientation, promotion and castling rights,
- renders moves back to UCI and posts them to the env.

Credit: sunfish by Thomas Ahle and contributors (github.com/thomasahle/sunfish).
This fork changes the driver and protocol handling; the search core is sunfish's.

## Result on the practice gauntlet

6 games vs depth-2/3/4 and nodes-100k/250k/500k house bots:
**3 wins, 1 draw, 2 losses, Elo 1809** (local kit scorer on trial-0).

## License

GPL-3.0 (a sunfish derivative). See LICENSE and NOTICE.

## Credits

The search core is a fork of [sunfish](https://github.com/thomasahle/sunfish)
by Thomas Ahle (GPL-3.0). This entry therefore ships under GPL-3.0; see
NOTICE for attribution.
