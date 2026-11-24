# FieldSim

The Visualized Simulation screen from The plan. Luminous field strands sweep around a white-hot core on a near-black grid, with a lime file rail down the left edge.

**Anatomy:**
- **File rail:** a 16px `field-lime` strip with a soft glow and `Visualized Simulation File: Case …` set vertically in dark type.
- **View:** a near-black ground with a fine 14px blue-grey grid and a 1px frame.
- **Caption:** a 22px title condensed to 80% width, ending in a colon, with an 11px description under it. White ink, top-left.
- **Strands:** drawn on a canvas with additive blending, so crossings brighten. Each strand is drawn twice, as a wide faint halo and a thin core. The families are:
  - **Cyan loops** (`sim-wire-bright`): the big, thick loops on the right.
  - **Teal loops** (`field-teal`): finer and wider.
  - **Blue swell** (`field-blue`): low, wide loops along the bottom.
  - **Red knot** (`alert-300`): a tight tangle on the left.
  - **Gold bundle** (`field-gold`): strands arcing from the knot up to the core.
  - **Core strands** (warm white): a few bright strands that weave across the middle like a helix.
- **Under-glow:** three radial gradients (blue, red, warm white) under the strands.

**Motion:** every strand drifts on its own phase. Under `prefers-reduced-motion` one frame is drawn.

**Accessibility:** the section and canvas are labelled. The strands are decoration, so put real findings in the caption.

**Consumer provides:** the file code, caption and description. Optionally the families (count, colour, anchors) or a live data source in place of the generated strands.
