"""Emit figma/variables.js: a use_figma script that creates/updates the Astryx NERV
variable collections from project/tokens.json. Idempotent (matches by name).
Run: python3 figma/gen_variables.py"""
import json, os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
t = json.load(open(os.path.join(ROOT, "project", "tokens.json")))
themes = [th["id"] for th in t["color"]["themes"]]
names = [th["name"] for th in t["color"]["themes"]]
prims, roles = [], []
for tok in t["color"]["tokens"]:
    (prims if isinstance(tok["value"], str) else roles).append(tok)
def path(n):  # ground-void -> ground/void ; color-text-primary -> text/primary
    if n.startswith("color-"): n = n[6:]
    a, _, b = n.partition("-")
    return f"{a}/{b}" if b else a
P = [[path(x["name"]), x["name"], x["value"], x.get("usage", "")[:90]] for x in prims]
R = []
for x in roles:
    vals = []
    for th in themes:
        v = x["value"].get(th)
        if v is None: v = x["value"].get(themes[0])
        m = re.fullmatch(r"\{(.+)\}", v or "")
        vals.append(path(m.group(1)) if m else v)
    R.append([path(x["name"]), x["name"], vals, x.get("usage", "")[:90]])
def px(v): return float(str(v).replace("px", ""))
N = []
for fam, scope in [("spacing", ["GAP", "WIDTH_HEIGHT"]), ("radius", ["CORNER_RADIUS"]),
                   ("size", ["WIDTH_HEIGHT"]), ("border", ["STROKE_FLOAT"])]:
    for x in t[fam]["tokens"]:
        N.append([f"{fam}/{x['name']}", x["name"], px(x["value"]), scope, x.get("usage", "")[:90]])
for x in t["shape"]["tokens"]:
    if str(x["value"]).endswith("px"):
        N.append([f"shape/{x['name']}", x["name"], px(x["value"]), ["CORNER_RADIUS", "WIDTH_HEIGHT"], x.get("usage", "")[:90]])
def leafs(rows):
    names = {r[0] for r in rows}
    for r in rows:
        if any(n.startswith(r[0] + "/") for n in names): r[0] += "/default"
leafs(P); leafs(R); leafs(N)
data = {"modes": names, "P": P, "R": R, "N": N}
js = open(os.path.join(ROOT, "figma", "variables.template.js")).read().replace("__DATA__", json.dumps(data, ensure_ascii=False, separators=(",", ":")))
open(os.path.join(ROOT, "figma", "variables.js"), "w").write(js)
print(len(P), "primitives,", len(R), "roles,", len(N), "dimensions;", len(js), "bytes")
