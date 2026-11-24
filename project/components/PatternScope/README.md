# PatternScope

The pattern-simulation screen from The spears, as seen on the handheld viewer. A rough, blocky pattern forms on the centre line, then splits into three lanes: the provisional pattern, an averaged ghost and a clean sample.

**The handset:** in the film this is a phone held upright and shot sideways, so its type reads bottom-to-top in a landscape frame. The component keeps that orientation, because that is how the screen is recognised. The same shell is used by StructuralDiagram.

**Anatomy:**
- **Lanes:** three dark rounded panels, one per MAGI, with an 8px gap between them.
- **MAGI labels:** `MAGI Achiral 3 / 2 / 1` with `Operational`, rotated and glowing, at the left of each lane.
- **Title:** rotated at the lower left, next to a 3px orange rule: `Pattern Simulation:` and the description.
- **Section columns:** thirteen columns, `SEC-ED`, `SEC-11 … SEC-01`, `SEC-ST`. Each has a stem crossing the centre line, a rotated label above and below, and rows of short dashes alternating dim orange and dim green.
- **Lane markers:** `| Provisional Pattern` and `Sample Pattern |`.
- **File tab:** a lime `Simulation File: Case …` tab on the top edge.
- **Caution marker:** a red line with end caps and `Caution: Data inconsistencies detected`.

**States:**
- **Forming** (`#stage=0`): one dense band of square blocks on the centre line, regenerated every 140ms so it shimmers. The caution marker is dimmed.
- **Resolved** (`#stage=1`):
  - Scattered block fragments in the top lane.
  - A blurred ghost band in the middle.
  - Below it, the sample: a thin spear outline with a twist at the grip and a forked tip.
  - The caution marker lights and blinks.

**Motion and accessibility:** the preview alternates between the two states. Under `prefers-reduced-motion` it shows the resolved state, still. The SVG's `aria-label` describes the current state and the caution.

**Consumer provides:** section labels, pattern data per lane (or a seed), the caution position and text, MAGI states, the file code and the title.
