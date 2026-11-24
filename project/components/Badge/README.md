# Badge

A small, fixed-height tag for a state or a category. It has a clipped corner and uppercase condensed text, and isn't clickable.

**When to use:** a compact state (`NOMINAL`, `WARNING`, `CRITICAL`, `PATTERN BLUE`) or a category tag.

**Props**

| Prop | Type | Default |
|---|---|---|
| `variant` | semantic `"neutral" \| "info" \| "success" \| "warning" \| "error"` (solid) or categorical `"amber" \| "red" \| "green" \| "blue" \| "wille" \| "indigo" \| "ochre" \| "gray" \| "magenta" \| "violet" \| "cyan" \| "mint" \| "gold"` | required |

**Look:**
- **Size and type:** 20px high, 9px side padding, `sans` 700 at 12px, uppercase.
- **Shape:** the top-right corner is cut at 5px.
- **Semantic badges:** a solid fill with its `on-*` ink, plus a small segmented tail. `success` and `error` glow in their own colour.
  - `success` → `color-success` / `color-on-success`
  - `warning` → `color-warning` / `color-on-warning`
  - `error` → `color-background-error-inverted` / `color-on-error`
  - `info` → `color-info-fill` / `color-on-info`
  - `neutral` → `color-background-gray` / `color-text-gray`
- **Categorical badges:** a `color-background-<hue>` tint inside a 1px `color-border-<hue>` frame. A 3px glowing leading bar and the text are both in `color-text-<hue>`.

**Companions shown in the preview:** the boxed `LIVE` tag and the black `ONLINE` chip from the live-feed screens.

**Rule:** a semantic badge says what state something is in; a categorical one says what kind of thing it is. Never use `red` to mean `error`. The spectrum hues (`magenta`, `violet`, `cyan`) are for pattern data only.

**What the consumer provides:** one or two words of label text.

## Badges taken from the films

A second row collects the small status marks the films use on their own, so they can be placed without building the full component around them.

- **Hex cell** (`.hexb`): a small red hexagon with ▲, a word and a level (`ALERT / LEVEL 3`). From HexWall. Give it `role="img"` and a label.
- **LIVE stack** (`.stack`): the boxed `LIVE`, the black `ONLINE` chip and a `mono` source code, stacked and right-aligned. From LiveFeed. `LIVE` now blinks in two steps.
- **File tab** (`.filetab`): the lime tab that marks simulation files (`Simulation File: Case FA0212`).
- **Zone chip** (`.zone`): letter-spaced `hardware` type on an eight-sided plate (`MST`, `GMT`). From ClockBoard.
- **Bracket title** (`.brk`): a name between drawn square brackets (`[ TEST PLUG 01 ]`).
- **Hazard tag** (`.tagb`): a tilted yellow tag with a striped end (`READY`).
- **MAGI state** (`.magi`): `MAGI / Achiral 2 / Operational`, stacked and glowing orange.
- **Label plate** (`.plateb`): the solid orange plate at badge size (`MATCHES`).

The blink is off under `prefers-reduced-motion`.
