# PartsBlueprint

Mari's parts-list blueprint from the New Eva Parts clip. Scaffold towers in pink line art stand on a pale, greenish-white ground. Each holds one EVA component with a part code and a centred caption, and a scan bar reads down them one at a time.

**Anatomy:**
- **Ground:** `blush-paper`, with a white wash from the top that fades by mid-height.
- **Towers:** each has a front face, a receding side face and a roof, so it reads as a box.
  - A 22px grid on the front.
  - Cross-bracing in the two outer bays.
  - A heavier `blush-500` frame.
  - A soft halo on the line art.
- **Parts:** drawn once and mirrored about the centre line. Three fills give depth: a light tint, a 45° hatch and a denser tint. The preview has a launcher rack, the JA-02 torso and arms, and stacked restraining chevrons.
- **Labels:**
  - A `mono` part code at the top of each tower (`SSM-0616`).
  - A caption in regular-weight `sans` 14px, all caps and centred over the art, with a paper-coloured outline so it stays readable.
- **City:** two rows of small pink blocks along the bottom.
- **Debris:** optional blurred red blobs, from the shot's out-of-focus foreground. Leave them out in product UI.

**Motion:** a hatched scan bar with a `CHECK` tag travels down one tower at a time, three seconds each. It is hidden under `prefers-reduced-motion`.

**Contrast:** captions use a darker pink (`#C8486C`), which is about 4:1 on the paper. That's fine at 14px for labels but not for body text. Keep real data in accessible text elsewhere.

**Accessibility:** the SVG is `role="img"` with a label naming the three parts.

**Consumer provides:** per tower a code, caption lines and a part drawing, and the number of towers.
