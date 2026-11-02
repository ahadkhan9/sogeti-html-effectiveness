# AI Slop in UI & Web Design, 2025–2026

**Scope.** Every pattern is observable in a rendered page or its source. Claims are attributed inline; single-crawl and vendor-blog evidence is flagged. Three 2026 projects do most of the empirical work: [Impeccable's `/slop` catalogue](https://impeccable.style/slop) (68 patterns, 62 machine-checkable), [Krebs's 1,590-page Show HN audit](https://www.adriankrebs.ch/blog/design-slop/), and the community [Signs of AI design](https://github.com/febbhav/signs-of-ai-design).

**Evidence caveat.** The 2026 numbers everyone quotes are not independent. Krebs scored 1,590 Show HN pages at 22% heavy (4+ of 16 patterns) / 32% mild / 46% clean, with a self-reported **5–10% manual-QA false-positive rate** ([Krebs, 20 Apr 2026](https://www.adriankrebs.ch/blog/design-slop/)). Secondary write-ups repeat them as settled, and the bins shifted when HN moderator `dang` re-tabulated the same data in-thread (5+ = 21%, 2–4 = 46%, 0–1 = 33%). Signal, not measurement.

---

## 1. Ten laws

**1. Slop is the absence of decisions, not the presence of a style.** *"The tell is not that Inter is a bad typeface. The tell is Inter, unchosen, next to twenty other unchosen defaults"* ([Signs of AI design](https://github.com/febbhav/signs-of-ai-design)). Could another product have shipped this page?

**2. One tell is noise; density is the signal.** "One match is noise. Ten matches is a signature" (ibid.). Krebs built tiers because every pattern has legitimate human owners.

**3. The tells decay; the mechanism does not.** Purple was the 2024 tell; models that learned purple is mocked now reach for cream, emerald, and italic serif (ibid.). A guide written against today's hex codes is obsolete in two quarters.

**4. Defaults come from the toolchain, not the model.** Generators share one stack — Tailwind, shadcn/ui, Lucide, Framer Motion — and emit its defaults verbatim. Adam Wathan apologised in Aug 2025 that `bg-indigo-500` made "every AI generated UI on earth also being indigo" (quoted in [prg.sh](https://prg.sh/ramblings/Why-Your-AI-Keeps-Building-the-Same-Purple-Gradient-Website)). Interrogate imports.

**5. Prose advice backfires; binary gates work.** The key 2026 finding for anyone building a design skill. Solo Design Studio ran six components across three arms — no skill, written guidance, mechanical gate. Written guidance scored **equal to or worse than no skill on five of six**, and nearly doubled bento-hero failures (7.0 → 11.7). Only the gate reversed it, to zero on three. *"The model reads 'be distinctive' as 'add more,' and more is the slop"* ([solodesign.cc](https://solodesign.cc/blog/ai-design-slop-the-tells/)). Write lints, not exhortations.

**6. Slop is a copy problem wearing a CSS costume.** The same model writes the words: *"the literal em-dash shows up inside the design, sitting right next to the visual defaults"* (ibid.). A perfect type system over "Elevate your workflow" still reads machine-made.

**7. Functional slop outranks aesthetic slop.** Missing validation, 1.6:1 contrast, content stuck at `opacity: 0` harm users; a purple gradient merely embarrasses the owner. Impeccable separates "AI slop" from "Quality" findings for this reason; Hallmark's **Floor** tier "never ships" ([Hallmark](https://github.com/Nutlope/hallmark)).

**8. Overcorrection is slop in the other direction.** "Layers of gradients, parallax effects on every section, custom cursors… This is not distinctive design. It is noise" ([925Studios](https://www.925studios.co/blog/ai-slop-web-design-guide)).

**9. Every pattern here is a legitimate pattern used without a job.** Glass solves real layering; dark glow is Linear's hand-built house style. The defect is the missing job.

**10. Distinctiveness is a constraint you encode, not a vibe you prompt.** Impeccable ships a `DESIGN.md` contract; Hallmark deals one of fifty material themes and lints to it; Solo enforces 50 rules. NN/g's framing: designers become *"designers of parameters and constraints,"* specifying `must show / should show / never show` ([NN/g, 22 Mar 2024](https://www.nngroup.com/articles/generative-ui/)).

---

## 2. Pattern catalogue

**Severity.** **S1** functional or fabricated, blocks ship · **S2** reads machine-made largely on its own · **S3** diagnostic in combination (3+) · **S4** noise. Follows Hallmark's Floor/Reflex/Finish logic and Signs of AI design's `Reliability` labels. Functional failures (contrast, focus, validation, overflow, broken `alt`) are not repeated here — they are Tier 1 of the checklist in §4, because they block a ship regardless of style.

### A. Colour, surface, light

| Pattern | Observable tell | Why it reads as slop | Sev | Replace with |
|---|---|---|---|---|
| **SaaS purple** | `from-indigo-500 to-purple-500`; `#6366F1`/`#8B5CF6`/`#A855F7`. One uncited 2026 crawl puts blue-purple near 78% of marketing sites, up from ~10% in 2020 | Tailwind's demo accent, recycled through training data | S3 | Palette from one brand fact |
| **Gradient text** | `bg-clip-text` on a heading or stat, hue shifting mid-word | No meaning; a demo pattern read as "dashboard" | S3 | One solid colour |
| **Neon-on-dark / halo** | Cyan or violet on near-black; coloured `box-shadow`; radial glow behind the hero | "Adds emphasis without explaining what matters" (Impeccable) | S3 | Cut glow until information wins |
| **Reflexive glass** | Backdrop-blur cards and navs where nothing overlaps | Blur solves overlay-on-imagery, not texture | S3 | Opaque surfaces, real elevation ramp |
| **Cream "tasteful" default** | Warm off-white ground, amber accent, "editorial" feel | "The second-wave default… after purple became a public joke" | S3 | Only if the product is editorial, food, or craft |
| **Side-tab accent** | 3–4px coloured stripe on an ordinary card | Pattern-matched from alerts; "almost as reliable a sign of AI-generated design as em-dashes" (designer quoted by Krebs) | S2 decorative / S1 semantic | Stripe only where status is real |

### B. Typography

| Pattern | Observable tell | Why it reads as slop | Sev | Replace with |
|---|---|---|---|---|
| **Inter/Geist defaultism** | `--font-sans` = `ui-sans-serif`/`system-ui`, or a declared webfont with no file served | "Geist has been called the new Inter: it is v0's default." **6 of 7 audited themes had no font file** — *"Declaring is not shipping"* | S2 | Ship and subset the font |
| **The escape-hatch trio** | Space Grotesk, Instrument Serif, Geist, Fraunces — chosen *because* Inter was called out | Escape attempts become tells. HN: "don't ruin great fonts… they are popular for a reason" ([thread](https://news.ycombinator.com/item?id=47864393)) | S3 | *Unexamined* popularity is the problem |
| **Oversized italic serif hero** | Huge italic serif headline, or one serif-italic accent word in a sans headline | "The universal 'tasteful AI startup' hero of 2025 and 2026… models conflate distinctive with appropriate" | S2 | Legitimate for editorial; ask if it works or decorates |
| **Eyebrow chip + tracked caps** | Tiny uppercase tracked label (`letter-spacing ≥ 0.1em`) or pill — "New", "v2.0 is here", sparkle prefix — directly above a centred display headline; repeated on every section | "One of the most recognizable current tells"; it "adds another line to read" | S2 | Put the useful words in the headline |
| **Icon tile above heading** | Rounded-square icon container above each feature heading | "Emitted in this exact shape by every major generator" | S3 | Icon beside the heading, or none |

### C. Layout and structure

| Pattern | Observable tell | Why it reads as slop | Sev | Replace with |
|---|---|---|---|---|
| **The hero formula** | Centred stack: badge → 64px+ sentence → one-line subhead → gradient "Get Started" + ghost secondary → orb | "The modal SaaS hero… also a genuinely effective conversion layout, which is how it became modal" | S3 | Keep clarity, break one axis |
| **Three-card feature row** | Exactly three equal cards, icon on top, short heading, two lines — the page's only feature section | "The single most consistently named tell"; suspicion rises "when the content visibly does not come in threes" | S2 | Let actual cardinality decide |
| **Bento bandwagon** | Asymmetric boxed grid, often dark with accent tiles | "It spread as the safe alternative once three-card rows were called out, and is now a tell of its own" | S3 | Fine when tiles differ in kind |
| **Cookie-cutter order** | hero → logo wall → 3 cards → testimonial → stats → pricing → FAQ → CTA | "Zero deviation plus other fingerprints is the signal" | S3 | Cut a section the product doesn't earn |
| **Fabricated trust chrome** | Grayscale logo wall and "500K Users · 99.9% Uptime" banner counting up on scroll | "Some shipped pages carry fully hallucinated logo sets"; "the tell sharpens when the numbers are invented… on a domain registered last month" | **S1 if fabricated**, else S3 | Only substantiable logos; one number with source and date |
| **Fake chrome / floating dashboard** | Code window with three macOS traffic lights, or a tilted glowing dashboard over a gradient, on a product that is neither | Depicts a UI nobody built, so surrounding copy must stay vague | S3 | Real screen at real density |
| **Monotonous spacing** | One spacing value everywhere, identical section padding | One theme measured **1.33:1 against a 1.75 floor**: "Nothing is loud, so nothing is quiet, so nothing is composed" | S3 | One oversized element per page |

### D. Copy and voice

| Pattern | Observable tell | Why it reads as slop | Sev | Replace with |
|---|---|---|---|---|
| **Weightless headline** | "Build faster. Ship smarter." / "Your all-in-one platform." | "Grammatically perfect, could describe any product" ([925Studios](https://www.925studios.co/blog/ai-slop-web-design-guide)) | S2 | Stripe: "Financial infrastructure for the internet" |
| **Buzzword layer** | streamline, supercharge, empower, unlock, elevate, seamlessly, world-class, enterprise-grade, best-in-class, robust | "Every one of these was coined by human marketers; density and combination are the fingerprint" | S2 at density | What the user can do, what improves |
| **"In today's fast-paced world"** | Opener on hero, about page, or deck | The most-cited copy tell; strong alone | S2 | Delete; start with the reader's situation |
| **Negative parallelism** | "It's not just X, it's Y." / "Not a feature. A platform." | Wikipedia files it as stereotypically AI — "clearing up a common misconception" nobody raised; Impeccable calls the short form **forced contrast** | S3 each, S2 at density | Explain the distinction |
| **Rule of three** | "adjective, adjective, adjective"; "phrase, phrase, and phrase" | "LLMs overuse the rule of three… to make superficial analyses appear more comprehensive" ([Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)) | S3 | Break the triad |
| **Em-dash cadence** | Spaced em dashes several times per paragraph | "Much more disposed to use them than nonprofessional human-written text"; AI dashes are usually **spaced**, against convention. Wikipedia dates its section *(2022–September 2026)* — GPT-5.1 suppressed them | S3 each, S2 at density | Full stops |

### E. Interaction and motion

| Pattern | Observable tell | Why it reads as slop | Sev | Replace with |
|---|---|---|---|---|
| **Universal fade-up** | Identical `opacity: 0; translateY(20px)` on every section, uniform stagger; incoherent neighbours that snap | "One pattern covers all entrances"; "the model never sees its output run." Weak alone — real teams use it constantly | S3 | One orchestrated load |
| **Hover-scale + cursor follower** | `scale(1.03)` + shadow bloom on all cards; blob or ring trailing the pointer | No informational purpose; everything asks for attention at once. Cursor is named overcorrection noise | S4 | Lift only on actionable surfaces |
| **Parallax / marquees** | Drifting layers; auto-scrolling logos | "Make people read at the page's pace"; marquees need pause controls (WCAG 2.2.2) | S3 | Static, or controls + `prefers-reduced-motion` |
| **Typewriter / blinking caret** | Characters typing into a hero; "> Building the future" with a caret | "Makes ordinary text look editable or like a terminal" | S4 | Static text |
| **Bounce / elastic / confetti** | Dialogs that spring in and overshoot; confetti on a routine save | "Can make a routine action feel fussy"; celebration implies an achievement that didn't happen | S4 | Short settled ease-out |
| **Theme toggle as decoration** | Dark/light switch for a palette nobody designed both modes for | Doubles the surface for no need; dark usually fails contrast | S4 | One mode done well |

### F. Imagery and illustration

| Pattern | Observable tell | Why it reads as slop | Sev | Replace with |
|---|---|---|---|---|
| **Glossy 3D blobs** | Gradient orbs, floating primitives, plastic quality | Preference tuning rewards smooth, saturated, symmetric | S3 | Real product surfaces or a commissioned system |
| **Isometric illustration / hexagons** | Servers, clouds, shields arranged isometrically; node-link hexagons, particle streams, DNA ribbons | Depicts a system that isn't the system; generic signifiers with no referent | S3 | Diagram the actual architecture, or show the data |
| **Robot hands** | A hand reaching toward a glowing orb | The most saturated AI-marketing cliché; signals no specific claim | S3 | Make a claim instead |
| **Synthetic diverse teams** | Impossibly lit office, perfect teeth, mid-laugh at one laptop | "Perfect pores and nothing behind the eyes" | S2 | Real team photos, credited |
| **Six fingers / melted jewellery** | Failures concentrate where hands *interact*: gripping, interlacing, chopsticks; ear cartilage, earrings, watch numerals | "Thin symmetric man-made objects… patch-based generation handles worst" | S2 | Regenerate or crop |
| **Garbled secondary text** | Foreground headlines largely fixed in 2026; **background** signage, plates, small print, non-Latin scripts still dissolve | "Check the third sign in the scene, not the first" | S2 | Never ship text you can't read |
| **Impossible architecture** | Windows off the building grid, two vanishing points, stairs to nowhere | "The most durable tells… fixing them requires scene-level world models" | S2 | Photography with provenance |

### G. Data visualization

| Pattern | Observable tell | Why it reads as slop | Sev | Replace with |
|---|---|---|---|---|
| **Fake dashboard** | Hero mock with invented metrics, impossible ratios, no source | Depicts a product that doesn't exist | S3 | Real screenshot, real numbers |
| **Meaningless sparkline** | Tiny line, no axis, scale, or label | Implies trend without direction, magnitude, or period | S3 | Label the period and delta |
| **Rainbow / gradient categorical palette** | 8–12 equal-weight hues; or a sequential ramp on nominal categories | Datawrapper: "try to avoid using more than seven… the harder it becomes to read"; a ramp implies a ranking that doesn't exist | S3 | ≤7 distinct hues, or small multiples |
| **3D / exploded pie** | Extruded wedges, perspective, shadows | Area and angle are already weak encodings; 3D destroys both | S3 | Sorted horizontal bars |
| **Animated counter, no source** | "10M+ users" ticking upward on scroll | Motion manufactures credibility; the number is unaudited | **S1 if invented** | Static number + source + date |
| **No axes, units, or baseline** | Floating bars, truncated y-axis, unlabeled units | Unfalsifiable by construction | **S1** | Axis, unit, zero baseline, caption |

---

## 3. Where the slop moved in 2026 — and what replaced it

**Four documented shifts.**

1. **Purple → cream → "tasteful" editorial.** Impeccable's era tabs run 2022 (purple, glass, neon) against 2026, and now flag **cream/beige** and the **oversized italic serif** as reflexes. On Krebs's own post: *"it's not the Tailwind purple anymore… it's more of the same beige scheme"* (`ChrisArchitect`, HN).
2. **Universal pattern → model dialects.** *"Almost every vibecoded website is Opus, which has its own style… Mixing them all into one and then using it to 'identify AI coded websites' doesn't work"* (`deaux`, HN).
3. **Aesthetic → functional.** The discourse moved from "it looks purple" to "it doesn't work" — encoded in Impeccable's *AI slop*/*Quality* split and Hallmark's Floor tier.
4. **Vibe → constraint.** `npx impeccable detect` + `DESIGN.md`; Hallmark's fifty themes + `sloplint` at eight widths; Solo's 50 rules.

**What strong teams do instead** — each is a replacement for a named entry, not a mood:

- **Give the page a job and end on it.** Hallmark builds "around what the visitor came to do… a booking page books, a shop sells… and the page ends on it."
- **Ship the face, then let it carry a point of view.** A two-font system with one deliberate display face "does more for brand differentiation than any gradient or animation" (925Studios). Give colour one true source, and semantic token names (`--color-action-primary`, not `--color-gradient-start`).
- **Break symmetry where the content is asymmetric** — a consequence of ranking content honestly, not a style.
- **Use real material** — screenshots, credited photographs (Hallmark ships 755, each credited), real numbers — and compose density: one oversized moment per page.
- **Motion with a stated purpose,** `prefers-reduced-motion` respected.
- **Evidence-led copy.** If the headline survives a competitor's logo swap, rewrite it.
- **Systems, not pages.** Linear's restraint, Stripe's typography, Duolingo's character system are consistent systems — "the part AI tools cannot give you on their own, because a model has no memory of your brand between one prompt and the next" (925Studios).

925Studios lists over-designing to compensate as the most common fix-failure, and Solo's data agrees quantitatively: telling a model to be distinctive made it add more and score worse.

---

## 4. Binary detection checklist

Count a hit only where the pattern is present **and** no stated job justifies it.

### Tier 1 — Blockers (any hit = do not ship)
1. Body contrast < 4.5:1, or large text < 3:1, against the real background. ☐
2. Any interactive element without a visible focus state. ☐
3. Content invisible at rest, waiting on a scroll handler. ☐
4. A form that cannot report a validation error. ☐
5. Horizontal overflow at 360px, or no mobile layout. ☐
6. A statistic, logo, customer, badge, or testimonial you cannot substantiate. ☐
7. Chart with no axis labels, units, or stated baseline. ☐
8. Broken/empty image `src`, or missing `alt` on a meaningful image. ☐

### Tier 2 — Identity tells (3+ is a diagnosis)
9. `--font-sans` = `ui-sans-serif`/`system-ui`, or a declared webfont with no file served. ☐
10. Inter/Geist as the only family, with no second deliberate face. ☐
11. Italic serif display headline, or one serif-italic accent word in a sans headline. ☐
12. Gradient text on a heading or number. ☐
13. Indigo/violet gradient anywhere, **or** emerald as the only accent. ☐
14. Cream ground + amber accent with no editorial reason. ☐
15. Radial glow behind a hero or section. ☐
16. `backdrop-filter: blur()` where nothing overlaps. ☐
17. Pill/eyebrow chip directly above the H1. ☐
18. `uppercase` + `letter-spacing ≥ 0.1em` on ≥3 unrelated labels. ☐
19. Rounded-square icon container above every feature heading. ☐
20. Exactly three equal feature cards, content not naturally in threes. ☐
21. Bento grid where tiles don't differ in kind. ☐
22. Grayscale logo wall. ☐
23. Stats banner with ≥3 numbers counting up on scroll. ☐
24. Fake browser chrome or terminal as the hero. ☐
25. One border radius on cards, inputs, buttons, and images alike. ☐
26. Every card has both a hairline border and a wide shadow. ☐
27. Decorative 3–4px coloured stripe on ordinary cards. ☐

### Tier 3 — Craft tells (corroborating)
28. Identical fade-up on every section. ☐
29. Hover-scale on non-actionable cards. ☐
30. Auto-scrolling marquee without pause controls. ☐
31. Custom cursor or follower. ☐
32. Parallax on more than one layer. ☐
33. Accent hue within 20° of primary in OKLCH, with no distinct job. ☐
34. Body line length > 80 characters, or justified body text. ☐

### Tier 4 — Copy tells (rate-based)
35. Headline that survives a competitor's logo swap, or ≥2 of: elevate, seamlessly, unlock, empower, supercharge, game-changing, world-class, enterprise-grade, best-in-class, robust. ☐
36. "In today's fast-paced world" or equivalent throat-clearing. ☐
37. "It's not just X, it's Y" or "Not a feature. A platform." ☐
38. Spaced em dash ≥3 times in one screen of copy. ☐
39. Two or more symmetrical triads ("Build. Ship. Scale."). ☐
40. Any claim with no number, name, date, or mechanism. ☐

### Scoring
- **Any Tier 1 hit → fail**, regardless of total. User harm, not taste.
- **Tier 2: 0–1 clean · 2 review · 3–5 likely slop · 6+ rewrite the page, don't restyle it.**
- **Tier 4 is rate-based** — one em dash is not evidence; three plus a triad plus "seamlessly" is.
- **Weight co-occurrence over count.** Three hits descending from one toolchain default (shadcn card + Lucide icon + `rounded-2xl`) are *one* decision.
- **The pass condition is subtraction.** Fixing a failure by adding a gradient trades one default for another. Score the delta, not the polish.

**Source-level heuristics for an LLM reviewer.** Grep `from-indigo-500`, `to-purple-500`, `bg-gradient-to-`, `bg-clip-text`, `shadow-lg`, `rounded-2xl`, `backdrop-blur`, `uppercase` near `letter-spacing:0.1em`, `animate-`, `Inter`, `ui-sans-serif`, `Sparkles`, `ArrowRight`. Verify `@font-face` `src` URLs resolve; check `prefers-reduced-motion` appears. Presence is not proof — **unmodified co-occurrence** is the signature. Sprawling `dark:` prefixes and shadcn `@/components/ui/*` imports point at v0-style generation.

---

## 5. False positives

Almost every pattern here was invented by human designers first: "AI tools amplified their frequency and uniformity until they became fingerprints."

- **Purple** is a real brand colour; the defect is the *unchosen gradient in the default hue*.
- **Dark mode with glow** was built by hand by Linear, Raycast, and Reflect from ~2019. Weak alone.
- **Inter and its alternatives.** Linear uses Inter deliberately; Vercel commissioned Geist for itself. The tell is the *unchosen* default.
- **Glassmorphism** legitimately solves overlay-on-imagery.
- **Three-card rows and centred heroes.** "It is also a genuinely effective conversion layout, which is how it became modal." Suspicion rises when content was forced into three.
- **The standard page order** "is also the standard human landing-page playbook." The sequence alone is weak.
- **Logo walls, stats, testimonials, three-tier pricing** when real and verifiable.
- **Coloured left borders.** *"I used a colored left-border on my blog and thought it looked pretty fresh. I didn't realize that was an AI pattern"* (`richard_chase`, HN). Semantic alerts keep theirs.
- **Serif display, editorial layouts, cream, bento.** Legitimate for many products; the defect is register mismatch or a substitute for a decision.

**Three structural cautions.**

1. **The base-rate problem.** Krebs never scored pre-2023 pages, and pre-AI landing pages were already formulaic — "before the AI era, everything looked like Bootstrap." The objection is right: *"these patterns were frequently seen in human-made sites too… several AI detectors claimed Declaration Of Independence was AI-generated"* (`raincole`, HN). A detector without a historical baseline measures the web, not the machine.
2. **Attribution is not a moral judgement.** "Identifying AI involvement in a design is not evidence of low effort, deception, or bad work, and misidentifying a human designer's work as AI causes real harm. Human detection accuracy on current AI images is barely above chance."
3. **The checklist goes stale.** Signs of AI design keeps a *"Signs that no longer work"* section — six fingers on resting hands, garbled headline text — because "citing these as evidence in 2026 mostly signals an outdated checklist." Wikipedia dates its em-dash section *(2022–September 2026)* because GPT-5.1 suppressed them.

---

## 6. "AI slop": origin and contested use

**Origin.** "Slop" for unwanted AI output surfaced in 2022–2023 among 4chan, Hacker News, and YouTube commenters, and broke mainstream in 2024. [Simon Willison](https://simonwillison.net/2024/May/8/slop/) popularised it on **8 May 2024**: *"Not all promotional content is spam, and not all AI-generated content is slop. But if it's mindlessly generated and thrust upon someone who didn't ask for it, slop is the perfect term for it."* **"Slop" was named 2025 Word of the Year by both Merriam-Webster and the American Dialect Society** ([Wikipedia](https://en.wikipedia.org/wiki/AI_slop)).

**Definition, and its refusal.** A January 2026 paper by Cody Kommers and colleagues notes slop has "so far resisted formal definition," while identifying three prototypical properties: **superficial competence, asymmetric effort, mass producibility.** That triad explains why slop looks *fine*: the competence is real, the effort is not, volume is the point.

**Three usages, routinely conflated.** (a) *Aesthetic-descriptive* — the visual fingerprint; weakest epistemically, most actionable practically. (b) *Provenance-inferential* — "a model made this"; useful as a review prompt, unreliable as an accusation. (c) *Effort-verdict* — "low effort, low specificity," independent of authorship. This is Willison's sense: a hand-built page can be slop, a heavily AI-assisted page need not be.

**Contested and overused uses.** Any design skill invoking the term should say these out loud:

- **It is used as a status weapon.** HN threads turn within a dozen comments from critique to gatekeeping: *"'vibe code' now just means 'coded with AI' which should not be anymore of an insult than 'IDE coded'"* (`xnx`).
- **It flattens model-specific aesthetics** that change quarterly (`deaux`).
- **It mistakes the web's own history for a machine signature.** Bootstrap-era, Tailwind-era, and AI-era sameness are one phenomenon at different amplification.
- **It is not a claim about quality.** Curator Francesco D'Isa argues most human production "has always been slop," the canon being "the surviving tip of an immense iceberg of forgotten, derivative, or simply boring creations."
- **Every specific tell has an expiry date.**

Operationally: use "slop" as a **diagnosis of missing decisions**, not a verdict about tools — and encode the diagnosis as checks, since prose guidance demonstrably fails (Law 5).

---

## 7. Annotated sources

**Primary catalogues and detectors**

- **[Impeccable — Slop](https://impeccable.style/slop)** (Paul Bakaus; accessed Nov 2026). 68 patterns, 62 machine-checkable rules, era tabs, `DESIGN.md` contract. Its *AI slop* vs *Quality* split is the model to copy.
- **[Signs of AI design](https://github.com/febbhav/signs-of-ai-design)** (Febian; CC BY-SA; accessed Nov 2026). Every entry carries `Reliability`, `Status`, and explicit **false positives**, modelled on Wikipedia's *Signs of AI writing*. Covers UI, images, video, logos, decks, print, copy; includes "signs that no longer work."
- **[Krebs — Scoring Show HN submissions](https://www.adriankrebs.ch/blog/design-slop/)** (20 Apr 2026). 1,590 pages, Playwright + computed styles, 16 deterministic checks, no LLM screenshot judging.
- **[HN discussion](https://news.ycombinator.com/item?id=47864393)** (22 Apr 2026, 333 pts). Best practitioner pushback: model dialects, missing pre-2023 baseline, WCAG failures.
- **[Hallmark](https://github.com/Nutlope/hallmark)** (Together AI, v2 2026). Floor / Reflex / Finish gates, fifty themes, 755 credited photos, `sloplint` at eight widths.
- **[Solo Design Studio](https://solodesign.cc/blog/ai-design-slop-the-tells/)** (Tridip Thrizu, 6 Jun 2026). Strongest empirical result: written guidance scored equal-or-worse than no skill on 5 of 6 components; only a mechanical gate reversed it.
- **[TailThemes](https://tailthemes.com/blog/ai-design-slop-quality-gate)** (20 Aug 2026). Quantitative craft audit: missing font files, 0.027 L separation, 5.4° "accent", 1.33:1 density.
- **[925Studios — Complete Guide](https://www.925studios.co/blog/ai-slop-web-design-guide)** (19 Mar 2026) and **[Fonts and Gradients](https://www.925studios.co/blog/ai-slop-design-tells)** (14 Jun 2026). Agency voice; best treatment of the fix and of overcorrection.
- **[Developers Digest](https://www.developersdigest.tech/blog/ai-design-slop-and-how-to-spot-it)** (22 Apr 2026, upd. 6 Oct 2026). Corroboration, not an independent measurement.

**Foundational and adjacent**

- **[Wikipedia — AI slop](https://en.wikipedia.org/wiki/AI_slop)**. Origin, 2025 WOTY, Kommers et al.'s three properties, D'Isa's dissent.
- **[Wikipedia — Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)**. The copy-tells canon: em-dash overuse *(2022–September 2026)*, negative parallelism, rule of three.
- **[Simon Willison](https://simonwillison.net/2024/May/8/slop/)** (8 May 2024). The definition that still works.
- **[prg.sh](https://prg.sh/ramblings/Why-Your-AI-Keeps-Building-the-Same-Purple-Gradient-Website)** (26 Oct 2025). The Tailwind→training-data→default loop; quotes Anthropic's `frontend-aesthetics` guidance.
- **[NN/g — Sparkles icon](https://www.nngroup.com/articles/ai-sparkles-icon-problem/)** (Kate Kaplan, 20 Sep 2024). Users read sparkles as plus signs, insignia, deals, favourites, accessibility.
- **[NN/g — Generative UI](https://www.nngroup.com/articles/generative-ui/)** (Moran & Gibbons, 22 Mar 2024). Designers as authors of constraints.
- **[WCAG 2.2 SC 1.4.3](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html)** (4.5:1 / 3:1) and **[SC 2.3.3](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions.html)** (animation from interactions).
- **[Datawrapper](https://www.datawrapper.de/academy/what-to-consider-when-choosing-colors-for-data-visualization)**. ≤7 categorical colours; no gradient ramps for categories; rainbow scales mislead.
- **[Quesma](https://quesma.com/blog/invisible-cities-one-shot/)** (Piotr Migdał, 7 Oct 2026). The counter-example: a 2026 one-shot that is *not* slop.
- **[Curbed — AI Bodega](https://www.curbed.com/article/ai-slop-bodega-signage-design.html)** (2026). Slop moving into physical signage — a production phenomenon, not a web one.

---

*Compiled 3 November 2026. Quantitative claims are traceable to their linked source; vendor blogs and single unverified crawls are flagged in place. Treat hex codes, fonts, and easing curves as perishable and the mechanisms — statistical averaging, toolchain defaults, preference tuning, the feedback loop — as the durable content.*
