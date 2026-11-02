# Sogeti on the Web: A 2025–2026 Digital Brand Audit

**Prepared:** November 2026 · **Method:** direct HTTP retrieval of `www.sogeti.com` pages and their CSS bundles, plus the site's own accessibility statement. Everything in **Observed** is quoted from retrieved source; everything in **Inferred** is my reading of that source.

---

## 1. Live site audit

**Observed.** `https://www.sogeti.com/` returns HTTP 200 and is a **WordPress 7.0.8 block theme** named `sogeti2024` (asset version `1.0.33`), built on **Bootstrap 5.3.3** + **GSAP 3.12.5 with ScrollTrigger**. Blocks come from three bespoke plugin families: `sogeti-blocks`, `sogeti-yeti-blocks`, and `cg-blocks` ("CG" = Capgemini Group). Analytics/CMP: Usercentrics, Parse.ly, Nelio A/B Testing.

The single most consequential observation is in the opening `<html>` tag:

```html
<html lang="en-US" data-cg-theme="dark" data-bs-theme="dark">
```

**The site ships dark by default.** `data-cg-theme` is a Capgemini Group-wide theme attribute, mirrored by `data-bs-theme` for Bootstrap 5.3's native colour modes. The header carries a real theme switch — `role="switch"`, `aria-checked="true"`, `checked`, an `aria-live="polite"` status region, and a keyboard handler — which is better accessibility engineering than most corporate theme toggles. Asset level, the pattern is duplicated everywhere: the logo ships as `sogeti-blue-new.svg` **and** `sogeti-white-new.svg`, and hero videos carry both `data-video-light-src`/`data-video-light-position` and `data-video-dark-position`. The dual-theme requirement is baked into the content model, not applied afterwards.

**Inner pages.** `/services/`, `/insights/`, `/careers/`, `/contact-us/` all return 200. `/about/` returns **404** — the canonical path is `/about-us/`. No page I fetched was bot-blocked; all CSS was retrievable.Header architecture is a two-tier masthead: a slim `header-topbar` (search, dark-mode switch, language selector) above `header-bottom` (logo + six primary nav items). Each nav item opens a mega-menu panel that mixes link columns with a promotional image and caption (`advertImageWrapper` → `advertImg` → `advertImgInfo`) — effectively an in-nav ad slot. Mobile has a parallel `header-mobile` tree rather than a responsive reflow.

Footer is a single flat list — *Discover Capgemini, Services, Client stories, Insights, Careers, About us, Contact us, Accessibility, Cookie policy, Cookie settings, Privacy notice, Terms of use* — then `© 2026 Sogeti. All rights reserved.` and LinkedIn/YouTube. The parent-brand link is labelled **"Discover Capgemini"**; "Part of Capgemini" appears only in the meta description, never the footer.

**Motion.** CSS keyframes are almost absent (one `@keyframes`, for filter spinners). Motion is JS-driven via GSAP + ScrollTrigger, with hooks such as `fade-in-up-content` on hero text. Heroes are full-bleed looping `<video>` at 40% overlay with a visible pause/play button.

**Discrepancy.** The guidelines describe an isometric illustration and icon system. The live homepage hero is **live-action video** fronted by a 3D yeti mascot ("Geti"), not isometric line art. Where icons appear they are **Tabler Icons** (32px icon font) plus a proprietary `zodiak-icons` set.

---

## 2. Typography in practice

**Observed.** Ubuntu is present, but loaded unusually: **16 inline `@font-face` declarations in the HTML `<head>`**, self-hosted as raw **`.ttf`**, not WOFF2:

```css
@font-face{font-family:Ubuntu;font-style:normal;font-weight:400;
  font-display:fallback;
  src:url('https://www.sogeti.com/wp-content/themes/sogeti2024/assets/fonts/ubuntu/Ubuntu-Regular.ttf')
  format('truetype');font-stretch:normal;}
```

