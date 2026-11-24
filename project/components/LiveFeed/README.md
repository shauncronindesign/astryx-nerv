# LiveFeed

Monitored-object video tiles: a centred `Monitored Object:` header with the object name in drawn pipes, a pilot and vitals block bottom-left, and a LIVE box with an ONLINE chip bottom-right. Tiles sit edge to edge, split by glowing orange rules.

**Theme:** Clock (frames 50, 120, 121). The video is warm-graded, and the type over it is near-white (`#f4eee4`) so it reads on any footage.

**Anatomy:**
- **`.media`:** put a `<video>` or `<img>` inside; it's covered with `object-fit: cover` and a scanline overlay.
- **Stand-in picture:** the preview draws a pilot in the plug seat so the tile isn't empty. It's dimmed and vignetted to sit under the type, with slow breathing and bubbles rising through the LCL. Replace it with real media.
- **Timecode:** a `mono` running timecode at the right edge.
- **Vitals strip:** a heartbeat trace in `color-text-accent` scrolling above the footer. Each tile has its own rate.
- **`.ticks`:** small tick marks on both edges at 40% and 70%.
- **`.hd`:** `Monitored Object:` 11px, then the name at 22px between drawn square brackets, then a tiny sub-code.
- **`.who`:** the pilot line, then vitals lines with a left rule.
- **`.live`:** LIVE boxed in `color-text-accent` with bloom (pulses in steps), an ONLINE chip, and a `mono` source code in `color-error`.
- **`.lost`:** replaces the picture with live static and a red `NO SIGNAL`, flat-lines the vitals strip in red, and turns LIVE and the chip red (OFFLINE).

**Motion:** under `prefers-reduced-motion` the trace, static, breathing and bubbles all hold still.

**Consumer provides:** the media, the object name, the pilot and vitals lines, and the online state. Give each tile an `aria-label` with its state, and captions or a transcript for any audio.
