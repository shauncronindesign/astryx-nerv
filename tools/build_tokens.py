"""Rebuild Astryx NERV tokens.json from tokens.base.json + colors sampled from the Rebuild frames.
Run: python3 tools/build_tokens.py  (from Arrow/astryx-nerv). Writes project/tokens.json and prints a contrast report."""
import json, re, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
base = json.load(open(os.path.join(HERE, "tokens.base.json")))

# ---------- primitives sampled from the films (frame numbers in usage) ----------
P = [
 # alert red — hex walls, EMERGENCY, CONDITION II
 ("alert-950", "#1c0204", "Deepest alert shade. Frame 45 timer ground."),
 ("alert-900", "#2a0306", "Alert-zone ground on dark themes."),
 ("alert-700", "#68222d", "Shade and dark type on red walls. Frame 31."),
 ("alert-600", "#8c1420", "Pressed / recessed red."),
 ("alert-500", "#a81c28", "Hex cell interior, red panels on a red wall."),
 ("alert-400", "#d32230", "THE alert red: MAGI hex wall ground. Frame 31, 52."),
 ("alert-300", "#e7323d", "EMERGENCY hexes, red banners. Frames W14, W17."),
 ("alert-200", "#f06a72", "Red hairlines on a red ground."),
 ("alert-100", "#ffd2cb", "Pale red ink on red."),
 # tactical — Tactical Mission Notification, AAAW, bracket captions
 ("tac-ground", "#1a0106", "Red-black ground of notification plates. Frame 244."),
 ("tac-panel", "#250308", "Plate fill one step up from the ground."),
 ("tac-lift", "#370704", "Popover / raised plate. Frame 244."),
 ("tac-rule", "#5a1a0c", "Dim orange-brown hairline."),
 ("tac-orange-700", "#8f221c", "Recessed orange; disabled ink."),
 ("tac-orange-600", "#c0391a", "Plate frame at rest."),
 ("tac-orange-500", "#e24319", "Orange mid tone. Frame 244."),
 ("tac-orange-400", "#fe7222", "Notification orange: titles, frames, the voice. Frames 151, 244."),
 ("tac-orange-200", "#ffa66a", "Light orange body copy."),
 ("tac-orange-100", "#ffd2ad", "Brightest orange ink, near the bloom core."),
 # gold / bloom — AAAW titles, glow cores
 ("gold-700", "#7d521e", "Dim gold rule. Frame 210."),
 ("gold-500", "#dcd849", "AAAW gold. Frame 205."),
 ("gold-300", "#f2e178", "AAAW title gold, readout digits. Frames 203, 205."),
 ("bloom-peach", "#f2ae7a", "Glow halo around orange type. Frame 73."),
 ("bloom-core", "#fde6c6", "Overexposed centre of glowing type. Frame 73."),
 ("bloom-cream", "#fff5e6", "Blown-out condition plate. Frame 57."),
 # clock amber
 ("clock-ground", "#0c0500", "Brown-black clock board ground. Frame 64."),
 ("clock-panel", "#1b0b01", "Clock panel fill."),
 ("clock-lift", "#291305", "Clock popover."),
 ("clock-rule", "#411c06", "Clock hairline."),
 ("clock-amber", "#ed8d25", "7-seg clock amber. Frame 64."),
 # hazard
 ("hazard-yellow", "#fbbd3d", "Chevron yellow. Frame 14."),
 ("hazard-red", "#e22f2f", "Red chevron band. Frame 14."),
 ("hazard-black", "#120806", "Chevron black."),
 # greens
 ("mint-900", "#04120c", "Green-black ground of the sync columns. Frame 11."),
 ("mint-800", "#072018", "Nominal panel."),
 ("mint-700", "#0c2e22", "Nominal popover."),
 ("mint-600", "#12402e", "Nominal hairline."),
 ("mint-500", "#2e8a66", "Nominal emphasized hairline."),
 ("mint-400", "#2beeae", "Sync slat mint. Frames 11, 46, W7."),
 ("mint-300", "#2df5b5", "Brightest sync mint."),
 ("mint-100", "#c8fbe9", "Pale mint ink."),
 ("lime-500", "#a3c92d", "Gate sign green. Frame 68."),
 ("lime-300", "#e0e835", "CENTRAL DOGMA / UNLOCKED glow. Frame 68."),
 ("aaaw-green", "#b1f34d", "AAAW vertical side label. Frame 205."),
 ("sign-green", "#1ab129", "Decontamination sign green. Frame 107."),
 # pattern spectrum
 ("pattern-ground", "#060426", "Violet-black ground. Frame 16."),
 ("pattern-panel", "#0d093e", "Pattern panel. Frame 16."),
 ("pattern-lift", "#1e0d50", "Pattern popover. Frame 16."),
 ("pattern-rule", "#2e1071", "Pattern hairline. Frame 16."),
 ("violet-500", "#841ad0", "Pattern violet. Frame 16."),
 ("violet-300", "#a45cf0", "Light violet, 3:1 hairline on pattern ground."),
 ("magenta-500", "#d21a9f", "A.T. field magenta. Frame 19."),
 ("fuchsia-400", "#e01ccb", "Fuchsia, brightest violet-pink. Frame 16."),
 ("pink-300", "#f058a9", "Plug schematic pink. Frame 133."),
 ("pink-100", "#f9aac2", "Pale pink. Frame 133."),
 ("cyan-700", "#145e75", "Deep plug cyan. Frame 47."),
 ("cyan-400", "#54d8fc", "Plug cyan. Frame 133."),
 ("cyan-200", "#6eedfd", "Brightest cyan. Frame 133."),
 # wunder
 ("wunder-ground", "#0a0a17", "Indigo-black of the Wunder bridge. Frame 178."),
 ("wunder-panel", "#130c21", "Wunder panel. Frame 178."),
 ("wunder-lift", "#1f1533", "Wunder popover."),
 ("wunder-haze", "#2b1e45", "Atmospheric haze, hairlines. Frame 178."),
 ("wunder-red", "#be2724", "Ring red. Frame 178."),
 ("wunder-red-bright", "#f0574f", "Ring red as text."),
 # activity timer
 ("timer-navy", "#090f20", "Timer panel ground. Frame 25."),
 ("timer-indigo", "#212457", "Timer panel shade. Frame 25."),
 ("timer-blue", "#416ab1", "EXTERNAL tab blue. Frame 25."),
 ("timer-blue-light", "#7d9cd0", "Timer tab highlight. Frame 25."),
 ("timer-violet", "#9052b1", "Timer gradient middle. Frame 25."),
 ("timer-mauve", "#c75c88", "Timer gradient start. Frame 25."),
 ("timer-red", "#de2550", "7-seg digits on the timer. Frame 25."),
 # system blue (hex-wall side panels)
 ("sysblue-500", "#3a6cad", "Hex-wall side panel blue. Frame 31."),
 ("sysblue-300", "#54a8e8", "Light system blue. Frame 31."),
 # --- 2026-11-23 video pass: Asuka, New Spear, System Unlocked, The plan, The spears, New Eva Parts ---
 # decryption key / pattern scope (orange on black)
 ("decrypt-ground", "#0d0602", "Brown-black ground of the Decryption Key panel. System Unlocked."),
 ("decrypt-panel", "#221206", "Decryption panel fill and dim histogram cells."),
 ("decrypt-rule", "#6d3e1b", "Decryption grid lines and bar outlines."),
 ("decrypt-orange", "#e48430", "Decryption bars, cluster plates, the big 98%. System Unlocked."),
 ("scope-orange", "#f08430", "Glowing waveform on the pattern simulation scope. The spears."),
 ("scope-ember", "#903c18", "Waveform halo and SEC tick labels. The spears."),
 # schematic paper (structural diagram)
 ("paper-50", "#eeebe2", "Brightest schematic paper; popovers. New Spear."),
 ("paper-100", "#e0ddd1", "Schematic paper ground. New Spear."),
 ("paper-200", "#c6c2bc", "Paper shade, grid and hairlines. New Spear."),
 ("paper-400", "#a4866c", "Warm grey-brown line art. New Spear."),
 ("rust-900", "#2a1810", "Darkest rust ink: body type on paper."),
 ("rust-700", "#482c1e", "Deep rust line art. New Spear."),
 ("rust-500", "#7b4627", "Rust fill of the linkage segments. New Spear."),
 ("rust-400", "#9c5424", "Rust label shade. New Spear."),
 ("label-orange", "#f09c48", "Vertical label plate on the structural diagram. New Spear."),
 # simulation grid / visualized simulation
 ("sim-ground", "#0d0d10", "Simulation multi-cam ground. Asuka."),
 ("sim-grid", "#25262d", "Perspective floor grid. Asuka."),
 ("sim-wire", "#3c8490", "Wireframe cyan-teal. Asuka."),
 ("sim-wire-bright", "#48d8d8", "Lit wireframe edges. Asuka, The plan."),
 ("sim-core", "#f08a30", "Orange core sphere inside the wireframe (eyeballed from Asuka)."),
 ("sim-violet", "#4a50c8", "Blue-violet weapon parts in the simulation (eyeballed from Asuka)."),
 ("field-navy", "#101a28", "Visualized Simulation ground. The plan."),
 ("field-blue", "#306084", "Deep field lines. The plan."),
 ("field-teal", "#3cb4c0", "Field-line teal. The plan."),
 ("field-gold", "#e8c070", "Warm field lines (eyeballed from The plan)."),
 ("field-lime", "#9ccc3c", "Green vertical side bar, 'Visualized Simulation File'. The plan."),
 # pink blueprint (Mari's parts list)
 ("blush-paper", "#eef3e8", "Greenish white of the parts blueprint. New Eva Parts."),
 ("blush-300", "#e490a8", "Pink line-art. New Eva Parts."),
 ("blush-500", "#db708e", "Dense pink line-art and labels. New Eva Parts."),
 # german timer (EVA-02 internal power)
 ("de-plum", "#341b19", "Timer housing shade. Asuka."),
 ("de-brick", "#6c2418", "INTERN / Hauptenergie panel brick. Asuka."),
 ("de-amber", "#c8963c", "7-seg digits on the German timer (sampled #9c6c3c through haze, lifted)."),
 ("de-red", "#c8302a", "SCHNELL button red (eyeballed). Asuka."),
]


