# Sogeti on the web, 2026

A synthesis of the live-site audit in
[`reference/research/SOGETI_DIGITAL_BRAND_REPORT.md`](../reference/research/SOGETI_DIGITAL_BRAND_REPORT.md),
with a clear recommendation for HTML artifacts. The PDF remains the brand
authority; the live site is evidence of current practice, not a new rulebook.

---

## 1. What the live site actually runs

- **Platform:** WordPress 7.0.8, theme `sogeti2024` v1.0.33, Bootstrap 5.3.3,
  GSAP 3.12.5 + ScrollTrigger.
- **Design system:** Capgemini Group's **Zodiak** token layer (`--zodiak-*`),
  with a legacy Bootstrap-derived `--sogeti-bs-*` layer bolted on top.
- **Theme:** dark by default (`<html data-cg-theme="dark">`), with a real,
  accessible theme switch. There is no documented dark palette in the 2024 PDF.
- **Type:** Ubuntu 300/400/500 and Ubuntu Mono 400/700, self-hosted as raw
  `.ttf` in sixteen inline `@font-face` blocks. WOFF2 is not used.
- **Headlines:** Ubuntu Light 300 / Regular 400, 2.5 rem hero, zero optical
  tracking. Mono is used for eyebrows, bylines, tags and data labels, not
  headlines.
- **Logo:** a two-shape SVG, wordmark `#0058AB` plus red dot `#F53B53`,
  viewBox 71×37 (1.92:1). The wordmark is Sogeti's own blue, not Capgemini Blue.
- **Imagery:** full-bleed video and a 3D yeti mascot (“Geti”). No isometric
  illustration system on the homepage.
- **Icons:** Tabler Icons plus a proprietary Zodiak set.

These are product decisions. Some are good, some are drift. Do not copy them
blindly into a brand artifact.

---

## 2. Where the site diverges from the PDF

| Area | PDF (2024) | Live site (2026) | This skill |
|---|---|---|---|
| Surface | Cool Grey is the go-to background | Dark mode is the default | Light-first; dark only with a reason |
| Deep Purple | Secondary palette | Zero occurrences | Kept as a tertiary/editorial colour |
| Headlines | Mono Bold at the top tier | Ubuntu Light/Regular, mono demoted | Mono display for the signature moment; Ubuntu for H2/H3 |
| Cool Tech Red | `#F53B53` | Six variants (`#FF4F66`, `#DB2443`, `#F64059`, …) | `#F53B53` for graphics/large text; `#DB2443` for red buttons; `#A31335` for small text |
| Logo blue | Capgemini Blue + Vibrant Blue | Wordmark `#0058AB` | Reference assets use the PDF's `#0070AD` lockup |
| Illustration | Isometric system | Video + 3D mascot | Captioned, diagrammatic isometric illustrations |
| Type loading | Brand fonts | Raw TTF, duplicated faces | Subset WOFF2, embedded base64 |

**Do not** treat the live site as the source of truth for an external brand
artifact. If a client asks for parity with the live site, confirm which template
and which theme they mean, and document the choice.

---

## 3. What to follow from the live practice

These are genuinely good and compatible with the PDF:

1. **Sentence case is real.** The live copy uses it almost everywhere. Keep it.
2. **Pill controls are consistent.** `border-radius: 999px`, 38/48/56 px heights,
   clear labels. The skill uses the same control language.
3. **Flat surfaces.** Cards are flat with a small radius and no heavy shadow.
4. **The logo is always “Sogeti”.** Title case, no accent, no all-caps.
5. **The voice is peer-to-peer.** Short headlines, second person, rhetorical
   questions, a deliberate full stop for emphasis. Use it, without the
   grammatical slips.
6. **Accessibility is taken seriously in public.** The site publishes a WCAG
   2.1 AA statement with its own non-conformities. That transparency is a model
   for artifacts. (See section 6.)
7. **Native disclosure widgets.** The AI microsite uses 118 `wp-block-details`
   elements rather than custom div accordions. The skill uses
   `details/summary`.

---

## 4. What not to copy

1. **Dark mode as the default for a document.** A consulting artifact is read in
   daylight, printed and projected. Light-first is the better default; dark is
   an event/stage choice.
2. **Light 300 at 40 px for a hero.** It looks elegant on a retina display and
   thin on a projector. Mono display or a stronger Ubuntu weight is more
   robust.
3. **Six reds.** Pick three roles: brand accent, action, text. Document them.
4. **Raw TTF and duplicate font faces.** Embed subset WOFF2; ship the file.
5. **Bootstrap defaults left in the token layer** (`#0d6efd`). They leak into
   components.
