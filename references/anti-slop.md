# The anti-slop field guide

A Sogeti-specific guide to AI-era UI tells, and the mechanical gate that keeps
them out of HTML artifacts. The full research report, with 19 annotated sources,
is [`reference/research/AI-SLOP-FIELD-GUIDE-2026.md`](../reference/research/AI-SLOP-FIELD-GUIDE-2026.md).
This file is the working doctrine.

---

## 1. The finding that shapes this skill

Prose advice backfires. In a controlled 2026 test, Solo Design Studio ran six
components across three arms: no skill, written guidance, and a mechanical gate.
Written guidance scored **equal to or worse than no skill on five of six**, and
nearly doubled bento-hero failures. The gate reduced failures to zero on three
components. The model reads “be distinctive” as “add more”, and more is the
slop.

So this skill does not ask you to “avoid AI slop”. It gives you:

1. A **40-item binary gate** ([`templates/14-slop-audit.html`](templates/14-slop-audit.html)).
2. A **script** that checks the source ([`scripts/sogeti_audit.py`](../scripts/sogeti_audit.py)).
3. A **brand system** with enough constraints that the default is already
   specific.

Read the principles, then run the gate. The gate wins.

---

## 2. Ten laws

1. **Slop is the absence of decisions, not the presence of a style.** The tell
   is not Inter. The tell is Inter, unchosen, next to twenty other defaults.
2. **One tell is noise; density is the signal.** Three hits descending from one
   toolchain default are one decision, not three.
3. **The tells decay; the mechanism does not.** Purple was 2024. Cream, emerald
   and the oversized italic serif are the 2026 reflex. Do not trade one default
   for another.
4. **Defaults come from the toolchain.** Tailwind, shadcn/ui, Lucide and Framer
   Motion emit their demo styles. Sogeti's system is deliberately not those
   defaults.
5. **Prose advice backfires; binary gates work.** Encode the constraint.
6. **Slop is a copy problem wearing a CSS costume.** A perfect type system over
   “Elevate your workflow” still reads machine-made.
7. **Functional slop outranks aesthetic slop.** Broken contrast, missing focus,
   invisible content and fabricated proof harm people. A gradient merely
   embarrasses the owner.
8. **Overcorrection is slop in the other direction.** Custom cursors, parallax
   everywhere, a “distinctive” serif and a beige ground are not a system.
9. **Every pattern is legitimate with a job.** Glass solves layering. Dark glow
   is Linear's hand-built house style. The defect is the missing job.
10. **Distinctiveness is a constraint you encode, not a vibe you prompt.**
    Sogeti's brand is the constraint: Ubuntu Mono, Capgemini Blue, the shape,
    sentence case, evidence.

---

## 3. What the 2026 tells look like

### Colour and surface

- Indigo/violet gradients (`#6366F1`, `#8B5CF6`, `#A855F7`).
- Gradient text on a heading or a number.
- Neon cyan on near-black, a radial glow behind the hero, coloured box shadows.
- Glassmorphism where nothing overlaps.
- The 2026 replacement: cream/beige ground, amber accent, oversized italic
  serif. This is now as reflexive as purple was.
- The 3–4 px coloured stripe on ordinary cards. Keep stripes for real status.

### Type

- Inter/Geist as the only family, or a declared webfont with no file served.
  “Declaring is not shipping.”
- The escape-hatch trio: Space Grotesk, Instrument Serif, Fraunces, chosen
  because Inter was called out.
- A huge italic serif headline, or one serif-italic word inside a sans headline.
- A pill/eyebrow chip directly above a centered display headline, often with
  tracked uppercase and “New” or “v2.0”.
- A rounded-square icon container above every feature heading.

### Layout

- The centered SaaS hero: badge → 64 px sentence → one-line subhead → gradient
  primary + ghost secondary → orb.
- Exactly three equal feature cards, regardless of the content's cardinality.
- Bento grids where the tiles do not differ in kind.
- The cookie-cutter order: hero → logo wall → three cards → testimonial → stats
  → pricing → FAQ → CTA.
- A grayscale logo wall and “500K users / 99.9% uptime” counters.
- Fake browser chrome or a tilted dashboard on a product that is neither.
- One spacing value everywhere; nothing loud, so nothing quiet.
- One border radius on cards, inputs, buttons and images; or a hairline border
  plus a wide shadow on every card.

### Copy

- “Build faster. Ship smarter.” Headlines that survive a competitor's logo swap.
- The buzzword layer: streamline, supercharge, empower, unlock, elevate,
  seamlessly, world-class, enterprise-grade, best-in-class, robust.
- “In today's fast-paced world.”
- Negative parallelism: “It's not just X, it's Y.” / “Not a feature. A platform.”
- The rule of three: “Innovate. Transform. Thrive.”
- Spaced em dashes several times per paragraph.
- Claims with no number, name, date or mechanism.