THEMES = [("tactical","Tactical"),("alert","Alert"),("clock","Clock"),("pattern","Pattern"),
          ("nominal","Nominal"),("wunder","Wunder"),("schematic","Schematic"),("terminal","Terminal")]

# ---------- role values per new theme (clock = old rebuild with overrides) ----------
def a(hexv, alpha):  # hex + alpha byte
    return hexv + "%02x" % round(alpha*255)

R = {}
R["tactical"] = {
 "color-accent":"{tac-orange-400}","color-accent-muted":a("#fe7222",.2),"color-on-accent":"{tac-ground}",
 "color-neutral":a("#fe7222",.12),"color-background-body":"{tac-ground}","color-background-surface":"{tac-panel}",
 "color-background-card":"{tac-panel}","color-background-popover":"{tac-lift}","color-background-muted":a("#fe7222",.06),
 "color-background-inverted":"{bloom-core}","color-background-error-inverted":"{alert-400}",
 "color-background-alert":"{alert-900}","color-background-system":"#0a1530",
 "color-overlay":"#0a0003cc","color-overlay-hover":a("#fe7222",.08),"color-overlay-pressed":a("#fe7222",.16),
 "color-text-primary":"{tac-orange-100}","color-text-secondary":"{tac-orange-200}","color-text-tertiary":"{tac-orange-400}",
 "color-text-disabled":"{tac-orange-700}","color-text-accent":"{tac-orange-400}","color-text-ghost":"#3a0a08",
 "color-on-dark":"{bloom-core}","color-on-light":"{tac-ground}",
 "color-icon-accent":"{tac-orange-400}","color-icon-primary":"{tac-orange-100}","color-icon-secondary":"{tac-orange-500}","color-icon-disabled":"{tac-orange-700}",
 "color-success":"{aaaw-green}","color-success-muted":a("#b1f34d",.15),"color-on-success":"{tac-ground}",
 "color-error":"#ff4f4f","color-error-muted":a("#d32230",.25),"color-on-error":"#ffffff",
 "color-warning":"{gold-300}","color-warning-muted":a("#f2e178",.15),"color-on-warning":"{tac-ground}",
 "color-info":"{sysblue-300}","color-info-fill":"{sysblue-500}","color-on-info":"#ffffff",
 "color-border":"{tac-rule}","color-border-emphasized":"{tac-orange-600}","color-border-accent":"{tac-orange-400}","color-border-alert":"{alert-300}",
 "color-skeleton":"{tac-lift}","color-track":"{tac-rule}","color-shadow":a("#fe7222",.4),"color-tint-hover":"{tac-orange-400}","color-scanline":"#00000026",
}
R["alert"] = {
 "color-accent":"#ffffff","color-accent-muted":"#ffffff33","color-on-accent":"{alert-700}",
 "color-neutral":"#00000026","color-background-body":"{alert-400}","color-background-surface":"{alert-500}",
 "color-background-card":"{alert-500}","color-background-popover":"{alert-700}","color-background-muted":"#0000001a",
 "color-background-inverted":"#ffffff","color-background-error-inverted":"{hazard-black}",
 "color-background-alert":"{alert-600}","color-background-system":"{sysblue-500}",
 "color-overlay":"#2a0306cc","color-overlay-hover":"#ffffff1a","color-overlay-pressed":"#00000033",
 "color-text-primary":"#ffffff","color-text-secondary":"#fff5f3","color-text-tertiary":"#fff0ed",
 "color-text-disabled":"{alert-200}","color-text-accent":"#fff6d6","color-text-ghost":"#dc3542",
 "color-on-dark":"#ffffff","color-on-light":"{alert-700}",
 "color-icon-accent":"#ffffff","color-icon-primary":"#ffffff","color-icon-secondary":"{alert-100}","color-icon-disabled":"{alert-200}",
 "color-success":"#e2fff4","color-success-muted":"#ffffff1f","color-on-success":"{alert-700}",
 "color-error":"#ffffff","color-error-muted":"#00000033","color-on-error":"#ffffff",
 "color-warning":"#fff3cf","color-warning-muted":a("#fbbd3d",.25),"color-on-warning":"{hazard-black}",
 "color-info":"#eef5ff","color-info-fill":"{sysblue-500}","color-on-info":"#ffffff",
 "color-border":"{alert-200}","color-border-emphasized":"#ffc0c0","color-border-accent":"#ffffff","color-border-alert":"{hazard-yellow}",
 "color-skeleton":"{alert-500}","color-track":"{alert-600}","color-shadow":"#ffffff40","color-tint-hover":"#ffffff","color-scanline":"#0000001a",
}
R["pattern"] = {
 "color-accent":"{magenta-500}","color-accent-muted":a("#d21a9f",.25),"color-on-accent":"#ffffff",
 "color-neutral":a("#a45cf0",.14),"color-background-body":"{pattern-ground}","color-background-surface":"{pattern-panel}",
 "color-background-card":"{pattern-panel}","color-background-popover":"{pattern-lift}","color-background-muted":a("#a45cf0",.06),
 "color-background-inverted":"#f4ecff","color-background-error-inverted":"#c4123e",
 "color-background-alert":"#3a0626","color-background-system":"#0a0440",
 "color-overlay":"#03021acc","color-overlay-hover":a("#e01ccb",.1),"color-overlay-pressed":a("#e01ccb",.18),
 "color-text-primary":"#f4ecff","color-text-secondary":"{pink-100}","color-text-tertiary":"#b9a6f0",
 "color-text-disabled":"#5a3f99","color-text-accent":"{pink-300}","color-text-ghost":"#1b0f55",
 "color-on-dark":"#f4ecff","color-on-light":"{pattern-ground}",
 "color-icon-accent":"{fuchsia-400}","color-icon-primary":"#f4ecff","color-icon-secondary":"{violet-300}","color-icon-disabled":"#5a3f99",
 "color-success":"{mint-300}","color-success-muted":a("#2df5b5",.15),"color-on-success":"{pattern-ground}",
 "color-error":"#ff5c7a","color-error-muted":a("#ff5c7a",.2),"color-on-error":"#ffffff",
 "color-warning":"{gold-300}","color-warning-muted":a("#f2e178",.15),"color-on-warning":"{pattern-ground}",
 "color-info":"{cyan-400}","color-info-fill":"{cyan-700}","color-on-info":"#ffffff",
 "color-border":"{pattern-rule}","color-border-emphasized":"{violet-300}","color-border-accent":"{fuchsia-400}","color-border-alert":"#ff5c7a",
 "color-skeleton":"{pattern-lift}","color-track":"{pattern-rule}","color-shadow":a("#e01ccb",.45),"color-tint-hover":"{fuchsia-400}","color-scanline":"#0000001f",
}
R["nominal"] = {
 "color-accent":"{mint-400}","color-accent-muted":a("#2beeae",.2),"color-on-accent":"{mint-900}",
 "color-neutral":a("#2beeae",.12),"color-background-body":"{mint-900}","color-background-surface":"{mint-800}",
 "color-background-card":"{mint-800}","color-background-popover":"{mint-700}","color-background-muted":a("#2beeae",.06),
 "color-background-inverted":"{mint-100}","color-background-error-inverted":"{alert-400}",
 "color-background-alert":"{alert-900}","color-background-system":"#04203a",
 "color-overlay":"#010805cc","color-overlay-hover":a("#2beeae",.08),"color-overlay-pressed":a("#2beeae",.16),
 "color-text-primary":"{mint-100}","color-text-secondary":"#8ff0cc","color-text-tertiary":"#5cc9a0",
 "color-text-disabled":"#2a6a52","color-text-accent":"{mint-300}","color-text-ghost":"#0c2a1e",
 "color-on-dark":"{mint-100}","color-on-light":"{mint-900}",
 "color-icon-accent":"{mint-400}","color-icon-primary":"{mint-100}","color-icon-secondary":"#5cc9a0","color-icon-disabled":"#2a6a52",
 "color-success":"{lime-300}","color-success-muted":a("#e0e835",.15),"color-on-success":"{mint-900}",
 "color-error":"#ff5a4a","color-error-muted":a("#ff5a4a",.2),"color-on-error":"#ffffff",
 "color-warning":"{gold-300}","color-warning-muted":a("#f2e178",.15),"color-on-warning":"{mint-900}",
 "color-info":"{cyan-400}","color-info-fill":"{cyan-700}","color-on-info":"#ffffff",
 "color-border":"{mint-600}","color-border-emphasized":"{mint-500}","color-border-accent":"{mint-400}","color-border-alert":"#ff5a4a",
 "color-skeleton":"{mint-700}","color-track":"{mint-600}","color-shadow":a("#2beeae",.4),"color-tint-hover":"{mint-400}","color-scanline":"#0000001f",
}
R["wunder"] = {
 "color-accent":"{wunder-red}","color-accent-muted":a("#be2724",.25),"color-on-accent":"#ffffff",
 "color-neutral":a("#b9afd0",.1),"color-background-body":"{wunder-ground}","color-background-surface":"{wunder-panel}",
 "color-background-card":"{wunder-panel}","color-background-popover":"{wunder-lift}","color-background-muted":a("#b9afd0",.05),
 "color-background-inverted":"#ece6f5","color-background-error-inverted":"{wunder-red}",
 "color-background-alert":"#2a0612","color-background-system":"#0c1838",
 "color-overlay":"#05050ccc","color-overlay-hover":a("#f0574f",.08),"color-overlay-pressed":a("#f0574f",.16),
 "color-text-primary":"#ece6f5","color-text-secondary":"#b9afd0","color-text-tertiary":"#9a8fb8",
 "color-text-disabled":"#4e4468","color-text-accent":"{wunder-red-bright}","color-text-ghost":"#1d1630",
 "color-on-dark":"#ece6f5","color-on-light":"{wunder-ground}",
 "color-icon-accent":"{wunder-red-bright}","color-icon-primary":"#ece6f5","color-icon-secondary":"#9a8fb8","color-icon-disabled":"#4e4468",
 "color-success":"#3fe08a","color-success-muted":a("#3fe08a",.15),"color-on-success":"{wunder-ground}",
 "color-error":"#ff5a50","color-error-muted":a("#ff5a50",.2),"color-on-error":"#ffffff",
 "color-warning":"#f2c24c","color-warning-muted":a("#f2c24c",.15),"color-on-warning":"{wunder-ground}",
 "color-info":"{blue-wille}","color-info-fill":"{sysblue-500}","color-on-info":"#ffffff",
 "color-border":"{wunder-haze}","color-border-emphasized":"#7a6aa2","color-border-accent":"{wunder-red-bright}","color-border-alert":"{wunder-red-bright}",
 "color-skeleton":"{wunder-lift}","color-track":"{wunder-haze}","color-shadow":a("#be2724",.45),"color-tint-hover":"{wunder-red-bright}","color-scanline":"#00000026",
}
R["schematic"] = {  # light: paper structural diagrams (New Spear)
 "color-accent":"{label-orange}","color-accent-muted":a("#f09c48",.25),"color-on-accent":"{rust-900}",
 "color-neutral":a("#7b4627",.1),"color-background-body":"{paper-100}","color-background-surface":"{paper-50}",
 "color-background-card":"{paper-50}","color-background-popover":"{paper-50}","color-background-muted":a("#7b4627",.05),
 "color-background-inverted":"{rust-900}","color-background-error-inverted":"{alert-500}",
 "color-background-alert":"#f3d3c8","color-background-system":"#d6e0e6",
 "color-overlay":"#2a1810b3","color-overlay-hover":a("#7b4627",.08),"color-overlay-pressed":a("#7b4627",.16),
 "color-text-primary":"{rust-900}","color-text-secondary":"{rust-700}","color-text-tertiary":"#6b4a36",
 "color-text-disabled":"#a49a8c","color-text-accent":"{rust-500}","color-text-ghost":"#d2cec2",
 "color-on-dark":"{paper-50}","color-on-light":"{rust-900}",
 "color-icon-accent":"{rust-500}","color-icon-primary":"{rust-900}","color-icon-secondary":"{rust-400}","color-icon-disabled":"#a49a8c",
 "color-success":"#3a6410","color-success-muted":a("#3a6410",.14),"color-on-success":"#ffffff",
 "color-error":"#a81c28","color-error-muted":a("#a81c28",.14),"color-on-error":"#ffffff",
 "color-warning":"#7a5000","color-warning-muted":a("#c98a10",.18),"color-on-warning":"#ffffff",
 "color-info":"#1d5a80","color-info-fill":"#1d5a80","color-on-info":"#ffffff",
 "color-border":"{paper-200}","color-border-emphasized":"{rust-400}","color-border-accent":"{rust-500}","color-border-alert":"{alert-500}",
 "color-skeleton":"{paper-200}","color-track":"{paper-200}","color-shadow":a("#7b4627",.25),"color-tint-hover":"{rust-500}","color-scanline":"#0000000d",
}
R["clock"] = {  # old rebuild theme, re-grounded on the clock board
 "color-accent":"{clock-amber}","color-on-accent":"{clock-ground}","color-background-body":"{clock-ground}",
 "color-background-surface":"{clock-panel}","color-background-card":"{clock-panel}","color-background-popover":"{clock-lift}",
 "color-text-accent":"{clock-amber}","color-icon-accent":"{clock-amber}","color-border":"{clock-rule}","color-border-accent":"{clock-amber}",
 "color-on-success":"{clock-ground}","color-on-warning":"{clock-ground}","color-skeleton":"{clock-lift}","color-track":"{clock-rule}",
 "color-text-primary":"{bloom-core}","color-text-secondary":"{amber-bright}","color-background-inverted":"{bloom-cream}",
}

