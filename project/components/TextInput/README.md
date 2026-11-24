# TextInput

The single-line field: a clipped terminal box with a solid leading bar, a pipe-marked label above, and a `mono` value that glows when focused.

**When to use:** free-text or code entry (`UNIT DESIGNATION`, `AUTH CODE`). Use the same states for every other field type.

**Props** (Astryx contract)

| Prop | Type | Default |
|---|---|---|
| `size` | `"sm" \| "md" \| "lg"` | `"md"` (`size-element-*`; preview shows `lg`) |
| `status` | `{type: "warning" \| "error" \| "success", message?: string}` | — |
| `isDisabled` | `boolean` | `false` |
| `placeholder` | `string` | — |

**Shape:** the top-right corner is cut at 8px. The frame is `--ink`, the fill is `color-background-body`, and a 3px bar in `--ink` runs down the left edge. The label is 12px 700 with a pipe in front.

**States**

- **Resting:** `--ink` is `color-border-emphasized`. The value is `mono` 15px in `color-text-primary`; the placeholder is `color-text-disabled`.
- **Hover:** `--ink` lifts to `color-text-secondary`.
- **Focus:** `--ink` becomes `color-border-accent`, the box gets `shadow-med`, the value gets `shadow-bloom`, and the caret is `color-text-accent`.
- **Status:** `--ink` and the value switch to `color-error` (or success / warning). The message sits below as a solid tag with a hazard-stripe tail; tie it to the input with `aria-describedby` and `aria-invalid`.
- **Disabled:** a `color-border` frame with `color-text-disabled` text.
- **Unit suffix:** optional, 11px in `color-text-tertiary` (`%`, `m`, `sec`).

**What the consumer provides:** value/onChange, a label, and a status once validation has an opinion.

## Film-derived additions

**Command line** (`.cli`): a field with a glowing `MAGI>` prompt before the typed text, for console input.

**Personal code** (`.cells`): the six-digit code from the gate sign.
- **Cells:** six boxes with a heavier bottom edge. A filled cell shows `●`. The next cell to fill is outlined in the accent colour and holds a blinking block cursor.
- **Input:** a single real `<input>` sits invisibly over the cells, so typing, pasting, deleting and screen readers all work as normal. Only digits are kept.
- **Check:** at six digits the status reads `SECURITY:CHECK` for a moment, then one of:
  - `SECURITY:OK · gate unlocked`, with the cells turning green.
  - `SECURITY:DENIED · code rejected`, with the cells turning red and `aria-invalid` set.
- **Status:** the line beside the cells is `role="status"` and is linked with `aria-describedby`.

In the preview, `000000` is rejected so both outcomes can be seen. Add `#ok` to pin a cleared code. The cursor blink is off under `prefers-reduced-motion`.
