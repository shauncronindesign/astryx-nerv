#!/bin/bash
# Re-render every component preview to dist/figma-shots/<Name>.png (Tactical theme, trimmed)
# for the "Film components" page of the Figma companion. Run from the repo root.
set -e
cd "$(dirname "$0")/.."
python3 tools/preview.py >/dev/null
mkdir -p dist/figma-shots
for c in $(ls project/components | grep -v Cover); do
  "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --hide-scrollbars \
    --allow-file-access-from-files --virtual-time-budget=1500 --window-size=1060,1800 \
    --screenshot=dist/figma-shots/$c.png "file://$PWD/dist/preview/$c.html" 2>/dev/null
done
python3 - <<'PY'
from PIL import Image, ImageChops
import glob
for f in glob.glob('dist/figma-shots/*.png'):
    im = Image.open(f).convert('RGB')
    bg = Image.new('RGB', im.size, im.getpixel((im.width-1, im.height-1)))
    box = ImageChops.difference(im, bg).convert('L').point(lambda p: 255 if p > 12 else 0).getbbox()
    if box: im = im.crop((0, 0, im.width, min(im.height, box[3] + 32)))
    im.save(f, optimize=True)
PY
echo "rendered $(ls dist/figma-shots | wc -l | tr -d ' ') shots"
