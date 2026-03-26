# Theme System — How It Works

Most repos have random colors. A badge is blue, a diagram is gray, the header is whatever the default is. Repo Skin fixes that by putting **every color in one file** and generating everything from it.

## The Problem

Without a theme system, your colors are scattered:

```
README.md         →  badge color hardcoded as ?color=blue
header-dark.svg   →  gradient hex values pasted in
header-light.svg  →  different gradient hex values pasted in
Mermaid diagram   →  style lines with random hex colors
```

Change your mind about the color? You're editing 4+ files manually and hoping you didn't miss one.

## The Solution: Theme Variables

One JSON file defines everything:

```
themes/lime-cyan.json   ← single source of truth
        │
        ├──▶ docs/assets/header-dark.svg    (generated)
        ├──▶ docs/assets/header-light.svg   (generated)
        ├──▶ docs/assets/mermaid-styles.md  (generated)
        └──▶ docs/assets/badges.md          (generated)
```

Change the JSON → re-run the script → everything updates.

## Theme File Structure

```json
{
  "name": "Lime Cyan",              // Human-readable name
  "id": "lime-cyan",                // URL/file-safe identifier
  "description": "Dev tools, CLI",  // When to use this theme

  "dark": {                         // Dark mode colors
    "gradient": [                   // 5 gradient stops, left to right
      "#39FF14",                    //   stop 0% — leftmost color
      "#00FF87",                    //   stop 25%
      "#00E5FF",                    //   stop 50% — center
      "#00B4D8",                    //   stop 75%
      "#0096C7"                     //   stop 100% — rightmost color
    ],
    "stroke": "#004D40",            // Border color (0.5px around the bar)
    "shadow": "#004D40",            // Inner shadow color (darker than gradient)
    "shadow_opacity": 0.5,          // Shadow intensity (0-1)
    "watermark_fill": "#000000",    // KevQ text color (dark bg = black text)
    "tagline_fill": "#6E6E73"       // Subtitle text color
  },

  "light": {                        // Light mode — same structure, darker colors
    "gradient": ["#2BD600", "#00D974", "#00C4DB", "#009AB8", "#007EA7"],
    "stroke": "#003D33",
    "shadow": "#003D33",
    "shadow_opacity": 0.4,
    "watermark_fill": "#ffffff",     // Light bg = white text
    "tagline_fill": "#86868B"
  },

  "mermaid": {                       // Mermaid diagram node colors
    "node1": {                       // Primary node
      "fill": "#39FF14",            //   background color
      "stroke": "#2BD600",          //   border color (usually the light-mode version)
      "color": "#000"               //   text color (#000 for light fills, #fff for dark)
    },
    "node2": { ... },                // Secondary node
    "node3": { ... },                // Accent node
    "node4": { ... },                // Muted node
    "node5": { ... },                // Deep node
    "node6": { ... }                 // Alt node
  },

  "badges": {                        // shields.io hex codes (no #)
    "primary": "39FF14",             // Build status, main badge
    "secondary": "00E5FF",           // License, version
    "tertiary": "00FF87",            // Language
    "quaternary": "00B4D8",          // Framework / tool
    "quinary": "0096C7"              // Extra badge
  }
}
```

### Why 5 gradient stops?

Apple's Neo Wallpaper gradients use 5-point transitions. This creates smooth color flow without banding. The stops map to:

```
|  0%  |  25%  |  50%  |  75%  | 100% |
|  ←   leftmost              rightmost →  |
```

### Why separate dark and light?

GitHub has dark and light modes. The `<picture>` element with `prefers-color-scheme` auto-switches. Dark mode uses brighter/neon colors. Light mode uses deeper/muted versions of the same palette.

### Why `stroke` and `shadow`?

The gradient bars have:
- A `0.5px` border (`stroke`) in the darkest tone from the palette
- An inner drop shadow (`shadow`) using SVG filters — gives the bar depth

Both should be significantly darker than the gradient itself. Usually the darkest shade from the palette at 50% of its brightness.

## How to Use

### 1. Pick a theme

```bash
ls themes/
# lime-cyan.json  magenta-purple.json  blue-indigo.json  ...
```

### 2. Run the script

```bash
./scripts/apply-theme.sh themes/lime-cyan.json "YOUR PROJECT" "Your tagline here."
```

This generates 4 files in `docs/assets/`.

### 3. Add the header to README.md

The script prints the exact HTML to paste. Copy it.

### 4. Use the Mermaid styles

Open `docs/assets/mermaid-styles.md` — it has a ready-to-paste style block:

```
    style NodeA fill:#39FF14,stroke:#2BD600,color:#000
    style NodeB fill:#00FF87,stroke:#00D974,color:#000
    ...
```

Add these lines at the bottom of any Mermaid diagram in your README.

### 5. Use the badge colors

Open `docs/assets/badges.md` — it has the hex codes for shields.io:

```html
<img src="https://img.shields.io/badge/build-passing-39FF14?style=flat-square">
```

## Creating a Custom Theme

Copy any existing theme file and modify:

```bash
cp themes/lime-cyan.json themes/my-theme.json
```

Edit the hex values. Rules of thumb:

1. **Dark gradient** — bright/neon/saturated colors
2. **Light gradient** — same hues at 60-70% brightness
3. **Stroke/shadow** — darkest shade, 20-30% of the brightest color's brightness
4. **Mermaid fills** — match the gradient stops. Strokes = the light-mode versions
5. **Mermaid text** — `#000` for light fills (value > `#888`), `#fff` for dark fills
6. **Badge hex** — same as gradient stops, without the `#`

Then run:

```bash
./scripts/apply-theme.sh themes/my-theme.json "MY PROJECT" "My tagline."
```

## File Tree

```
themes/
├── lime-cyan.json        # Each file = one complete color system
├── magenta-purple.json
├── blue-indigo.json
├── orange-gold.json
├── cyan-blue.json
├── green-teal.json
└── red-orange.json

scripts/
└── apply-theme.sh        # Reads any theme JSON, generates SVGs + docs

docs/assets/               # Generated output (committed to your repo)
├── header-dark.svg        # Dark mode header
├── header-light.svg       # Light mode header
├── mermaid-styles.md      # Copy-paste Mermaid style block
└── badges.md              # Badge hex codes for shields.io
```

## FAQ

**Q: Do I need Node.js / npm / any build tool?**
No. The script uses bash and python3 (which ships with macOS). Zero dependencies.

**Q: What if I want different Mermaid colors for different diagrams?**
The theme gives you 6 node styles. You can assign them to any node name — `NodeA` through `NodeF` are just conventions. Rename them to match your diagram.

**Q: Can I have more than 6 Mermaid node styles?**
Add more entries to the `mermaid` object in the theme JSON (`node7`, `node8`, ...) and extend the script. But 6 covers most diagrams — primary, secondary, accent, muted, deep, alt.

**Q: Why JSON and not YAML/TOML?**
Python's `json` module is a stdlib one-liner. No pip install needed. YAML and TOML would require external parsers.
