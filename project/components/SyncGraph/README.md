# SyncGraph

Two live graphs from the sync and A.T. field screens: the sync herringbone, and the realtime sensor feed drawn as a filled contour shape.

**Herringbone** (Nominal colours, frames 11, 46, W7):
- **Slats:** two groups. In each, pairs of slats lean in toward each other and stack into a column of chevrons.
  - A slat in sync is `mint-400` with a glow and a small `tac-orange-400` notch on its outer corner.
  - A slat still waiting is dark teal and carries a `SYNC` label along its length.
- **Fill direction:** slats light from the bottom up as the sync level rises. The second group lags the first slightly.
- **Wiring:** orange 1px lines run between the groups, with `mono` codes (`A0135`, `MT-01356`) on alternating rows. They feed two solid mint bars with footer codes.

**Sensor feed** (Pattern colours, frames 19–21):
- **Grid:** dull gold rules every ten units, a glowing white zero line, and bright white rules at the top and bottom limits.
- **Scale:** `+100 … ±00 … −100` in orange with tick marks, plus three `+` registration marks.
- **Contour shape:** nine nested contours rise from the left on a sigmoid, run flat, and drop back to the zero line through a rounded corner, which forms one plateau above the line and one below.
  - The outermost contour is filled with a horizontal gradient: `hazard-yellow` → `tac-orange-400` → `magenta-500` → `fuchsia-400` → `violet-300`.
  - The contours are white 1.1px lines.
  - The shape fades in from the left edge.
- **Label boxes:** two `REALTIME SENSOR DATA FEED` boxes with a dark backing, an orange frame, and Target Object and Energy origin lines.
- **Counters:** four signed eight-digit counters in small orange 7-segment digits, to the right of the scale.

**Motion:** the plateau heights and edges drift, the counters jitter, and the sync level rises and falls. Add `#t=<seconds>` to pin a frame. Under `prefers-reduced-motion` one still frame is drawn.

**Accessibility:** both SVGs are `role="img"`. The herringbone's label is rewritten with the sync rate.

**Consumer provides:** the sync level per group and the wiring codes; for the feed, the contour data (or plateau heights), label lines and counter values.
