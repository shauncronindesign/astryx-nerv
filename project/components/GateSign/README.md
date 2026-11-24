# GateSign

Physical signage: a glowing security-gate panel set into a bulkhead, and lit room-status plates on white walls.

**Gate panel** (frames 68–69):
- **Panel:** a black panel on a bolted metal mounting plate, set into a dark bulkhead and turned slightly in perspective. The plate picks up the neon's colour as a soft glow. A stencilled panel code (`CNT-7`) sits on the bulkhead.
- **Text:** a SECURITY LEVEL / PERSONAL CODE line and a SECURITY / NAME line, with a geometric diamond-and-leaf mark between them. The films show the NERV leaf here; this system uses no logos.
- **Name:** CENTRAL DOGMA, boxed, in `hardware` (Eurostile) 46px with a strong glow.
- **State line:** FINAL GATE / UNLOCKED.
- **Colours:** `--g` drives the whole sign. Unlocked uses `color-success` (lime in Tactical); `.locked` uses `alert-300`, and the separate EMERGENCY lamp lights.
- **Behaviour:** locking is instant. Unlocking is a short procedure: the personal code goes in one digit at a time, then security clears and the sign turns green. On every change the tubes stutter like neon striking. The toggle also swaps the state text, the SECURITY:OK / CHECK label and the lamp. Add `#locked` to pin the red state. Under `prefers-reduced-motion` the change is immediate, with no stutter or code entry. `role="status"` with `aria-live="polite"` announces the change.

**Room plate** (frames 105–107):
- **Plate:** a lit plate with clipped corners on a grey bulkhead. It carries the Japanese room name (`display` 900), an English line, a big status (使用中 In Use / 入室可 Entry Permitted) and a `signage` LEVEL-0n under it.
- **Colours:** red (`alert-400`, white ink) for in use or blocked; `.ok` (`sign-green`, dark ink) for complete or permitted.

**Consumer provides:** names, codes and the state.
