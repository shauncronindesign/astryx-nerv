# FrameChrome

The AAAW interrogation-room screen frame (Rebuild 3.0+1.0). It wraps any content: corner ticks, a source label, Linked/ONLINE chips, a vertical green case label, a subject strip and a location footer.

**Theme:** Tactical (frames 197–210).

**Slots and parts:**

| Part | Position | Look |
|---|---|---|
| Corners and rules | all four corners; 26px in from top and bottom | 1px `gold-700` |
| `.src` | top-left | `AUX Projector 01`, 10px `gold-300` |
| `.chips` | top-right | `Linked` and `ONLINE` outlined in `gold-300` |
| `.side` | left edge, centred | `aaaw-green` bar with rotated `Case: … Comprehensive Report` in `mint-900` |
| `.title` | top-left inside | 30px compressed gold title with a 4px bar and `shadow-bloom-strong`; a `TEST-00 \| BM-03 \|` line under it |
| `.slot` | middle | your content. The preview shows a status list (`CMD Remote Commander Active Status`) next to the choker drawing |
| `.subj` | bottom-left | `Test Subject` and `All Vitals` chips, a striped meter, and a mode/administrator line |
| `.foot` | bottom-right | `AAAW / Quarantined Interrogation Room 101` |

A scanline overlay sits over everything.

**Consumer provides:** the source label, case label, title, slot content, subject chips and footer. Give the section an `aria-label` naming the source and its link state.

**Choker** (frame 205): the slot's example content, drawn on a canvas. It's a turning band whose face is a grid of small tiles (green, gold, a few red and dark ones), with gold rims, over glowing red ground rings and a small registration cross. The far side of the band is dimmer.

**Executive authority** (frame 210): a state of the whole frame. A banner with hazard-striped ends and a gold outline cuts across the middle (`Executive Authority: Captain Katsuragi`), and the title, slot and subject chips dim to 22% behind it. It snaps open in three steps. Toggle it with the `authority` class on the frame. The banner is `role="status"`.

The preview shows the banner for three seconds in every eleven. Add `#auth` to pin it. Under `prefers-reduced-motion` the choker holds still and the banner stays closed.