Weights loaded: Ubuntu **300 / 400 / 500**, each with italic; Ubuntu Mono **400 / 700**, each with italic. Most declare `font-display:fallback`; one duplicate uses `swap`. Several faces are declared twice.

The canonical stacks, from CSS custom properties:

```css
--sogeti-bs-font-sans-serif: "Ubuntu", sans-serif;
--sogeti-bs-font-monospace:  "Ubuntu Mono", monospace;
--sogeti-bs-body-font-family: var(--sogeti-bs-font-sans-serif);
--wp--preset--font-family--heading:     "Ubuntu", sans-serif;
--wp--preset--font-family--heading-mono:"Ubuntu Mono", monospace;
```

`"Ubuntu",sans-serif` appears 121× in the theme stylesheet — it is the only display face in use.

**The headline weight is the headline finding.** The 2024 guidelines specify Ubuntu/Ubuntu Mono **Bold** for headlines. The live site sets headlines at **Light 300–Regular 400** with essentially zero tracking:

| Element | Observed declaration |
|---|---|
| Hero `h1.banner-heading` | `font-size:2.5rem; font-weight:300; line-height:3.5rem; letter-spacing:.12px` (mobile `2rem/2.75rem`) |
| Hero `.banner-description` | `font-size:1.5rem; font-weight:300; line-height:2.125rem; letter-spacing:.1px` |
| `h1` | `font-size:2rem; font-weight:400; letter-spacing:.12px` |
| `h2` | `1.75rem / 400 / .12px` |
| `h3` | `1.5rem / 400 / .1px` |
| `h4` | `1.25rem / 400 / .2px` |
| body | `1rem / 400` |

Letter-spacing of `.1–.2px` at 40px type is visually **neutral to slightly negative** — the opposite of the wide-tracked technical aesthetic the guidelines imply. Hero headings top out at **40px**, which is conservative for a 2026 enterprise site; scale is achieved through 696px hero height and full-bleed media, not through display type.

**Ubuntu Mono is demoted to micro-typography.** It never appears in a headline. It is used only for eyebrows, author bylines, tags, and data labels at `.875rem`–`1.125rem` — e.g. `.profile-card .profile-info h6`, `.box-author-name`, `.box-tags span`, training-data labels at `14px`. **Inferred:** the mono face has migrated from a headline device to a metadata texture, which is a real brand-system divergence worth resolving one way or the other.

Other type facts: `text-transform:uppercase` appears only **2×** in 812KB of CSS — the system is overwhelmingly sentence case. Body copy colour is `#121212`, not pure black.

---

## 3. Color in practice

**Observed.** Two token namespaces coexist and partly disagree: a legacy `--sogeti-bs-*` layer (225 names, Bootstrap-derived) and a newer **`--zodiak-*`** layer (69 hex tokens). Capgemini.com's own 2025 theme (`capgemini2025`) contains **72 `zodiak` references**, so Zodiak is the **group-wide Capgemini design system**, shared with Sogeti rather than Sogeti-specific. Sogeti's theme appears to be a Zodiak consumer with a Bootstrap skin bolted on top.

Core tokens verified in `app.css`:

```css
--sogeti-bs-blue-capgemini-600: #0070AD;   /* Capgemini Blue — matches guidelines */
--sogeti-bs-blue-vibrant-500:   #12ABDB;   /* Vibrant Blue — matches guidelines */
--sogeti-bs-cool-grey-50:       #F5F5F7;   /* Cool Grey — matches guidelines */
--sogeti-bs-cool-tech-red-500:  #FF4F66;   /* NOT the guidelines' #F53B53 */
--sogeti-bs-body-color:         #121212;
--sogeti-bs-link-color:         #005080;
--sogeti-bs-sogeti-blue:        #0058AB;   /* Sogeti's own historic blue */
```

