# BracketCaption

Pipe-bracketed status lines — `| Status : Locking Down Interior Array |` — stacked in a corner over a schematic, video or graph. The most common text pattern in the Rebuild UI.

**Anatomy** (frames 9, 47, 133, 142, 205)

- `.line` — `sans` 700, 15px, `color-text-accent` with `shadow-bloom`. Pipes are drawn 1.5px bars, so they stay thin at any size.
- `.k` — the label half (`Status :`) in `color-text-secondary`.
- `.hd` — an uppercase heading line (`MONITORED OBJECT PATTERN ANALYSIS`) in `color-text-primary`.
- `.crit` — a line that has gone critical, in `color-error`.
- `.open` — left pipe only, for the AAAW status lists (`| DSS Choker Connectivity: ACTIVE`).
- Placement: top-left for the subject, bottom-right (right-aligned) for status. Never centred.

**Theme:** captions keep the Tactical orange voice even when the art under them is Pattern or Nominal. Set `data-theme="tactical"` on the caption block.

**Consumer provides:** the lines, in order. Keep each to one line; captions never wrap.

**The subject under the captions** (frames 9, 133): the preview's first stage now shows what the captions describe, so the lines have something to point at.
- **Plug:** a glass capsule lit through the full spectrum, magenta to blue, with a white glass highlight, pale end caps and a faint seat outline.
- **Ring gear:** green rings around the plug's middle in `mint-300` with a glow, and one dashed outer ring that turns.
- **Depth marker:** a white bar labelled `DEPTH` that slides along the plug.
- **Structure:** thin grey struts and two circles behind.

The `Status : Locking Down…` line blinks in two steps while the lock is in progress. All motion is off under `prefers-reduced-motion`. The drawing is `aria-hidden`; the captions carry the meaning.
