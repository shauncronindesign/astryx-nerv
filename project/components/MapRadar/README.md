# MapRadar

The impact simulation map: a polar grid seen at a tilt, with the impact column rising from its centre, shock rings spreading across the ground, coloured damage zones and white tracks out to each unit.

**Theme:** Tactical, on a dark red radial ground (frames 113, 114, 140). The scene is drawn on a canvas, and the labels are HTML on top of it.

**Anatomy:**
- **Ground plane:** everything on the ground shares one tilt, so circles become ellipses.
- **Polar grid:** rings every 90 units and radials every 15°, in a glowing red-orange. Every third ring is brighter.
- **Damage zones:** flat-top hexagon cells on the plane, with pale outlines.
  - `gold-500` around the impact point.
  - `pink-300` to the north-east.
  - `magenta-500` to the east.
- **Impact column:** a translucent orange cone, wide at the top and narrowing to the impact point. It has a glowing orange rim near its mouth, and small bright motes fall through it.
- **Dish:** a pulsing cream ellipse at the impact point, inside one solid and one dashed white ring.
- **Shock rings:** three gold rings spread outward from the centre and fade.
- **Unit tracks:** white glowing polylines from the impact point to each unit, ending in a boxed tag (`EVA-00`, `EVA-01`, `EVA-02`).
- **Registration crosses:** a few small orange `+` marks.

**Labels (HTML):**
- **Object:** top-left, with a 3px left rule: `Object: 8th Angel / Impact Event Simulation`.
- **Countdown:** top-right in `mono`: `IMPACT T-00:42.0`, counting down.
- **Simulation box:** bottom-left, white outline, Japanese over English.
- **Caption:** bottom-right, orange outline: `第8使徒直撃による爆砕被害予測図 / Estimate of Blast Damage…`.

**Motion:** the shock rings, motes, dish pulse and countdown run live. Add `#t=<seconds>` to pin a frame. Under `prefers-reduced-motion` one still frame is drawn.

**Accessibility:** the canvas is `role="img"` with a label naming the object, the zones and the units.

**Consumer provides:** the impact point, the zone cells and colours, unit positions and names, the countdown, and the label text.
