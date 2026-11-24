# BigReadout

One huge measured value with labelled chips under it. It's the `00.000 - %` sync test (frame 203). There's also a compact map version with a Japanese/English label box (frame 109).

**Large:**
- **Value:** `sans` 700 at 150px, squeezed with `compress-standard` (0.70) and set in tabular numerals, in `gold-300`. Every glyph is filled with horizontal scan lines, and each zero carries a slash, as on the film's display. The glow is gold with an orange outer halo.
- **Frame:** 9px red (`alert-300`) glowing bars on both sides; the unit (`- %`) is at 90px.
- **Corner tags:** small outlined tags at the top: `AUX Projector 01` on the left, `Linked` and `ONLINE` on the right.
- **Chips:** 1.5px `tac-orange-500` outline with gold text: Object, Test Subject, Harmonics. The vitals chip has a striped meter. A gold hazard-stripe bar runs under the chips.
- **Ground:** a green wash fading from the left, over a faint green hexagon mesh and scanlines, as in the frame.

**Compact:** an outlined label box (Japanese over English) above a 46px gold value with a smaller `%`.

**Behaviour:** the large value runs a "measuring" sweep: it eases from zero to the target with decreasing jitter, holds, then repeats. It's static under `prefers-reduced-motion`. Add `#zero` to pin the `00.000` standby frame. The live number is `aria-live="off"`; an `aria-label` with the settled value is set once it lands.

**Consumer provides:** the value, unit, chips and the target for the sweep.
