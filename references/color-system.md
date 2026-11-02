# Colour system

Source: *Sogeti brand guidelines v3*, pages 6–9, plus measured contrast for the
digital palette used in this skill. Exact brand values are preserved. Functional
tints are derived and labelled as such.

---

## 1. The palette

### Primary

| Token | Hex | Pantone | CMYK | Use |
|---|---|---|---|---|
| `--blue` | `#0070AD` | 7461C | C100 M40 Y10 K0 | Brand fields, headings, links, primary buttons |
| `--vibrant` | `#12ABDB` | 2191C | C80 M0 Y5 K0 | Signal, data highlight, one accent per composition |

### Secondary

| Token | Hex | Pantone | CMYK | Use |
|---|---|---|---|---|
| `--purple` | `#2B0A3D` | 2695C | C80 M100 Y0 K60 | Depth, editorial ink, closing panels |
| `--red` | `#F53B53` | 1787C | C0 M86 Y55 K0 | Accent, status, graphics; large text only |
| `--grey` | `#F5F5F7` | Cool Grey 1 | C1 M1 Y0 K3 | The default page ground |
| `--white` | `#FFFFFF` | – | – | Surfaces, space, contrast |

**Sogeti Red** `#FF4019` (Pantone Warm Red C, RGB 255/64/25) is the logo i-dot.
It is **not** a UI or chart colour. It appears only inside the logo artwork.

### Functional, derived from the brand

These are not brand colours. They exist so the brand palette can carry status,
small text and interactive states without failing contrast.

| Token | Hex | Purpose | Contrast |
|---|---|---|---|
| `--blue-dark` | `#005A82` | Blue dark shade; footer, deep fields | 7.54:1 with white |
| `--blue-mid` | `#0E82BF` | Digital step between blue and vibrant | 4.6:1 with white |
| `--blue-200` | `#80B8D6` | Data tint, rules | graphics |
| `--vibrant-50` | `#88D5ED` | Vibrant tint; large labels on dark | 4.59:1 on `#005A82` |
| `--wash` | `#EDF6FA` | Selected rows, callouts | 4.89:1 with blue text |
| `--ink` | `#14181D` | Body and headings | 17.82:1 on white |
| `--ink-2` | `#39434C` | Secondary body | 9.9:1 on white |
| `--muted` | `#5D6973` | Captions, metadata | 5.62:1 on white |
| `--line` | `#D9E0E6` | Hairlines | non-text |
| `--line-strong` | `#B7C3CC` | Strong rules, input borders | non-text |
| `--red-action` | `#DB2443` | Red buttons with white text | 4.83:1 with white |
| `--red-ink` | `#A31335` | Small red text, risk labels | 7.77:1 on white |
| `--ok` | `#007A4D` | Success text | 4.76:1 on `#E3F5EC` |
| `--warn` | `#8A4B12` | Warning text | 6.06:1 on `#FDF0E3` |
| `--risk` | `#A31335` | Risk text | 6.64:1 on `#FDE8ED` |

`--red` (`#F53B53`) is 3.73:1 on white. It passes only for large text (≥24 px
regular or ≥19 px bold) and for non-text graphics. For small red text use
`--red-ink`; for a red button with white text use `--red-action`.

---

## 2. Contrast: the tested pairs

| Foreground | Background | Ratio | Normal text | Large text |
|---|---|---|---|---|
| `#0070AD` | `#FFFFFF` | 5.36 | Pass | Pass |
| `#0070AD` | `#F5F5F7` | 4.92 | Pass | Pass |
| `#FFFFFF` | `#0070AD` | 5.36 | Pass | Pass |
| `#0070AD` | `#EDF6FA` | 4.89 | Pass | Pass |
| `#12ABDB` | `#FFFFFF` | 2.67 | Fail | Fail |
| `#2B0A3D` | `#FFFFFF` | 17.31 | Pass | Pass |
| `#F53B53` | `#FFFFFF` | 3.73 | Fail | Pass |
| `#A31335` | `#FFFFFF` | 7.77 | Pass | Pass |
| `#5D6973` | `#FFFFFF` | 5.62 | Pass | Pass |
| `#FFFFFF` | `#005A82` | 7.54 | Pass | Pass |
| `#EAF6FB` | `#0070AD` | 4.86 | Pass | Pass |
| `#EAF6FB` | `#005A82` | 6.85 | Pass | Pass |
| `#88D5ED` | `#0070AD` | 3.26 | Fail | Fail |
| `#FFFFFF` | `#F53B53` | 3.73 | Fail | Pass |
| `#FFFFFF` | `#DB2443` | 4.83 | Pass | Pass |

