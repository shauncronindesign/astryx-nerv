# StructuralDiagram

The structural diagram from New Spear, on the same handheld viewer as PatternScope. Rust vertebra chains run across cream paper, and the middle chain is opened to show the serpentine linkage and the spear head. It uses the light **Schematic** theme.

**Anatomy:**
- **Screen:** `paper-100` with 10px rounded corners and a soft `label-orange` glow, so it reads as a lit display.
- **MAGI rail:** a paler strip on the left with `MAGI Achiral 3 / 2 / 1` rotated in `label-orange`.
- **Label plate:** a tall `color-label-plate` bar with white rotated type (`S-BLOCK: Spinal Linkage System`). Beside it is a `paper-50` slot with the sub-label in `label-orange`.
- **Chains:** one vertebra symbol, repeated with overlap. It has a `rust-500` armoured body, a `rust-700` outline, `label-orange` contour lines and a dark diamond core. The top and bottom lanes run the full width.
- **Linkage:** in the middle lane the chain opens into a serpentine tube, drawn as a `paper-50` channel with a `rust-700` wall and a dashed centre line. Then come two more vertebrae, a divider and the spear head, which is a larger vertebra with orange barbs.
- **Trusses:** thin `label-orange` frames, braces and bolt circles behind everything, at about half strength.
- **Callouts:** `mono` 9px labels on leader lines.
- **File tab:** a lime tab on the top edge.

**Motion:** a pale signal dot steps along the middle chain every 260ms. Under `prefers-reduced-motion` it stays on one vertebra.

**Theme:** set `data-theme="schematic"` on the element.

**Accessibility:** the SVG is `role="img"` with a label describing the diagram.

**Consumer provides:** the system name and sub-label, the rail labels, the chain lengths, the linkage turn count, and the callouts.
