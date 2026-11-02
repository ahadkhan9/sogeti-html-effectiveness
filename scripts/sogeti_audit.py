#!/usr/bin/env python3
"""Sogeti HTML artifact audit — mechanical gates, not stylistic advice.

Usage:
    python3 scripts/sogeti_audit.py path/to/artifact.html
    python3 scripts/sogeti_audit.py path/to/artifact.html --json
    python3 scripts/sogeti_audit.py references/templates/*.html --quiet

Exit codes: 0 = pass or review, 1 = fail (Tier 1 blocker or 3+ identity tells),
2 = usage error.

The checks are deliberately conservative. A hit means "present; confirm the job",
not "guilty". Read references/anti-slop.md before overriding a Tier 1 blocker.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from html.parser import HTMLParser
from pathlib import Path

# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

BRAND_HEX = {
    "#0070ad": "Capgemini Blue",
    "#005a82": "Capgemini Blue dark",
    "#0e82bf": "Blue mid (digital step)",
    "#12abdb": "Vibrant Blue",
    "#88d5ed": "Vibrant Blue 50",
    "#80b8d6": "Capgemini Blue 50",
    "#2b0a3d": "Deep Purple",
    "#f53b53": "Cool Tech Red",
    "#ff4019": "Sogeti Red (logo only)",
    "#f5f5f7": "Cool Grey",
    "#ffffff": "White",
}

DERIVED_HEX = {
    "#14181d", "#39434c", "#5d6973", "#d9e0e6", "#b7c3cc", "#edf6fa",
    "#e6eef3", "#007a4d", "#e3f5ec", "#8a4b12", "#fdf0e3", "#a31335",
    "#fde8ed", "#3d1554", "#f0e8f5", "#f4edf7", "#d92b43", "#fafbfc",
    "#eaf6fb", "#cde7f2", "#b9dee", "#a6d1e5", "#d6eaf4", "#f3fafd",
    "#ffb3bc", "#ff6b7d", "#b92339", "#220630", "#003a54", "#db2443", "#b01b3e", "#c9e2ef", "#eaf6fb",
}

BANNED_COPY = [
    "elevate", "seamless", "unlock", "empower", "supercharge", "game-chang",
    "world-class", "enterprise-grade", "best-in-class", "cutting-edge",
    "next-generation", "revolutioni", "transform your", "take your",
    "in today's fast-paced", "in today’s fast-paced", "unleash", "synerg",
    "leverage", "holistic", "paradigm", "frictionless", "best-of-breed",
    "future-proof", "mission-critical", "data-driven", "value-add",
]

SLOP_COLORS = [
    "#6366f1", "#8b5cf6", "#a855f7", "#7c3aed", "#4f46e5", "#667eea",
    "#764ba2", "#818cf8", "#c084fc", "#e879f9", "#0ea5e9", "#06b6d4",
]

PLACEHOLDER_RE = re.compile(
    r"lorem ipsum|dolor sit amet|\{\{\s*title\s*\}\}|\[client name\]|"
    r"\bTODO\b|\bTBD\b|placeholder|xxxx|99\.9% uptime|500k users",
    re.I,
)

A11Y_NAME_ATTRS = ("aria-label", "aria-labelledby", "title")


@dataclass
class Finding:
    tier: int
    code: str
    message: str
    detail: str = ""
    severity: str = "review"


@dataclass
class Audit:
    path: Path
    findings: list[Finding] = field(default_factory=list)
    stats: dict = field(default_factory=dict)

    def add(self, tier: int, code: str, message: str, detail: str = "", severity: str = "review") -> None:
        self.findings.append(Finding(tier, code, message, detail, severity))

    def by_tier(self, tier: int) -> list[Finding]:
        return [f for f in self.findings if f.tier == tier]


class Doc(HTMLParser):
    """Collect the pieces we need without pulling in a dependency."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.tags: list[tuple[str, dict]] = []
        self.text_parts: list[str] = []
        self.title = ""
        self.lang = ""
        self._in_title = False
        self._in_style = False
        self._in_script = False
        self._in_svg = 0
        self.svg_titles: list[str] = []
        self._current_svg_has_title = False
        self.images: list[dict] = []
        self.links: list[dict] = []
        self.buttons: list[dict] = []
        self._interactive: list[tuple[str, dict, list[str], bool]] = []
        self._label_depth = 0
        self.inputs: list[dict] = []
        self.labels: list[str] = []
        self.headings: list[tuple[str, str]] = []
        self._heading: str | None = None
        self._heading_text: list[str] = []
        self.styles: list[str] = []
        self.scripts: list[str] = []
        self._buf: list[str] = []

    def handle_starttag(self, tag: str, attrs_list: list[tuple[str, str | None]]) -> None:
        attrs = {k: (v or "") for k, v in attrs_list}
        self.tags.append((tag, attrs))
        if tag == "html":
            self.lang = attrs.get("lang", "")
        elif tag == "title":
            self._in_title = True
            self._buf = []
        elif tag == "style":
            self._in_style = True
            self._buf = []
        elif tag == "script":
            self._in_script = True
            self._buf = []
        elif tag == "svg":
            self._in_svg += 1
            self._current_svg_has_title = False
        elif tag == "title" and self._in_svg:
            self._current_svg_has_title = True
        elif tag == "img":
            self.images.append(attrs)
            if self._interactive:
                self._interactive[-1] = (self._interactive[-1][0], self._interactive[-1][1], self._interactive[-1][2], True)
        elif tag in ("a", "button"):
            self._interactive.append((tag, attrs, [], False))
        elif tag == "input":
            attrs["_in_label"] = "1" if self._label_depth else ""
            self.inputs.append(attrs)
        elif tag == "label":
            self.labels.append(attrs.get("for", ""))
            self._label_depth += 1
        elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
            self._heading = tag
            self._heading_text = []

    def handle_endtag(self, tag: str) -> None:
        if tag == "label" and self._label_depth:
            self._label_depth -= 1
        if tag in ("a", "button") and self._interactive and self._interactive[-1][0] == tag:
            kind, attrs, buf, has_img = self._interactive.pop()
            attrs["_text"] = "".join(buf).strip()
            attrs["_has_img"] = "1" if has_img else ""
            (self.links if kind == "a" else self.buttons).append(attrs)
        if tag == "title" and self._in_title:
            self.title = "".join(self._buf).strip()
            self._in_title = False
        elif tag == "style" and self._in_style:
            self.styles.append("".join(self._buf))
            self._in_style = False
        elif tag == "script" and self._in_script:
            self.scripts.append("".join(self._buf))
            self._in_script = False
        elif tag == "svg":
            if self._current_svg_has_title:
                pass
            self._in_svg = max(0, self._in_svg - 1)
        elif tag == self._heading:
            self.headings.append((tag, " ".join("".join(self._heading_text).split())))
            self._heading = None

    def handle_data(self, data: str) -> None:
        if self._in_title or self._in_style or self._in_script:
            self._buf.append(data)
            return
        if self._in_svg:
            if self._heading is None:
                # SVG text is not page copy; skip chart labels for copy checks.
                return
        self.text_parts.append(data)
        if self._heading:
            self._heading_text.append(data)
        if self._interactive:
            self._interactive[-1][2].append(data)

    @property
    def text(self) -> str:
        return " ".join("".join(self.text_parts).split())


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def strip_base64(html: str) -> str:
    return re.sub(r"data:[a-z/+.-]+;base64,[A-Za-z0-9+/=]+", "data:<embedded>", html)


