# Design system

The working system is one CSS file and one JS file:

- [`assets/sogeti.css`](../assets/sogeti.css) – tokens, reset, layout, components, print.
- [`assets/fonts.css`](../assets/fonts.css) – base64 WOFF2 Ubuntu / Ubuntu Mono.
- [`assets/sogeti.js`](../assets/sogeti.js) – nav, tabs, copy, print, year.
- [`assets/sogeti.css`](../assets/sogeti.css) is imported by the source templates;
  `scripts/build.py` inlines it, the fonts and local images into one file.

Do not add Tailwind, Bootstrap, a chart library, an icon pack or a font CDN.
The system is deliberately small and self-contained.

---

## 1. Tokens

### Surfaces

`--grey` `#F5F5F7` · `--white` `#FFFFFF` · `--wash` `#EDF6FA` · `--wash-2` `#E6EEF3`

### Ink

`--ink` `#14181D` · `--ink-2` `#39434C` · `--muted` `#5D6973`

### Brand

`--blue` `#0070AD` · `--blue-dark` `#005A82` · `--blue-mid` `#0E82BF` ·
`--vibrant` `#12ABDB` · `--vibrant-50` `#88D5ED` · `--purple` `#2B0A3D` ·
`--red` `#F53B53` · `--red-action` `#DB2443` · `--red-ink` `#A31335`

### Lines and status

`--line` `#D9E0E6` · `--line-strong` `#B7C3CC` · `--ok` `#007A4D` ·
`--warn` `#8A4B12` · `--risk` `#A31335`

### Type and space

`--sans`, `--mono`; `--fs-xs` to `--fs-display`; `--s1` 4px to `--s10` 128px;
`--wrap` 1180px; `--header-h` 88px; `--radius` 2px; `--pill` 999px.

Full values: [`color-system.md`](color-system.md), [`typography.md`](typography.md).

---

## 2. Layout primitives

| Class | Job |
|---|---|
| `.wrap` | 1180px max, fluid gutters |
| `.wrap--wide` / `.wrap--narrow` | 1380px / 760px |
| `.section` | Standard vertical rhythm (`clamp(3.5rem, 7vw, 6rem)`) |
| `.section--tight` | Smaller rhythm for stat strips and briefs |
| `.section--white` / `--grey` / `--wash` | Surface alternation |
| `.section--blue` / `--deep` / `--purple` | Dark fields; use once per page |
| `.grid--2/3/4` | Equal grids; content cardinality decides |
| `.split` | 7fr / 4fr editorial split |
| `.split--wide` | 8fr / 4fr |
| `.doc-layout` | Main document + 250px sticky rail |
| `.article-layout` | Article + 220px sticky contents |
| `.playbook-layout` | Playbook + progress rail |
| `.assessment` | Inputs + 420px sticky radar |
| `.appraisal` | Matrix + 360px results |
| `.slop-layout` | Checklist + 350px result |

Breakpoints: 1000px, 900px, 800px, 700px, 620px, 520px, 440px. Test 360px.

---

## 3. Components

### Navigation and page furniture

- `.site-head`, `.brand`, `.site-nav`, `.nav-toggle` – solid white header, 88px,
  logo 164px. No glass, no shadow.
- `.site-foot` – Capgemini Blue dark, white logo, three link columns.
- `.page-head` – compact opener for inner pages, optional pale shape and
  `.page-head__mark` (large faint number).
- `.hero--field` – signature split hero: text left, blue shape right.
- `.case-hero` – deep blue client-story opener.
- `.data-hero` – research opener with a large number.
- `.event-hero` + `.event-card` – event page.

### Typography

`.display`, `.display--s`, `.h1`–`.h4`, `.lede`, `.kicker`, `.mono`, `.num`,
`.source`, `.muted`, `.measure`, `.measure-s`.

### Actions

`.btn` + `--primary`, `--dark`, `--ghost`, `--light`, `--red`, `--sm`, `--block`.
Pill radius; 44px minimum height for touch. `.link-arrow`, `.actions`.

### Content

`.card` (2px radius, hairline border, no shadow), `.stat` (2px top rule),
`.tag`, `.status`, `.quote`, `.callout` (`--warn`, `--risk`, `--ok`, `--purple`),
`.pullstat`, `.source`, `.scenario-note`.

