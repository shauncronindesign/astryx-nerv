# StatusList

A system-status readout: one row per subsystem, with a glowing diamond marker, a name and a compressed state value. The rows sit in a clipped panel under a pipe-bracketed title.

**When to use:** a live list of units, links or subsystems where the state is the point, e.g. `EVA-01 Interface · NOMINAL`, `A.T. Field Sync · WARNING`, `Pattern Blue · CONFIRMED`.

**Props**

| Prop | Type | Notes |
|---|---|---|
| `items` | `{label: string, value: string, state: "nominal" \| "caution" \| "critical" \| "offline"}[]` | |
| `isLive` | `boolean` | turns on the glow and the critical pulse |

**Rows:** a 2px left rule in the state colour (`--s`) and a tint that fades out to the right. The marker is an 8px diamond with a glow. Labels are 13px 700 in `color-text-secondary`; values are 15px 700 with `compress-mild`, glowing in `--s`.

**State → token mapping:**
- `nominal`: `color-success`.
- `caution`: `color-warning`.
- `critical`: `color-error`, with a stronger red tint and a marker that blinks in steps.
- `offline`: `color-text-disabled`, with a hollow marker and no glow.

**Panel:** clipped with `chamfer-md`, a `color-border` frame and a `color-background-card` fill. The title is pipe-bracketed in `color-text-accent`, with a small `mono` source tag on the right. The pulse stops under `prefers-reduced-motion`.

**What the consumer provides:** the items, a title, and whether the feed is live.

## Check-in

The list now refreshes the way a console does. On each cycle every row goes back to a hollow marker and `—`, then the rows report one at a time, about 380ms apart. The row being checked is highlighted in the accent colour and reads `CHECKING`.

- **Summary line:** under the rows, in `mono`. It counts rows as they report (`3 / 6 REPORTING`) and adds the critical count once all are in (`6 / 6 REPORTING · 1 CRITICAL`). It is `role="status"`.
- **Cycle code:** a `CHECK 0412` code at the right, which increments on every cycle.
- **Markup stays final:** each row's real state is in the HTML. The script only plays the check-in over it, so the list is correct with scripts off.

A cycle starts every seven seconds. Add `#boot=<n>` to pin the check-in after n rows. Under `prefers-reduced-motion` the list shows its final state.
