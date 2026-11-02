# Catalog: 14 reference artifacts

Every file is a self-contained HTML document with embedded fonts, logo and
images. Open the gallery: [`templates/index.html`](templates/index.html).

| # | File | Job | Reader | Signature element | Interactive |
|---|---|---|---|---|---|
| 01 | [`01-insight-article.html`](templates/01-insight-article.html) | Change a belief | Client, market | Mono display + shape field | Copy summary |
| 02 | [`02-pursuit-one-pager.html`](templates/02-pursuit-one-pager.html) | Win a discovery | Client executive | Cover panel + value case | Copy exec summary, print |
| 03 | [`03-steerco.html`](templates/03-steerco.html) | Get three decisions | Steering group | RAG strip + delivery chart | Decision checkboxes, export |
| 04 | [`04-architecture.html`](templates/04-architecture.html) | Approve a boundary | CTO, architecture board | Current/target diagrams | Tabs |
| 05 | [`05-workshop-synthesis.html`](templates/05-workshop-synthesis.html) | Turn talk into decisions | Workshop attendees | Theme board | Select themes, filter, export |
| 06 | [`06-maturity-assessment.html`](templates/06-maturity-assessment.html) | Start an evidence conversation | CIO, AI lead | Live radar | 8 sliders, export |
| 07 | [`07-options-appraisal.html`](templates/07-options-appraisal.html) | Expose the weighting | Decision group | Weighted matrix | Weights, scores, presets, export |
| 08 | [`08-case-study.html`](templates/08-case-study.html) | Make the outcome credible | Prospective client | Dark outcome opener | Copy summary |
| 09 | [`09-event.html`](templates/09-event.html) | Fill the room | Invited executive | Square event card | ICS download, copy details |
| 10 | [`10-playbook.html`](templates/10-playbook.html) | Turn method into action | Delivery team | 20 checks + progress | Saved checks, export |
| 11 | [`11-data-story.html`](templates/11-data-story.html) | Make a finding legible | Research reader | Data opener + two charts | Copy findings |
| 12 | [`12-deck.html`](templates/12-deck.html) | Land an argument | Executive audience | 16:9 slides | Keyboard nav, notes, print |
| 13 | [`13-decision-brief.html`](templates/13-decision-brief.html) | Record a decision | Decision owner | Decision memo (two pages when printed) | Decision record, print |
| 14 | [`14-slop-audit.html`](templates/14-slop-audit.html) | Gate a design | Design reviewer | 40-item gate | Live verdict, export |

---

## 1. Choose by request

| If the user asks for… | Start from |
|---|---|
| “A thought-leadership piece / POV / article” | 01 |
| “A proposal / pitch / one-pager for a client” | 02 |
| “A status report / steerco / programme update” | 03 |
| “An architecture / solution design / current vs target” | 04 |
| “A workshop readout / synthesis / discovery summary” | 05 |
| “An assessment / diagnostic / maturity model” | 06 |
| “A comparison / options / build vs buy” | 07 |
| “A case study / client story / proof point” | 08 |
| “An event / summit / roundtable page” | 09 |
| “A playbook / field guide / checklist” | 10 |
| “A research report / data story / survey” | 11 |
| “A deck / presentation / readout” | 12 |
| “A decision memo / one-pager / sign-off” | 13 |
| “A design review / quality gate / slop check” | 14 |
| “A gallery / index of all of the above” | `index.html` |

If the request is a hybrid, choose the **job**, not the format. A “proposal
deck” is a deck (12) if it is presented, a pursuit (02) if it is read. A
“workshop report” is a synthesis (05), not an article (01).

---

## 2. What each file demonstrates

- **01 Insight article** – long-form editorial layout, sticky contents, a
  captioned isometric diagram, a quote treatment, a one-page summary export.
- **02 Pursuit** – a cover with the 2-colour logo, a brief grid, a phased
  approach, a value-case table with planning assumptions, a sign-off block.
- **03 Steerco** – RAG semantics, a decision list, a delivery-confidence chart
  with an honest projection, risk/action tables, print-friendly density.
- **04 Architecture** – functional diagrams (not decorative tech art), tabs,
  ADR table, “what we are not doing”, cutover rules.
- **05 Workshop synthesis** – a selectable theme board, filters, live count and
  Markdown export, decision register.
- **06 Assessment** – eight range inputs, a live SVG radar, a table fallback,
  dynamic recommendations, `localStorage`-free state.
- **07 Appraisal** – weighted matrix, select inputs, weight presets, live ranking
  and a recommendation that names the criterion doing the work.
- **08 Case study** – a dark blue hero, a 9→3 outcome, a handover figure, an
  outcomes table with a caveat, “what we would do differently”.
- **09 Event** – a square save-the-date card, agenda, roles instead of stock
  portraits, an ICS download, practical details.
- **10 Playbook** – 20 checks, saved progress, field notes, print, export.
- **11 Data story** – a data opener, direct-labelled bars, a grouped chart with
  axes, method and limits, a caveat.
- **12 Deck** – eight slides, keyboard navigation, speaker notes, fullscreen,
  print to PDF, no slideware.
- **13 Decision brief** – a decision memo, decision box, options, conditions,
  risks, sign-off, decision record export.
- **14 Slop audit** – 40 checks, four tiers, live verdict, false-positive
  discipline, export.

---

## 3. Reading order

If you are new to the skill:

1. [`brand-foundations.md`](brand-foundations.md) – the system.
2. [`anti-slop.md`](anti-slop.md) – the gate.
3. [`templates/01-insight-article.html`](templates/01-insight-article.html) –
   the editorial voice.
4. [`templates/03-steerco.html`](templates/03-steerco.html) – the data voice.
5. [`templates/14-slop-audit.html`](templates/14-slop-audit.html) – the gate as
   a tool.
6. [`templates/index.html`](templates/index.html) – the shelf.

For a specific task, use the table in section 1 and read the template's source
in `references/templates/_src/`.

---

## 4. Documentation map

| File | Use |
|---|---|
| [`brand-foundations.md`](brand-foundations.md) | Positioning, logo, colour, type, shapes, imagery, page map |
| [`color-system.md`](color-system.md) | Palette, tints, contrast, chart groups |
| [`typography.md`](typography.md) | Faces, scale, rules, fallback |
| [`logo-and-shapes.md`](logo-and-shapes.md) | Logo versions, clear space, shape geometry |
| [`voice-and-copy.md`](voice-and-copy.md) | Tone, mechanics, banned phrases, rewrites |
| [`design-system.md`](design-system.md) | Tokens, layouts, components, build |
| [`design-system-visual.html`](design-system-visual.html) | The system on one page, in the browser |
| [`data-visualization.md`](data-visualization.md) | Chart choice, anatomy, accessibility |
| [`accessibility.md`](accessibility.md) | WCAG 2.2 AA, keyboard, print, testing |
| [`content-models.md`](content-models.md) | Narrative, scenario, page structures, proof rules |
| [`anti-slop.md`](anti-slop.md) | Ten laws, Sogeti traps, the 40-item gate |
| [`quality-gates.md`](quality-gates.md) | The ship process |
| [`web-and-digital.md`](web-and-digital.md) | The 2026 live-site audit and digital adaptations |
| [`recipes.md`](recipes.md) | Copy-paste HTML blocks |
| [`catalog.md`](catalog.md) | This file |

The raw research is in [`reference/research/`](../reference/research/), and the
source PDF is [`reference/Sogeti-brand-V3-guidelines.pdf`](../reference/Sogeti-brand-V3-guidelines.pdf).
