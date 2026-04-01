#!/usr/bin/env python3
"""Render all skins as individual SVG files for GitHub README display.

Each skin becomes a pill-shaped SVG with baked-in blobs (simulating
backdrop-filter frost), Turrell radial glow, cloud layer, chrome rim,
and center bar. No CSS backdrop-filter — everything composited in SVG.
"""

from pathlib import Path

OUT = Path(__file__).parent.parent / "templates" / "skins" / "renders"
OUT.mkdir(parents=True, exist_ok=True)

TURRELL_SKINS = [
    {
        "name": "plasma-vesicle",
        "blobs": [("139,92,246", 0.42, 60, -20, 180), ("6,182,212", 0.30, 500, -10, 160), ("217,70,239", 0.24, 300, 10, 130)],
        "turrell": [("#ff2df0", 0), ("#c400e8", 0.12), ("#7a00cc", 0.28), ("#3d0066", 0.48), ("#0a0014", 0.72), ("#000", 1)],
        "cloud": ("255,45,240", 0.18, "160,0,255", 0.12),
        "bar": ["#ff2df0", "#d000e0", "#9b00d4", "#6d00c4", "#3d0066"],
    },
    {
        "name": "synth-meridian",
        "blobs": [("0,255,229", 0.30, 80, -20, 180), ("0,160,200", 0.24, 480, -10, 160), ("0,60,110", 0.20, 320, 5, 130)],
        "turrell": [("#00ffe5", 0), ("#00c4b8", 0.10), ("#0088a3", 0.22), ("#004d6d", 0.40), ("#001a2e", 0.62), ("#000", 1)],
        "cloud": ("0,255,229", 0.14, "0,180,200", 0.10),
        "bar": ["#00ffe5", "#00c8c0", "#0098a8", "#006888", "#003850"],
    },
    {
        "name": "reactor-bloom",
        "blobs": [("255,238,0", 0.32, 70, -25, 190), ("255,100,0", 0.26, 490, -10, 170), ("180,20,0", 0.20, 280, 8, 130)],
        "turrell": [("#ffee00", 0), ("#ffb800", 0.10), ("#ff6a00", 0.24), ("#cc2200", 0.42), ("#5c0a00", 0.64), ("#000", 1)],
        "cloud": ("255,238,0", 0.16, "255,120,0", 0.11),
        "bar": ["#ffee00", "#ffc200", "#ff7a00", "#e03000", "#8c0a00"],
    },
    {
        "name": "abyssal-signal",
        "blobs": [("77,255,180", 0.33, 60, -20, 180), ("0,200,140", 0.25, 500, -8, 150), ("0,90,70", 0.19, 310, 8, 120)],
        "turrell": [("#4dffb4", 0), ("#00e89c", 0.11), ("#00b87a", 0.25), ("#007a5c", 0.42), ("#002e22", 0.63), ("#000", 1)],
        "cloud": ("77,255,180", 0.15, "0,200,140", 0.10),
        "bar": ["#4dffb4", "#00d498", "#00a878", "#007c58", "#004030"],
    },
    {
        "name": "synaptic-discharge",
        "blobs": [("0,255,204", 0.35, 70, -20, 170), ("0,180,255", 0.25, 480, -10, 160), ("26,0,102", 0.40, 290, 5, 140)],
        "turrell": [("#00ffcc", 0), ("#0affb3", 0.08), ("#00e5ff", 0.20), ("#006aff", 0.40), ("#1a0066", 0.65), ("#0a001a", 0.85)],
        "cloud": ("0,255,170", 0.12, "0,180,255", 0.06),
        "bar": ["#00ffcc", "#0affb3", "#00e5ff", "#00a2ff", "#006aff"],
    },
    {
        "name": "plasma-liturgy",
        "blobs": [("255,0,229", 0.30, 65, -20, 180), ("123,0,255", 0.28, 495, -10, 155), ("45,0,163", 0.40, 300, 8, 135)],
        "turrell": [("#ff00e5", 0), ("#ff2aff", 0.08), ("#cc00ff", 0.18), ("#7b00ff", 0.35), ("#2d00a3", 0.55), ("#0d0033", 0.75)],
        "cloud": ("255,0,229", 0.10, "123,0,255", 0.08),
        "bar": ["#ff00e5", "#e000ff", "#cc00ff", "#a100ff", "#7b00ff"],
    },
    {
        "name": "xenobiome-signal",
        "blobs": [("170,255,0", 0.30, 75, -18, 175), ("0,255,136", 0.25, 485, -8, 155), ("0,77,64", 0.38, 310, 10, 130)],
        "turrell": [("#ccff00", 0), ("#aaff00", 0.08), ("#66ff33", 0.18), ("#00ff88", 0.35), ("#00cc99", 0.50), ("#004d40", 0.70), ("#001a15", 0.88)],
        "cloud": ("204,255,0", 0.09, "0,255,136", 0.07),
        "bar": ["#ccff00", "#88ff00", "#33ff66", "#00ff88", "#00cc99"],
    },
    {
        "name": "upload-hemorrhage",
        "blobs": [("255,51,0", 0.32, 60, -20, 180), ("255,0,136", 0.28, 490, -10, 160), ("102,0,102", 0.42, 280, 5, 140)],
        "turrell": [("#ff3300", 0), ("#ff5500", 0.08), ("#ff0055", 0.20), ("#ff0088", 0.35), ("#cc00aa", 0.50), ("#660066", 0.68), ("#1a001a", 0.85)],
        "cloud": ("255,51,0", 0.11, "255,0,85", 0.08),
        "bar": ["#ff3300", "#ff1a33", "#ff0055", "#ff0088", "#cc00aa"],
    },
    {
        "name": "synaptic-aurealis",
        "blobs": [("167,107,239", 0.35, 70, -18, 175), ("123,60,207", 0.28, 495, -10, 155), ("80,36,168", 0.22, 300, 8, 130)],
        "turrell": [("#e8d5ff", 0), ("#c9a0f7", 0.08), ("#a76bef", 0.16), ("#7b3ccf", 0.25), ("#5024a8", 0.34), ("#2d1278", 0.44), ("#1a0b52", 0.55), ("#0f0a1f", 0.82), ("#060408", 1)],
        "cloud": ("178,120,255", 0.18, "100,60,200", 0.12),
        "bar": ["#c9a0f7", "#a76bef", "#7b3ccf", "#5024a8", "#2d1278"],
    },
    {
        "name": "pelagic-drift",
        "blobs": [("61,217,203", 0.32, 65, -20, 180), ("18,160,168", 0.25, 490, -10, 160), ("8,94,120", 0.20, 295, 5, 130)],
        "turrell": [("#b8fff4", 0), ("#7af0e0", 0.07), ("#3dd9cb", 0.14), ("#1fbfb8", 0.22), ("#12a0a8", 0.30), ("#0b7e90", 0.38), ("#085e78", 0.47), ("#04374d", 0.65), ("#021e2e", 0.80), ("#00090f", 1)],
        "cloud": ("122,240,224", 0.15, "31,191,184", 0.10),
        "bar": ["#7af0e0", "#3dd9cb", "#12a0a8", "#0b7e90", "#064a63"],
    },
]

