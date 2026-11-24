# Card

A plate for grouped data, and the base surface most readouts sit inside. It has a clipped corner, a bracket header and a big glowing value.

**When to use:** a readout group, a stat panel or a usage card. Cards in a set butt together with a `space-0-5` (2px) seam.

**Props** (Astryx contract)

| Prop | Type | Default | Notes |
|---|---|---|---|
| `variant` | `"default" \| "transparent" \| "muted" \| "alert" \| "system" \| "amber" \| "red" \| "green" \| "blue" \| "wille" \| "indigo" \| "ochre" \| "gray"` | `"default"` | |
| `elevation` | `"none" \| "low" \| "med" \| "high"` | `"none"` | raises the frame from `color-border` to `color-border-accent` |

**Shape:** the top-right corner is cut with `chamfer-md`. The frame is `--ink` (default `color-border`) and the inner fill is `--fill`, inset 1px.

**Anatomy:**
- **Header:** a 3px bar, the label at 12px 700 in `color-text-tertiary`, and segmented ticks on the right.
- **Value:** 40px 700 with `compress-mild`, tabular numerals and `shadow-bloom-strong`, in `color-text-primary`.
- **Unit line:** 11px, with a 2px rule on its left.
- **Optional rail:** 4px of `color-track` with a glowing `color-accent` fill.

**Variant → token mapping:**
- `default`: `color-background-card` fill.
- `alert`: `color-background-alert` fill, a `color-border-alert` frame, `color-error` header and value, and a red/black hazard strip along the bottom.
- `system`: `color-background-system` fill with the blue sky-grid lattice, `color-border-blue` frame, `color-info` header and a `color-text-cyan` value.
- Categorical variants: a `color-background-<hue>` fill with a `color-border-<hue>` frame.

**What the consumer provides:** the header label, the value, the unit line and an optional rail percentage.

## Report cards (frame 116)

The pale unit-status sheets from the command centre's status board, shown under the metric cards.

- **Board** (`.board`): a dark panel with all four corners cut, covered in a green triangular lattice.
- **Sheet** (`.rep`): a pale cream card, slightly see-through, with a gold-brown frame and a thin orange outline. Type is dark, the reverse of every other card in the system.
  - Two tiny outlined tabs sit at the top (`Situation Record B-01`, `Case A1701`).
  - `Eva Unit Status:` and the unit name follow at 26px.
  - Under them are the damage level, the pilot and `Health: Normal`.
  - The feedback rate sits bottom-right at 24px.
- **Wide sheet** (`.rep.wide`): a location card with only a centred title (`TOKYO III Districts`).
- **Live values:** the feedback rates waver slightly while the situation is live.
- **Situation ended** (`.board.ended`): a red 状況終了 stamp slams in across the board in two steps and the sheets dim. The stamp is `role="status"`.

The preview shows the stamp for three seconds in every twelve. Add `#ended` to pin it. Under `prefers-reduced-motion` the values hold still and the stamp stays off.