def has_name(attrs: dict) -> bool:
    if any(attrs.get(a) for a in A11Y_NAME_ATTRS):
        return True
    if attrs.get("id"):
        return True
    if attrs.get("_text"):
        return True
    if attrs.get("_has_img"):
        return True
    return False


def css_text(doc: Doc, raw: str) -> str:
    inline = " ".join(re.findall(r'style=["\']([^"\']+)["\']', raw, flags=re.I))
    return "\n".join(doc.styles) + "\n" + inline


def near(text: str, needle: str, span: int = 90) -> str:
    i = text.lower().find(needle.lower())
    if i < 0:
        return ""
    return text[max(0, i - span): i + len(needle) + span].replace("\n", " ")


def visible_prose(raw: str) -> str:
    """Text a reader sees, excluding checklists that intentionally quote slop."""
    cleaned = re.sub(r'<label[^>]*class=["\'][^"\']*slop-item[^"\']*["\'][^>]*>.*?</label>', " ", raw, flags=re.I | re.S)
    cleaned = re.sub(r"<(script|style)\b[^>]*>.*?</\1>", " ", cleaned, flags=re.I | re.S)
    cleaned = re.sub(r"<[^>]+>", " ", cleaned)
    return re.sub(r"\s+", " ", cleaned)


def count_color(html: str, color: str) -> int:
    return len(re.findall(re.escape(color), html, flags=re.I))


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------

