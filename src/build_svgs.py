#!/usr/bin/env python3
"""Build the animated SVGs for the org profile README -> ../profile/assets/*.svg.

Fonts are embedded as base64 woff2 because GitHub serves README images through
a proxy that blocks external font loads.
"""
import base64
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE.parent / "profile" / "assets"

PURPLE = "#7F75E8"
INK = "#F8F8F6"
BG = "#0A0A0A"
MUTED = "#9A9A9A"


def font(name, family, weight):
    data = base64.b64encode((HERE / "fonts" / f"{name}.woff2").read_bytes()).decode()
    return (f"@font-face{{font-family:'{family}';font-weight:{weight};"
            f"src:url(data:font/woff2;base64,{data}) format('woff2')}}")


FONTS = "".join([
    font("sg700", "SG", 700),
    font("sg500", "SG", 500),
    font("jb500", "JB", 500),
])


def grid(w, h, step=80):
    lines = [f'<path d="M{x} 0V{h}" />' for x in range(step, w, step)]
    lines += [f'<path d="M0 {y}H{w}" />' for y in range(step, h, step)]
    return f'<g stroke="#FFFFFF" stroke-opacity=".045">{"".join(lines)}</g>'


def hero():
    w, h = 1280, 400
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<defs>
<style>{FONTS}
.eye{{font:500 14px 'JB',monospace;letter-spacing:3px;fill:{MUTED}}}
.h1{{font:700 56px 'SG',sans-serif;letter-spacing:-1.5px;fill:{INK}}}
.logo{{font:700 30px 'SG',sans-serif;fill:{INK}}}
.sub{{font:500 11px 'JB',monospace;letter-spacing:5px;fill:#8A8A8A}}
.mark{{font:700 250px 'SG',sans-serif;fill:{INK}}}
.in{{opacity:0;animation:up .9s cubic-bezier(.2,.7,.2,1) forwards}}
.d1{{animation-delay:.15s}}.d2{{animation-delay:.45s}}.d3{{animation-delay:.75s}}.d4{{animation-delay:1.1s}}
@keyframes up{{from{{opacity:0;transform:translateY(18px)}}to{{opacity:1;transform:none}}}}
.glow{{animation:glow 6s ease-in-out infinite;transform-origin:1100px 120px}}
@keyframes glow{{0%,100%{{opacity:.55;transform:scale(1)}}50%{{opacity:1;transform:scale(1.15)}}}}
.float{{animation:float 5s ease-in-out infinite}}
@keyframes float{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-12px)}}}}
.dot{{animation:dot 2.4s ease-in-out infinite;transform-box:fill-box;transform-origin:center}}
@keyframes dot{{0%,100%{{transform:scale(1)}}50%{{transform:scale(1.35)}}}}
.blink{{animation:blink 1s steps(1) infinite}}
@keyframes blink{{50%{{opacity:0}}}}
.scan{{animation:scan 7s linear infinite}}
@keyframes scan{{from{{transform:translateX(-300px)}}to{{transform:translateX(1500px)}}}}
</style>
<radialGradient id="g"><stop offset="0" stop-color="{PURPLE}" stop-opacity=".35"/><stop offset="1" stop-color="{PURPLE}" stop-opacity="0"/></radialGradient>
<linearGradient id="s" x1="0" x2="1"><stop offset="0" stop-color="{PURPLE}" stop-opacity="0"/><stop offset=".5" stop-color="{PURPLE}" stop-opacity=".8"/><stop offset="1" stop-color="{PURPLE}" stop-opacity="0"/></linearGradient>
<clipPath id="c"><rect width="{w}" height="{h}" rx="16"/></clipPath>
</defs>
<g clip-path="url(#c)">
<rect width="{w}" height="{h}" fill="{BG}"/>
{grid(w, h)}
<circle class="glow" cx="1100" cy="120" r="340" fill="url(#g)"/>
<rect class="scan" y="{h - 2}" width="300" height="2" fill="url(#s)"/>
<g class="in d1"><text class="logo" x="80" y="78">predev<tspan fill="{PURPLE}">.</tspan></text>
<text class="sub" x="81" y="98">SOLUTIONS</text></g>
<g class="in d2"><circle cx="84" cy="176" r="4" fill="{PURPLE}"/>
<text class="eye" x="100" y="181">// CAIRO · EGYPT · THE GULF<tspan class="blink" fill="{PURPLE}"> _</tspan></text></g>
<text class="h1 in d3" x="78" y="258">Mobile apps, web platforms,</text>
<text class="h1 in d4" x="78" y="320">and the brands around them<tspan fill="{PURPLE}">.</tspan></text>
<g class="float"><text class="mark" x="940" y="292">p</text>
<circle class="dot" cx="1128" cy="262" r="24" fill="{PURPLE}"/></g>
</g>
</svg>'''


def ticker():
    items = ["Rakeez", "Quick App", "iSpeaker", "Arabook", "Sofqaat",
             "Boutros Afandy", "NileMed", "BioTechnology Egypt"]
    x, parts = 0, []
    # two copies so the loop is seamless
    for _ in range(2):
        for it in items:
            parts.append(f'<text x="{x}" y="41" class="t">{it}</text>')
            x += len(it) * 13.2 + 36
            parts.append(f'<circle cx="{x - 18}" cy="34" r="4" fill="{PURPLE}"/>')
    half = x / 2
    w, h = 1280, 64
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<defs><style>{FONTS}
.t{{font:700 22px 'SG',sans-serif;fill:{INK};letter-spacing:-.3px}}
.lbl{{font:500 11px 'JB',monospace;letter-spacing:3px;fill:{BG}}}
.run{{animation:run {half / 60:.1f}s linear infinite}}
@keyframes run{{to{{transform:translateX(-{half:.1f}px)}}}}
</style>
<linearGradient id="f" x1="0" x2="1"><stop offset="0" stop-color="{BG}"/><stop offset=".22" stop-color="{BG}" stop-opacity="0"/><stop offset=".9" stop-color="{BG}" stop-opacity="0"/><stop offset="1" stop-color="{BG}"/></linearGradient>
<clipPath id="c"><rect width="{w}" height="{h}" rx="14"/></clipPath></defs>
<g clip-path="url(#c)"><rect width="{w}" height="{h}" fill="{BG}"/>
<g transform="translate(262 0)"><g class="run">{"".join(parts)}</g></g>
<rect width="{w}" height="{h}" fill="url(#f)"/>
<rect x="14" y="16" width="214" height="32" rx="16" fill="{PURPLE}"/>
<circle cx="34" cy="32" r="4" fill="{BG}"><animate attributeName="opacity" values="1;.2;1" dur="1.4s" repeatCount="indefinite"/></circle>
<text class="lbl" x="46" y="36">LIVE IN PRODUCTION</text>
<rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="14" fill="none" stroke="#26262D"/></g>
</svg>'''