6. **Fake or unverified trust chrome.** Logo walls, counters and badges need
   evidence.
7. **A 1 px near-invisible focus ring.** The skill uses a 3 px red ring with a
   3 px offset.
8. **Motion without a reduced-motion guard.** GSAP scroll effects are not
   automatically accessible.

---

## 5. Digital adaptations in this skill

The PDF is print-first. The skill adapts it deliberately:

- **Display:** Ubuntu Mono Bold for the hero/claim; Ubuntu 700/500 for H1–H3.
- **Body:** Ubuntu Regular at 17 px, not Light. Light for leads ≥20 px.
- **Surfaces:** Cool Grey/white; one Capgemini Blue field per page.
- **Red:** `#F53B53` for graphics and large text; `#DB2443` for red actions;
  `#A31335` for small red text.
- **Shapes:** the primary shape is a field, not a card. One per page.
- **Icons:** thin-line UI icons; isometric only for topic diagrams.
- **Motion:** one page-load moment, hover colour transitions, reduced-motion
  guard. No scroll-triggered everything.
- **Dark mode:** not the default; if used, design both modes, not a filter.

These adaptations are documented so a brand reviewer can challenge them
individually rather than discovering them by accident.

---

## 6. The public accessibility statement

The Sogeti site states **WCAG 2.1 Level AA**, **partial compliance**, audited in
November 2024 by Capgemini Group IT, with **48 of 68 criteria compliant, 10
non-compliant, 10 not applicable (83%)**. It publishes the failures, including
missing captions, keyboard traps, contrast issues, an unclosed div, duplicate
form labels and non-descriptive link titles.

Use the statement as a benchmark, not a shield:

- Target **WCAG 2.2 AA** for artifacts.
- Caption video; provide transcripts.
- Test the keyboard path; do not create traps.
- Check contrast against the real background.
- Validate HTML structure.
- Use one label per control.
- Write descriptive link text.
- Make errors readable by a screen reader.

The statement's transparency is worth emulating in an internal QA note: name
what you did not fix, and why.

---

## 7. Voice examples worth studying

From the live site (quoted in the research report):

- “Got a minute?”
- “BIG results start with the RIGHT guide.”
- “Ready when you are.”
- “Do you trust your AI?”
- “Cutting-edge solutions, world-leading tech, local delivery.”
- “The future belongs to the tech explorers and the innovators.”
- “Challenges feel smaller when your partner feels bigger.”
- “Technology doesn't need to be complicated to deliver real results.”
- “85% of AI projects fail to move beyond pilots.”
- “Right here. Right now.”

What works: brevity, second person, a question, a full stop used as emphasis,
one all-caps word for stress (used sparingly), a concrete number.

What does not: “cutting-edge solutions, world-leading tech, local delivery” is a
triad of abstractions; “the future belongs to…” is a weightless headline; the
service names (“Gen AI Augmented Software House”, “GreenFinOps Cloud
Optimization”) are jargon. Use the rhythm, not the abstractions.

---

## 8. Digital artifacts worth studying

| Artifact | URL | What to learn |
|---|---|---|
| AI in Action microsite | https://www.sogeti.com/make-way-for-ai-in-action/ | Native disclosures, bespoke blocks, long-form pacing |
| Reports library | https://www.sogeti.com/insights/reports/ | Faceted archive; check the hydration/placeholder defect |
| Meet Geti | https://www.sogeti.com/about-us/meet-geti/ | The fullest expression of the current voice |
| SogetiLabs | https://www.sogeti.com/about-us/sogetilabs/ | Sub-brand naming and thought leadership |
| Executive summits | https://www.sogeti.com/insights/executive-summits/ | Event-page structure |
| Client stories | https://www.sogeti.com/client-stories/ | Case-study structure |
| Accessibility | https://www.sogeti.com/accessibility/ | Public conformance disclosure |

Do not copy the Reports page's unrendered `{{ title }}` placeholder or the stray
“Access Denied” heading. They are production defects, not design patterns.

---

## 9. Sources

- Live site and CSS bundles, retrieved November 2026. Raw evidence in
  [`reference/research/`](../reference/research/).
- Sogeti accessibility statement,
  https://www.sogeti.com/accessibility/, dated 27 November 2024.
- *Sogeti brand guidelines v3*, November 2024,
  [`reference/Sogeti-brand-V3-guidelines.pdf`](../reference/Sogeti-brand-V3-guidelines.pdf).
- Full audit:
  [`reference/research/SOGETI_DIGITAL_BRAND_REPORT.md`](../reference/research/SOGETI_DIGITAL_BRAND_REPORT.md).

No public Capgemini brand hub URL could be verified; do not cite one.