def check_tier1(a: Audit, doc: Doc, raw: str, css: str) -> None:
    # 1. Self-contained
    remote = re.findall(
        r'<(?:script|link|img|iframe|source|video|audio)[^>]+(?:src|href)=["\'](https?:)?//[^"\']+',
        raw, flags=re.I,
    )
    if remote:
        a.add(1, "T1-remote", f"{len(remote)} remote asset reference(s). Artifact is not self-contained.",
              "; ".join(remote[:3]), "fail")

    # 2. Document basics
    if not doc.title:
        a.add(1, "T1-title", "Missing <title>.", severity="fail")
    if not doc.lang:
        a.add(1, "T1-lang", "Missing lang attribute on <html>.", severity="fail")
    if not re.search(r'name=["\']viewport["\']', raw, flags=re.I):
        a.add(1, "T1-viewport", "Missing viewport meta.", severity="fail")

    # 3. Skip link + main landmark
    if not re.search(r'class=["\'][^"\']*skip-link', raw):
        a.add(1, "T1-skip", "No skip link found.", severity="fail")
    if not re.search(r"<main\b", raw, flags=re.I):
        a.add(1, "T1-main", "No <main> landmark.", severity="fail")

    # 4. One h1
    h1s = [h for h in doc.headings if h[0] == "h1"]
    if len(h1s) != 1:
        a.add(1, "T1-h1", f"Expected exactly one h1; found {len(h1s)}.", severity="fail")

    # 5. Images have alt
    missing_alt = [im.get("src", "")[:80] for im in doc.images if "alt" not in im]
    if missing_alt:
        a.add(1, "T1-alt", f"{len(missing_alt)} image(s) without alt.", "; ".join(missing_alt[:3]), "fail")

    # 6. Interactive elements have accessible names
    unnamed = []
    for attrs in doc.links + doc.buttons:
        if not has_name(attrs) and not attrs.get("href", "").startswith("#"):
            unnamed.append(attrs.get("href", "button"))
    if unnamed:
        a.add(1, "T1-name", f"{len(unnamed)} link/button(s) without an accessible name.",
              "; ".join(unnamed[:3]), "fail")

    # 7. Inputs have labels
    label_for = {x for x in doc.labels if x}
    unlabelled = []
    for inp in doc.inputs:
        if inp.get("type") in ("hidden", "submit", "button"):
            continue
        if inp.get("aria-label") or inp.get("aria-labelledby") or inp.get("_in_label"):
            continue
        if inp.get("id") and inp["id"] in label_for:
            continue
        unlabelled.append(inp.get("name") or inp.get("id") or inp.get("type", "input"))
    if unlabelled:
        a.add(1, "T1-label", f"{len(unlabelled)} form control(s) without a label.",
              "; ".join(unlabelled[:3]), "fail")

    # 8. Reduced motion
    if "prefers-reduced-motion" not in css and "prefers-reduced-motion" not in raw:
        a.add(1, "T1-motion", "No prefers-reduced-motion handling.", severity="fail")

    # 9. Hidden-at-rest content
    if re.search(r"\.reveal\b[^{]*\{[^}]*opacity\s*:\s*0", css) and "is-in" not in raw:
        a.add(1, "T1-hidden", "Content may be invisible at rest (.reveal with opacity:0 and no is-in state).", severity="fail")

    # 10. Charts have an accessible title
    for m in re.finditer(r"<svg\b[^>]*class=[\"'][^\"']*chart[^\"']*[\"'][^>]*>(.*?)</svg>", raw, flags=re.I | re.S):
        inner = m.group(1)
        if not re.search(r"<title\b", inner) and "aria-label" not in m.group(0):
            a.add(1, "T1-chart", "Chart SVG has no <title> or aria-label.", severity="fail")
            break

    # 11. Placeholder / fabricated proof
    text = doc.text
    ph = PLACEHOLDER_RE.search(text)
    if ph:
        a.add(1, "T1-placeholder", f"Placeholder or unsubstantiated proof text found: “{ph.group(0)}”.",
              near(text, ph.group(0)), "review")

    # 12. Numbers without a source nearby
    numbers = re.findall(r"\b\d[\d.,]*\s?(?:%|percent|million|billion|x)\b", text, flags=re.I)
    if len(numbers) >= 3 and "source" not in text.lower() and "figure" not in text.lower():
        a.add(1, "T1-claims", f"{len(numbers)} numeric claims and no visible source/figure note.",
              ", ".join(numbers[:5]), "review")


