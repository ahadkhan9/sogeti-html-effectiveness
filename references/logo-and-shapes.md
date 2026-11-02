# Logo and brand shapes

Source: *Sogeti brand guidelines v3*, pages 3–5 (logo), 10–13 (shapes), 38–41
(SogetiLabs). The PDF is authoritative; this file translates the rules into
HTML/CSS.

---

## 1. Logo anatomy

The primary lockup has four elements:

1. **Sogeti wordmark** – custom letterforms, title case, red i-dot.
2. **Capgemini wordmark** – the descriptor line.
3. **Spade symbol** – the Capgemini heritage mark.
4. **Descriptor text** – “Part of”.

The full-colour logo uses the two blues from the palette and retains **Sogeti
Red** `#FF4019` for the i-dot. Sogeti Red is not available for wider use.

### Versions

| Version | Background | Minimum |
|---|---|---|
| Primary full colour | White / Cool Grey | 25 mm print · 160 px screen |
| Primary black | Single-colour print | 25 mm · 160 px |
| Primary white | Blue, purple, photography | 25 mm · 160 px |
| Primary 2-colour (white + red dot) | Blue / dark, preferred over 1-colour white | 25 mm · 160 px |
| Special use logo | Small formats, pens, merchandise | 40 mm · 260 px |

The PDF also mentions 100 px in one place. Use **160 px** as the conservative
minimum. Do not use the special-use logo just because it fits; use it only when
the primary lockup cannot meet the minimum size.

### Clear space and placement

- Clear space = height of the **“s”** in the Sogeti wordmark on all sides.
- Preferred positions: **top left or top right**.
- Bottom corners are allowed when the format dictates.
- Use the width of **“So”** as an X/Y positioning reference on print formats.
- Keep the logo prominent. Do not bury it in a nav bar with no space.

### Hard rules

- Use Global Marketing master artwork. Do not redraw the wordmark, spade or
  descriptor.
- Do not recolour the colour logo into black/white. The spade detail differs.
- Do not stretch, squash, rotate, outline, add shadow, glow or transparency.
- Do not crop the lockup or place text inside its clear space.
- Do not create a new lockup with another brand; follow the co-branding rules
  and use approved artwork.
- Do not use the logo as a decorative pattern or repeat it in a grid.

### Files in this skill

`assets/logos/` contains reference-quality PNGs extracted from the PDF:

- `sogeti-logo-color.png` – colour on light
- `sogeti-logo-white.png` – white + red dot on dark
- `sogeti-wordmark-color.png` / `sogeti-wordmark-white.png` – compact wordmark

They are **drafting assets**, not master artwork. Replace with Global Marketing
files before production. The full lockup is 1840×961 (1.915:1); the wordmark is
1840×690 (2.667:1).

---

## 2. Brand shape geometry

The primary shape is a rectangle with the **bottom-right corner scooped by a
quarter-circle**. It is not a rounded card and not a blob. The curve is derived
from the wordmark.

Normalized path (objectBoundingBox, 0–1):

```
Primary:   M0,0 H1 V0.62 C1,0.81 0.81,1 0.62,1 H0 Z
Mirror:    M1,0 H0 V0.62 C0,0.81 0.19,1 0.38,1 H1 Z
Wedge:     M0,0 H1 V0.76 L0,1 Z
```

- The primary shape's notch is at the bottom-right.
- The mirror's notch is at the bottom-left.
- The wedge is a straight diagonal cut from 76% height on the right to the
  bottom-left.

### HTML/CSS implementation

Define the clip paths once per document:

```html
<svg width="0" height="0" aria-hidden="true" style="position:absolute">
  <defs>
    <clipPath id="sogeti-shape-primary" clipPathUnits="objectBoundingBox">
      <path d="M0,0 H1 V0.62 C1,0.81 0.81,1 0.62,1 H0 Z"/>
    </clipPath>
    <clipPath id="sogeti-shape-left" clipPathUnits="objectBoundingBox">
      <path d="M1,0 H0 V0.62 C0,0.81 0.19,1 0.38,1 H1 Z"/>
    </clipPath>
    <clipPath id="sogeti-shape-wedge" clipPathUnits="objectBoundingBox">
      <path d="M0,0 H1 V0.76 L0,1 Z"/>
    </clipPath>
  </defs>
</svg>
```

Use it on a positioned field:

```css
.hero__field {
  position: absolute;
  inset: 0 0 0 auto;
  width: min(48%, 720px);
  background: var(--blue);
  clip-path: url(#sogeti-shape-primary);
}
```

Because `clipPathUnits="objectBoundingBox"` is used, the shape scales with the
element. The curve remains proportional. Do not replace it with
`border-radius`; the silhouette is the brand asset.

### Placement rules (from the PDF)

- Place the **longest edge of the shape at the side of the overall layout**.
- Set outside and inside margins to **5% of the longest artwork dimension**.
- Include some **vertical space outside the shape**; do not center it.
- The shape can be flipped and placed in **any corner**, but not rotated 90°.
- Do not make it too small, too large, or use it in two directions.
- The primary shape is for covers, opening titles, web pages, adverts and SoMe.
- Pair it with the 2-colour logo when the logo sits inside the shape.
- When the shape frames photography, do **not** put the logo in the shape.
- One primary shape per composition is enough.

Incorrect executions shown in the PDF: short edge near the side, shape too
small, rotated 90°, too large, centered in the layout, unpinned in two
directions, and using the wrong shape as the primary.

### Secondary shapes

- Anchor to a corner of the layout.
- Scale proportionally; extend along parallel sides if a longer format is
  needed.
- Rotate in 90° steps; flip horizontally or vertically.
- Use for inner content, quotes, testimonial frames, photography framing.
- Keep text away from the curved edge.
- Do not let secondary shapes compete with the primary shape.

### Quote marks

The shapes can be rotated to represent quotation marks, aligned with regional
quote styles. Use this sparingly. A simple 3 px left rule is often better and
less costume-like.

---

## 3. Shape + logo combinations

The strongest Sogeti opening is the **primary shape + 2-colour logo + one visual
or piece of typography**. The shape is the field; the logo sits inside it; the
visual overlaps the edge or sits inside. The composition should look like it
was built for the format, not like a template with a shape pasted on.

Do not:

- put the logo in the shape and also outside it;
- put two primary shapes on one page;
- center the shape behind a centered hero;
- use the shape as a background for body copy with no margin;
- use the shape at 10% opacity as “texture”.

---

## 4. Co-branding and SogetiLabs

- Co-branding follows the Capgemini rules. Use approved lockups; do not build a
  new one. Give both brands appropriate prominence and clear space.
- **SogetiLabs** is one word, capital S and capital L.
- SogetiLabs logo minimum: 40 mm print / 255 px screen for the primary; 60 mm /
  390 px for the special-use version (the PDF also says 160 px in one place;
  use the larger figure).
- Do not re-colour the SogetiLabs colour logo into black/white; the spade
  detail differs.

---

## 5. Do / don't

| Do | Don't |
|---|---|
| Use the shape as a field for type or image | Use it as a small decorative corner |
| Keep 5% margins outside the shape | Let text touch the curved edge |
| Flip to fit the layout | Rotate 90° |
| Use one primary shape | Tile the shape across a page |
| Use the 2-colour logo on blue | Recolour the logo to match the palette |
| Use master artwork | Trace or rebuild the wordmark |
