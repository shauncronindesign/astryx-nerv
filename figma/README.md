# Figma companion

Figma file: **Astryx NERV** — https://www.figma.com/design/qQZ7VjHkh7CbrRZKErKD4d
Repo: https://github.com/shauncronindesign/astryx-nerv (private; this Mac pushes with a repo deploy key)

| Page | What's there |
|---|---|
| Cover | Title card |
| Foundations | Theme roles × 8 modes, 178 film primitives, 21 type styles, 13 effects, spacing |
| Button · Badge · TextInput · Card | Component sets, every fill/stroke bound to Theme variables |
| Film components | Renders of the 28 coded components (canvas/motion pieces stay code-first) |

## Variables

| Collection | Modes | Source |
|---|---|---|
| Primitives | Value | `color.tokens` with a plain hex value (hidden from pickers) |
| Theme | Tactical, Alert, Clock, Pattern, Nominal, Wunder, Schematic, Terminal | `color.tokens` with per-theme values; aliases into Primitives |
| Dimensions | Value | spacing, radius, size, border, chamfer |

Names map `color-text-primary` → `text/primary`. A role that is also a group gets `/default`
(`color-accent` → `accent/default`). Every variable carries WEB code syntax `var(--<css-name>)`.

## Keeping it in sync

1. Edit `tools/build_tokens.py`, run it → `project/tokens.json`.
2. `python3 figma/gen_variables.py` → `figma/variables.js` (idempotent: updates by name).
3. Run `figma/variables.js` in the file (Figma MCP `use_figma`, or a scratch plugin).
4. For the gallery: `figma/capture.sh`, then upload the PNGs onto the `<Name> · render` layers.

## Known gaps

- Neue Helvetica Condensed and Matisse EB aren't available to Figma here; text styles use
  Inter Bold and Noto Serif JP Black and say so in their descriptions.
- `compress-*` (scaleX) has no Figma equivalent; it lives in code only.
- Chamfers are corner triangles filled with `background/body`, so they read as cuts on the
  body ground but not over other surfaces.