### Data

`.table-wrap` + `.table` (`--compact`, `--fit`), `.chart`, `.bars`, `.legend`,
`.matrix`, `.timeline`, `.phasebar`, `.steps`.

### Interactive

`.tabs` / `.tab` / `.tabpanel`, `details.disclosure`, `.field`, `.range`,
`.switch`, `.segmented`, `.searchbox`, `.decision-list`, `.theme` (synthesis),
`.option-card`, `.export-bar`, `.toast`.

### Documents

`.doc-layout`, `.doc-rail`, `.doc-section`, `.brief-grid`, `.signoff`,
`.cover-panel`, `.brief-sheet`, `.decision-box`.

### Deck

`.deck-body`, `.deck-top`, `.deck-stage`, `.slide`, `.slide--cover`,
`.slide--statement`, `.slide__grid`, `.deck-progress`, `.deck-notes`.

---

## 4. Shape and icon usage

Shape clip paths are defined once per document by
`_partials/shapes.html`. Use `.hero__field` or a positioned div with
`clip-path: url(#sogeti-shape-primary)`. One primary shape per page. See
[`logo-and-shapes.md`](logo-and-shapes.md).

Icons are inline `<symbol>` sprites:

```html
<svg class="icon" aria-hidden="true"><use href="#i-arrow"/></svg>
```

Available: `i-arrow`, `i-arrow-up`, `i-check`, `i-copy`, `i-download`,
`i-chev`, `i-menu`, `i-close`, `i-clock`, `i-shield`, `i-cloud`, `i-users`,
`i-target`, `i-info`, `i-warning`, `i-search`, `i-plus`, `i-linkedin`,
`i-youtube`.

Rules:

- UI icons are thin-line, 1.7px stroke, `currentColor`.
- Do not put every UI icon in a rounded square.
- Do not use isometric icons as bullet points.
- Icons need a text label or an accessible name. Decorative icons are
  `aria-hidden="true"`.

---

## 5. Motion

The system uses one page-load `rise` animation on `.intro` children, hover
colour transitions, and `prefers-reduced-motion` guards. That is the whole
motion language.

- No scroll-triggered fade-up on every section.
- No parallax, cursor followers, typewriter, confetti or hover-scale on cards.
- Slide changes and tab switches are instant or 180ms.
- All non-essential motion is removed under `prefers-reduced-motion`.
- Never hide content at rest waiting for JS. The one exception is a controlled
  reveal that has a no-JS fallback; the reference templates do not need it.

---

## 6. Print

Every artifact includes `@media print`:

- Hide header, footer, nav, filters, export bars, toasts.
- White background; ink text.
- Hide the shape field and page-head shape.
- Avoid page breaks inside cards, charts, tables and callouts.
- Deck: show every slide, one per page.
- Brief: full-width sheet, 16mm margins.
- Check that charts and tables remain legible in greyscale.

---

## 7. Build a new page

1. Copy [`examples/starter.html`](../examples/starter.html) or the closest
   `references/templates/_src/*.html`.
2. Keep the `<head>`, skip link, shapes partial, header partial and footer
   partial.
3. Write the content before styling. One job per page.
4. Pick one layout primitive and one signature moment (shape, display, chart or
   diagram). Not all four.
5. Add interactivity only if it closes a decision or produces an export.
6. Inline assets: `python3 scripts/build.py path/to/source.html`.
7. Run `python3 scripts/sogeti_audit.py path/to/built.html`.
8. Test 360px, keyboard, 200% zoom, print.
9. Save the built file in the project's `html-docs/` folder and link it.

---

## 8. Do not add

- A component library or utility CSS framework.
- A webfont CDN, icon CDN, analytics script or tracking pixel.
- A dark-mode toggle with no designed dark palette.
- A new radius scale (2px surfaces, pill controls, circles for numbers).
- A new shadow scale. The system uses no wide shadows.
- A gradient background, gradient text or glassmorphism.
- A three-card feature row just because the page feels empty.
- A stock photo of a team. Use type, a diagram or a real artifact.
