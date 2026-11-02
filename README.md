# Sogeti HTML effectiveness

A complete, self-contained skill for producing Sogeti-branded, single-file HTML
artifacts that are worth reading, safe to ship and hard to mistake for generic
AI output.

Built from the **Sogeti brand guidelines v3** (November 2024) and a 2026 audit of
the live Sogeti site, with a 40-item mechanical gate informed by 2026 research on
AI slop in UI.

---

## What is in the folder

```
sogeti-html-effectiveness/
├── SKILL.md                     ← the operating manual (start here)
├── README.md                    ← this file
├── reference/
│   ├── Sogeti-brand-V3-guidelines.pdf       ← the authoritative PDF
│   ├── brand-guidelines-raw.txt             ← searchable extraction
│   ├── README.md                            ← source notes and caveats
│   └── research/
│       ├── SOGETI_DIGITAL_BRAND_REPORT.md   ← 2026 live-site audit
│       ├── AI-SLOP-FIELD-GUIDE-2026.md      ← 40-item research + sources
│       └── logo.svg                         ← observed live logo
├── references/
│   ├── brand-foundations.md
│   ├── color-system.md
│   ├── typography.md
│   ├── logo-and-shapes.md
│   ├── voice-and-copy.md
│   ├── design-system.md
│   ├── design-system-visual.html
│   ├── data-visualization.md
│   ├── accessibility.md
│   ├── content-models.md
│   ├── anti-slop.md
│   ├── quality-gates.md
│   ├── web-and-digital.md
│   ├── recipes.md
│   ├── catalog.md
│   └── templates/
│       ├── index.html                       ← the gallery
│       ├── 01-insight-article.html
│       ├── …
│       └── 14-slop-audit.html
├── assets/
│   ├── sogeti.css               ← tokens + components
│   ├── fonts.css                ← base64 WOFF2
│   ├── sogeti.js                ← nav, tabs, copy, print
│   ├── fonts/                   ← WOFF2 + TTF + licence
│   ├── logos/                   ← colour / white lockups
│   ├── illustrations/           ← isometric diagrams + architecture SVGs
│   └── thumbnails/              ← gallery previews
├── examples/
│   └── starter.html             ← minimal self-contained starting point
└── scripts/
    ├── build.py                 ← inline CSS/JS/images + partials
    └── sogeti_audit.py          ← mechanical gate
```

---

## Quick start

### 1. Open the shelf

Open `references/templates/index.html` in a browser. Every file is standalone.

### 2. Read the manual

[`SKILL.md`](SKILL.md) – the workflow, non-negotiables and gate.
[`references/brand-foundations.md`](references/brand-foundations.md) – the brand.
[`references/anti-slop.md`](references/anti-slop.md) – the gate and the traps.

### 3. Build a new artifact

```bash
cp examples/starter.html ~/Documents/my-project/html-docs/page.html
# edit the content, keep the system
python3 scripts/sogeti_audit.py ~/Documents/my-project/html-docs/page.html
```

Or start from a source template and build a new one:

```bash
cp references/templates/_src/02-pursuit-one-pager.html \
   references/templates/_src/my-page.html
# edit it; the ../../../assets paths resolve from _src
python3 scripts/build.py references/templates/_src/my-page.html
cp references/templates/my-page.html \
   ~/Documents/my-project/html-docs/page.html
```

`build.py` expands partials, inlines the CSS (with fonts), JS and local images,
and writes the built file to `references/templates/`. The source must live at the
same depth as `_src` so the `../../../assets` paths resolve; otherwise adjust
the paths before building.

### 4. Audit

```bash
python3 scripts/sogeti_audit.py references/templates/*.html
python3 scripts/sogeti_audit.py path/to/artifact.html --json
```

Exit code `0` = pass/review, `1` = fail.

---

## Install globally

The repository root **is** the skill, so it can be cloned or linked directly
into any global skills directory. Run:

```bash
./scripts/install_global.sh
```

It links the skill into the global directories used on this machine:

- `~/.agents/skills/sogeti-html-effectiveness`
- `~/.dsh/skills/sogeti-html-effectiveness`
- `~/.claude/skills/sogeti-html-effectiveness`

Manual equivalent:

