# DecryptionKey

The Decryption Key panel from the Black Chamber sequence (System Unlocked). The panel shows a lock being picked: pins resolve one at a time, and when the last one lands, every match bar snaps into a single even row.

**Anatomy:**
- **Link dial:** a large dial cut off by the top edge, made of a dark disc, a thick ring, a hairline ring and a dotted ring. On it sits an `ILINK` readout with three boxed digits and `%`.
- **Header:**
  - `Decryption Key` at 46px, condensed to 80% width, with bloom.
  - A 15px subtitle beside it.
  - Two outlined status tags on the right. The second tag changes from `All Systems: Locked` to `Unlocked`.
- **Label plates:** solid `color-label-plate` blocks with dark type, used for `Current Target Cylinders` and `MATCHES`.
- **Chart:** four cylinders of ten pins, on a `decrypt-panel` band behind the centre line.
  - Above the line: a key bar marked `A` or `B`, with a thin stem up to the top rail.
  - Below the line: a match bar numbered `1–5`.
  - An unresolved pin is drawn as an outline with orange type. A resolved pin fills solid with dark type.
- **Frame lines:** a stepped line runs from the left labels into the chart frame, the way the film ties side labels to data.
- **Progress:** `Total Progress` and a 44px percentage.
- **Clusters:** a fill bar, a name and a status cell for each of `Cluster-A…D`. The highlight moves between the cells while decrypting.
- **Texture:** small registration crosses across the ground.

**States:**
- **Decrypting** (`#p=0…0.99`): pins fill in one by one, the percentage climbs from 90 and the cluster highlight cycles.
- **Matched** (`#p=1`): the percentage reads 100, every match bar becomes a short slanted tooth of equal height, all four cluster cells fill and read `Matched: Stage 05B`, and the tag reads `Unlocked`.

The preview loops through a 7-second run and a 3-second hold. Add `#p=<value>` to the URL to pin a state.

**Motion and accessibility:** under `prefers-reduced-motion` the panel renders one still frame at 96%. The SVG's `aria-label` is rewritten with the progress and state on every render.

**Colour:** fixed to the decrypt primitives (`decrypt-ground`, `decrypt-panel`, `decrypt-rule`, `decrypt-orange`) whatever the theme.

**Consumer provides:** the title and subtitle, status tags, per-pin key letter, heights, match number and resolved flag, the progress value, and cluster names, fill and stage.
