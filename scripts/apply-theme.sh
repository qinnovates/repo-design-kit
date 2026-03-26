#!/bin/bash
#
# apply-theme.sh — Generate SVG headers, Mermaid styles, and badge codes from a theme file.
#
# Usage:
#   ./scripts/apply-theme.sh <theme-file> <project-name> [tagline]
#
# Example:
#   ./scripts/apply-theme.sh themes/lime-cyan.json "KEYMAKER VAULT" "The right key, for the right agent, at the right time."
#
# What it generates:
#   docs/assets/header-dark.svg   — Dark mode SVG header
#   docs/assets/header-light.svg  — Light mode SVG header
#   docs/assets/mermaid-styles.md — Copy-paste Mermaid style block
#   docs/assets/badges.md         — Badge markdown with theme colors
#
# Requirements: bash, python3 (for JSON parsing — ships with macOS)

set -euo pipefail

THEME_FILE="${1:?Usage: apply-theme.sh <theme.json> <PROJECT NAME> [tagline]}"
PROJECT_NAME="${2:?Usage: apply-theme.sh <theme.json> <PROJECT NAME> [tagline]}"
TAGLINE="${3:-}"

if [ ! -f "$THEME_FILE" ]; then
    echo "Error: Theme file not found: $THEME_FILE"
    exit 1
fi

# Parse JSON with python3 (available on macOS, most Linux)
json() {
    python3 -c "import json,sys; d=json.load(open('$THEME_FILE')); print($1)"
}

# Read theme values
THEME_NAME=$(json "d['name']")
echo "Applying theme: $THEME_NAME"
echo "Project: $PROJECT_NAME"

# Dark mode values
D_G0=$(json "d['dark']['gradient'][0]")
D_G1=$(json "d['dark']['gradient'][1]")
D_G2=$(json "d['dark']['gradient'][2]")
D_G3=$(json "d['dark']['gradient'][3]")
D_G4=$(json "d['dark']['gradient'][4]")
D_STROKE=$(json "d['dark']['stroke']")
D_SHADOW=$(json "d['dark']['shadow']")
D_SHADOW_OP=$(json "d['dark']['shadow_opacity']")
D_WM=$(json "d['dark']['watermark_fill']")
D_TAG=$(json "d['dark']['tagline_fill']")

# Light mode values
L_G0=$(json "d['light']['gradient'][0]")
L_G1=$(json "d['light']['gradient'][1]")
L_G2=$(json "d['light']['gradient'][2]")
L_G3=$(json "d['light']['gradient'][3]")
L_G4=$(json "d['light']['gradient'][4]")
L_STROKE=$(json "d['light']['stroke']")
L_SHADOW=$(json "d['light']['shadow']")
L_SHADOW_OP=$(json "d['light']['shadow_opacity']")
L_WM=$(json "d['light']['watermark_fill']")
L_TAG=$(json "d['light']['tagline_fill']")

# Mermaid values
M1_FILL=$(json "d['mermaid']['node1']['fill']")
M1_STROKE=$(json "d['mermaid']['node1']['stroke']")
M1_COLOR=$(json "d['mermaid']['node1']['color']")
M2_FILL=$(json "d['mermaid']['node2']['fill']")
M2_STROKE=$(json "d['mermaid']['node2']['stroke']")
M2_COLOR=$(json "d['mermaid']['node2']['color']")
M3_FILL=$(json "d['mermaid']['node3']['fill']")
M3_STROKE=$(json "d['mermaid']['node3']['stroke']")
M3_COLOR=$(json "d['mermaid']['node3']['color']")
M4_FILL=$(json "d['mermaid']['node4']['fill']")
M4_STROKE=$(json "d['mermaid']['node4']['stroke']")
M4_COLOR=$(json "d['mermaid']['node4']['color']")
M5_FILL=$(json "d['mermaid']['node5']['fill']")
M5_STROKE=$(json "d['mermaid']['node5']['stroke']")
M5_COLOR=$(json "d['mermaid']['node5']['color']")
M6_FILL=$(json "d['mermaid']['node6']['fill']")
M6_STROKE=$(json "d['mermaid']['node6']['stroke']")
M6_COLOR=$(json "d['mermaid']['node6']['color']")

# Badge values
B_PRIMARY=$(json "d['badges']['primary']")
B_SECONDARY=$(json "d['badges']['secondary']")
B_TERTIARY=$(json "d['badges']['tertiary']")
B_QUATERNARY=$(json "d['badges']['quaternary']")
B_QUINARY=$(json "d['badges']['quinary']")

# Create output directory
mkdir -p docs/assets

