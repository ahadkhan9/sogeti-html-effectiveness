---
name: sogeti-html-effectiveness
description: Produce brand-faithful, interactive, self-contained single-file HTML artifacts for Sogeti – insight articles, pursuit one-pagers, steerco packs, architecture views, workshop syntheses, maturity assessments, options appraisals, client stories, event pages, playbooks, data stories, executive decks, decision briefs and design audits. Use whenever the user asks for Sogeti-branded HTML, a client-ready visual deliverable, a rich alternative to a deck or document, or an anti-AI-slop design review. Includes the Sogeti brand system, 14 reference templates, a 40-item gate and a mechanical audit script.
---

# Sogeti HTML effectiveness

Text and Markdown flatten spatial information. A diff, a handover, a weighted
choice, a maturity profile or a steerco decision becomes a wall of paragraphs
that is hard to disagree with precisely. A single-file HTML artifact gives the
work a 2D surface: real typography, side-by-side options, live states, a print
path and a one-click export that closes the loop back into the conversation.

This skill is not a prompt that says “make it beautiful”. It is a **system**:

- the Sogeti brand, translated into tokens and components;
- 14 reference artifacts that show the standard;
- a build step that produces one portable file;
- a mechanical gate that catches AI slop and accessibility failures;
- a writing and evidence discipline that keeps the page honest.

The test of a good artifact is not “does it look designed?” It is: **can the
reader make the decision without you in the room?**

---

## 1. Non-negotiables

1. **Save into `html-docs/`.** Every artifact goes in
   `<project-or-working-dir>/html-docs/<name>.html`. Create the folder if it
   does not exist. Link it in the response:
   `[Artifact name](file:///absolute/path/to/html-docs/<name>.html)`.
2. **One file, zero network dependencies.** No CDN, webfont, icon pack, chart
   library, analytics or tracker. Fonts, logo and images are embedded. Build
   with `scripts/build.py`; audit with `scripts/sogeti_audit.py`.
3. **Sogeti brand first.** Capgemini Blue, Vibrant Blue, Cool Grey, Deep Purple,
   Cool Tech Red, Ubuntu and Ubuntu Mono, the primary shape, sentence case.
   The brand PDF is the authority, not the live site.
4. **No fabricated proof.** No invented statistic, client, logo, quote, award or
   certification. Illustrative data is labelled as illustrative. Every number
   has a source, a date and a base, or a visible “illustrative” note.
5. **Gate before ship.** Run the audit, then the 360 px, keyboard, 200% zoom and
   print passes. Aesthetically pleasing but inaccessible is not done.
6. **One job per page.** Choose the artifact by the job, not by the format. A
   proposal that is presented is a deck; a proposal that is read is a pursuit.
7. **Close the loop.** Interactive artifacts end with a labelled export that
   produces Markdown a reader can paste into a decision record, brief or chat.
8. **Do not add a second design system.** No Tailwind, shadcn, Lucide, Framer
   Motion, Inter, gradient meshes, glass or dark-mode decoration. The constraint
   is the brand.

---

## 2. When to use HTML (and when not to)

| Use HTML when… | Use something else when… |
|---|---|
| The work is spatial: options, architecture, a journey, a dashboard | The client requires Word with tracked changes |
| The reader needs to interact: score, weight, select, filter, export | The deliverable is a signed contract or a regulated filing |
| The artifact will be read on screen and possibly printed | It must be editable by a non-technical author in Office |
| You want one file that works offline and can be emailed | A 60-slide deck is the expected social object |
| The design itself is part of the argument | The content is a short email or a chat answer |
| A PDF would flatten the comparisons | The page has no decision, no comparison and no interaction |

HTML is not a replacement for every document. It is the right surface when
**layout carries meaning**.

---

## 3. Sogeti in 60 seconds

- **Proposition:** making value. Hands-on technology partner; viable outcomes at
  speed; local proximity, global scale.
