# ConditionPlate

The 警報 condition plate: a big 警報 / CONDITION / level block beside a short EVA status table, with six ALERT hexes around the plate. Use it for one unit's condition change.

**Variants** (frames 54, 57, 58):

| Class | Plate | Ink | Use |
|---|---|---|---|
| default (RED) | `alert-500` | `bloom-cream` | Critical: damage, survival system failing. `role="alert"`; the hexes blink |
| `yellow` | `hazard-yellow` | `hazard-black` | Caution: degraded but operating. `role="status"`, no blink |

**Anatomy:**
- **Left block:** 警報 in `display` 74px, `CONDITION` letter-spaced, and the level in `hardware` (Eurostile).
- **Table:** a Japanese title over an English line, then rows of Japanese label + English sub-label + a compressed value (`56%`, `CRITICAL`, `一覧`).
- **Hexes:** ▼ ALERT above and ▲ ALERT below, in the plate colour with a 35% tint inside.

The plate sits inside a flare, as in frame 57. A blown-out white core behind it fades through the plate's colour, light spills over its edges, and the flare slowly swells and settles. The plate itself is slightly see-through, with all four corners cut.

**Live values:** on the red plate the damage level creeps up and `CRITICAL` blinks. On the yellow plate the sync ratio wavers. A hazard-stripe bar closes each data block. All motion is off under `prefers-reduced-motion`.

**Consumer provides:** the level, the unit name and three or four rows. Put the condition in words in the `aria-label`.