# categorical hues: new families + how each theme renders them
NEWCAT = {  # name: (hue, light text, border, usage)
 "magenta": ("#d21a9f", "#f6a6dc", "#7a1060", "A.T. field / pattern analysis"),
 "violet":  ("#a45cf0", "#d4b8ff", "#4d0a97", "Pattern violet / spectrum"),
 "cyan":    ("#54d8fc", "#a8f0ff", "#145e75", "Plug interior / schematic"),
 "mint":    ("#2beeae", "#a6f8dc", "#0f6a4c", "Sync / harmonics"),
 "gold":    ("#dcd849", "#f2e9a0", "#7d521e", "AAAW / readout"),
}
CATS = ["amber","red","green","blue","wille","indigo","ochre","gray"] + list(NEWCAT)

# ---------- assemble ----------
out = json.loads(json.dumps(base))
out["color"]["themes"] = [{"id":i,"name":n} for i,n in THEMES]
old = base["color"]["tokens"]
prim_names = {p[0] for p in P}
tokens = []
def theme_map(v):
    if isinstance(v, str): return {"rebuild": v}
    return dict(v)
for t in old:
    v = theme_map(t["value"]); reb = v.get("rebuild"); term = v.get("terminal", reb)
    name = t["name"]
    if not name.startswith("color-"):     # primitive: same everywhere
        tokens.append({"name":name,"value":reb,"usage":t.get("usage","")}); continue
    nv = {}
    for tid,_ in THEMES:
        if tid == "terminal": nv[tid] = term
        elif tid == "clock": nv[tid] = R["clock"].get(name, reb)
        else: nv[tid] = R[tid].get(name)
    tokens.append({"name":name,"value":nv,"usage":t.get("usage","")})