- **Brand line:** *The magic is in the making.* Use it sparingly.
- **Palette:** Capgemini Blue `#0070AD`, Vibrant Blue `#12ABDB`, Cool Grey
  `#F5F5F7`, Deep Purple `#2B0A3D`, Cool Tech Red `#F53B53`, white.
  Sogeti Red `#FF4019` is the logo i-dot only.
- **Type:** Ubuntu; Ubuntu Mono Bold for the top-tier display headline only;
  sentence case; Verdana fallback.
- **Shape:** a rectangle with the bottom-right corner scooped by a quarter
  circle. One primary shape per composition. It is architecture, not wallpaper.
- **Voice:** professional yet conversational, International English, short
  sentences, specific claims, no jargon, no “elevate/unlock/seamless”.
- **Look:** Cool Grey or white ground, one blue field, one oversized mono
  moment, hairline rules, flat surfaces, no wide shadows, restrained motion.

Full detail: [`references/brand-foundations.md`](references/brand-foundations.md)
and [`references/color-system.md`](references/color-system.md).

---

## 4. The shelf: 14 artifacts

Open the gallery: [`references/templates/index.html`](references/templates/index.html).

| # | Artifact | Job | Start from |
|---|---|---|---|
| 01 | Insight article | Change a belief | `01-insight-article.html` |
| 02 | Pursuit one-pager | Win a discovery | `02-pursuit-one-pager.html` |
| 03 | Steering group | Get three decisions | `03-steerco.html` |
| 04 | Architecture view | Approve a boundary | `04-architecture.html` |
| 05 | Workshop synthesis | Turn talk into decisions | `05-workshop-synthesis.html` |
| 06 | Maturity assessment | Start an evidence conversation | `06-maturity-assessment.html` |
| 07 | Options appraisal | Expose the weighting | `07-options-appraisal.html` |
| 08 | Client story | Make the outcome credible | `08-case-study.html` |
| 09 | Event page | Fill the room | `09-event.html` |
| 10 | 90-day playbook | Turn method into action | `10-playbook.html` |
| 11 | Data story | Make a finding legible | `11-data-story.html` |
| 12 | Executive deck | Land an argument | `12-deck.html` |
| 13 | Decision brief | Record a decision | `13-decision-brief.html` |
| 14 | Slop audit | Gate a design | `14-slop-audit.html` |

Selection matrix and what each demonstrates:
[`references/catalog.md`](references/catalog.md).

---

## 5. Workflow

### Step 0 – Write the artifact brief

Fill this before touching HTML:

```
Job:
Reader:
Decision or action:
One thing they should remember:
What they should do next:
Evidence I already have:
Evidence I must not invent:
Format: (article / pursuit / steerco / architecture / workshop / assessment /
         appraisal / case study / event / playbook / data story / deck /
         decision brief / audit)
Tone: (default Sogeti / more formal / more conversational)
Constraints: (length, print, mobile, accessibility, approvals)
```

If the job and the reader are unclear, ask. Do not build a beautiful page for an
unclear decision.

### Step 1 – Gather the evidence

Read the real brief, transcript, deck, spreadsheet or repo. Use real names,
numbers and quotes where they exist. Where they do not, write around the gap or
label the content as illustrative. Never fill a gap with a plausible invention.

### Step 2 – Choose the archetype and the signature moment

Pick the artifact by job. Then pick **one** signature move:

- a mono display claim;
- a primary shape field;
- a functional architecture diagram;
- a live chart or assessment;
- a document-grade table;
- a single large number.

Not all of them. One oversized moment per page. Everything else supports it.

### Step 3 – Start from the closest template

```bash
cp references/templates/01-insight-article.html \
   /path/to/project/html-docs/my-artifact.html
```

Or copy a source template from `references/templates/_src/` and keep the
partials. If starting from scratch, copy `examples/starter.html`.

Keep the head, skip link, shape defs, header and footer. Replace the content and
the sections. Do not start from a blank page and re-invent the type scale.

### Step 4 – Write the content

Use [`references/voice-and-copy.md`](references/voice-and-copy.md). The short
version:

