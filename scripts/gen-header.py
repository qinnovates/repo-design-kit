#!/usr/bin/env python3
"""Generate liquid glass SVG headers for GitHub READMEs.

Apple Liquid Glass aesthetic with internal light bar, inspired by
James Turrell's light installations. Neo-Y2K Futurism palette.

Usage:
    python gen-header.py "VIBECHECK" --subtitle "slop-stopper" --tagline "Stand out" --skin chrome
    python gen-header.py "QUORUM" --skin aurora --out docs/assets/
"""

import argparse
import textwrap
from pathlib import Path


SKINS = {
    "chrome": {
        "desc": "Metallic silver-to-white chrome. Y2K mirror finish.",
        "dark": {
            "glass_fill": "rgba(255,255,255,0.04)",
            "glass_stroke": "rgba(255,255,255,0.12)",
            "glass_blur": 12,
            "light_bar": ["#E0E0E0", "#FFFFFF", "#E0E0E0"],
            "light_glow": "#FFFFFF",
            "light_opacity": 0.6,
            "title_fill": ["#E8E8E8", "#FFFFFF", "#E8E8E8"],
            "subtitle_fill": "#8E8E93",
            "tagline_fill": "#636366",
            "watermark_fill": "#FFFFFF",
            "bg": "#000000",
        },
        "light": {
            "glass_fill": "rgba(0,0,0,0.03)",
            "glass_stroke": "rgba(0,0,0,0.08)",
            "glass_blur": 12,
            "light_bar": ["#B0B0B0", "#D4D4D4", "#B0B0B0"],
            "light_glow": "#C0C0C0",
            "light_opacity": 0.5,
            "title_fill": ["#3A3A3C", "#1D1D1F", "#3A3A3C"],
            "subtitle_fill": "#86868B",
            "tagline_fill": "#AEAEB2",
            "watermark_fill": "#000000",
            "bg": "#FFFFFF",
        },
    },
    "hotpink": {
        "desc": "Fuchsia-to-cyan. Y2K pop with cyber edge.",
        "dark": {
            "glass_fill": "rgba(255,0,110,0.06)",
            "glass_stroke": "rgba(255,0,110,0.15)",
            "glass_blur": 14,
            "light_bar": ["#FF006E", "#FF2D95", "#D946EF"],
            "light_glow": "#FF006E",
            "light_opacity": 0.7,
            "title_fill": ["#FF006E", "#FF2D95", "#D946EF"],
            "subtitle_fill": "#8E8E93",
            "tagline_fill": "#636366",
            "watermark_fill": "#FF006E",
            "bg": "#000000",
        },
        "light": {
            "glass_fill": "rgba(255,0,110,0.04)",
            "glass_stroke": "rgba(255,0,110,0.10)",
            "glass_blur": 14,
            "light_bar": ["#C4004F", "#D4006A", "#A020A0"],
            "light_glow": "#D4006A",
            "light_opacity": 0.5,
            "title_fill": ["#C4004F", "#D4006A", "#A020A0"],
            "subtitle_fill": "#86868B",
            "tagline_fill": "#AEAEB2",
            "watermark_fill": "#D4006A",
            "bg": "#FFFFFF",
        },
    },
    "aurora": {
        "desc": "Cyan-to-green. Northern lights on glass.",
        "dark": {
            "glass_fill": "rgba(6,182,212,0.05)",
            "glass_stroke": "rgba(6,182,212,0.12)",
            "glass_blur": 16,
            "light_bar": ["#06B6D4", "#22D3EE", "#34D399"],
            "light_glow": "#22D3EE",
            "light_opacity": 0.65,
            "title_fill": ["#06B6D4", "#22D3EE", "#34D399"],
            "subtitle_fill": "#8E8E93",
            "tagline_fill": "#636366",
            "watermark_fill": "#06B6D4",
            "bg": "#000000",
        },
        "light": {
            "glass_fill": "rgba(6,182,212,0.04)",
            "glass_stroke": "rgba(6,182,212,0.08)",
            "glass_blur": 16,
            "light_bar": ["#0891B2", "#0E7490", "#059669"],
            "light_glow": "#0E7490",
            "light_opacity": 0.45,
            "title_fill": ["#0891B2", "#0E7490", "#059669"],
            "subtitle_fill": "#86868B",
            "tagline_fill": "#AEAEB2",
            "watermark_fill": "#0E7490",
            "bg": "#FFFFFF",
        },
    },
    "ember": {
        "desc": "Red-to-orange. Warm glass, fire inside.",
        "dark": {
            "glass_fill": "rgba(255,69,58,0.05)",
            "glass_stroke": "rgba(255,69,58,0.12)",
            "glass_blur": 14,
            "light_bar": ["#FF453A", "#FF6B6B", "#FF9F0A"],
            "light_glow": "#FF6B6B",
            "light_opacity": 0.65,
            "title_fill": ["#FF453A", "#FF8A65", "#FFB74D"],
            "subtitle_fill": "#8E8E93",
            "tagline_fill": "#636366",
            "watermark_fill": "#FF453A",
            "bg": "#000000",
        },
        "light": {
            "glass_fill": "rgba(255,69,58,0.03)",
            "glass_stroke": "rgba(255,69,58,0.08)",
            "glass_blur": 14,
            "light_bar": ["#D70015", "#D84315", "#C77800"],
            "light_glow": "#D84315",
            "light_opacity": 0.45,
            "title_fill": ["#D70015", "#E65100", "#EF6C00"],
            "subtitle_fill": "#86868B",
            "tagline_fill": "#AEAEB2",
            "watermark_fill": "#D70015",
            "bg": "#FFFFFF",
        },
    },
    "hologram": {
        "desc": "Purple-to-pink-to-cyan. Iridescent Y2K holographic.",
        "dark": {
            "glass_fill": "rgba(139,92,246,0.05)",
            "glass_stroke": "rgba(139,92,246,0.12)",
            "glass_blur": 18,
            "light_bar": ["#8B5CF6", "#D946EF", "#06B6D4"],
            "light_glow": "#D946EF",
            "light_opacity": 0.6,
            "title_fill": ["#8B5CF6", "#D946EF", "#06B6D4"],
            "subtitle_fill": "#8E8E93",
            "tagline_fill": "#636366",
            "watermark_fill": "#8B5CF6",
            "bg": "#000000",
        },
        "light": {
            "glass_fill": "rgba(139,92,246,0.04)",
            "glass_stroke": "rgba(139,92,246,0.08)",
            "glass_blur": 18,
            "light_bar": ["#6D28D9", "#A020A0", "#0E7490"],
            "light_glow": "#7C3AED",
            "light_opacity": 0.4,
            "title_fill": ["#6D28D9", "#A020A0", "#0E7490"],
            "subtitle_fill": "#86868B",
            "tagline_fill": "#AEAEB2",
            "watermark_fill": "#6D28D9",
            "bg": "#FFFFFF",
        },
    },
    "ice": {
        "desc": "Blue-to-white. Frozen glass, cold light.",
        "dark": {
            "glass_fill": "rgba(96,165,250,0.05)",
            "glass_stroke": "rgba(96,165,250,0.10)",
            "glass_blur": 16,
            "light_bar": ["#3B82F6", "#60A5FA", "#BFDBFE"],
            "light_glow": "#60A5FA",
            "light_opacity": 0.55,
            "title_fill": ["#3B82F6", "#60A5FA", "#BFDBFE"],
            "subtitle_fill": "#8E8E93",
            "tagline_fill": "#636366",
            "watermark_fill": "#3B82F6",
            "bg": "#000000",
        },
        "light": {
            "glass_fill": "rgba(59,130,246,0.03)",
            "glass_stroke": "rgba(59,130,246,0.07)",
            "glass_blur": 16,
            "light_bar": ["#1D4ED8", "#2563EB", "#60A5FA"],
            "light_glow": "#2563EB",
            "light_opacity": 0.4,
            "title_fill": ["#1D4ED8", "#2563EB", "#3B82F6"],
            "subtitle_fill": "#86868B",
            "tagline_fill": "#AEAEB2",
            "watermark_fill": "#1D4ED8",
            "bg": "#FFFFFF",
        },
    },
}