### Interaction

- Identical fade-up on every section, uniform stagger.
- Hover-scale + shadow bloom on non-actionable cards.
- Cursor followers, parallax layers, typewriter text, confetti on a save.
- A theme toggle as decoration, with no designed second mode.
- Auto-playing marquees without pause controls.

### Imagery and data

- Glossy 3D blobs, floating primitives, robot hands, synthetic diverse teams.
- Isometric servers/clouds/shields arranged with no referent to the actual
  system.
- Impossible architecture, six fingers, garbled background signage.
- Fake dashboards, invented metrics, meaningless sparklines.
- Rainbow categorical palettes, 3D pies, no axes, no units, no baseline.
- Animated counters with no source.

---

## 4. Sogeti-specific traps

The generic tells are not enough. These are the ones this brand is most likely
to produce.

### 4.1 “Sogeti blue everywhere”

Capgemini Blue is strong. A blue hero, blue section, blue cards and blue footer
turn the page into a colour block and flatten the hierarchy. **One large blue
field per page.** Use Cool Grey and white for the rest.

### 4.2 Isometric decoration

Sogeti's illustration system is isometric, so an isometric image is not
automatically slop. The defect is an isometric image that **does not explain the
argument**: floating servers, random cubes, a cloud with no referent. Use the
provided illustrations as captioned diagrams, or do not use one. Never put an
isometric icon tile above every heading.

### 4.3 The three-pillar consulting page

“Strategy. Technology. People.” Three equal cards, three icons, three lines.
Real consulting work rarely divides into three equal parts. Let the argument's
cardinality decide the layout. The pursuit template uses a brief grid because
the brief genuinely has three parts; the workshop uses six themes because there
were six.

### 4.4 The fake dashboard

A hero screenshot with invented metrics and impossible ratios is a promise the
product cannot keep. Use a real screen at real density, or a diagram of the
actual system with a caption. If the data is illustrative, label it.

### 4.5 Stock “transformation” photography

A perfect, impossibly lit team mid-laugh at one laptop. Sogeti's photography
guidance asks for candid, natural, contextual images with rights. If you do not
have them, use type, a diagram or a real artifact. Do not generate a synthetic
team.

### 4.6 The AI-generated authority voice

“In today's rapidly evolving landscape, organizations must harness the power of
AI to unlock unprecedented value.” This is not a point of view. Replace it with
a specific observation, a mechanism and a consequence.

### 4.7 Dark mode as a personality

The live Sogeti site currently ships dark by default. That is a product
decision, not a brand rule. This skill defaults to light because Cool Grey is
the documented background, consulting artifacts are read in daylight and print,
and dark doubles the contrast surface. Use dark for a stage, a film or an
evening event, not to make a document look “tech”.

### 4.8 The overcorrection

Cream paper, italic serif and a rust accent is the 2026 “tasteful AI” reflex.
Sogeti is a blue, mono, precise brand. Do not sand it into a lifestyle magazine
to prove you are not generic.

---

## 5. Brand-authorized patterns (do not flag these)

The gate checks for patterns, not intent. These are legitimate in Sogeti work
when they have a job:

| Pattern | Why it is allowed |
|---|---|
| Capgemini Blue fields | Brand primary; one per page |
| The brand shape | Brand architecture, not decoration |
| Pill buttons | The brand's control shape; use one radius system |
| Ubuntu Mono display | The brand's top-tier headline face; sparingly |
| Kicker labels | Sentence-case category metadata, not a tracked uppercase chip |
| Isometric illustration | Brand system; must be captioned and explain the argument |
| Deep Purple panels | Brand secondary; use sparingly |
| Red status dots | Semantic, with a text label |
| 3-column brief grids | Only when the content genuinely has three parts |

If a reviewer flags one of these, ask what job it is doing and whether the
execution follows the brand rules. Do not remove the brand to satisfy a
generic checklist.

---

## 6. The gate

### 6.1 Tiers

- **Tier 1 – Blockers (8).** Any hit = do not ship. Contrast, focus, content at
  rest, form validation, 360 px overflow, fabricated proof, chart axes, alt text.
- **Tier 2 – Identity tells (19).** 0–1 clean · 2 review · 3–5 likely slop ·
  6+ rewrite the page, do not restyle it.
- **Tier 3 – Craft (8).** Corroborating only.
- **Tier 4 – Copy (5).** Rate-based; density matters.

### 6.2 Scoring

- Any Tier 1 hit → **FAIL**, regardless of total.
- Tier 2: 0–1 **PASS** · 2 **REVIEW** · 3+ **FAIL**.
- Tier 3 and 4 do not change the verdict on their own; they inform the rewrite.
- Weight **co-occurrence** over count. Three hits from one toolchain default are
  one decision.
