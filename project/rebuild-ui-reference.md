# Rebuild UI reference

A scan of the on-screen interfaces in the Rebuild films (1.11, 2.22, 3.33,
3.0+1.0): 252 Blu-ray frames plus the Misc and Eva Wallpapers sets. Only the
interfaces were read; character and story shots were skipped. The frames
are in the **References** asset group, named `<component>-<frame>.jpg`.

## What the current system gets wrong

The system now reads as a quiet amber terminal: hairline panels on near-black,
one accent, glow only for "live" items, no purple or magenta, no gradients.
The films don't look like that:

1. **Red is a ground, not a status dot.** The busiest screens (the MAGI hex
   wall, umbilical-cut wall, CONDITION II, EMERGENCY) put white or dark-red
   type on solid red at full saturation, edge to edge.
2. **Everything glows.** Orange, red and green type has a strong bloom
   halo. Static labels glow too, not only live values.
3. **Rebuild uses the full spectrum.** Pattern analysis, plug schematics and
   the A.T. field feed use magenta, violet, cyan and mint, often as a smooth
   gradient through hues (frames 9, 16, 19, 47, 129, 133). The README's
   "never purple, magenta, gradients between hue families" rule does not
   match these frames.
4. **Type is condensed Helvetica Bold with bloom, not mono.** Mono shows up
   only in small data runs. Headings are big, tight and bright: `Blood Type
   : BLUE`, `Executive Authority: Captain Katsuragi`, `KEEP OUT`.
5. **Panels are cut and angled, not square cards.** Hexagons, clipped
   corners, slanted plates, hazard stripes and bracket rules shape the
   panels. There are almost no plain rectangles with hairlines.