EXPERIMENTAL_SKINS = [
    {"name": "split-field", "type": "linear", "gradient": "linear-gradient(90deg,#ff6432,#ff4020,#880044,#2040ff,#3264ff)", "bar": ["#ffcc88", "#ffffff", "#88ccff"]},
    {"name": "double-aperture", "type": "dual", "g1": ("#ff00c8", 0.20), "g2": ("#00c8ff", 0.20), "bar": ["#ff00c8", "#440044", "#000000", "#004444", "#00c8ff"]},
    {"name": "horizon-line", "type": "linear-v", "gradient": "#001428,#002855,#1a4480,#ff8c3c,#ffaa55,#ff8c3c,#883318,#331108,#000", "bar": ["#ffaa55", "#ff8c3c", "#ff6622", "#ff8c3c", "#ffaa55"]},
    {"name": "interference", "type": "dual", "g1": ("#00ff96", 0.25), "g2": ("#ff0096", 0.25), "bar": ["#00ff96", "#88ffcc", "#ffffff", "#ff88cc", "#ff0096"]},
    {"name": "void-slit", "type": "void", "bar": ["#ffffff"]},
    {"name": "chromatic-stack", "type": "stack", "bar": ["#32ffb4", "#50ffc8", "#88ffdd", "#50ffc8", "#32ffb4"]},
    {"name": "scatter", "type": "scatter", "dots": ["#ff00c8", "#00ffc8", "#ffc800", "#c800ff", "#00c8ff", "#ff6432", "#32ff64", "#ff3264", "#6432ff"], "bar": ["#ff00c8", "#00ffc8", "#ffc800", "#c800ff", "#00c8ff"]},
    {"name": "deep-monochrome", "type": "radial", "color": "#0066ff", "bar": ["#0044bb", "#0066ff", "#3388ff", "#0066ff", "#0044bb"]},
    {"name": "bruise", "type": "radial", "color": "#7a4060", "bar": ["#c88840", "#9a6428", "#7a4060", "#5a2864", "#3a5020"]},
    {"name": "overexposed", "type": "bright", "bar": ["#ffdcf0", "#ffffff", "#dcf0ff", "#ffffff", "#ffdcf0"]},
    {"name": "static", "type": "static", "bar": ["#888888", "#aaaaaa", "#ffffff", "#aaaaaa", "#888888"]},
    {"name": "thermal", "type": "thermal", "bar": ["#0000aa", "#660088", "#ff0000", "#ffff00", "#ffffff"]},
    {"name": "oil-slick", "type": "rainbow", "bar": ["#b400ff", "#0064ff", "#00ffb4", "#ffff00", "#ff7800", "#ff0050", "#b400ff"]},
    {"name": "negative", "type": "negative", "bar": ["#1a0033", "#000a1a", "#001a0a", "#000a1a", "#1a0033"]},
    {"name": "pulse", "type": "pulse", "color": "#ff64c8", "bar": ["#ff64c8"]},
]