**Deep Purple `#2B0A3D` does not exist on the site.** I searched the 812KB stylesheet, the 677KB homepage, and the logo SVG: **zero occurrences**. The guideline's secondary palette is effectively absent from the web build.

**Cool Tech Red has fragmented into six values**, which is the clearest sign of drift:

| Where | Value |
|---|---|
| Guidelines | `#F53B53` |
| `--sogeti-bs-cool-tech-red-500` | `#FF4F66` |
| WP preset `primary` | `#FF2F4B` |
| Button **rest** state | `#DB2443` (white text) |
| Button **hover** state | `#FF767F` (black text) |
| Button **active** state | `#F53B53` (black text) |
| `--zodiak-red-500` | `#F64059` |

The official `#F53B53` survives only in the *pressed* state and in the logo dot. The rest state is a darker `#DB2443`. **Inferred:** this is likely an accessibility fix (black on `#F53B53` is roughly 4.5:1; black on lighter `#FF767F` is comfortably better) applied at component level without reconciling the token.

**Dark mode values** come from Zodiak neutrals, not the brand palette:

```css
[data-cg-theme="dark"]{
  color-scheme: dark;
  --zodiak-page-background:      #12151D;
  --zodiak-surface-fog-lite:     #1B1F27;
  --zodiak-surface-marine-heavy: #1D365A;
  --zodiak-text-primary:         #F8FAFC;
  --zodiak-text-disabled:        #888F9A;
}
```

A cool, slightly blue-black neutral ramp (`#12151D → #F8FAFC`), quite distinct from the guidelines' Cool Grey `#F5F5F7`, which is a *light* surface. There is **no documented dark-mode palette in the 2024 guidelines** — the entire dark system is Zodiak's.

**Unpurged Bootstrap defaults remain**: `--sogeti-bs-primary: #0d6efd` and `--sogeti-bs-blue: #0d6efd` are still Bootstrap's stock blue, untouched. A handful of stray literals also appear inline: `#003E89`, `#313131`, `#202020`, `#EEEEEE`, plus the full WordPress default palette (`#CF2E2E`, `#FCB900`, `#00D084`…) still registered as editable swatches — an editorial risk, since authors can pick non-brand colours from the block editor.

One further detail: the Sogeti **logo SVG is literally two shapes** — one path in `#0058AB` and one circle in `#F53B53` (`r="2.15"`, top-right, `viewBox="0 0 71 37"`). So the "primary brand shape derived from the wordmark" is the **dot of "Sogeti."** — and the wordmark still uses Sogeti's own `#0058AB`, not Capgemini Blue `#0070AD`.

---

## 4. Components & layout

**Buttons** are unambiguously **pill** shaped and this is the most consistent signature of the site:

```css
border-radius:999px; height:3rem; padding:12px 1.5rem;
font-size:1rem; letter-spacing:.1px; gap:.5rem;
display:inline-flex; align-items:center; justify-content:center;
border:none;
```

Variants are a 3×2 matrix: sizes `button-small | button-medium | button-large`, times `button-fill.button-red | button-fill.button-graphite | button-fill.button-white | button-outline`. Large fill buttons are `56px` tall; small are `38px`. Disabled state: `background:#3C414A; color:#A6ACB5`. Focus: `outline:1px solid #2E323A; outline-offset:2px` — a **1px** ring in a near-background grey is thin, and on the dark surface (`#12151D`) `#2E323A` is very low contrast. This is likely one of the contrast/keyboard items in the site's own audit.

Unusual: filled red buttons use **black** label text (`--zodiak-text-always-black`), not white. That black-on-red pill is a distinctive 2025-era look and reads more "tech campaign" than "consultancy conservative."

**Radius** is bimodal: `999px` (64 uses — pills, chips, avatars) and `4px` (23 uses — cards, inputs). A minority use 20/30/50px. So: fully rounded controls, near-square surfaces.

