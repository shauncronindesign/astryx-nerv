# SchematicCallout

The labels that sit on Rebuild's glowing wireframes and grid maps: a system title plate with heavy bars, region labels whose underline kinks down to a node, triangle nodes, and the `+ | Power Core` crosshair marker.

**Theme:** Clock (amber/peach) for power-grid and map schematics (frames 73–77, 82, 86); Tactical for AAAW schematics (frames 197–200).

**Parts**

| Part | Look | Tokens |
|---|---|---|
| `.plate` | 5px bars both sides; Japanese 26px over English 12px | `jp` 700 + `shadow-bloom-strong`; English in `color-text-secondary` |
| `.region` | Japanese over English, 1.5px underline with a 35° tail toward its node | `color-text-primary`, `shadow-bloom` |
| Pylons (canvas) | About 170 hollow glowing triangles scattered along the island chain, larger toward the front | `color-bloom`, glow in `color-text-accent` |
| Trunk line (canvas) | One glowing line along the spine of the chain, with white pulses travelling up it | `color-bloom` + glow |
| `.marker` | crosshair + 4px bar + compressed label, 30px | `color-text-accent`, `shadow-bloom-strong` |
| Floor (canvas) | Concentric arcs and radial lines from a point below the frame | `color-text-accent` at 28% |
| `.sys` | Small system tabs down the left edge: Japanese over English between two 3px bars | `color-text-primary`, `shadow-bloom` |

**Motion:** pylons brighten in a wave as power passes, and three pulses run up the trunk. Add `#t=<seconds>` to pin a frame. Under `prefers-reduced-motion` one still frame is drawn.

**Consumer provides:** the art underneath (or the pylon positions and trunk path for the built-in grid), the labels and their positions. Labels are absolutely placed; give the stage `role="img"` and one `aria-label` describing what the schematic shows.

**Don't:** box the labels or give them backgrounds. They float on the art and read through glow alone.