Rules of thumb:

- **Vibrant Blue is a graphics colour.** Do not set body, captions or small
  labels in `#12ABDB` on white. Use Capgemini Blue for text, Vibrant for bars,
  dots, rules and one large statement.
- **White on Capgemini Blue is safe** for normal text (5.36). White on Vibrant
  is not (2.67).
- **Light blue labels on Capgemini Blue** need `#EAF6FB`, not `#88D5ED`.
- **Red is an accent, not a body colour.** Small red text is `#A31335`.

---

## 3. Proportion and composition

A practical ratio for a document page:

```
70%  Cool Grey / White surfaces and space
20%  Capgemini Blue fields, header, footer, primary action
 7%  Vibrant Blue data, one highlight, one shape
 3%  Deep Purple / Red / status
```

This is a working discipline, not a brand law. The guidelines call Cool Grey
the go-to background and allow white space within the identity. They do not ask
for every surface to be blue.

**One saturated field per page.** A blue hero plus a blue section plus a blue
footer turns the page into a colour block. Alternate white and grey; use blue
for the moment that matters.

**One primary shape per composition.** The shape is architecture. If a second
shape is needed for inner content, use a secondary shape pinned to a corner.

**No gradients as decoration.** The illustration system uses gradients for
depth and red accents. UI surfaces use flat colour. Do not put a purple-blue
gradient behind a hero.

---

## 4. Infographic palette

The guidelines provide an expanded palette for charts and diagrams. Use it only
for information, never for decoration.

### Blue / purple group (start here)

`#005A82` · `#0070AD` · `#80B8D6` · `#12ABDB` · `#88D5ED` · `#2B0A3D`

### Green / aqua group

`#95E616` · `#C8FF16` · `#00C37B` · `#15596B` · `#0F999C` · `#01D1D0`

### Pink / purple group

`#F53B53` · `#FF7E83` · `#CB2980` · `#860864` · `#4701A7` · `#7E39BA`

### Peach / brown group

`#FFE2BE` · `#F5C499` · `#E5A071` · `#BA6C34` · `#904C1A` · `#5B2C05`

### Rules from the PDF

1. Start with the **Blue/Purple** grouping.
2. Pair it with **one** other group, not all three.
3. Use as few colours as possible. Group data into types to reduce the count.
4. Preserve contrast between adjacent elements.
5. For simple charts, colours that harmonise with the layout are acceptable.
6. More than seven categorical colours is usually unreadable. Prefer direct
   labels and small multiples.

Chart selection, axes and annotation: [`data-visualization.md`](data-visualization.md).

---

## 5. CSS tokens

```css
:root {
  --blue: #0070AD;
  --blue-dark: #005A82;
  --blue-mid: #0E82BF;
  --blue-200: #80B8D6;
  --vibrant: #12ABDB;
  --vibrant-50: #88D5ED;
  --purple: #2B0A3D;
  --red: #F53B53;
  --red-action: #DB2443;
  --red-ink: #A31335;
  --grey: #F5F5F7;
  --white: #FFFFFF;
  --ink: #14181D;
  --ink-2: #39434C;
  --muted: #5D6973;
  --line: #D9E0E6;
  --line-strong: #B7C3CC;
  --wash: #EDF6FA;
}
```

The full working set is in [`assets/sogeti.css`](../assets/sogeti.css).

---

## 6. Do / don't

| Do | Don't |
|---|---|
| Use Cool Grey or white as the page ground | Default to near-black “AI dashboard” dark mode |
| Use one large Capgemini Blue field | Stack blue hero, blue section, blue footer |
| Use Vibrant Blue for one data highlight | Set 12 px copy in Vibrant Blue on white |
| Use `#A31335` for small red text | Use `#F53B53` for 12 px risk labels |
| Use `#DB2443` behind white button text | Use `#F53B53` behind white button text |
| Derive functional tints and name them | Invent a new “brand” purple |
| Keep chart colour to two groups | Use a rainbow for six categories |
| Let white space carry the composition | Fill every band with a gradient mesh |
