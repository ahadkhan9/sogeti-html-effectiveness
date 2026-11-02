# Sogeti brand foundations

A working synthesis of *Sogeti brand guidelines, Version 3* (November 2024), the
authoritative PDF in [`reference/Sogeti-brand-V3-guidelines.pdf`](../reference/Sogeti-brand-V3-guidelines.pdf).
Page references below point to that document. Where the 2026 live site diverges,
the divergence is named rather than silently copied. See
[`web-and-digital.md`](web-and-digital.md) for the full digital audit.

---

## 1. Source hierarchy (read this before resolving a conflict)

1. **Sogeti Global Marketing master artwork and the current brand guidelines.**
   The PDF is the canonical source for logo geometry, colour values, type,
   shape rules and writing. When in doubt, ask the brand team.
2. **Approved current templates** (Capgemini Group / Zodiak digital templates,
   MS Office masters, event kits). These may legitimately update a detail.
3. **This skill's digital adaptations.** They are documented and deliberate:
   light-first surfaces, a mono display hierarchy, accessible red variants.
4. **The live website.** Useful evidence of current practice, never authority.
   It currently runs a Group-wide Zodiak theme with dark mode by default, no
   Deep Purple, Ubuntu Light headlines and Ubuntu Mono demoted to metadata.
   Those are product decisions, not new brand rules.

If a conflict affects an external deliverable, surface it. Do not average two
systems into a third.

---

## 2. What Sogeti is for

**Proposition.** At Sogeti, we believe in making value. We help organizations
take full advantage of technology opportunities and deliver viable outcomes at
speed.

**Narrative.** Disruption is the norm. The ability of IT to realize rapid value
is what determines how quickly an organization can respond. Sogeti calls this
**“value in the making.”** It is a hands-on partner from day one: agile,
innovative, close to the client, backed by a global network. The culture is
**“making IT work”**, complemented by deep knowledge of existing and emerging
technology.

**Brand line.** *The magic is in the making.*

Use the line sparingly. It is a signature, not a section heading. The same goes
for **“value in the making”** and **“hands-on.”** Their power comes from
scarcity.

**Positioning in one sentence.** Sogeti makes business value through technology
for organizations that need to implement innovation at speed, with a local
partner and global scale.

**The offering, in plain terms.** Quality engineering, cloud and application
development, digital product engineering, data and AI, cybersecurity and
intelligent automation, delivered through a DevOps approach. Only claim a
capability you can staff and evidence.

---

## 3. Personality and voice

| Dimension | What it means | What it is not |
|---|---|---|
| **Hands-on** | We build, run and stay. Verbs over abstractions. | Boastful “we do everything” language |
| **Precise** | Named systems, numbers, owners, dates. | Jargon used to signal expertise |
| **Progressive** | Curious about new technology, honest about its limits. | Hype, trend-chasing, “revolutionary” |
| **Human** | Professional yet conversational. Complex tech, human sentences. | Corporate stiffness or forced casualness |
| **Local, global** | Close enough to sit with the team; backed by scale. | Generic “global footprint” claims |

The guidelines ask for writing that is **professional yet conversational**,
with short clear sentences, brevity, logical flow and no unnecessary jargon or
culture-specific references. International English is the default: American
spelling and punctuation for web and published materials, CMOS as the reference.

Full rules, examples and a banned-phrase bank are in
[`voice-and-copy.md`](voice-and-copy.md).

---

## 4. Logo

The Sogeti logo combines four elements: the **Sogeti wordmark**, the
**Capgemini wordmark**, the **spade symbol** and **descriptor text**. The red
i-dot is a link to Sogeti's heritage. Sogeti Red is restricted to the logo and
the methods in the guidelines; it is **not** a general palette colour.

### Versions and minimum sizes

| Version | Use | Minimum width |
|---|---|---|
| Primary full colour | Default on light surfaces | 25 mm print / **160 px** screen |
| Primary black | Single-colour print or neutral applications | 25 mm / 160 px |
| Primary white | Dark or photographic surfaces | 25 mm / 160 px |
| Primary 2-colour (white + red dot) | Preferred over 1-colour white on dark or blue | 25 mm / 160 px |
| Special-use logo (with descriptor) | Formats too small for the primary lockup | **40 mm / 260 px** |