**Cards** are flat: 4px radius, cool-grey or Zodiak-surface fills, image on top, no heavy shadow. The AI microsite adds a `cg-block-card-circular` block (circular portrait/segment cards) — **inferred** from class naming; its stylesheet path returned 404 so I could not confirm the geometry.

**Spacing** is a 7-step WordPress preset (`--wp--preset--spacing--20` `0.44rem` through `--wp--preset--spacing--80` `5.06rem`). Type presets mix `clamp()` fluid scaling with a parallel fixed `rem` ramp (`xxxs` `0.875rem` … `xxl` `3.125rem`) — two competing scales, a maintenance risk.

**Layout**: 760px max-width hero content, `container` grid, 696px hero. Section rhythm is generous but not extreme.

---

## 5. Voice examples

Sentence case throughout. Short declaratives, heavy second person, frequent rhetorical questions, and a signature **all-caps emphasis word** inside a sentence. Zero jargon in headlines (jargon is confined to service names).

**Headlines**
1. "Got a minute?" — homepage H1, https://www.sogeti.com/
2. "Take a quick look of what makes Sogeti, Sogeti, and how we help clients navigate change, move faster, and achieve more." — hero deck, https://www.sogeti.com/ *(note: "look of" is a grammatical slip in live copy)*
3. "BIG results start with the RIGHT guide." — https://www.sogeti.com/
4. "Making BIG things happen" — https://www.sogeti.com/
5. "Ready when you are." — https://www.sogeti.com/
6. "Do you trust your AI?" — https://www.sogeti.com/
7. "What makes Sogeti, Sogeti?" — https://www.sogeti.com/
8. "Cutting-edge solutions, world-leading tech, local delivery" — https://www.sogeti.com/services/
9. "The future belongs to the tech explorers and the innovators" — https://www.sogeti.com/insights/
10. "Challenges feel smaller when your partner feels bigger." — https://www.sogeti.com/about-us/meet-geti/
11. "Technology doesn't need to be complicated to deliver real results." — https://www.sogeti.com/about-us/meet-geti/
12. "85% of AI projects fail to move beyond pilots." — https://www.sogeti.com/make-way-for-ai-in-action/ (stat-led headline with superscript citation)
13. "Make your next move?" — https://www.sogeti.com/careers/
14. "In good company. Working alongside ambitious organizations and trusted technology partners." — https://www.sogeti.com/

**CTAs** (all observed as button/link text): "Get in touch" · "Book a call with an expert" · "Meet Geti, the Sogeti Yeti" · "Learn more" · "Watch video" · "Watch now" · "Add to calendar" · "Read more".

**Nav labels**: Services · AI Enabled Business · Client stories · Insights · Reports · Featured articles · Newsroom · Executive summits · Careers · About us.

**Service naming** is where the jargon lives, and it is aggressively productized: "Future-Ready Apps Portfolio", "Gen AI Augmented Software House", "Next-Gen Workplace Automation", "Smart Quality at Speed", "Supercharging your ERP Quality", "GreenFinOps Cloud Optimization".

**Rhetorical device — "Right here. Right now."** This refrain recurs a dozen-plus times on the Geti page, always with the full stop isolated as its own emphasis, often on a separate line: *"Right here."* / *"Right now."* The full stop is doing brand work — the same dot as the logo.

**Inferred tone summary:** peer-to-peer, anti-consultancy ("Big decisions need more than just a video call"), speed-obsessed, deliberately un-corporate. Sentence length averages under 10 words in headlines. You/we ratio is strongly "you"-led.

---

## 6. Digital artifacts worth studying

