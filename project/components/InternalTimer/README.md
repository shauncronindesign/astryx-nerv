# InternalTimer

The EVA-02 internal-power countdown from the Asuka clip. It's the German-locale sibling of **ActivityTimer**: the same layout (7-segment digits, three power tabs, a mode strip), but on a brick and amber housing with German labels.

**Anatomy:**
- **Head:** `RESTLAUFZEIT:` ("time remaining") in condensed bold amber with `shadow-bloom`.
- **Prefix:** a slanted `T-` before the digits.
- **Digits:** heavy SVG 7-segment digits in `de-amber` with an amber glow, showing `M:SS:CC`. Unlit segments stay faintly visible at 7%, and the digit block is skewed −6°.
- **Tabs:**
  - `INTERN / ENERGIEVERSORGUNG`: brick fill with a red title and outline, and a red hatch block marking it as the live source.
  - `HAUPTENERGIE-VERSORGUNGSSYSTEM`: dark fill with an amber left rule.
  - `EXTERN`: amber fill with ghosted dark type.
- **Modes:** skewed buttons `STOP · NORMAL · LANGSAM · SCHNELL`, each with a small lamp, plus a blank slot. The active mode fills amber. When `SCHNELL` (fast) is active it turns `de-red` and blooms. The preview switches to it under 30 seconds.
- **Housing:** a gradient from `de-plum` to `de-brick`, clipped with `chamfer-lg`, with an inset hairline bevel and a faint amber haze behind the digits.

**Locale:** keep German and Japanese as separate components, not as string swaps on one. The two films' hardware differs in colour and tab styling as well as language.

**Motion and accessibility:** the panel is `role="timer"`, and its label is updated in German as the time changes. The countdown uses `requestAnimationFrame` and stays still under `prefers-reduced-motion`.

**Consumer provides:** the remaining time, the active mode, which power source is live, and the tab labels.