# --- Generate dark SVG ---
cat > docs/assets/header-dark.svg << DARKSVG
<svg xmlns="http://www.w3.org/2000/svg" width="700" height="160" viewBox="0 0 700 160">
  <defs>
    <linearGradient id="topbar" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="${D_G0}"/>
      <stop offset="25%" stop-color="${D_G1}"/>
      <stop offset="50%" stop-color="${D_G2}"/>
      <stop offset="75%" stop-color="${D_G3}"/>
      <stop offset="100%" stop-color="${D_G4}"/>
    </linearGradient>
    <linearGradient id="botbar" x1="100%" y1="0%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="${D_G0}"/>
      <stop offset="25%" stop-color="${D_G1}"/>
      <stop offset="50%" stop-color="${D_G2}"/>
      <stop offset="75%" stop-color="${D_G3}"/>
      <stop offset="100%" stop-color="${D_G4}"/>
    </linearGradient>
    <linearGradient id="title" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="${D_G0}"/>
      <stop offset="100%" stop-color="${D_G2}"/>
    </linearGradient>
    <filter id="innershadow">
      <feComponentTransfer in="SourceAlpha">
        <feFuncA type="table" tableValues="1 0"/>
      </feComponentTransfer>
      <feGaussianBlur stdDeviation="2"/>
      <feOffset dx="0" dy="1" result="shadow"/>
      <feFlood flood-color="${D_SHADOW}" flood-opacity="${D_SHADOW_OP}"/>
      <feComposite in2="shadow" operator="in"/>
      <feComposite in2="SourceGraphic" operator="over"/>
    </filter>
  </defs>
  <rect x="8" y="2" width="684" height="8" rx="4" ry="4" fill="url(#topbar)" filter="url(#innershadow)" stroke="${D_STROKE}" stroke-width="0.5"/>
  <text x="680" y="8" font-family="monospace" font-size="3.5" fill="${D_WM}" opacity="0.08" text-anchor="end">KevQ</text>
  <text x="350" y="78" font-family="'SF Pro Display', 'Inter', 'Helvetica Neue', 'Segoe UI', sans-serif" font-size="40" font-weight="300" fill="url(#title)" text-anchor="middle" letter-spacing="12">${PROJECT_NAME}</text>
  <text x="350" y="110" font-family="'SF Pro Text', 'Inter', 'Helvetica Neue', sans-serif" font-size="12" font-weight="300" fill="${D_TAG}" text-anchor="middle" letter-spacing="2">${TAGLINE}</text>
  <rect x="8" y="150" width="684" height="8" rx="4" ry="4" fill="url(#botbar)" filter="url(#innershadow)" stroke="${D_STROKE}" stroke-width="0.5"/>
  <text x="680" y="156" font-family="monospace" font-size="3.5" fill="${D_WM}" opacity="0.08" text-anchor="end">KevQ</text>
</svg>
DARKSVG

echo "  Created: docs/assets/header-dark.svg"

# --- Generate light SVG ---
cat > docs/assets/header-light.svg << LIGHTSVG
<svg xmlns="http://www.w3.org/2000/svg" width="700" height="160" viewBox="0 0 700 160">
  <defs>
    <linearGradient id="topbar" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="${L_G0}"/>
      <stop offset="25%" stop-color="${L_G1}"/>
      <stop offset="50%" stop-color="${L_G2}"/>
      <stop offset="75%" stop-color="${L_G3}"/>
      <stop offset="100%" stop-color="${L_G4}"/>
    </linearGradient>
    <linearGradient id="botbar" x1="100%" y1="0%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="${L_G0}"/>
      <stop offset="25%" stop-color="${L_G1}"/>
      <stop offset="50%" stop-color="${L_G2}"/>
      <stop offset="75%" stop-color="${L_G3}"/>
      <stop offset="100%" stop-color="${L_G4}"/>
    </linearGradient>
    <linearGradient id="title" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="${L_G0}"/>
      <stop offset="100%" stop-color="${L_G2}"/>
    </linearGradient>
    <filter id="innershadow">
      <feComponentTransfer in="SourceAlpha">
        <feFuncA type="table" tableValues="1 0"/>
      </feComponentTransfer>
      <feGaussianBlur stdDeviation="2"/>
      <feOffset dx="0" dy="1" result="shadow"/>
      <feFlood flood-color="${L_SHADOW}" flood-opacity="${L_SHADOW_OP}"/>
      <feComposite in2="shadow" operator="in"/>
      <feComposite in2="SourceGraphic" operator="over"/>
    </filter>
  </defs>
  <rect x="8" y="2" width="684" height="8" rx="4" ry="4" fill="url(#topbar)" filter="url(#innershadow)" stroke="${L_STROKE}" stroke-width="0.5"/>
  <text x="680" y="8" font-family="monospace" font-size="3.5" fill="${L_WM}" opacity="0.08" text-anchor="end">KevQ</text>
  <text x="350" y="78" font-family="'SF Pro Display', 'Inter', 'Helvetica Neue', 'Segoe UI', sans-serif" font-size="40" font-weight="300" fill="url(#title)" text-anchor="middle" letter-spacing="12">${PROJECT_NAME}</text>
  <text x="350" y="110" font-family="'SF Pro Text', 'Inter', 'Helvetica Neue', sans-serif" font-size="12" font-weight="300" fill="${L_TAG}" text-anchor="middle" letter-spacing="2">${TAGLINE}</text>
  <rect x="8" y="150" width="684" height="8" rx="4" ry="4" fill="url(#botbar)" filter="url(#innershadow)" stroke="${L_STROKE}" stroke-width="0.5"/>
  <text x="680" y="156" font-family="monospace" font-size="3.5" fill="${L_WM}" opacity="0.08" text-anchor="end">KevQ</text>
