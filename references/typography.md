# Typography

Source: *Sogeti brand guidelines v3*, pages 14–16. Digital adaptations are
explicitly marked.

---

## 1. The faces

| Face | Cuts | Role |
|---|---|---|
| **Ubuntu** | Light 300, Regular 400, Medium 500, Bold 700 | Body, supporting headlines, UI |
| **Ubuntu Mono** | Bold 700 (and Regular 400) | Primary headlines at the top tier, numbers, metadata |
| **Verdana** | Regular, Italic, Bold | System fallback where Ubuntu is unavailable |

The guidelines say: Ubuntu Mono Bold is the primary headline face at the top of
the messaging hierarchy; use it **sparingly**. Supporting headlines are Ubuntu
Medium or Bold. Body copy is Ubuntu Light. Only Regular or Bold cuts of Ubuntu
Mono exist.

**Do not** substitute Inter, Geist, Space Grotesk, Instrument Serif or a
“tasteful” italic serif. The Sogeti face is part of the brand. If Ubuntu is
unavailable, Verdana is the documented fallback; it is not a design choice.

The skill embeds subset WOFF2 files (Latin + punctuation + currency + arrows)
in [`assets/fonts.css`](../assets/fonts.css). They are self-contained and
licensed under the Ubuntu Font Licence 1.0. The raw TTFs are kept in
`assets/fonts/` for maintainers; production HTML uses the WOFF2 base64.

---

## 2. Digital adaptation

The PDF is written for print and designed layouts. At screen sizes, Ubuntu Light
becomes too thin below 20 px. This skill uses:

| Role | Face | Weight | Size | Line height | Tracking |
|---|---|---|---|---|---|
| Display / hero | Ubuntu Mono | 700 | `clamp(2.75rem, 6.4vw, 5.25rem)` | 0.98 | −0.055em |
| Display small | Ubuntu Mono | 700 | `clamp(2.25rem, 5vw, 3.75rem)` | 1.0 | −0.045em |
| H1 | Ubuntu | 700 | `clamp(2.25rem, 4.6vw, 3.5rem)` | 1.04 | −0.025em |
| H2 | Ubuntu | 500 | `clamp(1.75rem, 3.2vw, 2.5rem)` | 1.1 | −0.018em |
| H3 | Ubuntu | 500 | `clamp(1.375rem, 2.2vw, 1.75rem)` | 1.2 | −0.012em |
| Lead | Ubuntu | 300 | `clamp(1.1875rem, 1.6vw, 1.375rem)` | 1.5 | 0 |
| Body | Ubuntu | 400 | 1.0625rem (17 px) | 1.62 | 0 |
| Small | Ubuntu | 400 | 0.875rem | 1.5 | 0 |
| Metadata | Ubuntu Mono | 700 | 0.68–0.75rem | 1.4 | 0.01em |
| Stat / number | Ubuntu Mono | 700 | 1.4–5.5rem | 1.0 | −0.04em |

Why Mono for display: it is the most distinctive, ownable typographic move in
the brand. It is also easy to overuse. **One display statement per page.** Do
not set every heading in Mono; the page will read as a terminal.

Why Regular, not Light, for body: at 16–18 px on screen, Light loses stroke
contrast on Windows and in low-quality projectors. Use Light for leads and
large quotes only.

---

## 3. Type rules

### Sentence case

Capitalize the first word and proper nouns only. Do not capitalize for emphasis.

- **Incorrect:** Banking reform will focus on Data Management and Network Agility.
- **Correct:** Banking reform will focus on data management and network agility.

The live site follows sentence case almost everywhere; the PDF asks for it. This
is one of the strongest Sogeti writing signals. Do not use all-caps labels,
tracked-out eyebrows or title case to create hierarchy. Use scale, space and
colour.

### Headline limits

- Primary display: **maximum four lines**, no more than ~8 words per line.
- Do not end every headline with a full stop. The brand uses full stops for
  deliberate statements; if every heading has one, none of them land.
- Do not center a display headline over a pill chip. Left-align unless the
  format is genuinely symmetrical (a cover, a slide title).
- Do not use gradient text, outlined text, text shadows or italic serif accents.

### Measure and spacing

- Body line length: **60–75 characters**. Never past 80.
- Paragraph spacing: 0.9–1.2× the body line height.
- Do not justify body text. Ragged right is easier to read.
- Use en dashes (–) for ranges and parentheticals. Do not use spaced em dashes.
- Keep numerals tabular in tables and stat blocks.

### Hierarchy without decoration

Use this order:
1. Scale (display vs body).
2. Weight (500/700 vs 400).
3. Colour (ink vs muted vs blue).
4. Space (section rhythm, one oversized moment).

Do not use a coloured stripe, a rounded icon tile or a pill badge to do the
work of hierarchy. Those are the most common AI-generated defaults.

---

## 4. Specimen

```html
<p class="kicker">Insight: AI and data</p>

<h1 class="display">AI doesn’t fail at the model. It fails at the handover.</h1>

<p class="lede">Pilots look convincing in the demo room. Value shows up only
when ownership, data and decisions move into the line.</p>

<h2>01. The demo is not the operating model</h2>

<p>In a demo, the model meets a curated case and a patient audience.</p>

<p class="mono">DECISION LATENCY · 3 DAYS</p>
```

Rendered result: [`templates/01-insight-article.html`](templates/01-insight-article.html).

---

## 5. Fallback stack

```css
--sans: "Ubuntu", Verdana, "Segoe UI", system-ui, sans-serif;
--mono: "Ubuntu Mono", ui-monospace, "SFMono-Regular", Menlo, Consolas, monospace;
```

Verdana is wider and has a larger x-height than Ubuntu. If the fallback is
active, reduce headline sizes by ~8–10% and avoid long all-mono display lines.
Do not ship an artifact that depends on a network font.

---

## 6. Accessibility

- Body text ≥ 16 px; 17 px is the working default.
- Contrast: 4.5:1 for normal text, 3:1 for large text. See
  [`color-system.md`](color-system.md).
- Do not use Light 300 below 20 px.
- Do not use letter-spacing to make 10 px labels “technical”; increase size or
  remove the label.
- Line height ≥ 1.5 for body.
- Text must remain readable at 200% zoom and at 360 px width.
- Do not put text inside images. Charts need an accessible table or description.

---

## 7. Do / don't

| Do | Don't |
|---|---|
| Set display in Ubuntu Mono Bold, sentence case | Set all headings in Mono |
| Use Light for a 24 px lead | Use Light for 14 px captions |
| Use Verdana as the fallback | Load Inter from a CDN |
| Use tabular mono for numbers | Use a decorative serif for stats |
| Use one oversized statement | Use five headline sizes on one screen |
| Keep 60–75 characters per line | Set 110-character paragraphs |
| Use a full stop for a deliberate claim | End every heading with a full stop |