def _gradient_stops(colors: list[str], gradient_id: str) -> str:
    """Generate SVG linearGradient from color list."""
    n = len(colors)
    stops = []
    for i, color in enumerate(colors):
        pct = round(i / max(n - 1, 1) * 100)
        stops.append(f'      <stop offset="{pct}%" stop-color="{color}"/>')
    return textwrap.dedent(f"""\
    <linearGradient id="{gradient_id}" x1="0%" y1="0%" x2="100%" y2="0%">
{chr(10).join(stops)}
    </linearGradient>""")


def generate_header(
    title: str,
    *,
    subtitle: str = "",
    tagline: str = "",
    skin_name: str = "chrome",
    mode: str = "dark",
    width: int = 700,
    height: int = 200,
    watermark: str = "KevQ",
) -> str:
    """Generate a liquid glass SVG header."""
    skin = SKINS[skin_name][mode]

    # Layout calculations
    glass_x = 20
    glass_y = 16
    glass_w = width - 40
    glass_h = height - 32
    glass_rx = 24
    light_bar_y = glass_y + 4
    light_bar_h = 5

    # Text positions — adapt to content
    has_subtitle = bool(subtitle)
    has_tagline = bool(tagline)

    if has_subtitle and has_tagline:
        title_y = glass_y + glass_h * 0.40
        subtitle_y = title_y + 30
        tagline_y = subtitle_y + 24
    elif has_subtitle:
        title_y = glass_y + glass_h * 0.42
        subtitle_y = title_y + 32
        tagline_y = 0
    elif has_tagline:
        title_y = glass_y + glass_h * 0.42
        subtitle_y = 0
        tagline_y = title_y + 28
    else:
        title_y = glass_y + glass_h * 0.55
        subtitle_y = 0
        tagline_y = 0

    mid_x = width / 2

    # Build gradients
    title_gradient = _gradient_stops(skin["title_fill"], "titleGrad")
    light_gradient = _gradient_stops(skin["light_bar"], "lightBar")

    # Title letter spacing scales with length
    title_spacing = max(4, min(14, 180 // max(len(title), 1)))
    title_size = max(28, min(42, 420 // max(len(title), 1)))

    svg = f"""\
<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <defs>
    {title_gradient}
    {light_gradient}

    <!-- Glass frost filter -->
    <filter id="glassFrost" x="-10%" y="-10%" width="120%" height="120%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="{skin['glass_blur']}" result="blur"/>
      <feFlood flood-color="{skin['glass_fill']}" result="fill"/>
      <feComposite in="fill" in2="blur" operator="in" result="frosted"/>
      <feComposite in="frosted" in2="SourceGraphic" operator="over"/>
    </filter>

    <!-- Light bar glow -->
    <filter id="lightGlow" x="-20%" y="-200%" width="140%" height="600%">
      <feGaussianBlur stdDeviation="8" result="glow"/>
      <feMerge>
        <feMergeNode in="glow"/>
        <feMergeNode in="glow"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <!-- Title glow -->
    <filter id="titleGlow" x="-5%" y="-20%" width="110%" height="140%">
      <feGaussianBlur stdDeviation="3" result="glow"/>
      <feMerge>
        <feMergeNode in="glow"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>

    <!-- Inner highlight on glass -->
    <linearGradient id="innerHighlight" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="white" stop-opacity="0.08"/>
      <stop offset="50%" stop-color="white" stop-opacity="0.01"/>
      <stop offset="100%" stop-color="white" stop-opacity="0.04"/>
    </linearGradient>
  </defs>

  <!-- Glass panel -->
  <rect x="{glass_x}" y="{glass_y}" width="{glass_w}" height="{glass_h}"
        rx="{glass_rx}" ry="{glass_rx}"
        fill="{skin['glass_fill']}"
        stroke="{skin['glass_stroke']}" stroke-width="1"/>

  <!-- Inner highlight layer -->
  <rect x="{glass_x}" y="{glass_y}" width="{glass_w}" height="{glass_h}"
        rx="{glass_rx}" ry="{glass_rx}"
        fill="url(#innerHighlight)"/>

  <!-- Light bar (Turrell-inspired) -->
  <rect x="{glass_x + glass_rx}" y="{light_bar_y}" width="{glass_w - glass_rx * 2}" height="{light_bar_h}"
        rx="2.5" ry="2.5"
        fill="url(#lightBar)" opacity="{skin['light_opacity']}"
        filter="url(#lightGlow)"/>

  <!-- Title -->
  <text x="{mid_x}" y="{title_y}"
        font-family="'SF Pro Display', 'Inter', 'Helvetica Neue', 'Segoe UI', sans-serif"
        font-size="{title_size}" font-weight="200"
        fill="url(#titleGrad)" text-anchor="middle"
        letter-spacing="{title_spacing}"
        filter="url(#titleGlow)">{title}</text>"""

    if has_subtitle:
        svg += f"""

  <!-- Subtitle -->
  <text x="{mid_x}" y="{subtitle_y}"
        font-family="'SF Pro Display', 'Inter', 'Helvetica Neue', sans-serif"
        font-size="14" font-weight="300"
        fill="{skin['subtitle_fill']}" text-anchor="middle"
        letter-spacing="5">{subtitle}</text>"""

    if has_tagline:
        svg += f"""

  <!-- Tagline -->
  <text x="{mid_x}" y="{tagline_y}"
        font-family="'SF Pro Text', 'Inter', 'Helvetica Neue', sans-serif"
        font-size="11" font-weight="300"
        fill="{skin['tagline_fill']}" text-anchor="middle"
        letter-spacing="1.5">{tagline}</text>"""

    if watermark:
        svg += f"""

  <!-- Watermark -->
  <text x="{glass_x + glass_w - 12}" y="{glass_y + glass_h - 8}"
        font-family="monospace" font-size="3.5"
        fill="{skin['watermark_fill']}" opacity="0.08"
        text-anchor="end">{watermark}</text>"""

    svg += """
</svg>
"""
    return svg


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate liquid glass SVG headers for GitHub READMEs.",
        epilog="Skins: " + ", ".join(SKINS.keys()),
    )
    parser.add_argument("title", nargs="?", default="", help="Title text (e.g. VIBECHECK)")
    parser.add_argument("--subtitle", "-s", default="", help="Subtitle below title")
    parser.add_argument("--tagline", "-t", default="", help="Tagline below subtitle")
    parser.add_argument("--skin", default="chrome", choices=SKINS.keys(), help="Color skin")
    parser.add_argument("--out", "-o", default="docs/assets", help="Output directory")
    parser.add_argument("--width", type=int, default=700, help="SVG width")
    parser.add_argument("--height", type=int, default=200, help="SVG height")
    parser.add_argument("--watermark", default="KevQ", help="Corner watermark text")
    parser.add_argument("--list-skins", action="store_true", help="List available skins")

    args = parser.parse_args()

    if args.list_skins:
        for name, skin in SKINS.items():
            print(f"  {name:12s} — {skin['desc']}")
            dark_bar = skin["dark"]["light_bar"]
            print(f"               dark:  {' → '.join(dark_bar)}")
            light_bar = skin["light"]["light_bar"]
            print(f"               light: {' → '.join(light_bar)}")
            print()
        return

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    for mode in ("dark", "light"):
        svg = generate_header(
            args.title,
            subtitle=args.subtitle,
            tagline=args.tagline,
            skin_name=args.skin,
            mode=mode,
            width=args.width,
            height=args.height,
            watermark=args.watermark,
        )
        out_path = out_dir / f"header-{mode}.svg"
        out_path.write_text(svg)
        print(f"  {out_path}")

    print(f"\n  Skin: {args.skin} — {SKINS[args.skin]['desc']}")


if __name__ == "__main__":
    main()
