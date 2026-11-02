# Reference sources

This folder holds the primary sources behind the skill. The synthesis lives in
`../references/`; these files are for verification and for agents that need the
original wording.

| File | What it is | How to use it |
|---|---|---|
| `Sogeti-brand-V3-guidelines.pdf` | The official 45-page PDF, downloaded from sogeti.com (26 MB) | The authority for logo, colour, type, shapes, imagery, writing |
| `brand-guidelines-raw.txt` | `pdftotext -layout` extraction (3,017 lines) | Search for a phrase without opening the PDF |
| `research/SOGETI_DIGITAL_BRAND_REPORT.md` | The 2026 live-site audit (WordPress/Zodiak, dark mode, fonts, colour drift, voice, accessibility) | Read before making a digital-parity decision |
| `research/AI-SLOP-FIELD-GUIDE-2026.md` | The 4,249-word research report, 19 sources, 40-item checklist | The evidence behind `../references/anti-slop.md` |
| `research/app.css` | The live Sogeti theme stylesheet (812 KB) | Verify a token or font declaration cited in the audit |
| `research/logo.svg` | The live two-shape logo SVG (wordmark + dot) | Compare with the PDF lockup |

## Method

- The PDF was downloaded in November 2026 from
  `https://www.sogeti.com/wp-content/uploads/sites/3/2024/11/Sogeti-brand-V3-guidelines.pdf`
  (HTTP 200, 26,320,347 bytes).
- Text was extracted with `pdftotext -layout`; pages were rendered with
  `pdftoppm` at 80/300 dpi for visual inspection. The logo PNGs in
  `../assets/logos/` were extracted from page 3 at 300 dpi, background removed
  and colour-classified to the brand palette.
- The live-site audit used direct HTTP retrieval of the homepage and inner
  pages, the CSS bundles, and the public accessibility statement. Search
  backends were unavailable during that session; the report flags that limit.
- The AI-slop research used Brave Search, the HN Algolia API and direct fetches.
  `web_search` was unavailable; the report flags that too.

## Caveats

- The live site runs a Capgemini Group Zodiak theme and may change. It is not
  the brand authority. The PDF and approved master artwork are.
- The 2024 PDF contains a few internal inconsistencies (logo minimum 100 px vs
  160 px; SogetiLabs 160 px vs 255/390 px). This skill uses the conservative
  values and says so.
- No public Capgemini brand-hub URL could be verified. Do not cite one.
- The extracted logo PNGs are drafting assets, not master artwork. Replace them
  with Global Marketing files before production.
- Client names, quotes and metrics in the templates are fictional and labelled
  illustrative.

## Regenerate the text

```bash
pdftotext -layout Sogeti-brand-V3-guidelines.pdf brand-guidelines-raw.txt
```