6. **Grounds are tinted, never neutral.** "Black" is red-black (#1A0106),
   brown-black (#0C0500) or indigo-black (#0A0A17), depending on the scene.

## Components, by how often they appear

| # | Component | Frames | Anatomy |
|---|---|---|---|
| 1 | **Hex wall** (MAGI / alert wall) | 31–33, 36–39, 52–53, 96, 116, 124–125, 135, 165–168, W13–14 | Wall of large hex cells on red; a central plate with a Japanese title and an English subtitle; WARNING / ALERT / EMERGENCY hexes with ▲ LEVEL marks; MAGI Melchior 1 / Balthasar 2 / Casper 3 labels; `MODE: Tactics` chip; blue sky-grid panels at the edges |
| 2 | **Bracket caption** | 9–10, 47, 133, 136, 142–143, W8 | `\| Monitored Target Subject : EVA-01 Entry Plug \|` lines in orange Helvetica Cond., pipe-bracketed, stacked 2–3 deep, in a corner over a schematic |
| 3 | **Notification plate** (Tactical Mission Notification) | 151, 232, 237–244, 252 | Slanted dark-red plate, 1px orange frame, big bright title, a rule, 2–3 body lines, footer bar with segmented end caps and a tiny code line |
| 4 | **Activity timer** (活動限界まで) | 25–26, 39, 42, 45, 100, 115, 138, M1–M5, W5 | Huge 7-segment digits; 内部 INTERNAL / 主電源供給システム / 外部 EXTERNAL tabs on the right; STOP · SLOW · NORMAL · RACING · DANGER EMERGENCY strip; blue-mauve gradient panel, all-red variant |
| 5 | **Schematic / hologram** | 22–24, 28, 63, 73–77, 82, 86, 130–131, 197–200, 208–210 | Glowing wireframe on a perspective grid; `+ \| Power Core` callouts; Japanese label plates with an English line under them; triangle node markers |
| 6 | **AAAW frame chrome** (3.0+1.0) | 197–210 | Corner ticks; `AUX Projector 01` top left; `Linked` `ONLINE` chips top right; a vertical green side label; a footer `AAAW / Quarantined Interrogation Room 101`; `Test Subject … All Vitals: Normal` chips |
| 7 | **Clock board** | 63–64, 70 | Japanese label + English sub-label + 7-seg readout per row (到達予想時刻 / Countdown / 日本標準時 Live); chamfered amber frame |
| 8 | **Condition plate** (警報) | 54, 57–58 | Big 警報 + CONDITION RED/YELLOW, data rows (damage %, CRITICAL), six ALERT hexes around the plate |
| 9 | **Hazard band** | 14–15, 59, 116, 210, 213–215 | Yellow/black or red/black 45° chevrons; framing EMERGENCY / 非常事態 / CONDITION:RED CODE:102; short angled READY / OUT OF RANGE tags |
| 10 | **Gate / room sign** | 68–69, 105–107 | Glowing sign: SECURITY LEVEL line, logo, big title, status line; red = locked / in use, green = unlocked / complete; LEVEL-01 under the plate |
| 11 | **Data graphs** | 11, 17–21, 46, 201–202, W7, W11 | Diagonal sync slats (mint/red), brain-wave level columns, sensor feed with ±8-digit counters and a ±100 side scale, the sync helix |
| 12 | **Live feed tile** | 49–50, 90–91, 120–121 | Video tile; `Monitored Object:` with `[TEST PLUG 01]` in brackets; pilot/vitals lines; orange `LIVE` box + `ONLINE` chip; orange divider rules |
| 13 | **Comm card** (SOUND ONLY) | 117–119, 155–156 | White or blue floating card: `SOUND ONLY / SELECTED`, From / To blocks, `LIVE` tag, transmission footer |
| 14 | **Reticle + target tag** | 3–4, 85, 87–88, 127 | Thin ring with ticks and a triangle or bracket centre; a pipe-bracketed `Object` tag list (FCS Mode - Offline) |
| 15 | **Big readout** | 109, 203, 220 | Single huge value (`00.000 %`, `68.3861%`) with labelled chips under it |
| 16 | **Ring HUD** (Wunder) | 94–95, 175–184 | Concentric bloom rings, red on indigo-black, ALERT text set on the ring, R / L boxes |
| 17 | **Map / radar** | 13, 79–81, 113–114, 140 | Hex-zone impact maps, contour fields, diamond markers, `Estimate of…` captions |
| 18 | **Title card** | 144–149, W6, W17 | KEEP OUT: huge white condensed caps, rule, centred subtitle; red "New EVA-Unit" banner |
| 19 | **Personal / ID card** | 41, 51 | Photo, barcode, 検索結果:個人情報 footer tab |

The current system has Button, Badge, Card, Dialog, StatusList and
TextInput. Only Badge and StatusList come close to the films; every
component above except the ID card is missing.

## Colors sampled from the frames

Values are medians of the bright glyph pixels (or of the ground) in the frame shown.

| Family | Swatches | Frames |
|---|---|---|
| **Alert red** (grounds, hex walls) | `#D32230` wall, `#CE1B29`, `#E10F14` hex, `#E7323D` EMERGENCY hex, `#EA3223` banner, `#68222D` shade | 31, 36, W13, W14, W17 |
| **Notification orange** | `#FE7222` glyph, `#E24319` mid, `#EC571C` frame, ground `#1A0106` / `#370704` | 151, 244 |
| **Clock amber** | `#ED8D25` glyph, `#D67B20`, ground `#0C0500` | 64, 120 |
| **AAAW gold** | `#F2E178`, `#DCD849`, `#E3C242` titles; wire orange `#E58832` | 197, 203, 205 |
| **Bloom peach** (glow core) | `#FDE6C6`, `#F2AE7A`, `#F2C189` | 73, 57 |
| **Hazard** | yellow `#FBBD3D` / `#F7B239`, red `#E22F2F` | 14 |
| **Gate green** | `#E0E835` bright, `#A3C92D` | 68 |
| **Sign green** | `#45B43F`, `#1AB129`, tint `#E1FAD1` | 107 |
| **Sync mint** | `#2DF5B5`, `#2BEEAE` | 11, W7 |
| **AAAW side green** | `#B1F34D`, `#94D241` | 205 |
| **Reticle** | yellow `#DDB02C`, green `#1AD46D` | 127 |
| **Timer** | 7-seg red `#DE2550`, mauve `#C75C88`, blue tab `#416AB1` / `#6593D3`, navy `#090F20` | 25 |
| **Spectrum / pattern** | magenta `#D21A9F`, violet `#841AD0`, fuchsia `#E01CCB`, pink `#F058A9`, cyan `#54D8FC`, mint `#52DEA2` | 9, 16, 19, 133 |
| **Wunder** | ring red `#BE2724`, ground `#0A0A17`, haze `#2B1E45` | 178 |
| **System blue** | `#3A6CAD`, `#54A8E8`, external `#2860C1` | 31, 94 |
| **Signage white** | `#FEFEFE` KEEP OUT, cream `#FFF5E6` / `#F6BF80` | 144, 57 |

Next to the current tokens: `amber-core` #E09030 is close to clock amber
and can stay. `red-core` #DD2200 is too orange for the films' alert red,
which sits around #D32230 (hue ~355°, slightly blue). The orange
`signal-*` ramp from the TV-era spec is close to notification orange.
Nothing in the system covers the gold, mint, gate-green, magenta, violet
or cyan families.

## Themes needed

The films change the whole palette from scene to scene, not just the
accent. Six themes cover every scanned screen:

| Theme | Ground | Voice | Accents | Used for |
|---|---|---|---|---|
| **Tactical** (default) | red-black `#1A0106` | notification orange `#FE7222` | gold, peach bloom | Notification plates, bracket captions, AAAW, schematics |
| **Alert** | alert red `#D32230` (fill) | white / dark red `#68222D` | hazard yellow, system blue | Hex walls, EMERGENCY, CONDITION, banners |
| **Clock** | brown-black `#0C0500` | clock amber `#ED8D25` | peach | Clock boards, power-grid schematics, ID cards |
| **Pattern** | violet-black `#060426` | magenta `#D21A9F` | cyan, mint, violet, spectrum gradient | Pattern analysis, plug schematics, A.T. field feed |
| **Nominal** | green-black `#04120C` | sync mint `#2DF5B5` | gate green, lime | Sync columns, unlocked gates, "all systems green" |
| **Wunder** | indigo-black `#0A0A17` | ring red `#BE2724` | system blue | AAA Wunder bridge, ring HUDs |

Keep **Terminal** (the TV-era spec) as a seventh theme. The current
Rebuild theme (amber on #050401) is closest to Clock.

## Type, as seen

- **Condensed Helvetica Bold** for nearly all English: titles, chips, captions. Scale it with `compress-mild` and make it much bigger than the system does now (titles take 8–15% of frame height).
- **Matisse EB** for Japanese titles on plates and timers, always with a smaller English line under it.
- **7-segment digits** for every timer and clock. This needs its own family; Share Tech Mono doesn't read as a segment display.
- Pipe brackets `| … |` and square brackets `[ … ]` wrap captions and object names.
- Bloom: one tight glow plus a wide soft one, in the glyph's own color. Example: `0 0 2px currentColor, 0 0 12px color-mix(currentColor 60%)`.


## Video pass (2026-11-23)

The Rebuild.zip held the same frames as the folder already scanned, so the new material came from its six video clips (Asuka, New Eva Parts, New Spear, System Unlocked, The plan, The spears). Frames were extracted every 2s and scanned for UI only. New reference frames are in the References group with a clip code instead of a frame number (`su` System Unlocked, `sp` The spears, `ns` New Spear, `as` Asuka, `pl` The plan, `ep` New Eva Parts).

### New components

| Component | Source | What it adds |
|---|---|---|
| **DecryptionKey** | System Unlocked | Paired A/B key bars over 1–5 match bars, big % progress, cluster status strip; solid orange label plates |
| **PatternScope** | The spears | One glowing orange trace across SEC sections; MAGI Achiral 1–3 column; red caution marker |
| **StructuralDiagram** | New Spear | Rust line art on cream paper, vertical label plate, MAGI rail; introduced the **Schematic** theme |
| **SimGrid** | Asuka | Multi-cam wireframe takes: CAM tiles, timecode, ENEMY marker, perspective floor, orange core |
| **FieldSim** | The plan | Multicolour field lines (teal, blue, gold, red) on navy with a lime file rail |

### Recurring patterns confirmed

- **Solid orange label plates** with dark type head sections (`Current Target Cylinders`, `MATCHES`, `S-BLOCK…`). The token is `color-label-plate`.
- **Lime file tabs and rails** (`Simulation File: Case …`) mark every simulation view. The primitive is `field-lime`.
- **MAGI Achiral 1/2/3** status columns appear beside scopes and diagrams.
- **Condensed Helvetica Bold** everywhere, often squeezed to about 82–88% width.
- **German labels** on the EVA-02 internal timer (`RESTLAUFZEIT`, `HAUPTENERGIE-VERSORGUNGSSYSTEM`, `STOP / NORMAL / LANGSAM / SCHNELL`) on a brick and amber housing (`de-*` primitives). Built as **InternalTimer**.
- **Pink line-art blueprints** on a greenish white ground for Mari's parts list (`blush-*` primitives). Built as **PartsBlueprint**.

### New tokens

- **Primitives:**
  - `decrypt-*`
  - `scope-orange` and `scope-ember`
  - `paper-*` and `rust-*`
  - `label-orange`
  - `sim-*`
  - `field-*`
  - `blush-*`
  - `de-*`
- **Roles:**
  - `color-scope` and `color-scope-halo`
  - `color-wireframe`, `color-wireframe-dim` and `color-wireframe-core`
  - `color-label-plate` and `color-on-label-plate`
- **Theme:** the eighth theme, **Schematic**, is light. Paper ground, rust ink, AA contrast throughout, and tinted categorical chips with dark ink.
- Values marked "eyeballed" in their usage note were read off the frame by eye rather than sampled.

### What the web says

- **Who designed the screens.** Ichifuru is credited for "Monitor Design Collaboration" on the NERV HQ screens from *2.0* onward, a credit new to Japanese anime production. [route2015 interview #04](https://route2015.otakumode.com/interview/04/5/)
- **Typefaces.** The display face is Matisse EB, paired with all-caps Helvetica that is often compressed. The SOUND ONLY monoliths are Helvetica. [Fonts In Use](https://www.fontsinuse.com/uses/28760/neon-genesis-evangelion) · [Typography case study, HKU](https://arthistory.hku.hk/index.php/typography-and-cultural-intersections-a-case-study-on-neon-genesis-evangelion-part-one/)
- **Matisse versions.** The Rebuild films use Eva-Matisse-Standard; the TV series uses Eva-Matisse-Classic. [Fontworks](https://en.fontworks.co.jp/products/evamatisse/)
- **Fan palette.** Fan UI kits agree on orange labels, green data, cyan wireframes and red alerts on black. That matches Tactical, Nominal and SimGrid here. [NERV-UI](https://mdrbx.github.io/nerv-ui/docs/getting-started/installation)
- **Anno's logos.** The English logos are hand-drawn by Hideaki Anno, which suggests one-off lettering for titles rather than a typeface. [ANN](https://www.animenewsnetwork.com/interest/2020-04-23/khara-reveals-that-evangelion-english-logos-are-hand-drawn-by-hideaki-anno/.158846)
- **General FUI context.** [Gizmodo on sci-fi UIs](https://gizmodo.com/lets-take-a-second-to-admire-sci-fi-user-interfaces-1834354325) · [80.lv: an Eva-inspired diegetic HUD](https://80.lv/articles/neon-genesis-evangelion-inspired-diegetic-hud-for-space-game)
- **No deep source.** There is no in-depth published breakdown of the Rebuild screens. The frames in this References group are the best primary source.


## Second pass on the video components (2026-11-23)

A closer look at the clips, frame by frame, changed how seven components are built.

- **These are handset screens.** PatternScope and StructuralDiagram are the same phone app, held upright and filmed sideways. That is why their type reads bottom-to-top. Both now share one shell: three MAGI lanes, a lime file tab, rotated labels.
- **Screens have a before and an after.** The decryption chart's match bars snap into one even row at 100%. The pattern scope goes from one rough band to three lanes with a clean sample. Components now carry those states and loop between them.
- **Patterns are blocky, not smooth.** The scope's trace is built from square blocks with blur on top, not a sine line.
- **Light is additive.** The field strands brighten where they cross and have a white-hot core. FieldSim is now drawn on a canvas with additive blending.
- **Wireframes are meshes.** Simulation figures have volume: capsule limbs with rungs, a faint fill, and a glowing core.
- **Dense line art.** The paper diagram and the pink blueprint are packed with repeated, armoured parts, hatching and scaffold bracing.

Pinned states for review: `DecryptionKey#p=1`, `PatternScope#stage=0`, `SimGrid#t=2.4`.


## Second pass on five original components (2026-11-23)

The same treatment as the video components, applied to five of the original set by comparing each render side by side with its frames.

| Component | What the frames showed | What changed |
|---|---|---|
| **HexWall** | The wall is a honeycomb of translucent glass over a blue sky, and it changes message (frames 31 → 52) | Rebuilt as a honeycomb; two states with a white flash between them |
| **NotificationPlate** | Plates float in front of a wire mesh, with sparks and tethers | Mesh backdrop, tethers, footer stubs; content switches on line by line |
| **ActivityTimer** | Under a minute the whole housing turns red (frame 45) | Emergency state, heavier digits, ruler ticks |
| **ClockBoard** | Frame 70 is a different, larger board with giant unit digits | Added the operation board: giant scan-lined numerals, zone chips, `T+` and GMT rows |
| **SyncGraph** | Slats are a herringbone with orange wiring; the feed is a filled contour shape, not a bundle of lines | Both graphs rebuilt |

Pinned states for review: `HexWall#state=1`, `ActivityTimer#left=45`, `SyncGraph#t=1.2`.


## Second pass on five more original components (2026-11-24)

| Component | What the frames showed | What changed |
|---|---|---|
| **RingHud** | Wide red belts in real perspective around a shaft, with `ALERT` on the surface, a sensor net and glowing contacts (frame 178) | Wunder view redrawn on a canvas as belts with mapped lettering, shaft, net, contacts and status hexes |
| **Reticle** | A thin amber ring and a green triangle with lit corners (frame 127) | Seeking and locked states, corner dots, status and range readouts |
| **LiveFeed** | Tiles carry a pilot picture; titles sit in square brackets (frame 120) | Pilot stand-in, heartbeat strip, timecode; a lost feed shows static and `NO SIGNAL` |
| **BigReadout** | Slashed zeros, scan-lined digits, red end bars, a hazard strip (frame 203) | All four added, plus corner tags and a hexagon mesh |
| **CommCard** | The card is a lit sheet, also seen mirrored from behind (frame 117) | Voice-level bars, sheen, LIVE blink, and a back-view variant |

Pinned states for review: `RingHud#t=2`, `Reticle#t=1` (seeking), `Reticle#t=4` (locked), `BigReadout#zero`.


## Second pass on a third set of five originals (2026-11-24)

| Component | What the frames showed | What changed |
|---|---|---|
| **ConditionPlate** | The plate sits in a blinding flare (frame 57) | Flare behind and over the plate, cut corners, hazard strip, live values |
| **GateSign** | A neon sign on a bolted plate; red when locked, green when unlocked (frames 68, 69) | Mounting plate and bolts, perspective, neon stutter, code entry before unlock |
| **SchematicCallout** | The map is hundreds of glowing pylons on a radial floor (frame 73) | About 170 pylons, trunk line with pulses, radial floor, left-edge system tabs |
| **BracketCaption** | Captions sit over a glass plug in ring gear (frames 9, 133) | Spectrum plug, green rings, sliding depth marker |
| **FrameChrome** | The slot holds the choker; an authority banner can cut across (frames 205, 210) | Turning tiled choker, Executive Authority state |

Pinned states for review: `GateSign#locked`, `FrameChrome#auth`, `SchematicCallout#t=2`.


## Second pass on the last four film components (2026-11-24)

| Component | What the frames showed | What changed |
|---|---|---|
| **HazardBand** | Big glowing chevrons that point at a boxed plate set into the band (frame 14) | 72px mirrored chevron bands with the plate inside, glowing red rules |
| **TitleCard** | The same KEEP OUT heading over changing lines (frames 144–149) | Three notices with hard cuts between them; the entry animation that hid the heading is gone |
| **MapRadar** | A tilted disc with an impact column and glowing dish (frame 113) | Redrawn on a canvas: tilted polar grid, column with motes, shock rings, zones, unit tracks, countdown |
| **IdCard** | Large rounded cards with bilingual fields, stacked, one still loading (frame 41) | Rebuilt at full size with bilingual fields, footer blocks, stacking, and searching and found states |

Pinned states for review: `TitleCard#n=2`, `MapRadar#t=3`, `IdCard#searching`, `IdCard#found`.

All 25 film components have now had this pass. The six basics (Button, Badge, Card, Dialog, StatusList, TextInput) have not.


## Second pass on the six basics (2026-11-24)

The basics were already in the Rebuild visual language. This pass added behaviour and variants that the films show.

| Component | Added | Source in the films |
|---|---|---|
| **Button** | Press flash, label plate, mode-key strip, guarded action with a hazard cover | Timer mode strip, decryption label plates |
| **Badge** | Hex cell, LIVE stack, file tab, zone chip, bracket title, hazard tag, MAGI state | HexWall, LiveFeed, simulation screens, ClockBoard |
| **TextInput** | Command line with prompt, six-cell personal code that checks itself | Gate sign's personal code |
| **Card** | Pale report sheets on a green lattice board, 状況終了 stamp | Status board, frame 116 |
| **StatusList** | Rows check in one at a time, summary line, cycle code | Console refresh behaviour |
| **Dialog** | MAGI three-way vote that unlocks the action, auto-cancel fuse | MAGI voting |

Pinned states for review: `Button#armed`, `TextInput#ok`, `Card#ended`, `StatusList#boot=3`, `Dialog#carried`, `Dialog#denied`.

Every component in the system has now had the second pass.
