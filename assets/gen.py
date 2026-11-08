"""Generate Linear-style SVG assets for the GitHub profile README (dark + light)."""
import os, sys
from xml.sax.saxutils import escape

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)

FONT = "Inter, -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "'Berkeley Mono', 'SF Mono', ui-monospace, Menlo, Consolas, monospace"

THEMES = {
    "dark": dict(bg="#08090A", panel="#0F1011", panel2="#141516", border="#1F2023", border2="#2A2B2E",
                 text="#F7F8F8", text2="#8A8F98", text3="#62666D", accent="#7170FF", accent2="#5E6AD2",
                 grid="#FFFFFF", gridop="0.035", glowop="0.22", titlefrom="#FFFFFF", titleto="#8A8F98"),
    "light": dict(bg="#FCFCFD", panel="#F7F8F8", panel2="#F1F2F4", border="#E6E7EA", border2="#D9DADE",
                  text="#08090A", text2="#5C6068", text3="#8A8F98", accent="#5E6AD2", accent2="#5E6AD2",
                  grid="#08090A", gridop="0.045", glowop="0.12", titlefrom="#08090A", titleto="#5C6068"),
}

def t(x, y, s, size, fill, weight=400, anchor="start", family=FONT, ls=0, extra=""):
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}" letter-spacing="{ls}" {extra}>{escape(s)}</text>')

