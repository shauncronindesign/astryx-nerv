# ClockBoard

Operation clocks: each row pairs a Japanese label (with an English line under it) with an amber 7-segment readout. The rows are 到達予想時刻 Estimated Time Of Breach, 到達予想時間 Estimated Time Remaining and 日本標準時 Japan Standard Time.

**Theme:** Clock (frames 63, 64, 70).

**Anatomy:**
- **Board:** `color-background-body`, a 2px `color-border-accent` frame clipped with `chamfer-lg`, and an inner 1px `color-border` frame.
- **Label:** `display` 900, 40px, `color-text-accent` + `shadow-bloom`. The English line is 14px 700 in `color-text-secondary`.
- **Tag:** `About` / `Countdown` / `Live` above the readout, in 14px `color-text-accent`.
- **Readout:** `HH:MM:SS:FF` drawn as SVG 7-segment digits in `color-text-accent`. Unlit segments are at 7%, the digits are skewed −6°, and `-` renders as the middle segment only (used for unknown frames: `12:41:31:--`).

**Behaviour:** the Live row shows JST computed from the viewer's clock. Countdown rows tick in frames (60 per second). Under `prefers-reduced-motion` the readouts update once a second. Digits are `aria-hidden`; give the board a `role="group"` and update an accessible summary yourself if the values matter to the reader.

**Consumer provides:** the rows (label, English line, tag) and a target time or duration for each.

**Operation board** (frame 70): the larger layout above the three-row board.
- **Zone label:** a slanted outlined box with the Japanese name in `display` (`bloom-core`) over a small English line.
- **Giant readout:** `HH MM SS` in 124px `hardware` numerals, narrowed to 66%. The fill is horizontal scan lines in `bloom-cream` and amber, with a two-layer amber glow. Each pair is followed by a unit stack: `h / 時`, `m / 分`, `s / 秒`.
- **Frames:** each readout sits in a 2px `color-border-accent` frame with two cut corners and a `Live` / `Countdown` / `GMT` tag.
- **Zone chips:** `MST` and `GMT` in letter-spaced `hardware` type on an eight-sided plate.
- **T+ row:** `T+` and `HH:MM:SS` in 7-segment digits, then a dot and smaller hundredths.

The giant readout shows live JST, the T+ row counts up from page load, and the GMT row shows live UTC.
