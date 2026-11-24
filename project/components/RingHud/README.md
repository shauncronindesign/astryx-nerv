# RingHud

Two ring displays: the AAA Wunder's red ALERT belts, drawn in real perspective around a central shaft, and the blue external-power rings with R / L collectors.

**Wunder** (Wunder theme, frames 175–184), drawn on a canvas:
- **Belts:** three wide red bands. Each is a strip on a cylinder, tilted on its own axis and turning at its own speed.
  - The far half is drawn darker and behind the shaft. The near half is brighter, with a red glow, and is drawn in front of it.
  - Dark teeth run along the lower edge.
- **Lettering:** `ALERT` repeats around each belt, mapped onto the surface so it follows the curve and the perspective. It reads correctly on the near side and mirrored on the far side, where you see the belt from behind.
- **Shaft:** a jagged dark silhouette through the centre, which the belts pass behind and in front of.
- **Sensor net:** about 70 small red points in 3D, joined by faint violet lines where they are close.
- **Contacts:** four larger nodes with a white-hot centre, a red halo and a `mono` label (`CNT-01`). They pulse.
- **Status hexes:** small `tac-orange-400` outlined hexagons at the lower right (`ACTIV`, `ALERT`, `01`).

Add `#t=<seconds>` to pin a frame.

**External power** (frames 94–95):
- **Rings:** `sysblue-300` rings, the outer one dashed and turning.
- **Collectors:** two collector circles with `R` and `L` boxes in `mint-400`.
- **Status:** centred status text: `External Power Supply Mode / Verification Complete`.
- **Base:** a tick base line along the bottom.

**Motion:** the belts turn, the net drifts and the contacts pulse. Under `prefers-reduced-motion` the Wunder view draws one still frame and the blue ring stops turning. Each view is `role="img"` with its state in the label.

**Consumer provides:** the belt word, belt sizes and tilts, contacts and their positions, the status hexes, and the collector states.
