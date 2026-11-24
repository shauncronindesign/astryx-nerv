# TitleCard

Full-frame typographic cards: the white-on-black **KEEP OUT** card, and the red perspective banner that announces a new unit.

**KEEP OUT** (frames 144–149, W6):
- **Title:** `sans` 700 at about 160px, squeezed with `compress-extreme` (0.55) and tight tracking, in pure white with a three-layer white glow.
- **Rule:** a 2px white rule at 86% width.
- **Subtitle:** two or three centred lines at 36px with `compress-standard`. Keep each line short: `TOKYO-III / NEAR THIRD IMPACT / GROUND ZERO`.

**Activation banner** (W17):
- **Plate:** an `alert-300` plate tilted in 3D (`rotateX(18deg) rotateZ(-8deg)`), with a faint grid and red glow, on an `alert-950` ground.
- **Type:** dark `alert-950` text at 76px with a 30px `- … -` subtitle.
- **Rails:** dashed red rails above and below, tilted to match the plate.

**Notices:** the KEEP OUT card keeps its heading and cuts between sets of lines, the way the film does:
- `TOKYO-III / NEAR THIRD IMPACT / GROUND ZERO`
- `EVA-01 RESTRICTED AREA / NO ENTRY BEYOND THIS POINT`
- `LILITH PRESERVATION SITE / ACCESS STRICTLY RESTRICTED`

A small `NOTICE n / 3` counter sits at the bottom-left. Add `#n=<number>` to pin one.

**Motion:** changes are hard cuts. The lines drop out for a few frames, swap, and flick once more. The heading's glow slowly swells and settles. The resting state is always fully visible, because nothing is hidden by an entry animation, and all motion is off under `prefers-reduced-motion`.

**Use:** scene breaks, restricted areas, story beats. One per screen; never as an inline heading.

**Consumer provides:** the title and subtitle lines. Use a `<section>` with an `aria-label` that reads the whole card as one sentence.
