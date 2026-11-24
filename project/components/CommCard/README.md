# CommCard

The floating SOUND ONLY card that appears when a voice-only call is selected. It's a bright plate turned in 3D, with sender and recipient blocks and a LIVE tag.

**Variants** (frames 117–119, 155):

| Class | Card | Ink | Use |
|---|---|---|---|
| default | `#f8f6f2` near-white with a white glow | near-black; tags in `tac-orange-400/500` | Standard line, NERV internal |
| `cmdr` | `sysblue-500` | white | Command or priority channel |

**Anatomy:**
- **Header:** `Classified` at top-left; channel lines and an ONLINE chip at top-right.
- **Centre:** **SOUND / ONLY** at 52px compressed, with `SELECTED` under it.
- **Voice level:** a row of 21 small bars under `SELECTED`. They rise and fall in speech-like bursts with pauses, and each card has its own pattern. It is the only sign of life on a sound-only line.
- **Addresses:** From / To blocks, each with a 2px left rule.
- **Footer:** a LIVE box that blinks in two steps, and the transmission notes (`Recording Saved To MAGI 01 Databanks`).
- **Sheen:** a soft diagonal highlight crosses each card every seven seconds.

**Back view** (frame 117): the `back` class shows a card from behind, mirrored, see-through and slightly soft. Use it when the card floats between the viewer and the speaker. It is `aria-hidden`, since it repeats a card that is already announced.

**Placement:** turned with `rotateY(±22–24deg)` toward the speaker's side of the screen; mirror it for the other side. The card bobs gently. Under `prefers-reduced-motion` the bob, sheen, blink and voice bars all stop.

**Consumer provides:** the channel, From and To, and the footer notes. Use an `<article>` with an `aria-label` that says who is calling whom, and provide a transcript for the audio.