# insert new primitives after the old primitives
idx = next(i for i,t in enumerate(tokens) if t["name"].startswith("color-"))
tokens[idx:idx] = [{"name":n,"value":v,"usage":u} for n,v,u in P]

# categorical: fill new themes for old hues; add new hues
def cat_vals(hue, text, border, kind, tid):
    if tid == "schematic":
        return {"background":a(hue,.18),"border":border,"icon":border,"text":"{rust-900}"}[kind]
    if tid == "alert":
        return {"background":"#00000033","border":"#ffffff59","icon":"#ffffff","text":"#ffffff"}[kind]
    return {"background":a(hue,.15),"border":border,"icon":hue,"text":text}[kind]
for t in tokens:
    m = re.match(r"color-(background|border|icon|text)-(%s)$" % "|".join(CATS[:8]), t["name"])
    if not m: continue
    kind, hue = m.groups()
    for tid in ("tactical","pattern","nominal","wunder"):
        if t["value"].get(tid) is None:
            t["value"][tid] = t["value"]["clock"]
    if hue == "indigo" and kind == "text":
        t["value"]["nominal"] = "#b8b8ee"
    if t["value"].get("alert") is None:
        t["value"]["alert"] = cat_vals(None,None,None,kind,"alert")
for hue in CATS[:8]:  # schematic: derive from the clock icon hue
    ic = next(t for t in tokens if t["name"] == f"color-icon-{hue}")["value"]["clock"]
    bd = next(t for t in tokens if t["name"] == f"color-border-{hue}")["value"]["clock"]
    for kind in ("background","border","icon","text"):
        t = next(t for t in tokens if t["name"] == f"color-{kind}-{hue}")
        hx = ic
        while hx.startswith("{"): hx = next(x for x in tokens if x["name"] == hx[1:-1])["value"]
        hx = hx if isinstance(hx, str) else "#888888"
        t["value"]["schematic"] = {"background":a(hx[:7],.18),"border":bd,"icon":ic,"text":"{rust-900}"}[kind]
