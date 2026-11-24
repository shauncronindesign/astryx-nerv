# Button

The default clickable action. Use one accent action per group; everything else is secondary or ghost.

**When to use:** any single, explicit action, such as confirm, launch, abort or navigate. Labels are uppercase `sans` 700 at 14px, compressed with `compress-mild` and glowing with `shadow-bloom`: `LAUNCH`, `ABORT`, `CONFIRM SYNC`.

**Props** (unchanged from Astryx)

| Prop | Type | Default | Notes |
|---|---|---|---|
| `variant` | `"primary" \| "secondary" \| "ghost" \| "destructive"` | `"secondary"` | |
| `size` | `"sm" \| "md" \| "lg"` | `"md"` | `size-element-sm/md/lg` (24/30/36px); `lg` uses `chamfer-md` |
| `label` | `string` | — | uppercase |
| `icon` | `ReactNode` | — | geometric mark only (■ ◈ ▶) |
| `isIconOnly` / `isDisabled` / `isLoading` | `boolean` | `false` | |
| `href` | `string` | — | renders `<a>` |

**Shape:** two opposite corners cut with `chamfer-sm` (6px). The frame is the element's own background (`--ink`) showing around an inner fill (`--fill`) inset by 1px, so the cut diagonal gets a stroke too.

**Variant → token mapping**

- `primary`: solid `color-accent` with `color-on-accent` ink, a soft inner glow, and a segmented tail mark on the right.
- `secondary`: `color-background-surface` fill inside a 1px `color-border-accent` frame, label in `color-text-accent` with bloom.
- `ghost`: no fill or frame; the label sits in pipes, like `| DETAILS |`.
- `destructive`: `color-background-error-inverted` fill, `color-on-error` ink, `color-border-alert` frame, and a hazard-stripe block on the left.

**States:** hover brightens (`filter: brightness(1.18)`); pressed dims. `:focus-visible` is a 1px `color-border-accent` outline at 3px offset. Disabled uses `color-text-disabled` in a `color-border` frame, with no glow and no opacity fade. Loading shows a blinking `■` (set `aria-busy`).

**On Alert theme:** primary turns white with `alert-700` ink, and secondary sits on `alert-500`. The preview shows both.

**What the consumer provides:** a label (or an accessible name for icon-only) and a click handler or `href`.

## Film-derived additions

**Press feedback:** every button flashes bright for one frame when pressed, like a key lighting under a finger.

**Label plate** (`.plate`): the solid orange plate from the decryption and diagram screens, as a square-cornered button. It uses `color-label-plate` with `color-on-label-plate` type and no glow. Use it for a section's main action or as a clickable heading.

**Mode keys** (`.keys` / `.key`): the skewed key strip from under the activity timers.
- Each key has a 2px top rule and a small lamp.
- The live key fills with `color-accent` and blooms.
- A `danger` key is red, and fills `alert-300` when live.
- The strip is a `radiogroup`. Left and right arrows move the selection, and only the live key is in the tab order.

**Guarded action** (`.guard`): for actions that can't be undone.
- **At rest:** a hazard-striped cover sits over the key, with the action's name on a black plate.
- **First press:** the cover lifts in three steps and the key is armed. A pale fuse line runs along the bottom edge for three seconds.
- **Second press, inside the window:** the action fires. The key flashes pale and the label changes (`Ejected`).
- **No second press:** the cover drops back.

A `role="status"` note beside the key says what state it is in. Add `#armed` to pin the lifted cover.
