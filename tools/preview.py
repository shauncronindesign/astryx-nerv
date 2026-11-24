"""Local preview harness: compiles project/tokens.json to tokens.css the way the
Design System page does, and wraps each components/<Comp>/preview.html so it can
be opened from disk. Output: dist/preview/<Comp>.html and dist/preview/index.html.
Run from Arrow/astryx-nerv: python3 tools/preview.py"""
import json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, "project")
OUT = os.path.join(ROOT, "dist", "preview")
os.makedirs(OUT, exist_ok=True)
t = json.load(open(os.path.join(P, "tokens.json")))

def cval(v):
    m = re.fullmatch(r"\{(.+)\}", v)
    return f"var(--{m.group(1)})" if m else v

themes = [th["id"] for th in t["color"]["themes"]]
blocks = {th: [] for th in themes}
for fam in ("color", "shadow"):
    for tok in t[fam]["tokens"]:
        v = tok["value"]
        if isinstance(v, str):
            blocks[themes[0]].append(f"--{tok['name']}: {cval(v)};")
        else:
            for th in themes:
                if th in v and v[th] is not None:
                    blocks[th].append(f"--{tok['name']}: {cval(v[th])};")
css = [":root, [data-theme=\"%s\"] { %s }" % (themes[0], " ".join(blocks[themes[0]]))]
for th in themes[1:]:
    css.append("[data-theme=\"%s\"] { %s }" % (th, " ".join(blocks[th])))
root = []
for fam, body in t.items():
    if fam in ("color", "shadow", "type") or not isinstance(body, dict) or "tokens" not in body:
        continue
    for tok in body["tokens"]:
        root.append(f"--{tok['name']}: {tok['value']};")
for k, v in t["type"]["families"].items():
    root.append(f"--font-{k}: {v};")
css.append(":root { %s }" % " ".join(root))
for f in t["type"]["fonts"]:
    css.append("@font-face { font-family: \"%s\"; src: url(\"../../project/%s\"); font-weight: %s; font-style: %s; }"
               % (f["family"], f["file"], f["weight"], f.get("style", "normal")))
open(os.path.join(OUT, "tokens.css"), "w").write("\n".join(css))

comps = sorted(d for d in os.listdir(os.path.join(P, "components"))
               if os.path.exists(os.path.join(P, "components", d, "preview.html")))
links = []
for c in comps:
    src = open(os.path.join(P, "components", c, "preview.html")).read()
    theme = sys.argv[1] if len(sys.argv) > 1 else themes[0]
    inline = "\n".join(l for l in css if not l.startswith("@font-face"))  # inlined: the pane opens files as snapshots
    src = src.replace("<head>", f"<head><style>{inline}</style>", 1)
    src = re.sub(r"<html[^>]*>", f'<html data-theme="{theme}">', src, count=1)
    open(os.path.join(OUT, f"{c}.html"), "w").write(src)
    links.append(f'<li><a href="{c}.html">{c}</a></li>')
open(os.path.join(OUT, "index.html"), "w").write("<ul>%s</ul>" % "".join(links))
print("wrote", len(comps), "previews to", OUT)