def check_tier2(a: Audit, doc: Doc, raw: str, css: str) -> None:
    # Typography
    if not re.search(r"@font-face", css):
        a.add(2, "T2-fontfile", "No @font-face block; declared brand type may not ship.")
    families = re.findall(r"font-family\s*:\s*([^;}{]+)", css, flags=re.I)
    if families and not any("ubuntu" in f.lower() for f in families):
        a.add(2, "T2-font", "Ubuntu is not the first family in any font-family declaration.")
    if re.search(r"font-family\s*:\s*(?:inter|geist)\b", css, flags=re.I):
        a.add(2, "T2-defaultfont", "Inter/Geist defaultism.")
    if re.search(r"background-clip\s*:\s*text", css, flags=re.I):
        a.add(2, "T2-gradtext", "Gradient/clipped text.")

    # Colour
    for c in SLOP_COLORS:
        if count_color(raw, c):
            a.add(2, "T2-slopcolor", f"Reflex palette colour {c} present.")
            break
    if re.search(r"(?:linear|radial)-gradient\([^)]*(?:purple|indigo|violet)", css, flags=re.I):
        a.add(2, "T2-grad", "Purple/indigo gradient.")
    if re.search(r"radial-gradient\([^)]*(?:#|rgb)", css, flags=re.I) and "glow" in css.lower():
        a.add(2, "T2-glow", "Radial glow treatment.")
    if re.search(r"backdrop-filter\s*:\s*blur", css, flags=re.I):
        a.add(2, "T2-glass", "backdrop-filter blur (glass) present.")

    # Shape/layout
    if re.search(r"filter\s*:\s*grayscale", css, flags=re.I):
        a.add(2, "T2-logowall", "Grayscale filter suggests a logo wall.")
    if re.search(r"text-transform\s*:\s*uppercase", css):
        a.add(2, "T2-caps", "Uppercase labels present; count of unrelated labels matters.")

    # Three equal cards: grid--3 with exactly three direct card children in source
    for grid in re.finditer(r"<div[^>]+class=[\"'][^\"']*\bgrid--3\b[^\"']*[\"'][^>]*>(.*?)</div>\s*</div>", raw, flags=re.I | re.S):
        body = grid.group(1)
        if body.count('class="card') == 3:
            a.add(2, "T2-threecards", "Three equal cards in a single feature row.")
            break

    # Hero eyebrow chip
    if re.search(r"<h1\b", raw, flags=re.I):
        pre = raw[: raw.lower().find("<h1")]
        if re.search(r'class=["\'][^"\']*(?:badge|chip|pill)[^"\']*["\'][^>]*>[^<]{1,40}</', pre[-1200:], flags=re.I):
            a.add(2, "T2-eyebrow", "Pill/chip immediately before the H1.")
    if re.search(r"border-radius\s*:\s*(?:999px|9999px|50%)", css) and not re.search(r"--radius\s*:\s*2px|border-radius\s*:\s*2px", css):
        a.add(2, "T2-pillonly", "Only pill/round radii; no near-square surface radius.")

    # Counters
    if re.search(r"data-count(?:er)?|requestAnimationFrame\([^)]*count", raw, flags=re.I):
        a.add(2, "T2-counter", "Animated counter detected.")

    # Uniform radius? (heuristic: only one radius value across cards)
    radii = set(re.findall(r"border-radius\s*:\s*([0-9.]+(?:px|rem)|var\(--[a-z-]+\))", css))
    if len(radii) == 1 and "var(--pill)" not in radii:
        a.add(2, "T2-radius", f"Single radius value everywhere ({next(iter(radii))}).")

    # Card border + broad shadow
    if re.search(r"\.card\b[^{]*\{[^}]*border\s*:[^;}]+[^}]*box-shadow\s*:\s*0\s+[1-9]\d", css, flags=re.S):
        a.add(2, "T2-cardshadow", "Card has hairline border and a wide shadow.")

    # Decorative side/top accent stripe
    if re.search(r"\.card[^{]*\{[^}]*border-(?:top|left|right)\s*:\s*[34]px solid", css, flags=re.S):
        a.add(2, "T2-stripe", "Decorative 3–4px stripe on a card; use only where status is real.")