</svg>
LIGHTSVG

echo "  Created: docs/assets/header-light.svg"

# --- Generate Mermaid style block ---
cat > docs/assets/mermaid-styles.md << MERMAID
# Mermaid Styles — ${THEME_NAME}

Paste this block at the bottom of any Mermaid diagram to apply your theme.

\`\`\`
    style NodeA fill:${M1_FILL},stroke:${M1_STROKE},color:${M1_COLOR}
    style NodeB fill:${M2_FILL},stroke:${M2_STROKE},color:${M2_COLOR}
    style NodeC fill:${M3_FILL},stroke:${M3_STROKE},color:${M3_COLOR}
    style NodeD fill:${M4_FILL},stroke:${M4_STROKE},color:${M4_COLOR}
    style NodeE fill:${M5_FILL},stroke:${M5_STROKE},color:${M5_COLOR}
    style NodeF fill:${M6_FILL},stroke:${M6_STROKE},color:${M6_COLOR}
\`\`\`

### Quick reference

| Node | Fill | Stroke | Text |
|------|------|--------|------|
| A (primary) | \`${M1_FILL}\` | \`${M1_STROKE}\` | \`${M1_COLOR}\` |
| B (secondary) | \`${M2_FILL}\` | \`${M2_STROKE}\` | \`${M2_COLOR}\` |
| C (accent) | \`${M3_FILL}\` | \`${M3_STROKE}\` | \`${M3_COLOR}\` |
| D (muted) | \`${M4_FILL}\` | \`${M4_STROKE}\` | \`${M4_COLOR}\` |
| E (deep) | \`${M5_FILL}\` | \`${M5_STROKE}\` | \`${M5_COLOR}\` |
| F (alt) | \`${M6_FILL}\` | \`${M6_STROKE}\` | \`${M6_COLOR}\` |
MERMAID

echo "  Created: docs/assets/mermaid-styles.md"

# --- Generate badge codes ---
cat > docs/assets/badges.md << BADGES
# Badge Colors — ${THEME_NAME}

Use these hex codes in your shields.io badge URLs.

| Role | Hex | Badge URL param |
|------|-----|-----------------|
| Primary | \`#${B_PRIMARY}\` | \`?color=${B_PRIMARY}\` |
| Secondary | \`#${B_SECONDARY}\` | \`?color=${B_SECONDARY}\` |
| Tertiary | \`#${B_TERTIARY}\` | \`?color=${B_TERTIARY}\` |
| Quaternary | \`#${B_QUATERNARY}\` | \`?color=${B_QUATERNARY}\` |
| Quinary | \`#${B_QUINARY}\` | \`?color=${B_QUINARY}\` |

### Example badge row

\`\`\`html
<p align="center">
  <img src="https://img.shields.io/badge/build-passing-${B_PRIMARY}?style=flat-square">
  <img src="https://img.shields.io/badge/license-MIT-${B_SECONDARY}?style=flat-square">
  <img src="https://img.shields.io/badge/language-rust-${B_TERTIARY}?style=flat-square">
  <img src="https://img.shields.io/badge/version-0.1.0-${B_QUATERNARY}?style=flat-square">
</p>
\`\`\`
BADGES

echo "  Created: docs/assets/badges.md"
echo ""
echo "Done! Theme '${THEME_NAME}' applied to ${PROJECT_NAME}."
echo ""
echo "Add this to your README.md:"
echo ""
echo '<p align="center">'
echo '  <picture>'
echo '    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/header-dark.svg">'
echo '    <source media="(prefers-color-scheme: light)" srcset="docs/assets/header-light.svg">'
echo "    <img alt=\"${PROJECT_NAME}\" src=\"docs/assets/header-dark.svg\" width=\"700\">"
echo '  </picture>'
echo '</p>'