def stats():
    cards = [("14", "", "FULL-TIME SPECIALISTS"), ("8", "+", "PRODUCTS LIVE"),
             ("10", "", "INDUSTRIES SERVED"), ("2", "wk", "BUILD CYCLES")]
    chips = [("Mobile apps", True), ("Web platforms", True), ("Product strategy", False),
             ("UI/UX", False), ("Payments", False), ("Brand", False), ("Arabic RTL", False)]
    w, h = 580, 640
    out = []
    for i, (n, acc, lbl) in enumerate(cards):
        x, y = 36 + (i % 2) * 260, 128 + (i // 2) * 138
        out.append(f'''<g class="in" style="animation-delay:{.2 + i * .15:.2f}s">
<rect x="{x}" y="{y}" width="246" height="124" rx="16" fill="#111114" stroke="#24242B"/>
<text class="n" x="{x + 22}" y="{y + 66}">{n}<tspan fill="{PURPLE}">{acc}</tspan></text>
<text class="l" x="{x + 22}" y="{y + 100}">{lbl}</text></g>''')
    cx, cy, row = 58, 470, []
    for label, accent in chips:
        cw = len(label) * 7.0 + 26
        if cx + cw > 520:
            cx, cy = 58, cy + 40
        stroke = PURPLE if accent else "#33333D"
        fill = "#B9B3FF" if accent else "#E8E8EA"
        row.append(f'<rect x="{cx}" y="{cy}" width="{cw:.0f}" height="30" rx="15" fill="none" stroke="{stroke}"/>'
                   f'<text class="c" x="{cx + 13}" y="{cy + 20}" fill="{fill}">{label}</text>')
        cx += cw + 8
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
<defs><style>{FONTS}
.n{{font:700 54px 'SG',sans-serif;fill:{INK};letter-spacing:-2px}}
.l,.k{{font:500 11px 'JB',monospace;letter-spacing:2px;fill:{MUTED}}}
.c{{font:500 12px 'SG',sans-serif}}
.t{{font:700 26px 'SG',sans-serif;fill:{INK}}}
.m{{font:700 34px 'SG',sans-serif;fill:{INK}}}
.s{{font:500 10px 'JB',monospace;letter-spacing:4px;fill:#8A8A8A}}
.in{{opacity:0;animation:up .8s cubic-bezier(.2,.7,.2,1) forwards}}
@keyframes up{{from{{opacity:0;transform:translateY(14px)}}to{{opacity:1;transform:none}}}}
.glow{{animation:glow 6s ease-in-out infinite;transform-origin:520px 600px}}
@keyframes glow{{0%,100%{{opacity:.5}}50%{{opacity:1}}}}
.border{{stroke-dasharray:60 2300;animation:trace 6s linear infinite}}
@keyframes trace{{to{{stroke-dashoffset:-2360}}}}
</style>
<radialGradient id="g"><stop offset="0" stop-color="{PURPLE}" stop-opacity=".3"/><stop offset="1" stop-color="{PURPLE}" stop-opacity="0"/></radialGradient>
<clipPath id="c"><rect width="{w}" height="{h}" rx="24"/></clipPath></defs>
<g clip-path="url(#c)"><rect width="{w}" height="{h}" fill="{BG}"/>
{grid(w, h, 48)}
<circle class="glow" cx="520" cy="600" r="220" fill="url(#g)"/>
<g class="in"><rect x="36" y="36" width="56" height="56" rx="14" fill="#111" stroke="#2A2A30"/>
<text class="m" x="47" y="74">p<tspan fill="{PURPLE}">.</tspan></text>
<text class="t" x="108" y="62">predev<tspan fill="{PURPLE}">.</tspan></text>
<text class="s" x="109" y="82">SOLUTIONS</text></g>
{"".join(out)}
<g class="in" style="animation-delay:.85s">
<rect x="36" y="404" width="506" height="{cy + 58 - 404}" rx="16" fill="#111114" stroke="#24242B"/>
<text class="k" x="58" y="446">WHAT WE BUILD</text>{"".join(row)}</g>
<g class="in" style="animation-delay:1s"><circle cx="40" cy="600" r="3.5" fill="{PURPLE}"/>
<text class="k" x="52" y="604" style="letter-spacing:3px">CAIRO · EGYPT · THE GULF</text></g>
<rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="24" fill="none" stroke="#23232A"/>
<rect class="border" x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="24" fill="none" stroke="{PURPLE}" stroke-width="2"/>
</g></svg>'''


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for name, fn in [("hero", hero), ("ticker", ticker), ("about", stats)]:
        p = OUT / f"{name}.svg"
        p.write_text(fn())
        print(p.name, p.stat().st_size)