def check_tier3(a: Audit, doc: Doc, raw: str, css: str) -> None:
    if len(re.findall(r"\b(?:opacity\s*:\s*0|translateY\()", css)) >= 3 and "IntersectionObserver" in raw:
        a.add(3, "T3-fade", "Repeated fade/translate reveal.")
    if re.search(r":hover[^{]*\{[^}]*transform\s*:\s*scale", css, flags=re.S):
        a.add(3, "T3-hoverscale", "Hover scale on cards or non-actionable surfaces.")
    if re.search(r"<marquee\b|@keyframes\s+marquee", raw, flags=re.I) or "marquee" in css.lower():
        a.add(3, "T3-marquee", "Marquee present; needs pause controls.")
    if re.search(r"cursor\s*:\s*none|\.cursor-", css, flags=re.I):
        a.add(3, "T3-cursor", "Custom cursor.")
    if "parallax" in css.lower():
        a.add(3, "T3-parallax", "Parallax.")
    if re.search(r"max-width\s*:\s*(?:8[1-9]|9\d)ch", css):
        a.add(3, "T3-measure", "Body measure may exceed 80ch.")


def check_tier4(a: Audit, doc: Doc, raw: str, css: str) -> None:
    text = visible_prose(raw)
    low = text.lower()
    hits = []
    for word in BANNED_COPY:
        if word in low:
            hits.append(word)
    if len(hits) >= 2:
        a.add(4, "T4-buzz", f"{len(hits)} buzzword(s): {', '.join(sorted(set(hits))[:8])}.",
              "Density is the fingerprint; one may be a literal use.")
    if re.search(r"not just (?:a |an |the )?\w+[,.]? it(?:'|’)s", low) or re.search(r"not a \w+\. a \w+\.", low):
        a.add(4, "T4-neg", "Negative parallelism (“not just X, it's Y”).")
    em = text.count("—")
    if em >= 3:
        a.add(4, "T4-emdash", f"{em} em dashes in visible copy; use full stops or en dashes.")
    if "in today’s fast-paced" in low or "in today's fast-paced" in low:
        a.add(4, "T4-today", "“In today's fast-paced world” throat-clearing.")
    # Headline swap test is manual. Flag slogan-shaped triads in h1/h2 only.
    for tag, h in doc.headings:
        if tag in ("h1", "h2") and re.search(r"\b\w+\.\s+\w+\.\s+\w+\.\s*$", h):
            a.add(4, "T4-triad", f"Slogan triad in <{tag}>: “{h}”.")


def check_brand(a: Audit, doc: Doc, raw: str, css: str) -> None:
    # Fonts and logo
    if "Ubuntu" not in css:
        a.add(0, "B-font", "Ubuntu not referenced in CSS.")
    if not re.search(r'sogeti-(?:logo|wordmark)', raw) and not re.search(r'alt="[^"]*Sogeti', raw, flags=re.I):
        a.add(0, "B-logo", "No Sogeti logo asset reference found.")
    if not re.search(r'<clipPath id="sogeti-shape-primary"', raw):
        a.add(0, "B-shape", "Brand shape clipPath missing.")
    # Colour drift
    colors = {c.lower() for c in re.findall(r"#[0-9a-fA-F]{6}\b", css)}
    unknown = sorted(c for c in colors if c not in BRAND_HEX and c not in DERIVED_HEX)
    if unknown:
        a.add(0, "B-hex", f"{len(unknown)} non-system hex value(s) in CSS: {', '.join(unknown[:8])}.")
    # Writing the name
    if re.search(r"\bSOGETI\b|\bSogetiLabs\b", doc.text):
        if re.search(r"\bSOGETI\b", doc.text):
            a.add(0, "B-name", "Sogeti is set in all caps in copy; use title case.")
    # Currency/date smoke test
    if re.search(r"\b\d{1,2}/\d{1,2}/\d{2,4}\b", doc.text):
        a.add(0, "B-date", "Slash date found; Sogeti style is Month D, YYYY.")