def turrell_to_svg(skin: dict) -> str:
    """Generate SVG for a Turrell skin."""
    w, h = 680, 28
    name = skin["name"]

    # Build radial gradient stops for turrell layer
    t_stops = "\n".join(
        f'      <stop offset="{int(pct*100)}%" stop-color="{color}" stop-opacity="0.9"/>'
        for color, pct in skin["turrell"]
    )

    # Build bar gradient stops
    bar_stops = "\n".join(
        f'      <stop offset="{int(i/(len(skin["bar"])-1)*100)}%" stop-color="{c}"/>'
        for i, c in enumerate(skin["bar"])
    )

    # Build blob circles (baked, blurred via filter)
    blob_els = ""
    for rgb, opa, x, y, size in skin["blobs"]:
        cx = x + size/2
        cy = h/2 + y/6
        r = size/3
        blob_els += f'  <circle cx="{cx}" cy="{cy}" r="{r}" fill="rgba({rgb},{opa})" filter="url(#blobBlur)"/>\n'

    # Cloud layer
    cr1, co1, cr2, co2 = skin["cloud"]

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <defs>
    <radialGradient id="t" cx="50%" cy="50%" r="55%">
{t_stops}
    </radialGradient>
    <radialGradient id="c" cx="50%" cy="50%" r="70%">
      <stop offset="0%" stop-color="rgb({cr1})" stop-opacity="{co1}"/>
      <stop offset="40%" stop-color="rgb({cr2})" stop-opacity="{co2}"/>
      <stop offset="100%" stop-color="rgb({cr2})" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="bar" x1="0%" x2="100%">
{bar_stops}
    </linearGradient>
    <linearGradient id="rim" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="white" stop-opacity="0.50"/>
      <stop offset="15%" stop-color="white" stop-opacity="0.12"/>
      <stop offset="40%" stop-color="white" stop-opacity="0.02"/>
      <stop offset="60%" stop-color="white" stop-opacity="0.02"/>
      <stop offset="85%" stop-color="white" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="white" stop-opacity="0.40"/>
    </linearGradient>
    <linearGradient id="spec" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="white" stop-opacity="0.18"/>
      <stop offset="50%" stop-color="white" stop-opacity="0.03"/>
      <stop offset="100%" stop-color="white" stop-opacity="0"/>
    </linearGradient>
    <filter id="blobBlur"><feGaussianBlur stdDeviation="18"/></filter>
    <filter id="barGlow"><feGaussianBlur stdDeviation="3" result="g"/><feMerge><feMergeNode in="g"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <clipPath id="pill"><rect x="0" y="0" width="{w}" height="{h}" rx="{h//2}"/></clipPath>
  </defs>
  <g clip-path="url(#pill)">
    <rect width="{w}" height="{h}" fill="#000"/>
{blob_els}    <rect width="{w}" height="{h}" fill="url(#t)"/>
    <rect width="{w}" height="{h}" fill="url(#c)"/>
    <rect width="{w}" height="{h}" fill="url(#spec)"/>
    <rect x="8" y="{h//2-1}" width="{w-16}" height="3" rx="1.5" fill="url(#bar)" opacity="0.55" filter="url(#barGlow)"/>
    <rect x="8" y="{h//2}" width="{w-16}" height="1.5" rx="0.75" fill="url(#bar)" opacity="0.85"/>
  </g>
  <rect width="{w}" height="{h}" rx="{h//2}" fill="none" stroke="url(#rim)" stroke-width="1.5"/>