for hue,(h,txt,bd,use) in NEWCAT.items():
    for kind in ("background","border","icon","text"):
        val = {tid: cat_vals(h,txt,bd,kind,tid) for tid,_ in THEMES}
        tokens.append({"name":f"color-{kind}-{hue}","value":val,"usage":f"{kind.title()} for {hue} categorical tags — {use}. Rebuild-only family."})

# new roles
def role(name, vals, usage): tokens.append({"name":name,"value":vals,"usage":usage})
allt = lambda v: {tid: v for tid,_ in THEMES}
role("color-hazard", allt("{hazard-yellow}"), "Hazard chevron fill — 45° bands around EMERGENCY and READY / OUT OF RANGE tags. Frame 14.")
role("color-hazard-alt", allt("{hazard-black}"), "Second stripe of the chevron band.")
role("color-on-hazard", allt("{hazard-black}"), "Type set on a hazard-yellow fill.")
role("color-bloom", {"tactical":"{bloom-peach}","alert":"#ffffff","clock":"{bloom-peach}","pattern":"{pink-100}","nominal":"{mint-100}","wunder":"#ff8a80","schematic":"{label-orange}","terminal":"{signal-100}"},
     "Glow-core tint: the halo colour behind bright type and rules.")
role("color-spectrum-start", allt("{magenta-500}"), "A.T. field / plug spectrum gradient, first stop. Frames 9, 19.")
role("color-spectrum-mid", allt("{tac-orange-400}"), "Spectrum gradient, middle stop. Frame 19.")
role("color-spectrum-end", allt("{cyan-400}"), "Spectrum gradient, last stop. Frame 9.")
role("color-timer-start", allt("{timer-mauve}"), "Activity-timer panel gradient, left. Frame 25.")
role("color-timer-mid", allt("{timer-violet}"), "Activity-timer gradient, middle.")
role("color-timer-end", allt("{timer-blue}"), "Activity-timer gradient, right / EXTERNAL tab.")
role("color-timer-digit", allt("{timer-red}"), "7-segment digits on the activity timer.")
role("color-scope", allt("{scope-orange}"), "Glowing waveform trace on pattern-simulation scopes. The spears.")
role("color-scope-halo", allt("{scope-ember}"), "Halo and tick labels around a scope trace.")
role("color-wireframe", allt("{sim-wire-bright}"), "Lit wireframe edges in simulation views. Asuka, The plan.")
role("color-wireframe-dim", allt("{sim-wire}"), "Back edges and secondary wireframe.")
role("color-wireframe-core", allt("{sim-core}"), "Orange core sphere / target inside a wireframe.")
role("color-label-plate", allt("{label-orange}"), "Solid orange label plate (vertical titles, MATCHES, cluster tabs). New Spear, System Unlocked.")
role("color-on-label-plate", allt("{rust-900}"), "Type on a label plate.")
out["color"]["tokens"] = tokens