The PDF contains an earlier “100 px” mention; the conservative
**160 px minimum** is used throughout this skill.

### Clear space and placement

- Clear space is defined by the height of the **“s”** in the Sogeti wordmark.
- Preferred print positions: **top left or top right**. Bottom corners are
  allowed when the format demands it.
- For positioning, use the width of the letters **“So”** as an X/Y reference.
- Never re-colour the colour logo to create a black-and-white version; the
  spade has different detail in the single-colour artwork.
- Never stretch, rotate, outline, add effects, crop or rebuild the lockup.
- Always use Global Marketing master artwork for production.

### Writing the name

**Sogeti** in title case, capital S. No accent, no all caps, no space.
**SogetiLabs** is one word, capital S and capital L. **TMAP®** carries the
registered mark. **Geti, the Sogeti Yeti** is a proper noun when used.

The extracted logo files in `assets/logos/` are reference-quality PNGs for
drafting. They are not a substitute for master artwork. The full lockup is
1.915:1; the wordmark is 2.67:1.

---

## 5. Colour

### Primary

| Colour | Hex | Pantone | Role |
|---|---|---|---|
| Capgemini Blue | `#0070AD` | 7461C | Primary brand field, headings, links, structure |
| Vibrant Blue | `#12ABDB` | 2191C | Signal, data highlight, energy; large text and graphics |

### Secondary

| Colour | Hex | Pantone | Role |
|---|---|---|---|
| Deep Purple | `#2B0A3D` | 2695C | Depth, contrast, editorial ink; used sparingly |
| Cool Tech Red | `#F53B53` | 1787C | Accent, status, the i-dot lineage |
| Cool Grey | `#F5F5F7` | Cool Grey 1 | The go-to background for general artwork |
| White | `#FFFFFF` | – | Space, surfaces, contrast |

**Sogeti Red** `#FF4019` is the logo i-dot and nothing else in this system.
Do not use it for buttons, charts or status.

### Proportions for digital artifacts

A useful working ratio, not a brand law:

- **60–70%** Cool Grey / White surfaces
- **20–30%** Capgemini Blue (fields, headers, footers, primary actions)
- **5–10%** Vibrant Blue (data, one highlight, one shape)
- **≤5%** Red and Deep Purple (status, one number, one editorial accent)

If a page needs a third saturated field to feel finished, the layout is doing
too little. Fix the composition, not the palette.

Exact tint ramps, contrast pairs, chart groups and CSS tokens:
[`color-system.md`](color-system.md).

---

## 6. Typography

**Ubuntu** is the brand typeface. **Ubuntu Mono Bold** is the primary headline
face at the top tier of the messaging hierarchy. Use Mono Bold sparingly, with
care. Supporting headlines use Ubuntu Medium or Bold; body copy uses Ubuntu
Light. Only Regular and Bold cuts of Ubuntu Mono exist.

The system fallback is **Verdana**, chosen for screen legibility. It is a
fallback, not a brand face.

### The digital adaptation used in this skill

The PDF assumes print and designed layouts. Screens need a slightly different
hierarchy:

| Role | Face | Weight | Why |
|---|---|---|---|
| Display / hero | Ubuntu Mono Bold | 700 | The signature Sogeti voice; max 4 lines |
| H1 / H2 | Ubuntu | 700 / 500 | Readable at scale without shouting |
| H3 / labels | Ubuntu Medium | 500 | Structure |
| Body | Ubuntu Regular | 400 | Light at 16–18 px is too thin on screen |
| Lead paragraph | Ubuntu Light | 300 | Only at ≥20 px |
| Metadata / numbers | Ubuntu Mono Bold | 700 | Tabular, precise |

Sentence case everywhere. No all-caps labels. No letter-spacing tricks to make
a small label look “technical”. Type scale, line length, tracking and fallback
stacks: [`typography.md`](typography.md).

---

## 7. Brand shapes

Three shapes are derived from the wordmark. The **primary shape** is the
leading device for covers, opening titles, web pages, adverts and social. The
**secondary shapes** are for inner content and stay pinned to a corner.