def audit_file(path: Path) -> Audit:
    raw = path.read_text(encoding="utf-8", errors="replace")
    a = Audit(path=path)
    doc = Doc()
    doc.feed(strip_base64(raw))
    css = css_text(doc, raw)
    check_tier1(a, doc, raw, css)
    check_tier2(a, doc, raw, css)
    check_tier3(a, doc, raw, css)
    check_tier4(a, doc, raw, css)
    check_brand(a, doc, raw, css)
    a.stats = {
        "bytes": len(raw),
        "headings": len(doc.headings),
        "images": len(doc.images),
        "links": len(doc.links),
        "words": len(doc.text.split()),
    }
    return a


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------

def verdict(a: Audit) -> tuple[str, str]:
    t1 = [f for f in a.findings if f.tier == 1 and f.severity == "fail"]
    t1_review = [f for f in a.findings if f.tier == 1 and f.severity != "fail"]
    t2 = [f for f in a.findings if f.tier == 2]
    if t1:
        return "FAIL", f"{len(t1)} Tier 1 blocker(s)"
    if len(t2) >= 3:
        return "FAIL", f"{len(t2)} identity tells (3+ = rewrite)"
    if t2 or t1_review:
        return "REVIEW", f"{len(t2)} identity tell(s), {len(t1_review)} claim(s) to verify"
    return "PASS", "no blocking findings"


def print_report(a: Audit) -> None:
    status, why = verdict(a)
    print(f"\nSogeti audit · {a.path.name}")
    print("=" * 64)
    print(f"Verdict: {status} — {why}")
    print(f"Words: {a.stats.get('words', 0)} · images: {a.stats.get('images', 0)} · "
          f"links: {a.stats.get('links', 0)} · size: {a.stats.get('bytes', 0)/1024:.0f} KB")

    names = {
        1: "Tier 1 · blockers",
        2: "Tier 2 · identity tells",
        3: "Tier 3 · craft",
        4: "Tier 4 · copy",
        0: "Brand system",
    }
    for tier in (1, 2, 3, 4, 0):
        items = a.by_tier(tier)
        if not items:
            continue
        print(f"\n{names[tier]} ({len(items)})")
        for f in items:
            flag = "✕" if f.severity == "fail" else "!"
            print(f"  {flag} [{f.code}] {f.message}")
            if f.detail:
                print(f"      {f.detail[:240]}")
    if status == "PASS":
        print("\nNo blocking findings. Still do the 360px and keyboard pass")
        print("and verify every number, quote and client name before external use.")
    print()


def main() -> int:
    ap = argparse.ArgumentParser(description="Audit a Sogeti HTML artifact.")
    ap.add_argument("files", nargs="+", type=Path)
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--quiet", action="store_true", help="only print the verdict line")
    args = ap.parse_args()

    audits = []
    for path in args.files:
        if not path.is_file():
            print(f"not a file: {path}", file=sys.stderr)
            return 2
        audits.append(audit_file(path))

    if args.json:
        payload = []
        for a in audits:
            status, why = verdict(a)
            payload.append({
                "file": str(a.path),
                "verdict": status,
                "reason": why,
                "stats": a.stats,
                "findings": [f.__dict__ for f in a.findings],
            })
        print(json.dumps(payload, indent=2))
    else:
        for a in audits:
            if args.quiet:
                status, why = verdict(a)
                print(f"{a.path.name}: {status} — {why}")
            else:
                print_report(a)

    return 1 if any(verdict(a)[0] == "FAIL" for a in audits) else 0


if __name__ == "__main__":
    raise SystemExit(main())
