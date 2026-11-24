# Dialog

A modal plate over the `color-overlay` scrim, built like a Tactical Mission Notification: a blinking kicker, a big glowing title with a rule, the body, and an action row.

**When to use:** a decision that must block the screen, such as confirming an abort, accepting a MAGI verdict or acknowledging an alert.

**Props** (Astryx contract): `variant` `"standard" | "fullscreen"`, `width`.

**Structure:**
- **Plate:** clipped on two corners with `chamfer-lg`. The frame is `--ink` (`color-border-accent`) and the fill is `color-background-popover`, with a faint inward glow.
- **Kicker:** a blinking `■` and a line such as `Confirmation Required`, 11px 700.
- **Title:** 32px 700 with `compress-mild`, in `--ink` with `shadow-bloom-strong`, then a 3px rule.
- **Body:** 14px 700 in `color-text-secondary`.
- **Action row:** a `mono` code line on the left, then `Button`s on the right: a ghost `| CANCEL |` and the confirm action.

**Alert variant** (`role="alertdialog"`): `--ink` becomes `color-error`, a hazard band runs along the top edge, and the confirm action is `destructive`. Never use it for routine confirmations.

**What the consumer provides:** the kicker, title and body, and explicit confirm/cancel actions that lead to a clear next state. Set `aria-modal`, label the dialog with its title and, for alerts, describe it with the body. Return focus to the trigger when it closes.

## Film-derived additions

**MAGI resolution** (`.dialog.magi`): a decision that three computers vote on.
- **Vote cells:** `MELCHIOR · 1`, `BALTHASAR · 2` and `CASPER · 3`, each a chamfered cell.
  - While deliberating, a cell shows 審議中 blinking, in a dim outline.
  - On approval it turns green and shows 承認 / `APPROVE`.
  - On denial it turns red and shows 否定 / `DENY`.
- **Tally:** a `mono` status line under the cells. It reads `AWAITING 2 VOTES`, then `RESOLVED 2 : 1 · MOTION CARRIED` or `MOTION DENIED`. It is `role="status"`, and the dialog points to it with `aria-describedby`.
- **Action:** `Execute` stays disabled until two computers approve.

The preview runs through three rounds: carried 2–1, denied 1–2, and carried 3–0. Add `#carried` or `#denied` to pin a result.

**Auto-cancel fuse:** the critical dialog now has a red bar that runs down over ten seconds, with `AUTO-CANCEL 10s` counting in the footer as a `role="timer"`. A decision this serious should not sit open. Wire the timeout to the Cancel action.

Under `prefers-reduced-motion` the vote shows a settled result and the fuse holds full.
