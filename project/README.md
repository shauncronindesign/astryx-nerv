# Astryx NERV

Astryx NERV is a fork of the Astryx interface system re-skinned with the
on-screen UI of the Evangelion Rebuild films: saturated, glowing type on
tinted near-black grounds, solid red alert walls, semantic color with fixed
meaning, and mechanically compressed type. The Astryx **role vocabulary is
unchanged** —
`color-accent`, `color-background-surface`, `color-text-secondary`,
`shadow-inset-selected` and the rest keep their names — so any Astryx
component ports across by swapping the token file, then you make it your
own from there.

The films change the whole palette from scene to scene, not just the
accent, so the system carries seven themes. Six come from a scan of the
Rebuild UI frames (see *Rebuild UI reference* and the **References**
assets); the seventh is the TV-era spec. Switch with `data-theme`.

| Theme | Ground | Voice | Use it for | Frames |
|---|---|---|---|---|
| **Tactical** (default) | red-black `tac-ground` #1A0106 | notification orange `tac-orange-400` #FE7222 | Mission notifications, bracket captions, AAAW screens, schematics | 151, 205, 244 |
| **Alert** | solid red `alert-400` #D32230 | white | MAGI hex walls, EMERGENCY, CONDITION, cable-cut walls | 31, 36, 52, 165 |
| **Clock** | brown-black `clock-ground` #0C0500 | clock amber `clock-amber` #ED8D25 | Clock boards, power-grid maps, ID cards. The former *Rebuild* theme | 41, 64, 73 |
| **Pattern** | violet-black `pattern-ground` #060426 | magenta `magenta-500` #D21A9F | Pattern analysis, plug schematics, A.T. field feeds | 9, 16, 19, 133 |
| **Nominal** | green-black `mint-900` #04120C | sync mint `mint-400` #2BEEAE | Sync columns, unlocked gates, "all systems green" | 11, 68, 107 |
| **Wunder** | indigo-black `wunder-ground` #0A0A17 | ring red `wunder-red` #BE2724 | AAA Wunder bridge, ring HUDs | 175–184 |
| **Schematic** (light) | paper `paper-100` #E0DDD1 | rust `rust-500` #7B4627 on a `label-orange` #F09C48 plate | Paper structural diagrams; the one light panel in the films | New Spear clip |
| **Terminal** | pure void #000000 | Signal Orange `signal-300` #F07020 | TV-era screens (*Color + Typography Foundation v2.0*) | — |

Every theme passes 4.5:1 for text roles (and for categorical tag text on
its tag) on body, surface and popover. Alert gets there by keeping all
text near-white, since nothing else reads on #D32230.

## Content fundamentals

- **Color carries meaning, not decoration.** Amber/orange = standard data
  and the voice. Green = nominal, approved, connected. Red = threat,
  failure, hostile. Blue = Pattern Blue / Angel classification (and WILLE
  in 3.33). White = SEELE, title cards, flash frames. Using green where red
  belongs is misinformation, not a style choice.
- **Write like an instrument.** Labels are ALL CAPS, short, and specific:
  `SYNC RATE · 89.2%`, `DIRECT LINK 108`, `EVA-00 [OFFLINE]`,
  `±0:02:18649`. Units are always shown, in `color-text-tertiary`.
- **Bilingual where it earns it.** A Japanese title in the display face over
  an English HUD label in Helvetica caps is the signature pairing
  (`色彩基盤` / `COLOR FOUNDATIONS`).
- **Red is a ground as well as a status.** When the whole room is in
  alert, switch to the Alert theme instead of adding red dots.
- **The spectrum is for pattern data only.** Magenta, violet, cyan and the
  `color-spectrum-*` gradient belong to Pattern-theme screens (plug
  schematics, A.T. field feeds). Don't use them for ordinary chrome.
- **Never in this system:** pastels as fills, rounded corners, drop
  shadows.

## Visual foundations

