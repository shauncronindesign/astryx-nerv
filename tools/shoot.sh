#!/bin/bash
# usage: tools/shoot.sh <Component> [tag] [height] [#hash]  -> dist/shots/<Component>-<tag>.png
# Headless virtual time does not advance requestAnimationFrame, so pin animated states with a #hash.
cd "$(dirname "$0")/.." && python3 tools/preview.py >/dev/null
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --hide-scrollbars --allow-file-access-from-files --virtual-time-budget=800 --window-size=1060,${3:-480} --screenshot=dist/shots/$1-${2:-1}.png "file://$PWD/dist/preview/$1.html$4" 2>/dev/null