- sentence case;
- International English, American spelling;
- short sentences, one idea per paragraph;
- no em dashes, no rule-of-three slogans, no “elevate/unlock/seamless”;
- every number has a unit, a base and a source or an illustrative label;
- every quote is approved or labelled composite;
- the headline passes the logo-swap test.

### Step 5 – Build and inline

Source templates link `../../../assets/sogeti.css` and the local images. Build:

```bash
python3 scripts/build.py path/to/source.html
```

The build expands `<!-- @include _partials/... -->`, inlines the CSS (with the
base64 fonts), inlines the JS, and embeds local images as data URIs. The output
is one portable `.html` file. The build prints a warning if a remote asset
remains.

### Step 6 – Run the gate

```bash
python3 scripts/sogeti_audit.py path/to/built.html
```

Then the manual pass:

- 360 px: no horizontal scroll; display type still works.
- keyboard: skip link, focus visible, every action reachable.
- 200% zoom: no overlap or clipping.
- print/PDF: chrome hidden, no broken cards, charts legible in greyscale.
- content: every number sourced or labelled; every quote approved.

The full process is [`references/quality-gates.md`](references/quality-gates.md).

### Step 7 – Save, link and explain

Save to `html-docs/`. Link the file with an absolute path. In the response, name
the artifact's job, the one signature decision, and any evidence the user still
needs to verify. Do not paste the entire HTML into chat.

---

## 6. The anti-slop gate

The research is unambiguous: **prose advice backfires; binary gates work.**
Telling a model to “be distinctive” makes it add more. The gate makes it remove.

### 6.1 Ten laws

1. Slop is the absence of decisions, not the presence of a style.
2. One tell is noise; density is the signal.
3. The tells decay; the mechanism does not. Purple → cream/italic serif is the
   2026 replacement reflex.
4. Defaults come from the toolchain. Do not ship the toolchain's demo.
5. Prose advice backfires; encode constraints.
6. Slop is a copy problem wearing a CSS costume.
7. Functional slop outranks aesthetic slop.
8. Overcorrection is slop in the other direction.
9. Every pattern is legitimate with a job.
10. Distinctiveness is a constraint you encode, not a vibe you prompt.

### 6.2 The 40-item gate

The interactive gate is
[`references/templates/14-slop-audit.html`](references/templates/14-slop-audit.html).
The source checker is [`scripts/sogeti_audit.py`](scripts/sogeti_audit.py).

- **Tier 1 – Blockers (8).** Any hit = fail.
- **Tier 2 – Identity tells (19).** 0–1 clean · 2 review · 3+ fail.
- **Tier 3 – Craft (8).** Corroborating.
- **Tier 4 – Copy (5).** Rate-based.

Run the script on every artifact. It checks self-containment, headings, labels,
alt text, reduced motion, brand fonts and colours, chart titles, placeholder
copy, banned phrases, em dashes, card/shadow/stripe patterns and more.

### 6.3 Sogeti-specific traps

- **Blue everywhere.** One large blue field per page; use Cool Grey/white for
  the rest.
- **Isometric decoration.** The brand's illustration system is isometric, but an
  image that does not explain the argument is decoration. Caption it or cut it.
- **The three-pillar consulting page.** Let the content's cardinality decide.
- **The fake dashboard.** Real screen at real density, or a diagram with a
  caption.
- **Stock transformation photography.** Use type, a diagram or a real artifact.
- **Dark mode as personality.** Light-first; dark only with a reason.
- **The 2026 overcorrection.** Cream + italic serif is as reflexive as purple.

Full guide: [`references/anti-slop.md`](references/anti-slop.md).

---

## 7. Technical standards

- **HTML5, semantic.** `header`, `nav`, `main`, `section`, `footer`, one `h1`,
  logical heading order. `lang` on `<html>`.
- **CSS.** One file, custom properties, `clamp()` for type, grid/flex, no
  framework. Surfaces have 2 px radius; buttons are pills; numbers can be
  circles. No wide shadows.