| Artifact | URL | Why it matters |
|---|---|---|
| **AI in Action** microsite | `https://www.sogeti.com/make-way-for-ai-in-action/` | 1.16MB, bespoke block set — `cg-block-split-hero`, `cg-block-card-circular`, `cg-block-accordion-block`, `cg-block-spaced-article`. **118 `wp-block-details`** elements: FAQs use native disclosure widgets, a genuinely accessible choice. |
| **Reports library** | `https://www.sogeti.com/insights/reports/` | Flagship research hub ("World Payments Report 2027", "A world in balance 2026: The resilience reset"). Faceted archive; a gated branch exists — the DOM contains a literal `Access Denied` heading. |
| **Meet Geti** | `https://www.sogeti.com/about-us/meet-geti/` | Mascot microsite; fullest expression of the voice system and the "Right here. Right now." device. |
| **SogetiLabs** | `https://www.sogeti.com/about-us/sogetilabs/` | Thought-leadership sub-brand (camelCase, one word). |
| **Executive summits** | `https://www.sogeti.com/insights/executive-summits/` | Event-page template. |
| **Client stories** | `https://www.sogeti.com/client-stories/` | Case-study template. |
| **Accessibility statement** | `https://www.sogeti.com/accessibility/` | Rare in this sector — full conformance disclosure. |

**Production defect worth flagging:** the Reports page ships an unrendered template placeholder (`{{ title }}`) and an "Access Denied" heading into the public DOM — an archive-shortcode JS app failing to hydrate. The homepage also shows orphan `• -->` fragments in button text. **Inferred:** archive components are under-tested at build time.

---

## 7. Brand/legal constraints

**What I could verify directly.** The wordmark is always **"Sogeti"** — capital S, no accent, no all-caps, no space. It renders as `Sogeti` + a red dot, SVG `viewBox="0 0 71 37"`, i.e. a **1.92:1** lockup. Two files (`-blue-new`, `-white-new`) swap per theme; no separate icon/favicon lockup appears in the header. The site's own meta description uses *"Sogeti, a leading technology solutions provider and part of Capgemini"* — lowercase "part of" mid-sentence, treating it as a descriptor rather than a lockup. The footer instead says **"Discover Capgemini"**, and no "Part of Capgemini" lockup appears on the page.

**Could not verify — do not take my word for it.** Minimum sizes and clear-space rules live in the PDF you already hold, not on the public web. I probed `brand.capgemini.com`, `brandhub.capgemini.com`, `capgemini.com/brand/`, `capgemini.com/brand-hub/`, `sogeti.com/brand/` — all 404 or no DNS. **Web search was unavailable in this session** (search backend HTTP 400) and DuckDuckGo's HTML endpoints returned 202 blocks, so no public brand portal could be located or cited. Do not cite a "Capgemini brand hub" URL on my authority; the only public artifacts I confirmed are the live site and its accessibility statement.

Other naming details observed: **TMAP®** carries a registered mark; **"Geti, the Sogeti Yeti"** is always capitalised as a proper noun; **SogetiLabs** is one camelCase word.

---

## 8. Accessibility

**Observed** — quoted from `https://www.sogeti.com/accessibility/`:

- Target: **WCAG 2.1 Level AA**, with an explicit pledge as a **Valuable 500** signatory.
- Status: **"partial compliance"**.
- Audit: November 2024, by **Capgemini Group IT accessibility experts**, against WCAG 2.1 A and AA. Statement dated **27/11/2024**.
- Result: **83% of 68 criteria met — 48 compliant, 10 non-compliant, 10 not applicable.**
- Declared non-conformities: *"Transcript and captions are missing for video and audio"*, *"Some of the actionable elements are not accessible through keyboard"*, *"Color contrast issues"*, *"Unclosed element div which fails parsing the HTML code"*, *"Multiple labels are associated with a single form control due to the same form being rendered in multiple tabs simultaneously"*, *"Link title not descriptive at places"*, *"Errors are not readable by screen reader"*.
- Tested pages (11) include the homepage, Client stories, About us, Newsroom, Featured articles, Careers, Reports, Responsible Business, Services Data, Services, Contact Us.
- Tooling: WAVE, Contrast Colour Checker, Web Developer toolbar, Accessibility Insights for web, NVDA, Chrome Lighthouse, Landmark help; keyboard testing on Chrome and Edge.