```bash
ln -sfn ~/Documents/sogeti-html-effectiveness \
      ~/.agents/skills/sogeti-html-effectiveness
ln -sfn ~/Documents/sogeti-html-effectiveness \
      ~/.dsh/skills/sogeti-html-effectiveness
ln -sfn ~/Documents/sogeti-html-effectiveness \
      ~/.claude/skills/sogeti-html-effectiveness
```

The skill name in `SKILL.md` is `sogeti-html-effectiveness`. If the folder
moves, rerun the installer.

## Repository layout

There is no nested `.skills/` directory. The repo root is the skill: `SKILL.md`
is the entry point, `references/` is the progressive-disclosure layer,
`assets/` is the shared design system, and `scripts/` contains the build and
audit tools. Cloning the repo into a skills directory gives you a working skill
with no extra nesting.

## Design decisions

- **Light-first.** Cool Grey/white surfaces, one Capgemini Blue field per page.
  The live site's dark default is a product decision, not a brand rule.
- **Mono display, sparingly.** Ubuntu Mono Bold is the signature top-tier
  headline face. It is used once per page, not on every heading.
- **Shape as architecture.** The primary shape is a field with a scooped corner,
  implemented as a responsive `clip-path`, not a rounded card.
- **Flat surfaces.** 2 px surfaces, pill controls, hairline rules, no wide
  shadows, no glass, no gradients as decoration.
- **Typographic scale is a system.** `clamp()` sizes, 60–75 character measures,
  sentence case, no uppercase tracking.
- **Evidence over assertion.** No invented stats; illustrative data is labelled;
  charts have axes, units and sources.
- **Gates over advice.** The 40-item checklist and the audit script do the work
  that a paragraph of “avoid AI slop” cannot.

---

## The reference artifacts

| # | Artifact | What it shows |
|---|---|---|
| 01 | Insight article | Editorial long-form, shape hero, captioned diagram, summary export |
| 02 | Pursuit one-pager | Cover, brief grid, phased approach, value case, sign-off |
| 03 | Steering group | RAG, decisions, delivery chart, risks, actions |
| 04 | Architecture | Current/target diagrams, ADR, cutaway rules, tabs |
| 05 | Workshop synthesis | Selectable themes, filters, decision register, export |
| 06 | Maturity assessment | Live radar, 8 dimensions, table fallback, export |
| 07 | Options appraisal | Weighted matrix, presets, live ranking, export |
| 08 | Client story | Dark outcome opener, handover figure, outcomes, caveats |
| 09 | Event page | Square card, agenda, roles, ICS download |
| 10 | 90-day playbook | 20 checks, saved progress, field notes, export |
| 11 | Data story | Data opener, direct-labelled charts, method, caveat |
| 12 | Executive deck | Keyboard nav, notes, fullscreen, print-to-PDF |
| 13 | Decision brief | Decision memo, decision record, sign-off |
| 14 | Slop audit | 40 checks, four tiers, live verdict, export |

---

## Trademarks, fonts and sources

- **Sogeti**, **Capgemini**, the wordmarks, the spade symbol and the brand
  shapes are trademarks of Sogeti/Capgemini. Use them only for authorized work.
- The PNG logos in `assets/logos/` are reference-quality extractions from the
  public brand PDF, not master artwork. Replace with Sogeti Global Marketing
  files for production.
- **Ubuntu** and **Ubuntu Mono** are licensed under the
  [Ubuntu Font Licence 1.0](https://ubuntu.com/legal/font-licence). The subset
  WOFF2 files are embedded for offline use; the TTF sources and licence notice
  are in `assets/fonts/`.
- Brand source: *Sogeti brand guidelines, Version 3* (November 2024), PDF in
  `reference/`.
- Live-site research: `reference/research/SOGETI_DIGITAL_BRAND_REPORT.md`.
- AI-slop research: `reference/research/AI-SLOP-FIELD-GUIDE-2026.md`.

The reference client **Northline Group**, its people, quotes and metrics are
fictional and labelled illustrative. Replace them with approved client facts
before any external use.

---

## License

The skill's original documentation, CSS, JS and templates are provided for
internal Sogeti/Capgemini work and for the user's personal use. The Sogeti and
Capgemini marks, the brand PDF and the extracted logo assets remain the property
of their owners and are not licensed by this repository. Photography, client
logos and third-party assets require their own permissions.

If you reuse the system outside Sogeti, replace the brand assets and the
Northline scenario, and keep the accessibility and anti-slop gates.