- The pass condition is **subtraction**. Fixing a failure by adding a gradient
  trades one default for another.

### 6.3 Run the gate

```bash
python3 scripts/sogeti_audit.py path/to/artifact.html
python3 scripts/sogeti_audit.py references/templates/*.html
```

The script checks self-containment, headings, labels, alt text, focus/motion
handling, brand fonts and colours, placeholder copy, banned phrases, em dashes,
chart titles, card/shadow/stripe patterns and more. It is conservative: a hit
means “present; confirm the job”.

### 6.4 The manual pass

The script cannot see everything. Before shipping:

1. **Keyboard.** Tab through every interactive element. Is focus visible? Can
   you reach the export button? Can you close the menu?
2. **360 px.** Set the viewport to 360 px. Is there horizontal overflow? Does
   the display type still work? Do tables scroll inside their wrapper?
3. **200% zoom.** Does the layout survive?
4. **Print.** Save to PDF. Are the header, footer and buttons hidden? Do cards
   split across pages? Is the chart legible?
5. **Content.** Does every number have a source or an “illustrative” label? Does
   every quote have an approval? Does the headline pass the logo-swap test?
6. **Brand.** Is the logo the master artwork? Is the shape used once, with
   margins? Is Mono used once, not on every heading? Is the red used as an accent, not a
   field?

---

## 7. Replacement patterns

Do not just delete the tell. Replace it with something that has a job.

| Tell | Replacement |
|---|---|
| Centered hero + gradient CTA | Asymmetric hero with a specific claim and one action |
| Three equal feature cards | A numbered argument, a table, or a diagram with the real cardinality |
| Icon tile above every heading | Icon beside the heading, or no icon |
| Grayscale logo wall | One named client with a real quote and permission |
| Counting stats | One number, a source, a date and a baseline |
| Fake dashboard | A real screen or a system diagram with annotations |
| Isometric decoration | A captioned diagram of the actual handover |
| Gradient text | One solid brand colour and a larger type size |
| Glass nav | Opaque surface with a hairline rule |
| Universal fade-up | One orchestrated page-load moment; static sections |
| Theme toggle | One designed mode, or two fully designed modes |
| “Elevate / unlock / seamless” | A specific verb, number and mechanism |

---

## 8. False positives

Almost every pattern was invented by a human designer first. A detector without
a baseline measures the web, not the machine.

- Purple is a real brand colour. The defect is the unchosen gradient.
- Dark mode with glow was hand-built by Linear, Raycast and Reflect. Weak alone.
- Inter is a deliberate choice at Linear. The tell is the unchosen default.
- Glass legitimately solves overlay-on-imagery.
- Three-card rows and centered heroes are effective conversion layouts. The
  defect is forcing content into three.
- Logo walls, stats and testimonials are fine when real and verifiable.
- Coloured left borders are fine for semantic alerts.
- Serif display, editorial layouts, cream and bento are legitimate for many
  products. The defect is register mismatch or a substitute for a decision.
- **Quoting a slop pattern in a checklist is not using it.** The audit ignores
  `.slop-item` text for this reason.

Attribution is not a moral judgement. “AI-assisted” is not an insult. The
useful question is: **what decision is missing?**

---

## 9. Sources

Primary catalogues and studies:

- Impeccable, *Slop* (68 patterns, 62 machine-checkable) –
  https://impeccable.style/slop
- Signs of AI design (Reliability, Status, false positives) –
  https://github.com/febbhav/signs-of-ai-design
- Krebs, *Scoring Show HN submissions* (1,590 pages, 16 checks, 5–10% false
  positives), 20 April 2026 – https://www.adriankrebs.ch/blog/design-slop/
- Solo Design Studio, *AI design slop: the tells* (three-arm test), 6 June 2026 –
  https://solodesign.cc/blog/ai-design-slop-the-tells/
- Hallmark, Floor / Reflex / Finish gates –
  https://github.com/Nutlope/hallmark
- TailThemes, *AI design slop quality gate*, 20 August 2026 –
  https://tailthemes.com/blog/ai-design-slop-quality-gate
- 925Studios, *AI slop web design guide*, 19 March 2026 –
  https://www.925studios.co/blog/ai-slop-web-design-guide
- Wikipedia, *AI slop* – https://en.wikipedia.org/wiki/AI_slop
- Wikipedia, *Signs of AI writing* –
  https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- Simon Willison, *Slop*, 8 May 2024 –
  https://simonwillison.net/2024/May/8/slop/
- Datawrapper, colour guidance –
  https://www.datawrapper.de/academy/what-to-consider-when-choosing-colors-for-data-visualization

The full annotated list, including the HN thread and the pre-2023 baseline
caveat, is in the research report.
