# Accessibility and quality

Target: **WCAG 2.2 AA** for every artifact. The Sogeti public accessibility
statement commits to WCAG 2.1 AA with partial compliance and publishes its
known gaps. This skill aims higher for the artifacts it produces, and it never
uses the statement as an excuse.

Accessibility is not a final checklist. It is a set of decisions made while
building.

---

## 1. The non-negotiables

1. **Semantic HTML.** One `<main>`, one `<h1>`, logical heading order,
   `<header>`, `<nav>`, `<footer>`, `<table>` for tables.
2. **Skip link** as the first focusable element.
3. **Visible focus** on every interactive element: 3px red outline, 3px offset.
4. **Contrast:** 4.5:1 for normal text, 3:1 for large text and UI graphics.
5. **Keyboard:** every action reachable and operable without a mouse.
6. **No content hidden at rest** waiting for a scroll handler.
7. **Reduced motion:** respect `prefers-reduced-motion`.
8. **Labels:** every form control has a visible label or an accessible name.
9. **Alt text:** meaningful images have alt; decorative images have `alt=""`.
10. **Zoom and reflow:** usable at 200% zoom and 360px width without horizontal
    scrolling, except data tables and diagrams inside a labelled scroll region.

---

## 2. Contrast

Use the tested pairs in [`color-system.md`](color-system.md). The traps:

- Vibrant Blue `#12ABDB` on white is **2.67:1**. Do not use it for text.
- Cool Tech Red `#F53B53` on white is **3.73:1**. Large text only. Use
  `#A31335` for small red text.
- White on `#F53B53` is **3.73:1**. Use `#DB2443` for red buttons with white.
- Light blue labels on Capgemini Blue need `#EAF6FB` (4.86:1), not `#88D5ED`
  (3.26:1).
- Muted grey `#5D6973` on white is 5.62:1; on Cool Grey 5.17:1. Fine for
  captions, not for long body copy.

Do not rely on colour alone for status. A red dot needs a text label (“High”),
not just a red dot.

---

## 3. Keyboard and focus

- Tab order follows the visual order.
- The skip link appears on focus and jumps to `#main`.
- Mobile menu toggle has `aria-expanded`, `aria-controls` and a label.
- Tabs use `role="tablist"`, `role="tab"`, `aria-selected`, `aria-controls`,
  arrow-key navigation and `hidden` panels.
- `details/summary` is used for disclosures rather than a div with a click
  handler.
- Buttons are `<button>`, links are `<a href>`. Do not put a click handler on a
  div.
- Focus is never trapped except in a modal; the templates do not use modals.
- After a slide change, the counter has `aria-live="polite"`; focus is not
  stolen.
- `:focus-visible` is styled globally. Do not remove outlines.

---

## 4. Motion

- All non-essential motion is wrapped in
  `@media (prefers-reduced-motion: no-preference)` or disabled under
  `prefers-reduced-motion`.
- No auto-playing video or audio.
- No marquee without pause controls.
- No parallax or cursor followers.
- The one page-load `rise` is optional and short.
- No flashing content.

---

## 5. Forms and interactive tools

- Every input has a `<label for>` or is wrapped in a `<label>`.
- Ranges have a visible label and an output; the output is associated with the
  input.
- Buttons that copy or print state what they do, not just an icon.
- Exports use `aria-live="polite"` for the confirmation toast.
- Error messages say what happened and how to fix it. A form that cannot report
  an error is a Tier 1 blocker.
- Do not use placeholder text as the only label.
- Do not disable zoom (`user-scalable=no`) or set a maximum scale.

---

## 6. Tables and charts

- Tables have `<caption>`, `<th scope="col">` and `<th scope="row">` where
  relevant.
- Wide tables scroll inside `.table-wrap`, which has a visible border and can be
  focused. Add `tabindex="0"` and an `aria-label` if the table is wider than the
  viewport.
- Charts have `role="img"`, `<title>`, `<desc>` and a table fallback when the
  data is complex.
- Do not use colour alone to distinguish series.
- Do not put text in images.

---

## 7. Print and PDF

- Hide navigation, filters, export bars and toasts.
- Do not split cards, charts or tables across pages.
- Use a white background and dark ink.
- Keep the logo and the source lines.
- Test in greyscale. A chart that only works in colour fails in print.
- For the deck, print every slide, one per page.
- For the decision brief, use 16mm margins and a single sheet where possible.

---

## 8. Testing

### Automated

```bash
python3 scripts/sogeti_audit.py path/to/artifact.html
```

The script checks the structural Tier 1 items it can see: alt text, labels,
one h1, skip link, main landmark, remote assets, reduced motion, chart titles,
placeholder copy and numeric claims. It cannot measure rendered contrast or
horizontal overflow. Those are manual.

### Manual, 10 minutes

1. **Keyboard only.** Tab from the top. Can you reach the skip link, nav, every
   control and the export? Is focus visible? Can you activate with Enter/Space?
2. **360px.** Resize. Check for horizontal scroll. Check the display type,
   tables, deck slides and footer.
3. **200% zoom.** Check reflow and overlap.
4. **Screen reader spot check.** Headings outline, image alts, form labels,
   `aria-live` confirmations.
5. **Print preview.** Check page breaks, hidden chrome, chart legibility.
6. **Reduced motion.** Enable it in the OS/browser. Confirm nothing disappears
   or fails to animate in.
7. **Content.** Every number has a source or an illustrative label. Every quote
   is approved or labelled composite. Every client name is approved.

### Useful tools

- Browser accessibility tree / Lighthouse.
- WAVE or axe DevTools.
- Contrast checker for the exact rendered colours.
- `prefers-reduced-motion` emulation in DevTools.
- Print preview at A4 and Letter.

---

## 9. Known trade-offs

- The templates use `clip-path` on the brand shape. It is decorative and
  `aria-hidden`; the content is outside it.
- The deck uses `hidden` on inactive slides; print CSS overrides it so every
  slide prints. Screen readers only see the active slide.
- The assessment radar is an SVG with a title/description and a table fallback.
  The range inputs are the source of truth.
- The synthesis board uses a filter that hides themes; hidden themes are removed
  from the export. The filter state is not persisted.
- The playbook saves checkbox state in `localStorage`. It does not send data
  anywhere. The “Reset” button clears it.

---

## 10. Definition of done

- [ ] `sogeti_audit.py` verdict is PASS or an explained REVIEW.
- [ ] Keyboard pass complete.
- [ ] 360px pass complete.
- [ ] 200% zoom pass complete.
- [ ] Print/PDF pass complete.
- [ ] Every number sourced or labelled illustrative.
- [ ] Every quote approved or labelled composite.
- [ ] Logo is master artwork (or flagged as draft).
- [ ] No external network requests.
- [ ] File saved in `html-docs/` and linked in the response.
