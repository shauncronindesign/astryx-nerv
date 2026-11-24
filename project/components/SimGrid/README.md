# SimGrid

The EVA-02 multi-camera combat simulation from the Asuka clip. A wireframe mannequin with a rifle is seen from seven cameras across two takes. The figure moves between poses and the timecode runs.

**Layout:**
- **Take 2199:** one large tile (`CAM:01`) beside a 2×2 block (`CAM:02–05`).
- **Caption strip:** `Object:EVA-02 Simulation Take 2199` on the left and `Take 2200` on the right, in 14px condensed white.
- **Take 2200:** two large tiles (`CAM:06`, `CAM:07`).
- Gaps are 4px.

**Tile:**
- Near-black ground, with orange corner brackets top-left and bottom-right.
- `mono` 8px timecode and a condensed `CAM:0n` id. They sit in the top-right, top-left or bottom-right corner depending on the tile.
- Main views add a gold `▼ ENEMY-γ` target marker.

**Scene:**
- **Floor:** concentric ellipses and radial lines, which read as a dome grid on the ground plane. Two dotted white horizon lines and small registration crosses sit above it.
- **Mannequin:** every limb is a capsule outline with cross rungs and a faint cyan fill (`color-wireframe` on a `sim-wire` glow). The head has latitude and longitude lines.
- **Rifle:** boxed sections in `sim-violet` with mesh lines.
- **Core:** a pulsing `color-wireframe-core` sphere with two orbit rings. It is the only warm colour in the frame.

**Poses and cameras:** poses are joint angles (`stand`, `aim`, `run`, `kneel`). Each tile blends between two poses on a 6-second loop and has its own zoom, pan and roll, so the close-up tiles show dutch-angled crops of the same motion.

**Motion and accessibility:** add `#t=<seconds>` to pin a frame. Under `prefers-reduced-motion` one still frame is drawn. The whole grid is one `role="img"` with a label naming the object, takes and target.

**Consumer provides:** take labels, and per tile the camera id, timecode, target marker and view content. The mannequin can be replaced by a canvas, WebGL view or video.
