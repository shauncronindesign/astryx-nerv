# HazardBand

The hazard family: 45° chevron bands, the EMERGENCY strip between them, short angled status tags, and the authority bar with striped end caps.

**Tokens:** `color-hazard` / `color-hazard-alt` / `color-on-hazard`, `hazard-angle` (45°), `hazard-pitch` (24px, used by the small end caps and tags; the big bands use their own 68px pitch) and `slant-tag` (−30°).

**Parts:**

| Part | Frames | Notes |
|---|---|---|
| `.band` | 14, 59 | A 72px band of big chevrons. Two mirrored halves of 45° stripes (34px wide, 68px pitch) meet in the middle, so the stripes read as arrows pointing at the band's plate. `.rev` points them the other way for the lower band; `.red` swaps in `hazard-red`. The band blooms, and the stripes crawl toward the centre |
| `.strip` | 14–15 | Bands over and under a black strip with glowing 4px `alert-300` rules. A boxed 非常事態 plate sits in the middle of each band, breaking the stripes, as in frame 14. CONDITION:RED / **EMERGENCY** / CODE:102 fill the strip. The word flashes in steps |
| `.tag` | 213–215 | Hazard fill + striped tail + outlined detail, rotated by `slant-tag`. `.oor` (OUT OF RANGE) switches to red. Leave about 40px of space around tags; they rotate out of their box |
| `.auth` | 210 | 2px accent rules with striped caps, a gold title at `shadow-bloom-strong` and a small `mono` code line above |

**Motion:** the crawl and flash are both skipped under `prefers-reduced-motion`.

**Don't:** use hazard stripes as decoration. They mean "danger to people or the unit right now".
