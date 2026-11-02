# Data visualisation

Sogeti charts are precise, flat and annotated. They are not dashboards and they
are not decoration. The test is simple: can a reader who was not in the room
state the finding, the unit and the source without asking a question?

---

## 1. Choose the chart from the question

| Question | Chart | Avoid |
|---|---|---|
| How do categories compare? | Sorted horizontal bars | 3D bars, pie with many slices |
| How has a measure moved? | Line, with a clear time axis | Sparkline with no period |
| What is the composition? | Stacked bar (few categories) or a table | 3D pie, donut with 8 slices |
| How is a population distributed? | Histogram or dot plot | A single average with no spread |
| Is there a relationship? | Scatter with labelled outliers | Two lines on unrelated scales |
| What is the journey? | Timeline or process diagram | A bar chart of stages |
| What is the system? | Architecture/flow diagram | Isometric tech art |

If a table communicates faster, use a table. Sogeti artifacts often need a
table, not a chart.

---

## 2. Palette

Use the infographic groups from [`color-system.md`](color-system.md):

1. Start with **Blue/Purple**: `#005A82`, `#0070AD`, `#80B8D6`, `#12ABDB`,
   `#88D5ED`, `#2B0A3D`.
2. Pair with **one** other group: green/aqua, pink/purple or peach/brown.
3. Use as few colours as possible. Group data into types to reduce the count.
4. Never use more than seven categorical colours. Prefer direct labels and
   small multiples.
5. Do not use a sequential ramp for nominal categories. A ramp implies a
   ranking that does not exist.
6. Do not use a rainbow for ordered data.

Semantic status colours are separate from the infographic palette: `--ok`
`#007A4D`, `--warn` `#8A4B12`, `--risk` `#A31335`, with their background tints.

---

## 3. Anatomy of a Sogeti chart

Every chart has:

- **Title** that states the finding, not the metric. “Ownership is the first
  constraint”, not “Bar chart of barriers”.
- **Subtitle** with the unit, base and period.
- **Axis labels** with units. A y-axis without `%`, `€` or `days` is incomplete.
- **A zero baseline** for bars. If the axis is truncated, say so and explain why.
- **Direct labels** where possible. Legends are a last resort.
- **One annotation** that names the insight, not every data point.
- **Source line** with owner and date, or a visible “illustrative” label.
- **Accessible title and description**, plus a table fallback for complex data.

No 3D, no perspective, no drop shadows, no gradient fills on bars, no
background images, no animated counters.

---

## 4. SVG recipe

```html
<div class="chart">
  <div class="chart__head">
    <div>
      <p class="chart__title">Phase 2 scope completion</p>
      <p class="chart__sub">Percent of agreed scope, weeks 1–12</p>
    </div>
  </div>

  <svg viewBox="0 0 720 320" role="img" aria-labelledby="chart-title chart-desc">
    <title id="chart-title">Scope completion is 82 percent at week 8 against a plan of 100 percent.</title>
    <desc id="chart-desc">Line chart from week 1 to week 12. Plan rises to 100 percent at week 8. Actual reaches 82 percent at week 8, then a dashed projection runs to 96 percent at week 12.</desc>

    <g class="grid-line">
      <line x1="56" y1="40" x2="690" y2="40"/>
      <line x1="56" y1="100" x2="690" y2="100"/>
    </g>
    <g class="axis-line">
      <line x1="56" y1="280" x2="690" y2="280"/>
      <line x1="56" y1="40" x2="56" y2="280"/>
    </g>

    <!-- direct labels, no legend -->
    <polyline points="56,280 445,40 668,40" fill="none"
      stroke="#B7C3CC" stroke-width="2" stroke-dasharray="5 5"/>
    <polyline points="56,280 112,261 167,242 223,222 278,198 334,174 390,148 445,83"
      fill="none" stroke="#0070AD" stroke-width="3"/>
    <circle cx="445" cy="83" r="5" fill="#0070AD"/>
  </svg>

  <p class="chart__source">Joint delivery dashboard, week 8. Illustrative data.</p>
</div>
```

The working example is in
[`templates/03-steerco.html`](templates/03-steerco.html), and a full research
page is [`templates/11-data-story.html`](templates/11-data-story.html).

---

## 5. Accessible charts

- Every chart SVG has `role="img"` and `aria-labelledby` pointing to a `<title>`
  and `<desc>`.
- The title states the finding; the description states the series, period and
  unit.
- For complex charts, provide a `<details>` table with the same values.
- Do not put the only copy of the data in an image.
- Do not use colour alone. Label series directly, or use line styles and markers.
- Ensure 3:1 non-text contrast for bars/lines against the background.
- Provide a source and a date in text, not only in a tooltip.

---

## 6. Numbers and claims

- A number without a unit is not a finding.
- A percentage without a base is not a finding.
- A target without a baseline is a wish.
- A source without a date is not a source.
- A trend without a period is a decoration.
- An animated counter without a source is a credibility risk.

If the data is illustrative, say so visibly. The Northline templates do this:
“Client-reported outcomes for an illustrative scenario.” The research template
does this in the method note and the caveat.

---

## 7. Do / don't

| Do | Don't |
|---|---|
| Sort horizontal bars by value | Random category order |
| Label the unit on the axis | “Value” as an axis title |
| Annotate the one point that matters | Label every point |
| Use one accent colour | Rainbow categorical palette |
| Put the source under the chart | Hide the source in a tooltip |
| Use a table for exact comparison | Force a chart when a table is clearer |
| State the base in the subtitle | “%” with no denominator |
| Show a zero baseline for bars | Truncate the axis silently |
| Use flat fills | 3D, bevels, gradients on data |
