# Reticle

Targeting overlays: the ring-and-triangle lock with its pipe-bracketed Object tag, and the plug's bracket sight with a heading tape.

**Lock** (frame 127):
- **Ring:** a thin ring with eight ticks in `clock-amber`, glowing. It turns slowly.
- **Crosshair:** a dashed crosshair in `gold-300`, with outer stubs.
- **Triangle:** the lock marker. It has two states, on a seven-second loop:
  - **Seeking** (`#t=1`): a dashed amber triangle, enlarged, hunting around the centre. The status reads `SEEKING` and the range readout runs down.
  - **Locked** (`#t=4`): the triangle snaps to the centre and turns solid `sign-green`, with lit `aaaw-green` dots on its three corners. The status reads `LOCK`.
- **Status and range:** a small letter-spaced status at top-left, and a `mono` `RNG 0412` readout under the ring.
- **Tag:** a boxed **Object** heading with a 4px bar, then a list of pipe-ruled lines. The last line goes `color-error` when fire control is offline.

**Bracket sight** (frames 3–4):
- **Reticle:** four `hazard-yellow` corner brackets and a small square at the centre.
- **Tapes:** a heading tape across the top (−95…+95), and a pitch ladder on the right.
- **Readouts:** a battery bar with the operation clock bottom-left, and the trapezoid `CENTER` tab bottom-centre.

**Motion:** under `prefers-reduced-motion` the ring stops and the view holds the locked state.

**Consumer provides:** the view underneath, the target's screen position, and the tag lines. Each view is `role="img"`; the lock view rewrites its `aria-label` as it moves between "Seeking target: …" and "Target locked: …".