- **Fonts.** Subset WOFF2, base64, `font-display: swap`. Ubuntu first, Verdana
  fallback. Never a network font.
- **Images.** Local, with `width`/`height`, `alt` and, where useful, a caption.
  Inline SVG for diagrams and icons. No stock photos without rights.
- **Charts.** SVG with `role="img"`, `<title>`, `<desc>`, axis labels, units,
  source and a table fallback for complex data.
- **Motion.** One page-load moment; hover colour transitions; no scroll-triggered
  everything; `prefers-reduced-motion` guard.
- **JS.** Vanilla, small, progressive. No framework. Clipboard with a fallback.
  No network calls.
- **Print.** Hide chrome; avoid breaks inside cards/tables/charts; greyscale-safe.
- **Performance.** One file, ideally under ~500 KB. The embedded font and logo
  account for most of the weight; optimise images to the display size.
- **Privacy.** No analytics, cookies, trackers or external requests. State that
  data stays in the page when the page collects input.

---

## 8. Quality gates

| Gate | Question | Evidence |
|---|---|---|
| 0 Job | What is this for, and who reads it? | Filled artifact brief |
| 1 Content | Is every claim true, sourced or labelled? | Source lines, approvals, illustrative labels |
| 2 Mechanical | Does the source pass the audit? | `sogeti_audit.py` output |
| 3 Human | Can a person use it? | Keyboard, 360 px, zoom, print |
| 4 Brand/legal | Is it safe to publish? | Logo, trademarks, quotes, photos, data |

**Definition of done:** audit PASS or an explained REVIEW; keyboard, 360 px,
200% zoom and print passes complete; every number sourced or labelled; every
quote approved or labelled composite; logo is master artwork or flagged; no
external requests; file saved in `html-docs/` and linked.

---

## 9. Reading paths

| If you need… | Read |
|---|---|
| The full brand system | `brand-foundations.md` |
| Exact colours and contrast | `color-system.md` |
| Type scale and rules | `typography.md` |
| Logo and shape geometry | `logo-and-shapes.md` |
| Voice, mechanics, banned phrases | `voice-and-copy.md` |
| Components and layout classes | `design-system.md` |
| Chart choice and SVG | `data-visualization.md` |
| Accessibility and print | `accessibility.md` |
| Narrative, scenario, page structures | `content-models.md` |
| The gate and the ten laws | `anti-slop.md` |
| The ship process | `quality-gates.md` |
| The 2026 live-site audit | `web-and-digital.md` |
| The system in the browser | `design-system-visual.html` |
| Copy-paste blocks | `recipes.md` |
| Which template to start from | `catalog.md` |

The raw research is in `reference/research/`; the source PDF is
`reference/Sogeti-brand-V3-guidelines.pdf`.

---

## 10. Legal and brand hygiene

- Sogeti, Capgemini, the wordmarks, the spade and the brand shapes are
  trademarks. Use them only for Sogeti-authorized work.
- The PNG logos in `assets/logos/` are extracted reference assets, not master
  artwork. Replace with Global Marketing files for production.
- Photography needs a licence and a credit. Client logos need permission.
  Quotes need approval. Personal data needs a lawful basis.
- Fictional clients, quotes and metrics must be visibly labelled as
  illustrative.
- The public Sogeti accessibility statement targets WCAG 2.1 AA with partial
  compliance. This skill targets WCAG 2.2 AA for artifacts; do not use the
  statement as a reason to ship a known barrier.
- The live site is not the brand authority. The PDF and approved master artwork
  are.

---

## 11. The five things to remember

1. **One job, one reader, one decision.**
2. **The brand is the constraint:** Capgemini Blue, Ubuntu Mono, the shape,
   sentence case, evidence.
3. **One signature moment per page.** Everything else supports it.
4. **The gate is subtraction.** Do not fix a default by adding another.
5. **If the reader cannot decide without you, the artifact is not done.**

Now open the shelf: [`references/templates/index.html`](references/templates/index.html).