# shadows: per theme glow, plus bloom (valid as text-shadow too)
GLOW = {"tactical":"254,114,34","alert":"255,255,255","clock":"237,141,37","pattern":"224,28,203","nominal":"43,238,174","wunder":"240,87,79","schematic":"240,156,72"}
for s in out["shadow"]["tokens"]:
    v = dict(s["value"]); reb = v.pop("rebuild")
    nv = {}
    for tid,_ in THEMES:
        if tid == "terminal": nv[tid] = v["terminal"]
        else: nv[tid] = re.sub(r"rgba\(224,144,48", "rgba(%s" % GLOW[tid], reb)
    s["value"] = nv
out["shadow"]["tokens"] += [
 {"name":"shadow-bloom","value":{tid:("0 0 2px rgba(%s,0.9), 0 0 10px rgba(%s,0.55)" % (GLOW.get(tid,"240,112,32"),GLOW.get(tid,"240,112,32"))) for tid,_ in THEMES},
  "usage":"Glow on bright type and rules — use as text-shadow or box-shadow. In the films nearly everything bright blooms; this is the default for titles, readouts and frames."},
 {"name":"shadow-bloom-strong","value":{tid:("0 0 3px rgba(%s,1), 0 0 14px rgba(%s,0.7), 0 0 40px rgba(%s,0.35)" % ((GLOW.get(tid,"240,112,32"),)*3)) for tid,_ in THEMES},
  "usage":"Big titles and 7-seg readouts: KEEP OUT, Blood Type : BLUE, the activity timer."},
]
# shape family: chamfers, slants, hazard pitch
out["shape"] = {"note":"Panels in the films are cut, slanted or hexagonal, not rounded. Use chamfers via clip-path polygons.","tokens":[
 {"name":"chamfer-sm","value":"6px","usage":"Clipped corner on chips, LIVE / ONLINE tags."},
 {"name":"chamfer-md","value":"12px","usage":"Clipped corner on plates and clock boards. Frame 64."},
 {"name":"chamfer-lg","value":"24px","usage":"Clipped corner on hex-wall title plates. Frame 31."},
 {"name":"slant-plate","value":"-8deg","usage":"Skew for Tactical Mission Notification plates. Frame 244."},
 {"name":"slant-tag","value":"-30deg","usage":"Angled READY / OUT OF RANGE tags. Frames 213-215."},
 {"name":"hazard-angle","value":"45deg","usage":"Chevron stripe angle. Frame 14."},
 {"name":"hazard-pitch","value":"24px","usage":"Width of one chevron stripe pair."},
 {"name":"hex-ratio","value":"1.1547","usage":"Hex cell width / height (2/sqrt 3) for flat-top hex walls."},
]}
out["meta"]["themesFrom"] = "Rebuild UI frames scan 2026-11-23 (see rebuild-ui-reference.md); old 'rebuild' theme became 'clock'"
json.dump(out, open(os.path.join(HERE, "..", "project", "tokens.json"), "w"), indent=2, ensure_ascii=False)

