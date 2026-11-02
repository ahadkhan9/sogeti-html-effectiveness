# Recipes

Copy-paste blocks that match the working system. The complete starter is
[`examples/starter.html`](../examples/starter.html). All source templates live in
[`references/templates/_src/`](templates/_src/).

---

## 1. Document skeleton

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Page title – Sogeti</title>
<meta name="description" content="One sentence that says what this page is for.">
<link rel="stylesheet" href="../../../assets/sogeti.css">
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
<!-- @include _partials/shapes.html -->
<!-- @include _partials/header.html -->

<main id="main">
  <section class="page-head" id="context">
    <div class="page-head__shape" aria-hidden="true"></div>
    <span class="page-head__mark" aria-hidden="true">01</span>
    <div class="wrap">
      <p class="kicker">Section / Topic</p>
      <h1 class="display display--s">The claim.</h1>
      <p class="lede">The evidence or the tension in two sentences.</p>
      <div class="page-head__meta">
        <span>Owner</span><time datetime="2026-11-14">14 November 2026</time>
      </div>
    </div>
  </section>

  <section class="section section--white" id="approach">
    <div class="wrap">
      <div class="section-head">
        <div><p class="kicker">01 / The point</p><h2 class="h2 mt-3">A specific heading.</h2></div>
        <p class="lede">A short framing paragraph.</p>
      </div>
      <!-- content -->
    </div>
  </section>
</main>

<!-- @include _partials/footer.html -->
<script src="../../../assets/sogeti.js"></script>
</body>
</html>
```

Build:

```bash
python3 scripts/build.py references/templates/_src/your-page.html
python3 scripts/sogeti_audit.py references/templates/your-page.html
```

---

## 2. Signature hero with the brand shape

```html
<section class="hero hero--field">
  <div class="hero__field" aria-hidden="true"></div>
  <div class="wrap hero__inner intro">
    <div class="hero__copy">
      <p class="kicker">Insight: AI and data</p>
      <h1 class="display">AI doesn’t fail at the model. It fails at the handover.</h1>
      <p class="lede">Pilots look convincing in the demo room. Value shows up only when ownership, data and decisions move into the line.</p>
      <div class="hero__actions">
        <a class="btn btn--primary" href="#context">Read the field note
          <svg class="icon" aria-hidden="true"><use href="#i-arrow"/></svg>
        </a>
        <a class="btn btn--ghost" href="#contact">Talk to the team</a>
      </div>
    </div>
    <figure class="hero__art">
      <img src="../../../assets/illustrations/value-stack.svg" width="640" height="520" alt="Isometric diagram of a value stack.">
      <figcaption class="hero__caption">The value stack: data, models and decisions only compound when someone owns the join.</figcaption>
    </figure>
  </div>
</section>
```

One shape. One display statement. One visual with a caption.

---

## 3. Section head

```html
<div class="section-head">
  <div>
    <p class="kicker">02 / Delivery confidence</p>
    <h2 class="h2 mt-3">The first slice is live. The plan is not the point.</h2>
  </div>
  <p class="lede">At week 8, 82% of the phase scope is complete against a plan of 100%.</p>
</div>
```

---

## 4. Stat row

```html
<div class="grid grid--4">
  <div class="stat"><div class="stat__value">68%</div><p class="stat__label">Have a pilot in production</p><p class="stat__note">At least one use case</p></div>
  <div class="stat stat--vibrant"><div class="stat__value">31%</div><p class="stat__label">Have a named service owner</p><p class="stat__note">For the live service</p></div>
  <div class="stat"><div class="stat__value">22%</div><p class="stat__label">Track an operating metric</p><p class="stat__note">Beyond model accuracy</p></div>
  <div class="stat stat--red"><div class="stat__value">17%</div><p class="stat__label">Tested a rollback</p><p class="stat__note">With live-like traffic</p></div>
</div>
```

---

## 5. Table with a caption and source

```html
<div class="table-wrap">
  <table class="table">
    <caption>Handover evidence we ask to see before a production go-live.</caption>
    <thead><tr><th scope="col">Handover</th><th scope="col">Question</th><th scope="col">Evidence</th></tr></thead>
    <tbody>
      <tr><td class="strong">Ownership</td><td>Who is accountable?</td><td>A name in the service catalog, with budget</td></tr>
      <tr><td class="strong">Data</td><td>Which input can stop it?</td><td>A monitored contract with a fallback</td></tr>
    </tbody>
  </table>
</div>
<p class="source mt-3">Client discovery notes, week 4. Illustrative.</p>
```

For narrow columns, add `table--compact table--fit`.

---

## 6. Quote

```html
<blockquote class="quote">
  <blockquote>The model did not change the queue. The owner did.</blockquote>
  <figcaption><b>Operations director, Northline Group</b>Composite quote for layout reference. Replace with an approved quote.</figcaption>
