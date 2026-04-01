<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/header-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="docs/assets/header-light.svg">
    <img alt="Repo Design Kit" src="docs/assets/header-dark.svg" width="400">
  </picture>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-64D2FF?style=flat-square" alt="License">
  <img src="https://img.shields.io/badge/GitHub-Markdown-BF5AF2?style=flat-square" alt="GitHub Markdown">
  <img src="https://img.shields.io/badge/dark%20mode-supported-32D74B?style=flat-square" alt="Dark Mode">
  <img src="https://img.shields.io/badge/skins-25-FF9F0A?style=flat-square" alt="Skins">
</p>


<p align="center"><img src="templates/skins/renders/divider.svg" width="100%" alt="divider"></p>


> [!TIP]
> Copy the `docs/assets/` folder and `README.md` template into your repo. Pick a gradient. Push. Done.

## What This Is

A collection of **SVG header skins**, **Mermaid diagram color palettes**, and **README templates** that make GitHub repos look polished — with dark/light mode support, gradient color bars, and every dynamic feature GitHub actually renders.

No build tools. No dependencies. Just SVG files and markdown.


<p align="center"><img src="templates/skins/renders/divider.svg" width="100%" alt="divider"></p>


## Before & After

**Before:** Plain text, no visual identity, blends in with 300 million other repos.

**After:**

```mermaid
graph LR
    A["Your Repo"] --> B["SVG Header\n+ gradient bars"]
    A --> C["Neo-colored\nMermaid diagrams"]
    A --> D["Collapsible\nsections"]
    A --> E["Alert\ncallouts"]
    A --> F["Live\nbadges"]

    style A fill:#FF2D55,stroke:#D70015,color:#fff
    style B fill:#BF5AF2,stroke:#8944AB,color:#fff
    style C fill:#5E5CE6,stroke:#3634A3,color:#fff
    style D fill:#64D2FF,stroke:#0071A4,color:#000
    style E fill:#32D74B,stroke:#248A3D,color:#000
    style F fill:#FF9F0A,stroke:#C77800,color:#000
```


<p align="center"><img src="templates/skins/renders/divider.svg" width="100%" alt="divider"></p>


## Table of Contents