**Color** — 72 primitives from the two foundation documents, plus 73
sampled from the films (`alert-*`, `tac-*`, `gold-*`, `bloom-*`,
`clock-*`, `hazard-*`, `mint-*`, `lime-*`, `pattern-*`, `violet-*`,
`magenta-500`, `pink-*`, `cyan-*`, `wunder-*`, `timer-*`, `sysblue-*`;
each token's note names its frame), feed ~100 semantic roles that alias
them per theme. New roles: `color-hazard` / `-hazard-alt` /
`on-hazard` (chevron bands), `color-bloom` (glow core),
`color-spectrum-start/mid/end`, `color-timer-start/mid/end/digit`. Grounds step
`color-background-body` → `-surface` / `-card` → `-popover`. Two extra
roles Astryx did not have: `color-background-alert` (red-deep / threat-900
panel ground) and `color-background-system` (blue-deep / system-500 radar
backdrop). Status: `color-success`, `color-error`, `color-warning` and
`color-info`, each with `-muted` and `on-*`. Warning (`amber-peak`,
`signal-100`) is deliberately lighter than accent so caution and the
standard voice separate by lightness, not hue.

Categorical hues: `amber`, `red`, `green`, `blue`, `wille`, `indigo`,
`ochre`, `gray`, plus Rebuild's `magenta`, `violet`, `cyan`, `mint` and
`gold`. Each has `background-`, `border-`, `icon-` and `text-` roles at
4.5:1. On Alert every tag renders white on a dark tint.

**Typography** — seven families. Every stack names the typeface from the
films first, then the open-licence font shipped in `fonts/` (woff2, all
SIL Open Font License, from Google Fonts):

| key | as seen on screen | shipped stand-in | role |
|---|---|---|---|
| `display` | Matisse EB / Pro EB (Fontworks) | Noto Serif JP Black 900 | Title cards, Japanese identity, compressed |
| `sans` | Helvetica / Neue Helvetica | Inter 400, 700 | ALL-CAPS HUD headings and callouts |
| `mono` | bitmap / OCR-B terminal | Share Tech Mono 400, IBM Plex Mono 400 | Body, data, MAGI boot output |
| `jp` | — (spec body face) | Zen Kaku Gothic New 300, 400, 700 | Japanese subtitles, ghost-kanji texture |
| `signage` | Futura | Jost 400, 500, 700 | Tokyo-3 signage, axis markers |
| `poster` | — (spec masthead face) | Bebas Neue 400 | Document mastheads and section titles |
| `hardware` | Eurostile / Eurostile Extended | Eurostile 400 (URW), EuroStyle Normal 400 | Vehicle stencils, military hardware |

The licensed originals are listed first in each stack, so they take over
automatically on any machine that has them installed; to ship them, add
their files to `fonts/` once licensed. Inter is the spec's own
"prototyping only" Helvetica substitute — Helvetica Neue still wins where
the OS has it.

`hardware` ships the actual Eurostile (URW, 1992) with EuroStyle Normal
(Alex Bokov, free) as its fallback. The Eurostile file's embedding flag
is *restricted*: keep this system private, or confirm a web-font licence
before sharing it, and drop `Eurostile-Regular.woff2` to fall back to
EuroStyle.

**Compression doctrine** — display and headline type is mechanically
squeezed with `transform: scaleX()`, `transform-origin: left`:
`compress-mild` 0.82, `compress-standard` 0.70, `compress-extreme` 0.55.
Rebuild display Japanese goes the other way with `stretch-rebuild` 1.18.

**Spacing** — 4px-rooted with a 2px seam (`space-0-5`): swatches, cards
and panels sit 2px apart, never floating on large gaps. Section rhythm is
`space-14` (56px) above a section label, `space-18` (72px) between
sections.

**Radius and shape** — never rounded. Everything is `0px` except
`radius-element` (1px) and `radius-full` (status dots and radar blips
only). Panels are shaped by cuts instead, using the `shape` tokens:
`chamfer-sm/md/lg` (6/12/24px clipped corners via `clip-path`),
`slant-plate` (−8°, notification plates), `slant-tag` (−30°, READY / OUT
OF RANGE tags), `hazard-angle` + `hazard-pitch` (45° chevrons, 24px), and
`hex-ratio` for flat-top hex walls.

**Elevation and bloom** — no drop shadows. `shadow-low` / `-med` /
`-high` are a hairline ring plus a bloom in the theme's own hue. In the
films nearly everything bright glows, so glow is the default, not the
exception: `shadow-bloom` goes on titles, readouts, plate frames and
rules (it works as `text-shadow` too), and `shadow-bloom-strong` on big
titles and 7-segment readouts. `shadow-glow-*` stays for live
indicators.

**Texture** — a scanline overlay (`color-scanline`, Rebuild 3px/4px pitch,
Terminal 1px/3px) and an optional ghost-kanji layer in
`color-text-ghost`. If the ghost layer is readable at a glance, it is too
bright.

## Iconography

No icon set ships yet. Use geometric marks only: filled squares (`■`, the
blinking kicker), diamonds (`◈`), 6–8px status dots in `radius-full`, and
1px crosshair/tick rules. Draw them in the `color-icon-*` roles or the
matching categorical `icon-<hue>`. Never a pictorial or rounded icon set.

## Usage rules

- Build every surface from `color-background-*` + `color-text-*` +
  `color-border-*` as a set. Hairlines are `border-width` (1px) in
  `color-border`; `border-width-alert` (2px, `color-border-alert`) only for
  an EMERGENCY frame.
- One `color-accent` action per group. Secondary actions sit on
  `color-neutral`; ghost actions are text-only in `color-text-accent`.
- Solid status fill + its `on-*` pair for badges, verdicts and strips;
  `-muted` tints for zone backgrounds.
- `color-text-disabled` and `color-text-ghost` are below 4.5:1 on purpose —
  disabled and decorative only, never content.
- Source pairs that fail text contrast are kept as fills only and flagged in
  their token notes: `amber-low`, `red-core`, `blue-pattern`, `gray-muted`,
  `threat-300` on `threat-900`. From the films: `wunder-red`,
  `violet-500` and `alert-400` fail as text on dark grounds. Use them as
  fills, and use `wunder-red-bright`, `violet-300` or white for text.
- `tokens.json` is generated by `tools/build_tokens.py` in the local
  `Arrow/astryx-nerv` folder. That script holds the per-theme role tables
  and the contrast check, so change it there and rebuild rather than
  editing theme values by hand.

---

*Forked from Astryx (token roles and component contracts). Foundations from
the two uploaded documents: "NGE REBUILD — Color Foundations" v1.0 and
"NERV UI · Color Foundation System" v2.0. A fan reference system for
personal use; it uses no logos or marks from the films.*
