# NotificationPlate

The Rebuild 3.0+1.0 Tactical Mission Notification: a slanted, chamfered plate with one big glowing title, a rule, two or three lines of detail and a footer bar. Use it for events the operator must read now.

**Theme:** Tactical (default). The plate takes its ink from `--ink`, so the same markup gives three tones:

| Variant | `--ink` | Frames |
|---|---|---|
| default | `color-border-accent` (notification orange) | 151, 244 |
| `warning` | `color-error` | 230–231, 252 |
| `confirmed` | `color-warning` (gold) | 232 |

**Anatomy:** optional kicker (`Incoming Subject: UNKNOWN`, 11px `color-text-secondary`) · title (`sans` 700, 34–48px, `compress-mild`, `shadow-bloom-strong`) · 3px rule in `--ink` · body lines (17px 700, `color-text-secondary`, indented `space-6`) · footer: segmented end caps + framed label bar with a tiny `mono` code line.

**Shape:** clipped with `chamfer-md` on two corners; the 1px frame is a masked layer that follows the clip and glows with `drop-shadow`. The plate sits in perspective: `rotateY(-12deg) rotateZ(-2deg)`; flip the Y sign for a plate on the right of the screen.

**Setting:** in the films the plates float in front of the thing they describe. The preview shows that with three backdrop layers:
- A faceted wire mesh in `color-error`.
- Small `+` registration sparks.
- A dashed tether from each plate toward the mesh.

The backdrop is decoration and is `aria-hidden`.

**Footer details:** a short double-line stub sits outside each end cap, as on the film plates.

**Motion:** a plate arrives in order. The frame is there first, then the kicker, title, rule, each body line and the footer switch on about 140ms apart, in hard steps with no fade or slide. Click a plate to replay. The resting state is fully visible, so nothing stays hidden where scripts or motion are off. Disabled under `prefers-reduced-motion`.

**Consumer provides:** title, up to three body lines, the footer label, and an `aria-label`. Announce it with `role="status"` (or `alert` for the warning variant) when it appears.