- [Quick Start](#quick-start)
- [Skins](#skins)
- [Dynamic Features](#dynamic-features)
- [Mermaid Color Palettes](#mermaid-color-palettes)
- [Full Template](#full-template)
- [Included Files](#included-files)


<p align="center"><img src="templates/skins/renders/divider.svg" width="100%" alt="divider"></p>


## Quick Start

**1. Copy the template files into your repo:**

```bash
# Clone this repo
git clone https://github.com/qinnovates/repo-skin.git

# Copy what you need
cp -r repo-skin/docs/assets/ your-project/docs/assets/
cp repo-skin/templates/README.template.md your-project/README.md
```

**2. Edit the SVG header** — change the title text in `docs/assets/header-dark.svg` and `header-light.svg`:

```xml
<!-- Find this line and change the text -->
<text ... font-size="36" ...>YOUR PROJECT NAME</text>
```

**3. Pick a gradient** from the [Skins catalog](templates/skins/SKINS.md) and update the `<linearGradient>` stops.

**4. Push.** GitHub renders everything automatically.


<p align="center"><img src="templates/skins/renders/divider.svg" width="100%" alt="divider"></p>


## Skins — 25 Options

Pill-shaped glass chrome banners with Turrell-inspired light art, Y3K colors, and experimental gradient techniques. [Full catalog →](templates/skins/SKINS.md)

### Turrell + Cloud + Y3K (10 skins)

Radial aperture glows with atmospheric cloud layers inside chrome glass pills.

| Skin | Colors | Mood |
|------|--------|------|
| `plasma-vesicle` | Magenta → ultraviolet | Bioluminescent jellyfish in a pressure-black trench |
| `synth-meridian` | Cyan → teal → black | Synthetic cyan decaying through surgical teal |
| `reactor-bloom` | Yellow → orange → crimson | Nuclear yellow through plasma orange |
| `abyssal-signal` | Green → jade → black | Deep-sea sonar in bioluminescent algae |
| `synaptic-discharge` | Cyan → blue → violet | Thought propagating through cerebrospinal fluid |
| `plasma-liturgy` | Magenta → violet → purple | Dark matter collapsing into consciousness |
| `xenobiome-signal` | Lime → green → teal | A chloroplast that learned to think |
| `upload-hemorrhage` | Red → magenta → purple | Consciousness ripping itself in half |
| `synaptic-aurealis` | Lavender → violet → deep purple | Event horizon of an unthought thought |
| `pelagic-drift` | Mint → teal → deep ocean | Deep-sea creature generating its own light |

### Experimental (15 skins)

Structural gradient techniques — not just color swaps.

| Skin | Technique |
|------|-----------|
| `split-field` | Warm left / cold right, bar at the weather front |
| `double-aperture` | Two portals, void between |
| `horizon-line` | Top-to-bottom sunset, bar IS the horizon |
| `interference` | Two overlapping radials creating constructive interference |
| `void-slit` | Near-black, thin white line is the only light |
| `chromatic-stack` | RGB bands stacked vertically |
| `scatter` | Many tiny colored blobs like particle collisions |
| `deep-monochrome` | Single hue (Klein blue), infinite depth |
| `bruise` | Purple-brown-yellow-green — colors of healing skin |
| `overexposed` | Washed out, blown highlights |
| `static` | Speckled white noise behind glass |
| `thermal` | FLIR infrared false color |
| `oil-slick` | Full iridescent rainbow |
| `negative` | Inverted: bright pill, dark bar |
| `pulse` | Single bright point, rest void |

> Preview all skins locally: open `templates/skins/preview/turrell-cloud.html` or `experimental.html` in a browser. Toggle button cycles black / transparent / checker backgrounds.


<p align="center"><img src="templates/skins/renders/divider.svg" width="100%" alt="divider"></p>


## Dynamic Features

Everything GitHub **actually** renders — tested and verified.[^1]

### Alert Callouts

```markdown
> [!NOTE]
> Useful information that users should know.

> [!TIP]
> Helpful advice for doing things better.

> [!IMPORTANT]
> Key information users need to know.

> [!WARNING]
> Urgent info that needs immediate attention.

> [!CAUTION]
> Negative potential consequences of an action.
```

> [!NOTE]
> These render with colored borders and icons on GitHub. Free visual hierarchy.

### Collapsible Sections

```html
<details>
<summary><strong>Click to expand</strong></summary>

Hidden content here. Markdown works inside.

- Bullet points
- Code blocks
- Even nested collapsibles

</details>
```

<details>
<summary><strong>Live example — click me</strong></summary>

This content is hidden by default. Use collapsible sections for:
- Verbose documentation
- Optional details
- FAQ answers
- Long code examples

</details>

### Nested Collapsibles (Accordion)

<details>
<summary><strong>Architecture</strong></summary>

<details>
<summary>Frontend</summary>

React, TypeScript, Tailwind...

</details>

<details>
<summary>Backend</summary>

Rust, Axum, SQLite...

</details>

<details>
<summary>Infrastructure</summary>

Docker, Cloudflare, GitHub Actions...

</details>

</details>

### Keyboard Keys

```markdown
Press <kbd>Ctrl</kbd> + <kbd>C</kbd> to copy.
```

Press <kbd>Ctrl</kbd> + <kbd>C</kbd> to copy.

### Footnotes

```markdown
This uses AES-256-GCM[^1] for encryption.

[^1]: Advanced Encryption Standard with Galois/Counter Mode.
```

Hover over the footnote number to see a preview. Click to jump to the definition.

### Dark/Light Mode Images

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="dark-image.svg">
  <source media="(prefers-color-scheme: light)" srcset="light-image.svg">
  <img alt="Description" src="dark-image.svg" width="700">
</picture>
```

GitHub automatically switches the image based on the user's theme.

### Star History Chart

Every public repo should include a star history graph. It's a live SVG that updates automatically — zero maintenance.

```markdown
[![Star History Chart](https://api.star-history.com/svg?repos=USER/REPO&type=Date)](https://star-history.com/#USER/REPO&Date)
```

Options:
- `&type=Date` — timeline view (default, best for most repos)
- `&type=Timeline` — compact timeline
- `&legend=top-left` — move legend position

Multiple repos in one chart:
```markdown
[![Star History Chart](https://api.star-history.com/svg?repos=USER/REPO1,USER/REPO2&type=Date)](https://star-history.com/#USER/REPO1&USER/REPO2&Date)
```

> [!NOTE]
> The chart is a live SVG from star-history.com — it updates automatically as your repo gains stars. No CI or build step needed.

### Math (LaTeX)

Inline: `$E = mc^2$` → $E = mc^2$

Block:
```
$$
\sum_{i=1}^{n} x_i = x_1 + x_2 + \cdots + x_n
$$
```

$$\sum_{i=1}^{n} x_i = x_1 + x_2 + \cdots + x_n$$


<p align="center"><img src="templates/skins/renders/divider.svg" width="100%" alt="divider"></p>


## Mermaid Color Palettes

GitHub renders Mermaid diagrams natively. Here are copy-paste palettes using the Neo colors.

### Flowchart

```mermaid
graph TD
    A["Input"] --> B{"Decision"}
    B -->|"Yes"| C["Process"]
    B -->|"No"| D["Reject"]
    C --> E["Output"]
    D --> F["Log"]

    style A fill:#64D2FF,stroke:#0071A4,color:#000
    style B fill:#FF9F0A,stroke:#C77800,color:#000
    style C fill:#32D74B,stroke:#248A3D,color:#000
    style D fill:#FF453A,stroke:#D70015,color:#fff
    style E fill:#30D158,stroke:#248A3D,color:#000
    style F fill:#BF5AF2,stroke:#8944AB,color:#fff
```

### Sequence Diagram

```mermaid
sequenceDiagram
    participant U as User
    participant A as Agent
    participant V as Vault
    participant L as Audit Log

    U->>A: "Get my API key"
    A->>V: keymaker_get("api_key")
    V->>V: Check policy
    V->>L: Log access
    V-->>A: Decrypted value
    A-->>U: Used in context
```

### Gantt Chart

```mermaid
gantt
    title Project Roadmap
    dateFormat YYYY-MM
    axisFormat %b %Y

    section Phase 1
    Core features     :done, p1, 2026-03, 2026-04
    Testing           :done, p1b, 2026-03, 2026-04

    section Phase 2
    Advanced features :active, p2, 2026-04, 2026-06

    section Phase 3
    Dashboard         :p3, 2026-06, 2026-08
```

### Pie Chart

```mermaid
pie title Language Distribution
    "Rust" : 45
    "Python" : 25
    "Swift" : 20
    "TypeScript" : 10
```

### State Diagram

```mermaid
stateDiagram-v2
    [*] --> Stored
    Stored --> Retrieved : keymaker_get
    Stored --> Deleted : keymaker_delete
    Retrieved --> Stored : returned
    Deleted --> [*]

    state Stored {
        [*] --> Encrypted
        Encrypted --> Decrypting : valid policy
        Decrypting --> Encrypted : re-encrypted
    }
```

### Decision Tree

```mermaid
gitGraph
    commit id:"init"
    commit id:"scaffold"
    branch feature-auth
    checkout feature-auth
    commit id:"add-jwt"
    commit id:"add-middleware" tag:"v0.2.0"
    checkout main
    commit id:"hotfix" type: HIGHLIGHT
    commit id:"docs"
    merge feature-auth
    commit id:"release" tag:"v1.0.0"
    branch feature-dashboard
    checkout feature-dashboard
    commit id:"ui-shell"
    commit id:"charts"
    checkout main
    commit id:"ci-fix"
    merge feature-dashboard
    commit id:"ship" tag:"v1.1.0"
```

### Copy-Paste Style Block

Use this style block in any Mermaid diagram for consistent Neo colors:

```
    style NodeA fill:#32D74B,stroke:#248A3D,color:#000
    style NodeB fill:#64D2FF,stroke:#0071A4,color:#000
    style NodeC fill:#FF9F0A,stroke:#C77800,color:#000
    style NodeD fill:#BF5AF2,stroke:#8944AB,color:#fff
    style NodeE fill:#FF453A,stroke:#D70015,color:#fff
    style NodeF fill:#FF2D55,stroke:#D70015,color:#fff
    style NodeG fill:#5E5CE6,stroke:#3634A3,color:#fff
    style NodeH fill:#FFD60A,stroke:#C77800,color:#000
```


<p align="center"><img src="templates/skins/renders/divider.svg" width="100%" alt="divider"></p>


## Full Template

<details>
<summary><strong>Copy-paste README template</strong></summary>

```markdown
<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/assets/header-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="docs/assets/header-light.svg">
    <img alt="Project Name" src="docs/assets/header-dark.svg" width="700">
  </picture>
</p>

<p align="center">
  <a href="LICENSE.md"><img src="https://img.shields.io/github/license/USER/REPO?style=flat-square&color=64D2FF"></a>
  <img src="https://img.shields.io/badge/language-rust-BF5AF2?style=flat-square">
</p>


<p align="center"><img src="templates/skins/renders/divider.svg" width="100%" alt="divider"></p>


> [!TIP]
> One-line quick start instruction here.

## The Problem

What pain does this solve? Be specific. Show the broken state.

## How It Works

` ` `mermaid
graph TD
    A["Step 1"] --> B["Step 2"] --> C["Step 3"]
    style A fill:#64D2FF,stroke:#0071A4,color:#000
    style B fill:#32D74B,stroke:#248A3D,color:#000
    style C fill:#BF5AF2,stroke:#8944AB,color:#fff
` ` `

## Quick Start

` ` `bash
git clone ...
cd ...
make build
` ` `

<details>
<summary><strong>Detailed Setup</strong></summary>

Extended setup instructions here...

</details>

## Features

| Feature | Description |
|---------|-------------|
| **Feature 1** | What it does |
| **Feature 2** | What it does |

<details>
<summary><strong>Architecture</strong></summary>

` ` `mermaid
graph TD
    ...
` ` `

</details>

## Roadmap

| Phase | Status | Features |
|-------|--------|----------|
| 1 | Done | Core |
| 2 | Active | Advanced |
| 3 | Planned | Dashboard |

## License

[MIT](LICENSE.md)


<p align="center"><img src="templates/skins/renders/divider.svg" width="100%" alt="divider"></p>


<p align="center">Built by <a href="https://github.com/USER">You</a></p>
```

</details>


<p align="center"><img src="templates/skins/renders/divider.svg" width="100%" alt="divider"></p>


## Included Files

```
repo-design-kit/
├── docs/assets/
│   ├── header-dark.svg              # Generated SVG header (dark mode)
│   └── header-light.svg             # Generated SVG header (light mode)
├── scripts/
│   ├── gen-header.py                # Liquid glass SVG generator
│   └── mockups/                     # Working HTML mockups
├── templates/
│   ├── skins/
│   │   ├── SKINS.md                 # 25 skins catalog
│   │   └── preview/                 # HTML previews (open in browser)
│   │       ├── turrell-cloud.html   # 10 Turrell + Y3K skins
│   │       └── experimental.html    # 15 experimental skins
│   ├── README.template.md           # beautiful-basic-template (with AI guide)
│   ├── vibecheck.yml                # GitHub Action template for vibecheck
│   └── CONTRIBUTING.template.md     # Contributing template
├── .gitignore
├── LICENSE.md
└── README.md                        # This file
```


<p align="center"><img src="templates/skins/renders/divider.svg" width="100%" alt="divider"></p>


## What GitHub Cannot Render

Before you try — these **do not work** in GitHub markdown:

| Feature | Why |
|---------|-----|
| Inline CSS (`style=""`) | Stripped by GitHub sanitizer |
| `<font color="">` | Stripped |
| `<style>` blocks | Stripped |
| JavaScript | Blocked by CSP |
| Animated SVG (JS) | JS blocked inside SVGs |
| `<iframe>` | Blocked |
| ANSI color codes | Ignored in markdown |
| `<marquee>` | Stripped |
| Hover tooltips | `title` attributes stripped from most elements |

**The workaround for all color/visual needs: SVG files referenced via `<img>` or `<picture>`.** That's what this repo provides.


<p align="center"><img src="templates/skins/renders/divider.svg" width="100%" alt="divider"></p>


<p align="center">
  Built by <a href="https://github.com/qinnovates">Qinnovate</a>
</p>

[^1]: Tested on GitHub.com as of March 2026. GitHub occasionally adds new markdown features — check [GitHub's docs](https://docs.github.com/en/get-started/writing-on-github) for the latest.