</blockquote>
```

The CSS adds the curly quotes. Do not type them in the HTML as well.

---

## 7. Decision list (interactive)

```html
<div class="decision-list" id="decisions">
  <label class="decision">
    <input type="checkbox" checked data-decision="D1" data-label="Approve the intake slice">
    <span class="decision__body">
      <span class="decision__id">D1 · Approve</span>
      <strong>Approve the intake slice for production rollout.</strong>
      <span class="decision__note">The slice ran live for four weeks. <em>Recommendation: approve.</em></span>
    </span>
  </label>
</div>
<button class="btn btn--primary" type="button" id="copy-decisions">Copy decision record</button>
```

See the script in [`templates/_src/03-steerco.html`](templates/_src/03-steerco.html).

---

## 8. Export pattern

```html
<div id="summary" class="sr-only">
# Page summary

- One decision
- One owner
- One date
</div>

<button class="btn btn--primary" type="button"
  data-copy="#summary" data-copy-message="Summary copied as Markdown">
  <svg class="icon" aria-hidden="true"><use href="#i-copy"/></svg> Copy summary
</button>
```

The helper reads `innerText` from the target. Use `.sr-only`, not `hidden`, if
you need `innerText` to work reliably.

---

## 9. Chart block

```html
<div class="chart">
  <div class="chart__head">
    <div><p class="chart__title">Phase 2 scope completion</p><p class="chart__sub">Percent of agreed scope, weeks 1–12</p></div>
    <span class="tag tag--warn">Week 8</span>
  </div>
  <svg viewBox="0 0 720 320" role="img" aria-labelledby="chart-title chart-desc">
    <title id="chart-title">Scope completion is 82 percent at week 8 against a plan of 100 percent.</title>
    <desc id="chart-desc">Line chart from week 1 to week 12.</desc>
    <!-- grid, axes, plan, actual, direct labels -->
  </svg>
  <p class="chart__source">Joint delivery dashboard, week 8. Illustrative data.</p>
</div>
```

Full example: [`templates/_src/03-steerco.html`](templates/_src/03-steerco.html).

---

## 10. Tabs

```html
<div class="tabs" role="tablist" aria-label="Views" data-tabs>
  <button class="tab" id="tab-a" role="tab" aria-selected="true" aria-controls="panel-a" tabindex="0">Current</button>
  <button class="tab" id="tab-b" role="tab" aria-selected="false" aria-controls="panel-b" tabindex="-1">Target</button>
</div>
<div class="tabpanel" id="panel-a" role="tabpanel" aria-labelledby="tab-a" tabindex="0">…</div>
<div class="tabpanel" id="panel-b" role="tabpanel" aria-labelledby="tab-b" tabindex="0" hidden>…</div>
```

`Sogeti.initTabs` handles click, arrow keys, Home/End and `hidden`.

---

## 11. Deck slide

```html
<section class="slide" data-slide="2" data-notes="Speaker note for this slide." hidden aria-hidden="true">
  <p class="slide__eyebrow">The premise</p>
  <h2 class="mt-3">A specific claim.</h2>
  <div class="slide__grid slide__grid--3 mt-6">
    <div class="slide__item"><b>01</b><h3>Ownership</h3><p>Who answers on Monday?</p></div>
    <div class="slide__item"><b>02</b><h3>Data</h3><p>Who guarantees the input?</p></div>
    <div class="slide__item"><b>03</b><h3>Measurement</h3><p>Which number moves?</p></div>
  </div>
  <div class="slide__foot"><span>Section</span><span>02</span></div>
</section>
```

One `h1` in the deck (the cover). Eight slides is a good maximum for a readout.

---

## 12. Build and inline assets

From the skill root:

```bash
# build one
python3 scripts/build.py references/templates/_src/02-pursuit-one-pager.html

# build all
python3 scripts/build.py

# audit one
python3 scripts/sogeti_audit.py references/templates/02-pursuit-one-pager.html

# audit all, quiet
python3 scripts/sogeti_audit.py references/templates/*.html --quiet
```

The build:

- inlines `assets/sogeti.css` (with `fonts.css`),
- inlines `assets/sogeti.js`,
- inlines local `<img>` sources as base64,
- expands `<!-- @include ... -->` partials,
- prints a warning if a remote asset remains.

Source templates use `../../../assets/...` paths. The built file has no external
dependencies.

---

## 13. Starter

```bash
cp examples/starter.html /path/to/project/html-docs/page.html
```

Or copy the closest template and replace the content. Do not start from a blank
page and re-invent the type scale; the system is the point.
