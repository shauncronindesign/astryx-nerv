# HexWall

The MAGI wall: a honeycomb of translucent red glass over a blue sky grid, with one title plate, two flanking alert cells and the three MAGI names. The wall changes state, as it does in the films. Use it for full-room alert states, not inline status.

**Theme:** always `data-theme="alert"` on the container. Red is the ground here, not a fill you add.

**Anatomy** (frames 31, 52, 165, W14):
- **Sky:** a diagonal white grid on `sysblue-500`, visible at both flanks, with a white haze at the corners.
- **Honeycomb:** flat-top hexagon cells in `alert-400` with `alert-200` outlines. Cells thin out toward the flanks so the sky shows through. Each cell's opacity drifts slightly, which makes the wall look like lit glass.
- **Title plate:** one wide hexagon in `alert-300` with a glowing white outline.
  - The Japanese title is set in `display` in dark `alert-950`, one or two lines.
  - The English line sits under it.
  - A boxed tag sits at each end (`警報` / `分析終了`).
- **Flank cells:** large `alert-500` hexagons with a white outline. Each holds ▲, `LEVEL n` and one word (`WARNING`, `ALERT`), which is white, condensed to 84% and bloomed.
- **Chips:** small chamfered plates in `alert-700` with white type (`MODE: Tactics`, `検証中`).
- **MAGI names:** `MAGI` at 15px over `Melchior 1` / `Balthasar 2` / `Casper 3` at 40px, under a 2px `alert-200` rail.
- **Cell vocabulary:** the row under the wall shows single cells: default, `dark` (EMERGENCY) and `hz` (hazard outline, DANGER).

**States:**
- **Battle stations** (`#state=0`): `第一種戦闘配置 / Battle Stations Condition One`, `WARNING · LEVEL 1`, `MODE: Tactics`.
- **Pattern analysis** (`#state=1`): `分析パターン：青 / 第6使徒と推測`, `ALERT · LEVEL 3`, tags read `分析終了`.
- **Change:** a white flash crosses the cells from left to right, then the text swaps.

The preview alternates every five seconds. Add `#state=<n>` to pin one.

**Motion and accessibility:** under `prefers-reduced-motion` the wall holds the first state with no flash. The SVG is `role="img"`, and its `aria-label` is rewritten to state the condition in words whenever the state changes.

**Consumer provides:** per state, the title lines, tags, flank word and level, and chips.

**Don't:** put body copy on the wall, or use it on a dark theme. A red wall is a state of the whole screen.