def svg(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img" aria-label="{escape(title)}"><title>{escape(title)}</title>{body}</svg>\n')

def frame(c, w, h, r=16, fill=None):
    return (f'<rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="{r}" fill="{fill or c["bg"]}" '
            f'stroke="{c["border"]}"/>')

def write(name, theme, content):
    with open(os.path.join(OUT, f"{name}-{theme}.svg"), "w") as f:
        f.write(content)

# ---------------------------------------------------------------- hero
def hero(c, th):
    W, H = 1200, 460
    b = f'''<defs>
  <radialGradient id="glow" cx="50%" cy="0%" r="70%">
    <stop offset="0" stop-color="{c["accent"]}" stop-opacity="{c["glowop"]}"/>
    <stop offset="1" stop-color="{c["accent"]}" stop-opacity="0"/>
  </radialGradient>
  <linearGradient id="ttl" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0.25" stop-color="{c["titlefrom"]}"/><stop offset="1" stop-color="{c["titleto"]}"/>
  </linearGradient>
  <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
    <path d="M40 0H0V40" fill="none" stroke="{c["grid"]}" stroke-opacity="{c["gridop"]}"/>
  </pattern>
  <linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#fff" stop-opacity="1"/><stop offset="1" stop-color="#fff" stop-opacity="0"/>
  </linearGradient>
  <mask id="m"><rect width="{W}" height="{H}" fill="url(#fade)"/></mask>
  <clipPath id="clip"><rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="20"/></clipPath>
</defs>
<g clip-path="url(#clip)">
  <rect width="{W}" height="{H}" fill="{c["bg"]}"/>
  <rect width="{W}" height="{H}" fill="url(#grid)" mask="url(#m)"/>
  <ellipse cx="{W/2}" cy="0" rx="640" ry="300" fill="url(#glow)"/>
</g>
<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="20" fill="none" stroke="{c["border"]}"/>
'''
    # pill
    pw = 340
    px = (W - pw) / 2
    b += f'<rect x="{px}" y="72" width="{pw}" height="32" rx="16" fill="{c["panel2"]}" stroke="{c["border2"]}"/>'
    b += f'<circle cx="{px+20}" cy="88" r="4" fill="{c["accent"]}"/>'
    b += f'<circle cx="{px+20}" cy="88" r="8" fill="{c["accent"]}" fill-opacity="0.18"/>'
    b += t(px + 36, 93, "Senior Product Designer  ·  India", 14, c["text2"], 500)
    b += t(W/2, 192, "Chayananda Nagesh", 68, "url(#ttl)", 600, "middle", ls=-2.2)
    b += t(W/2, 244, "Designing calm, legible interfaces for complex,", 22, c["text2"], 400, "middle", ls=-0.2)
    b += t(W/2, 274, "AI-driven enterprise products.", 22, c["text2"], 400, "middle", ls=-0.2)
    # meta row
    items = [("Education", "NID · M.Des"), ("Experience", "8 years"),
             ("Focus", "AI products"), ("Portfolio", "chayananda.com")]
    cw, gap = 230, 16
    total = cw * 4 + gap * 3
    x0 = (W - total) / 2
    for i, (k, v) in enumerate(items):
        x = x0 + i * (cw + gap)
        b += f'<rect x="{x}" y="326" width="{cw}" height="76" rx="12" fill="{c["panel"]}" stroke="{c["border"]}"/>'
        b += t(x + 20, 356, k.upper(), 11, c["text3"], 500, ls=1.2)
        b += t(x + 20, 384, v, 17, c["text"], 500, ls=-0.2)
    write("hero", th, svg(W, H, b, "Chayananda Nagesh — Senior Product Designer"))

# ---------------------------------------------------------------- now / focus
def focus(c, th):
    W, H = 1200, 250
    b = frame(c, W, H, 16, c["bg"])
    b += t(32, 46, "FOCUS", 11, c["accent"], 600, ls=1.6)
    b += t(88, 46, "What I care about", 13, c["text3"], 500)
    cols = [
        ("01", "Clarity", ["Making complex products feel", "simple, calm and obvious."]),
        ("02", "Trust in AI", ["Interfaces that help people", "understand and rely on AI."]),
        ("03", "Systems", ["Design systems and patterns", "that scale across teams."]),
    ]
    cw, gap, x0, y0 = 368, 16, 32, 72
    for i, (n, ttl, lines) in enumerate(cols):
        x = x0 + i * (cw + gap)
        b += f'<rect x="{x}" y="{y0}" width="{cw}" height="146" rx="12" fill="{c["panel"]}" stroke="{c["border"]}"/>'
        b += t(x + 22, y0 + 34, n, 12, c["text3"], 500, family=MONO)
        b += t(x + 22, y0 + 68, ttl, 19, c["text"], 600, ls=-0.3)
        for j, ln in enumerate(lines):
            b += t(x + 22, y0 + 96 + j * 21, ln, 14, c["text2"])
    write("focus", th, svg(W, H, b, "Focus: clarity, trust in AI, design systems"))

# ---------------------------------------------------------------- project cards
def glyph(kind, c, x, y):
    s = c["text2"]; a = c["accent"]
    g = ""
    if kind == "chart":  # South Indian chart: 4x4 ring with empty centre
        sz = 11
        for r in range(4):
            for q in range(4):
                if r in (1, 2) and q in (1, 2):
                    continue
                fill = a if (r, q) == (0, 2) else "none"
                op = "0.9" if fill != "none" else "1"
                g += (f'<rect x="{x+q*sz}" y="{y+r*sz}" width="{sz}" height="{sz}" fill="{fill}" '
                      f'fill-opacity="{op}" stroke="{s}" stroke-width="1"/>')
        g += f'<path d="M{x+sz} {y+sz}L{x+3*sz} {y+3*sz}M{x+3*sz} {y+sz}L{x+sz} {y+3*sz}" stroke="{c["border2"]}"/>'
    elif kind == "cite":
        g += t(x - 2, y + 34, "[1]", 26, s, 500, family=MONO)
        g += f'<rect x="{x+40}" y="{y+6}" width="8" height="8" rx="2" fill="{a}"/>'
    elif kind == "bars":
        for i, hgt in enumerate([14, 26, 18, 40, 30]):
            col = a if i == 3 else s
            g += f'<rect x="{x+i*9}" y="{y+44-hgt}" width="6" height="{hgt}" rx="1.5" fill="{col}" fill-opacity="{1 if i==3 else 0.55}"/>'
    elif kind == "pads":
        for r in range(4):
            for q in range(4):
                lit = (r, q) in [(0, 0), (1, 2), (3, 1), (2, 3)]
                g += (f'<rect x="{x+q*11}" y="{y+r*11}" width="8" height="8" rx="2" '
                      f'fill="{a if lit else s}" fill-opacity="{1 if lit else 0.3}"/>')
    return g

def card(c, th, name, kind, tag, title, lines, foot):
    W, H = 590, 280
    b = frame(c, W, H, 16, c["panel"])
    b += f'<rect x="28" y="28" width="68" height="68" rx="14" fill="{c["bg"]}" stroke="{c["border"]}"/>'
    b += glyph(kind, c, 40, 40)
    tw = 18 + len(tag) * 7.2
    b += f'<rect x="{W-28-tw}" y="30" width="{tw}" height="26" rx="13" fill="none" stroke="{c["border2"]}"/>'
    b += t(W - 28 - tw / 2, 47, tag, 12, c["text2"], 500, "middle")
    b += t(28, 140, title, 24, c["text"], 600, ls=-0.5)
    for j, ln in enumerate(lines):
        b += t(28, 176 + j * 23, ln, 15, c["text2"])
    b += f'<line x1="28" y1="{H-58}" x2="{W-28}" y2="{H-58}" stroke="{c["border"]}"/>'
    b += t(28, H - 28, foot, 12, c["text3"], 500, family=MONO)
    b += t(W - 28, H - 28, "→", 16, c["text3"], 500, "end")
    write(name, th, svg(W, H, b, f"{title} — {' '.join(lines)}"))

CARDS = [
    ("card-1", "chart", "Side project", "Horoscene",
     ["A Vedic horoscope tool exploring", "traditional chart visualisation."],
     "JYOTIṢA · DATA VIZ"),
    ("card-2", "cite", "Practice", "Designing for AI",
     ["Research and interaction patterns", "for AI-powered experiences."],
     "UX RESEARCH · AI"),
    ("card-3", "bars", "Dashboard", "Channel analytics",
     ["An interactive dashboard for", "a cultural YouTube channel."],
     "DATA VIZ"),
    ("card-4", "pads", "Experiment", "Shortcut deck",
     ["A MIDI pad controller turned into", "a custom shortcut deck."],
     "HARDWARE · TINKERING"),
]

# ---------------------------------------------------------------- toolkit
def toolkit(c, th):
    W = 1200
    rows = [
        ("Practice", ["UX research", "Interaction design", "UI copy", "Design systems"]),
        ("Design", ["Figma", "Axure RP", "Adobe Suite"]),
        ("3D & motion", ["Cinema 4D", "Blender"]),
        ("Build", ["HTML · CSS · JS", "VS Code", "GitHub"]),
    ]
    H = 48 + len(rows) * 58 + 18
    b = frame(c, W, H, 16, c["bg"])
    b += t(32, 46, "TOOLKIT", 11, c["accent"], 600, ls=1.6)
    for i, (label, chips) in enumerate(rows):
        y = 76 + i * 58
        if i:
            b += f'<line x1="32" y1="{y-14}" x2="{W-32}" y2="{y-14}" stroke="{c["border"]}"/>'
        b += t(32, y + 23, label, 14, c["text3"], 500)
        x = 200
        for ch in chips:
            w = 26 + len(ch) * 7.9
            b += f'<rect x="{x}" y="{y}" width="{w}" height="34" rx="8" fill="{c["panel"]}" stroke="{c["border"]}"/>'
            b += t(x + w / 2, y + 22, ch, 14, c["text"], 500, "middle")
            x += w + 10
    write("toolkit", th, svg(W, H, b, "Toolkit: UX research, interaction design, UI copy, design systems, Figma, Axure RP, Adobe Suite, Cinema 4D, Blender, HTML/CSS/JS, VS Code, GitHub"))

# ---------------------------------------------------------------- off the canvas
def offcanvas(c, th):
    W, H = 1200, 150
    b = frame(c, W, H, 16, c["bg"])
    b += t(32, 46, "OFF THE CANVAS", 11, c["accent"], 600, ls=1.6)
    items = [("ज्योतिष", "Jyotiṣa"), ("संस्कृत", "Sanskrit"), ("ಕನ್ನಡ", "Classical Kannada"),
             ("वेदान्त", "Vedānta"), ("♪", "Carnatic music")]
    cw, gap = 214, 15
    for i, (glyph_, lbl) in enumerate(items):
        x = 32 + i * (cw + gap)
        b += f'<rect x="{x}" y="66" width="{cw}" height="56" rx="10" fill="{c["panel"]}" stroke="{c["border"]}"/>'
        b += t(x + 18, 100, glyph_, 17, c["accent"], 500,
               family="'Noto Sans Devanagari', 'Noto Sans Kannada', 'Nirmala UI', 'Kohinoor Devanagari', " + FONT)
        b += t(x + cw - 18, 100, lbl, 14, c["text"], 500, "end")
    write("offcanvas", th, svg(W, H, b, "Off the canvas: Jyotiṣa, Sanskrit, classical Kannada, Vedānta, Carnatic music"))


# ---------------------------------------------------------------- follow / socials
ICONS = {  # simple, consistent 24px line icons (stroke-based)
    "film": '<rect x="3" y="9" width="18" height="12" rx="2"/><path d="M3 9l2.5-5 15.5 0-2.5 5"/><path d="M8.5 4l-2.5 5M14 4l-2.5 5"/>',
    "book": '<path d="M12 6c-2-1.5-5-2-8-1.5v14c3-.5 6 0 8 1.5 2-1.5 5-2 8-1.5v-14c-3-.5-6 0-8 1.5z"/><path d="M12 6v14"/>',
    "pin": '<path d="M12 21s-6.5-6.2-6.5-11.2a6.5 6.5 0 0 1 13 0C18.5 14.8 12 21 12 21z"/><circle cx="12" cy="9.8" r="2.4"/>',
    "camera": '<path d="M4 8h3.5l1.8-2.5h5.4L16.5 8H20a1 1 0 0 1 1 1v10a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V9a1 1 0 0 1 1-1z"/><circle cx="12" cy="13.5" r="3.6"/>',
    "people": '<circle cx="9" cy="8.5" r="3.2"/><path d="M3 20c.6-3.4 3-5.5 6-5.5s5.4 2.1 6 5.5"/><circle cx="17" cy="9.5" r="2.4"/><path d="M16.5 14.6c2.4.2 4 1.9 4.5 4.6"/>',
    "chat": '<path d="M20.5 11.5a8.5 8.5 0 0 1-12.6 7.4L3.5 20.5l1.6-4.2A8.5 8.5 0 1 1 20.5 11.5z"/><path d="M8.5 11.5h.01M12 11.5h.01M15.5 11.5h.01" stroke-width="2.4"/>',
    "play": '<circle cx="12" cy="12" r="9"/><path d="M10 8.6v6.8l5.6-3.4z"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.6 2.7 3.8 5.7 3.8 9s-1.2 6.3-3.8 9c-2.6-2.7-3.8-5.7-3.8-9S9.4 5.7 12 3z"/>',
}
SOCIALS = [  # file, icon, name, handle, cta, tint
    ("social-letterboxd", "film", "Letterboxd", "Films I watch & rate", "Follow", "#FF8A3D"),
    ("social-goodreads", "book", "Goodreads", "Books on my shelf", "Follow", "#C9A26B"),
    ("social-instagram", "camera", "Instagram", "@chayananda.nagesh", "Follow", "#E1306C"),
    ("social-youtube", "play", "YouTube", "@chayanandanagesh", "Subscribe", "#FF4D4D"),
    ("social-pinterest", "pin", "Pinterest", "Boards & visual references", "Follow", "#E60023"),
    ("social-facebook", "people", "Facebook", "chayananda.nagesh", "Follow", "#4F8CFF"),
    ("social-whatsapp", "chat", "WhatsApp", "Say hello directly", "Message", "#25D366"),
    ("social-portfolio", "globe", "Portfolio", "chayananda.com", "Visit", None),
]

def social(c, th, name, icon, title, sub, cta, tint):
    W, H = 590, 124
    tint = tint or c["accent"]
    b = frame(c, W, H, 16, c["panel"])
    b += f'<rect x="24" y="26" width="72" height="72" rx="16" fill="{tint}" fill-opacity="0.12" stroke="{tint}" stroke-opacity="0.35"/>'
    b += (f'<g transform="translate(42 44) scale(1.5)" fill="none" stroke="{tint}" stroke-width="1.6" '
          f'stroke-linecap="round" stroke-linejoin="round">{ICONS[icon]}</g>')
    b += t(118, 56, title, 21, c["text"], 600, ls=-0.4)
    b += t(118, 84, sub, 14, c["text2"])
    bw = 20 + len(cta) * 9.4 + 34
    bx = W - 24 - bw
    b += f'<rect x="{bx}" y="44" width="{bw}" height="36" rx="18" fill="{c["text"]}"/>'
    b += t(bx + 20, 67, cta, 14, c["bg"], 600)
    b += t(bx + bw - 18, 67, "→", 14, c["bg"], 600, "end")
    write(name, th, svg(W, H, b, f"{cta} on {title}" if title != "Portfolio" else "Visit chayananda.com"))

def follow_header(c, th):
    W, H = 1200, 96
    b = frame(c, W, H, 16, c["bg"])
    b += t(32, 44, "FOLLOW ALONG", 11, c["accent"], 600, ls=1.6)
    b += t(32, 72, "Films, books, visual references and the odd video — come say hi.", 17, c["text2"], 400, ls=-0.2)
    write("follow", th, svg(W, H, b, "Follow along — films, books, visual references and videos"))

for th, c in THEMES.items():
    hero(c, th); focus(c, th); follow_header(c, th)
    for args in SOCIALS:
        social(c, th, *args)
print("ok")