**What I independently corroborate:**

- **Contrast.** The `#DB2443` rest / `#FF767F` hover red button states, the `1px #2E323A` focus ring, and `--zodiak-text-disabled:#888F9A` on `#12151D` are all plausible sources of the declared contrast issues. Body `#121212` on white and link `#005080` on white are fine.
- **Keyboard.** Positive: `role="switch"` with a keydown handler on the theme toggle, `aria-expanded` on mega-menu buttons, visible skip link.
- **Captions.** The homepage hero is a muted `loop` video with **no `<track>` element** — consistent with the declared missing-captions failure. A pause/play control does exist.
- **Reduced motion.** Exactly **one** `prefers-reduced-motion` query exists, guarding only smooth scrolling: `@media(prefers-reduced-motion: no-preference){:root{scroll-behavior:smooth}}`. The GSAP scroll animations have **no reduced-motion path** — a gap the statement does not list.
- **Headings.** `/careers/` returned **no `<h1>`**; the page opens at `h2`.

**Inferred:** the statement is unusually honest by industry standards (publishing a 10-criterion failure list is rare), but it is **two years old** in your 2025–2026 window, predates the dark-mode rollout, and does not cover the AI in Action microsite or the hydration defects.

---

## 9. Sources

**Directly fetched (HTTP 200):** homepage; `/services/`, `/insights/`, `/careers/`, `/contact-us/`, `/about-us/`, `/about-us/meet-geti/`, `/about-us/our-story/`, `/about-us/sogetilabs/`, `/about-us/responsible-business/`, `/insights/reports/`, `/insights/executive-summits/`, `/make-way-for-ai-in-action/`, `/accessibility/`. Plus `themes/sogeti2024/public/dist/app.css` (812,130 bytes), the `sogeti-custom-button`, `yeti-banners` and `cg-block-intro-para-video` block stylesheets, and `sogeti-blue-new.svg`. https://www.capgemini.com/ confirms the `capgemini2025` theme and shared `zodiak` tokens.

**Failed / unavailable:** `sogeti.com/about/` (404); `capgemini.com/brand/`, `/about-us/brand/`, `/brand-hub/` (404); `brand.capgemini.com`, `brandhub.capgemini.com` (no DNS); DuckDuckGo HTML endpoints (202); web search backend (400 — unavailable this session).

---

## 10. Bottom line — discrepancies vs. the 2024 guidelines

| # | Guideline says | Live site does |
|---|---|---|
| 1 | Deep Purple `#2B0A3D` secondary | **Absent entirely** (0 occurrences) |
| 2 | Ubuntu / Ubuntu Mono **Bold** headlines | **Light 300 / Regular 400**, `.1–.2px` tracking |
| 3 | Ubuntu Mono for headlines | Mono only in bylines, tags, labels at ≤1.125rem |
| 4 | Isometric illustration & icons | Video heroes, 3D yeti mascot, Tabler Icons |
| 5 | Cool Tech Red `#F53B53` | Six reds; `#F53B53` only as pressed state + logo dot |
| 6 | *(silent on theme)* | **Dark mode by default**, undocumented Zodiak neutral ramp |
| 7 | Capgemini Blue `#0070AD` primary | Wordmark keeps `#0058AB`; `#0070AD` largely token-only |
| 8 | *(silent on delivery)* | Fonts served as raw **`.ttf`**, 16 duplicate `@font-face` blocks |
| 9 | *(silent on system)* | Two token layers plus unpurged Bootstrap `#0d6efd` |

The honest summary: Sogeti's web presence in 2025–2026 has **moved onto Capgemini's Zodiak design system** and adopted a dark-first, video-led, pill-button aesthetic the November 2024 guidelines do not describe. The guidelines' colour and type rules survive in *token names* but not in *rendered output*. Reconciling those two documents is the substantive brand-governance task here.
