# Theme System — How It Works

Most repos have random colors. A badge is blue, a diagram is gray, the header is whatever the default is. Repo Design Kit fixes that by putting **every color in one file** so your repo has a cohesive visual identity.

## The Problem

Without a theme system, your colors are scattered:

```
README.md         →  badge color hardcoded as ?color=blue
header-dark.svg   →  gradient hex values pasted in
header-light.svg  →  different gradient hex values pasted in
Mermaid diagram   →  style lines with random hex colors
```

Change your mind about the color? You're editing 4+ files and hoping you didn't miss one.

## The Solution: Theme Variables

One JSON file is the reference for everything:

```
themes/lime-cyan.json   ← single source of truth
        │
        │  You read the values and apply them to:
        │
        ├──▶ docs/assets/header-dark.svg    (copy hex values into SVG)
        ├──▶ docs/assets/header-light.svg   (copy hex values into SVG)
        ├──▶ Mermaid diagrams               (copy style block into diagrams)
        └──▶ Badge URLs                     (copy hex into shields.io URLs)
```

No scripts. No build tools. No code execution. You open the JSON, copy the values, paste them where they go. The JSON is a **reference file**, not an input to a generator.

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

Browse `themes/` and open the JSON for the palette you want. Each file has all the hex values you need.

### 2. Copy the SVG template

Copy `docs/assets/header-dark.svg` and `docs/assets/header-light.svg` into your repo at the same path. Then open each SVG in a text editor and replace:

- **The gradient `stop-color` values** — paste from `dark.gradient[]` or `light.gradient[]`
- **The `stroke` value** on the `<rect>` elements
- **The `flood-color` value** in the `<filter>` — paste from `shadow`
- **The `flood-opacity` value** — paste from `shadow_opacity`
- **The project name** in the `<text>` element
- **The tagline** in the second `<text>` element

### 3. Add the header to README.md

```html
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/header-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="docs/assets/header-light.svg">
    <img alt="Your Project" src="docs/assets/header-dark.svg" width="700">
  </picture>
</p>
```

### 4. Apply Mermaid styles

Open your theme JSON and find the `mermaid` section. Copy the values into style lines at the bottom of any Mermaid diagram:

```
    style NodeA fill:#39FF14,stroke:#2BD600,color:#000
    style NodeB fill:#00FF87,stroke:#00D974,color:#000
    style NodeC fill:#00E5FF,stroke:#00B4D8,color:#000
    style NodeD fill:#00B4D8,stroke:#0096C7,color:#000
    style NodeE fill:#0096C7,stroke:#007EA7,color:#fff
    style NodeF fill:#00FF87,stroke:#39FF14,color:#000
```

### 5. Apply badge colors

Use the `badges` hex codes from your theme JSON in shields.io URLs:

```html
<img src="https://img.shields.io/badge/build-passing-39FF14?style=flat-square">
<img src="https://img.shields.io/badge/license-MIT-00E5FF?style=flat-square">
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

## Why No Script?

A previous version included a shell script that read theme JSON and generated SVGs. It was removed because:

- Shell scripts that interpolate JSON values into file output are an injection surface
- Users shouldn't have to audit 200 lines of bash to trust a design tool
- The manual workflow is 5 minutes of copy-paste — a script saves 3 minutes and adds risk
- The theme JSON is a **reference document**, not a build input

If you want automation, use a GitHub Action in a sandboxed CI runner — not a local script.

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

docs/assets/               # Your repo's themed assets
├── header-dark.svg        # Dark mode header (edit with theme values)
├── header-light.svg       # Light mode header (edit with theme values)
```

## FAQ

**Q: Do I need any build tools?**
No. Open JSON, copy hex values, paste into SVG and README. That's it.

**Q: What if I want different Mermaid colors for different diagrams?**
The theme gives you 6 node styles. Assign them to any node name — `NodeA` through `NodeF` are just conventions.

**Q: Can I have more than 6 Mermaid node styles?**
Add more entries to the `mermaid` object in the theme JSON (`node7`, `node8`, ...). 6 covers most diagrams.

**Q: Why JSON and not YAML/TOML?**
JSON is universally readable. Every editor highlights it. No parser needed — it's a reference file you read with your eyes.