# ---------- contrast report ----------
vals = {t["name"]: t["value"] for t in tokens}
def resolve(name, tid, depth=0):
    v = vals[name]; v = v if isinstance(v, str) else v[tid]
    m = re.fullmatch(r"\{(.+)\}", v)
    return resolve(m.group(1), tid, depth+1) if m else v
def rgba(h):
    h = h.lstrip("#"); 
    if len(h)==3: h="".join(c*2 for c in h)
    r,g,b = (int(h[i:i+2],16)/255 for i in (0,2,4)); al = int(h[6:8],16)/255 if len(h)==8 else 1
    return r,g,b,al
def over(fg,bg):
    r,g,b,al = fg; R_,G,B,_ = bg; return (r*al+R_*(1-al), g*al+G*(1-al), b*al+B*(1-al), 1)
def lum(c):
    f = lambda x: x/12.92 if x<=0.03928 else ((x+0.055)/1.055)**2.4
    return 0.2126*f(c[0])+0.7152*f(c[1])+0.0722*f(c[2])
def cr(a_,b_):
    l1,l2 = sorted([lum(a_),lum(b_)], reverse=True); return (l1+0.05)/(l2+0.05)
fails = []
for tid,_ in THEMES:
    grounds = {g: rgba(resolve(g,tid)) for g in ["color-background-body","color-background-surface","color-background-popover"]}
    text = ["color-text-primary","color-text-secondary","color-text-tertiary","color-text-accent","color-success","color-error","color-warning","color-info"]
    for g,gv in grounds.items():
        for t in text:
            c = cr(over(rgba(resolve(t,tid)),gv), gv)
            if c < 4.5: fails.append((tid,t,g,round(c,2)))
        for t in ["color-border-emphasized","color-border-accent","color-icon-secondary"]:
            c = cr(over(rgba(resolve(t,tid)),gv), gv)
            if c < 3: fails.append((tid,t,g,round(c,2)))
        for hue in CATS:
            bg = over(rgba(resolve(f"color-background-{hue}",tid)), gv)
            c = cr(over(rgba(resolve(f"color-text-{hue}",tid)),bg), bg)
            if c < 4.5: fails.append((tid,f"text-{hue} on its tag",g,round(c,2)))
    for fill,on in [("color-accent","color-on-accent"),("color-success","color-on-success"),("color-warning","color-on-warning"),
                    ("color-background-error-inverted","color-on-error"),("color-info-fill","color-on-info"),("color-hazard","color-on-hazard")]:
        f = over(rgba(resolve(fill,tid)), grounds["color-background-body"]); c = cr(rgba(resolve(on,tid)), f)
        if c < 4.5: fails.append((tid,on,fill,round(c,2)))
print(len(tokens), "color tokens;", len(fails), "contrast failures")
for f in fails: print("  ", *f)
