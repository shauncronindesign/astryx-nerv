# ActivityTimer

The 活動限界まで (active time remaining) countdown: huge red 7-segment digits on a mauve-to-navy panel, with the INTERNAL / MAIN ENERGY SUPPLY SYSTEM / EXTERNAL tabs and the STOP · SLOW · NORMAL · RACING · DANGER EMERGENCY mode strip.

**Anatomy** (frames 25, 45, 115, M4)

| Part | Tokens |
|---|---|
| Panel | gradient `color-timer-start` → `color-timer-mid` → `timer-indigo` → `timer-navy`, clipped with `chamfer-lg` |
| Label | 活動限界まで / あと in `display` on a navy block; `ACTIVE TIME REMAINING:` in `sans` 700 |
| Digits | `M:SS:CC` drawn as SVG 7-segment polygons in `color-timer-digit`; unlit segments at 8% opacity; skewed −8°; heavy segments, matching InternalTimer |
| Tabs | 内部 INTERNAL (`timer-blue-light` fill, `alert-600` ink, red slash stripes) · 主電源供給システム (navy, outlined) · 外部 EXTERNAL (`timer-blue`, dimmed when not the active supply) |
| Modes | five cells; active cell inverts to `timer-blue-light`; DANGER EMERGENCY is `alert-600`, `alert-400` when active (under 1:00) |
| Ruler | fine white ticks along the top edge of the housing |

**Emergency state** (frame 45): under one minute the whole housing changes, not only the mode cell.
- The panel floods from bright red through `alert-600` to `alert-950`.
- The digits brighten to `#FF2A2A` on a dark window, so they stay readable on red.
- The tabs and mode strip turn red.
- The DANGER EMERGENCY cell blinks in two steps. The blink is off under `prefers-reduced-motion`.

The colour change snaps in three steps. Add `#left=<seconds>` to pin a time, or use `JUMP TO 1:05` in the preview to watch the change happen.

No segment font needed: the preview's `digit()` helper draws each digit from seven polygons. Swap in DSEG7 later if you prefer a font.

**Behaviour:** counts down in hundredths with `requestAnimationFrame`. Under `prefers-reduced-motion` the digits step by whole seconds only on user action. The container is `role="timer"` with a plain-language `aria-label` updated per second; the digits themselves are `aria-hidden`.

**Variants to add:** magenta (frame 115), unlit `88:88:88` standby.

**Consumer provides:** remaining milliseconds, which supply is active, and the mode.