</svg>'''


def experimental_bar_svg(skin: dict) -> str:
    """Generate simple bar SVG for experimental skins."""
    w, h = 680, 28
    bar = skin["bar"]
    bar_stops = "\n".join(
        f'      <stop offset="{int(i/(max(len(bar)-1,1))*100)}%" stop-color="{c}"/>'
        for i, c in enumerate(bar)
    )

    # Background depends on type
    bg = '#000'
    fill_extra = ""
    if skin.get("type") == "negative":
        bg = "rgba(255,255,255,0.12)"
    elif skin.get("type") == "overexposed" or skin.get("type") == "bright":
        bg = "rgba(255,255,255,0.08)"

    bar_opacity = "0.85"
    glow_opacity = "0.55"
    if skin.get("type") == "void":
        glow_opacity = "0.40"
        bar_opacity = "0.90"
    if skin.get("type") == "negative":
        bar_opacity = "0.95"
        glow_opacity = "0.80"

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">
  <defs>
    <linearGradient id="bar" x1="0%" x2="100%">
{bar_stops}
    </linearGradient>
    <linearGradient id="rim" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="white" stop-opacity="0.50"/>
      <stop offset="15%" stop-color="white" stop-opacity="0.12"/>
      <stop offset="40%" stop-color="white" stop-opacity="0.02"/>
      <stop offset="60%" stop-color="white" stop-opacity="0.02"/>
      <stop offset="85%" stop-color="white" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="white" stop-opacity="0.40"/>
    </linearGradient>
    <linearGradient id="spec" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="white" stop-opacity="0.18"/>
      <stop offset="50%" stop-color="white" stop-opacity="0.03"/>
      <stop offset="100%" stop-color="white" stop-opacity="0"/>
    </linearGradient>
    <filter id="barGlow"><feGaussianBlur stdDeviation="3" result="g"/><feMerge><feMergeNode in="g"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    <clipPath id="pill"><rect x="0" y="0" width="{w}" height="{h}" rx="{h//2}"/></clipPath>
  </defs>
  <g clip-path="url(#pill)">
    <rect width="{w}" height="{h}" fill="{bg}"/>
    <rect width="{w}" height="{h}" fill="url(#spec)"/>
    <rect x="8" y="{h//2-1}" width="{w-16}" height="3" rx="1.5" fill="url(#bar)" opacity="{glow_opacity}" filter="url(#barGlow)"/>
    <rect x="8" y="{h//2}" width="{w-16}" height="1.5" rx="0.75" fill="url(#bar)" opacity="{bar_opacity}"/>
  </g>
  <rect width="{w}" height="{h}" rx="{h//2}" fill="none" stroke="url(#rim)" stroke-width="1.5"/>
</svg>'''


if __name__ == "__main__":
    for skin in TURRELL_SKINS:
        svg = turrell_to_svg(skin)
        path = OUT / f"{skin['name']}.svg"
        path.write_text(svg)
        print(f"  {path.name}")

    for skin in EXPERIMENTAL_SKINS:
        svg = experimental_bar_svg(skin)
        path = OUT / f"{skin['name']}.svg"
        path.write_text(svg)
        print(f"  {path.name}")

    print(f"\n  {len(TURRELL_SKINS) + len(EXPERIMENTAL_SKINS)} SVGs → {OUT}")