### Primary shape rules

- Place the longest edge along the side of the layout.
- Keep a margin of **5% of the longest artwork dimension** outside the shape.
- Include vertical space outside the shape; do not center it in the layout.
- Flip and place in any corner. Do not rotate 90°.
- Do not make it too small, too large, or use it in two directions.
- Pair with the 2-colour logo for the strongest recognition.
- When framing photography inside it, omit the logo.
- One primary shape per composition is enough.

### Secondary shape rules

- Anchor to a corner; they are the supporting device, not the lead.
- Scale proportionally in both directions; extend along the parallel sides if
  a longer format is needed.
- Rotate in 90° steps, flip horizontally or vertically.
- Use them for quotes, inner content or photography framing.
- Do not let text sit too close to the curved edge.

The clip paths are implemented in `assets/sogeti.css` and documented with the
geometry in [`logo-and-shapes.md`](logo-and-shapes.md). The primary shape is a
rectangle whose bottom-right corner is scooped by a quarter-circle. It is not a
rounded card.

---

## 8. Icons, illustration and photography

**Icons.** Sogeti's icon style is isometric, in the same visual language as the
illustration system, usually held in a circular field. One icon, one meaning.
Do not introduce new icons without the brand team. In HTML artifacts, use the
thin-line UI icon set for interface actions and reserve isometric artwork for
topic illustration. Never put a rounded-square icon tile above every heading.

**Illustration.** Isometric perspective, modular components, people working
together with technology, consistent shadows, rounded corners that balance the
precise construction. The palette includes light and dark shades of the primary
palette plus infographic colours; red accents link back to the logo. New
components require brand consultation.

For this skill, three reference SVG illustrations are provided. They are
**diagrammatic**, captioned and used once per page. They are not a licence to
generate generic “floating isometric tech” art. If the illustration does not
explain the argument, remove it.

**Photography.** Natural, candid, spontaneous, not posed. Do not over-edit or
depict unrealistic events. Look for moments, closeness, shallow depth of field
and context. Colleague portraits: plain light background, even lighting, eye
level, casual business clothing, confident and welcoming expression. Consider
cultural sensitivities. Use real, credited photography with rights. Never use
synthetic “diverse team” imagery or AI-generated faces.

---

## 9. Digital expression

The guidelines' web example shows a clean white page, the logo top left, a
photographic hero, an isometric illustration in the article and a blue CTA.
The social guidance is **square-first**: design for 1:1 and adapt, rather than
making several formats from the start.

For HTML artifacts:

- Lead with **Cool Grey or White**, not dark mode.
- Use **one** primary shape as architecture, not wallpaper.
- Use **one** oversized typographic moment per page. Mono display is the
  signature; repetition kills it.
- Let the content's cardinality decide the grid. Do not force three cards.
- Put the logo where it is prominent, with clear space; do not rebuild it.
- Use real content, real numbers and named owners. If the content is
  illustrative, label it visibly.

The 2026 live site defaults to dark mode and has retired Deep Purple. This
skill deliberately keeps a **light-first** system because the guidelines call
Cool Grey the go-to background, because most consulting artifacts are read in
daylight or printed, and because a dark default doubles the contrast surface
without a content reason. A dark variant is allowed for a stage, a film or an
evening event; it is a design decision, not a default.

---

## 10. Page map of the PDF

| Pages | Content |
|---|---|
| 2 | Positioning, narrative, what is new in v3 |
| 3–5 | Logo, versions, usage, co-branding |
| 6–9 | Colour palette, infographic palette and pairing |
| 10–13 | Brand shapes, primary/secondary principles, samples |
| 14–16 | Typefaces, typographic principles, system typeface |
| 17 | Writing guidelines, tone, rules |
| 18–21 | Charts, figures, diagrams, email |
| 22–28 | Icons, illustration, photography, colleague and emotive imagery |
| 29–31 | Video idents and guidance |
| 32–38 | Social, web, PowerPoint, Word, events, SogetiLabs |
| 39–45 | Contact and back matter |

The raw extracted text is at
[`reference/brand-guidelines-raw.txt`](../reference/brand-guidelines-raw.txt)
for search. The PDF remains the authority.
