# Quality gates

A page is not done when it looks good. It is done when the argument is clear, the
evidence is honest, the gate passes, and a human has tested it at 360 px, with a
keyboard, at 200% zoom, and in print.

---

## 1. The five gates

| Gate | Question | Evidence | Owner |
|---|---|---|---|
| 0. Job | What is this page for, and who reads it? | One-sentence job; reader; decision | Author |
| 1. Content | Is every claim true, sourced or labelled? | Source lines; approvals; illustrative labels | Author + account lead |
| 2. Mechanical | Does the source pass the Sogeti audit? | `sogeti_audit.py` output | Builder |
| 3. Human | Can a person use it? | Keyboard, 360 px, zoom, print | Reviewer |
| 4. Brand/legal | Is it safe to publish? | Logo, trademarks, quotes, photos, data | Brand/legal |

Do not skip Gate 1 because Gate 2 passes. A technically clean page with a
fabricated stat is worse than a rough page with real evidence.

---

## 2. Gate 0: the job

Write these five lines before opening a template:

```
Job:
Reader:
Decision or action:
One thing they should remember:
What they should do next:
```

If you cannot fill them, the page is not ready. A “brochure” is not a job.

---

## 3. Gate 1: content

- [ ] Every number has a source, a date and a base, or a visible “illustrative”
      label.
- [ ] Every quote has a name, role, organization and written approval, or is
      labelled composite.
- [ ] Every client name and logo has permission.
- [ ] Every certification, award or partnership is current and evidenced.
- [ ] The headline passes the logo-swap test.
- [ ] There is no lorem ipsum.
- [ ] The CTA describes the next step.
- [ ] The export produces a useful Markdown record, not a screenshot of the page.
- [ ] The page has one job and one reader.
- [ ] The first screen answers the reader's question.

Approval record:

| Item | Approved by | Date | Notes |
|---|---|---|---|
| Client name | | | |
| Metrics | | | |
| Quotes | | | |
| Logo/photography rights | | | |
| Legal/regulatory | | | |

---

## 4. Gate 2: mechanical

Run:

```bash
python3 scripts/sogeti_audit.py path/to/artifact.html
```

Interpretation:

| Verdict | Meaning | Action |
|---|---|---|
| **PASS** | No Tier 1 or 2 findings | Continue to Gate 3 |
| **REVIEW** | One identity tell or a claim to verify | Fix or justify in writing |
| **FAIL** | A Tier 1 blocker or 3+ identity tells | Fix before shipping |

The script is conservative. A finding means “present; confirm the job”. Do not
“fix” a finding by adding decoration. The pass condition is subtraction.

The script cannot see:

- rendered contrast on a gradient or image;
- horizontal overflow at 360 px;
- keyboard traps;
- whether a chart is truthful;
- whether a quote is approved;
- whether the logo is master artwork.

Those are Gate 3 and Gate 4.

---

## 5. Gate 3: human

### 5.1 Keyboard

Tab from the top.

- [ ] Skip link appears and jumps to `#main`.
- [ ] Focus is visible on every link, button, input and select.
- [ ] The mobile menu opens and closes with Enter/Space, and `aria-expanded`
      changes.
- [ ] Tabs move with arrow keys.
- [ ] The export button is reachable and works with Enter.
- [ ] No focus trap and no lost focus after an action.
- [ ] The deck advances with arrow keys, Home/End, and `N` toggles notes.

### 5.2 360 px

- [ ] No horizontal scroll on the page.
- [ ] Display type fits; no single word on a line by itself.
- [ ] Tables scroll inside `.table-wrap`, not the page.
- [ ] The deck is usable (slides may stack; controls remain).
- [ ] The footer columns stack.
- [ ] Buttons are at least 44 px tall.

### 5.3 200% zoom

- [ ] No overlap.
- [ ] No clipped text.
- [ ] The layout reflows rather than requiring horizontal scroll.
- [ ] Charts remain readable.

### 5.4 Print / PDF

- [ ] Header, footer, nav, filters and export bars are hidden.
- [ ] No card or table splits awkwardly across pages.
- [ ] Charts are legible in greyscale.
- [ ] The logo and source lines remain.
- [ ] The deck prints one slide per page.
- [ ] The brief fits the intended page count.

### 5.5 Reduced motion

- [ ] Enable `prefers-reduced-motion` in the OS/browser.
- [ ] Nothing disappears or fails to appear.
- [ ] No auto-playing motion remains.
- [ ] The page is usable without animation.

---

## 6. Gate 4: brand and legal

- [ ] Logo is master artwork, or the draft is flagged as using reference art.
- [ ] Logo meets minimum size (160 px screen) and clear space.
- [ ] The shape is used once, with margins, not rotated 90°.
- [ ] Colours are from the system; no invented brand hex.
- [ ] Ubuntu is embedded; Verdana is the only fallback.
- [ ] Sentence case is used throughout.
- [ ] No em dashes, no banned buzzwords, no rule-of-three slogans.
- [ ] Photography is real, credited and licensed; no synthetic people.
- [ ] No external network requests, trackers or CDNs.
- [ ] The artifact contains no confidential client data beyond the approved
      audience.
- [ ] The “illustrative” label is visible wherever fictional data appears.

---

## 7. Common failures and fixes

| Symptom | Likely cause | Fix |
|---|---|---|
| Hero text touches the shape or overflows | Grid child `min-width:auto`; max-width too wide | `min-width:0` on grid children; cap `.hero__copy` |
| Page scrolls horizontally at 360 px | A wide table or image outside a wrapper | `.table-wrap`, `max-width:100%`, `min-width:0` |
| Font looks like Times | CSS not inlined or `@font-face` missing | Build with `scripts/build.py`; check `fonts.css` |
| Logo is pixelated | Scaled beyond the PNG's resolution | Use a larger master; keep 164 px header / 196 px footer |
| Audit fails `T1-remote` | CDN font, icon pack or image | Inline everything; no external requests |
| Audit fails `T1-label` | Inputs without labels | Add `<label for>` or wrap in `<label>` |
| Audit fails `T1-chart` | SVG chart without a title | Add `role="img"`, `<title>`, `<desc>` |
| Contrast fails | Vibrant Blue text on white | Use `--blue` for text; keep vibrant for graphics |
| Shape looks like a rounded card | Used `border-radius` | Use the clip path |
| Everything fades up on scroll | Generic reveal added | Remove it; use one page-load moment |
| Three equal cards appear | Layout default, not content | Use a numbered argument, table or real cardinality |
| Deck prints only one slide | Print CSS missing | `.slide[hidden]{display:flex!important}` |
| Copy button fails on `file://` | Clipboard API requires a secure context | `Sogeti.fallbackCopy` is built in |
| Assessment radar is blank | JS error or missing IDs | Check the console; keep `data-dim` and output IDs aligned |
| Appraisal ranking does not move | Weight inputs not bound | Check `data-weight` / `data-criterion` names |

---

## 8. Sign-off

```
Artifact:
Path:
Job:
Reader:
Gate 1 content:   PASS / FAIL   Reviewer:        Date:
Gate 2 mechanical: PASS / REVIEW / FAIL   Verdict:
Gate 3 human:     PASS / FAIL   Reviewer:        Date:
Gate 4 brand/legal: PASS / FAIL Reviewer:        Date:
Known exceptions:
Ship decision:    SHIP / HOLD
```

Attach the audit output to the sign-off. If you overrode a finding, write why.
“It looks better” is not a reason; “the status stripe is the risk control, and
the label is present” is.
