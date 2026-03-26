# Available Skins

Gradient palettes inspired by Apple's Neo Wallpaper collection. Each skin includes dark and light mode variants.

## Neo Palette

| Skin | Colors | Best For |
|------|--------|----------|
| **Lime Cyan** | `#32D74B` → `#64D2FF` | Dev tools, CLI, infrastructure |
| **Magenta Purple** | `#FF2D55` → `#BF5AF2` | AI/ML, creative tools |
| **Blue Indigo** | `#0A84FF` → `#5E5CE6` | Mobile apps, design systems |
| **Orange Gold** | `#FF9F0A` → `#FFD60A` | Education, accessibility |
| **Cyan Blue** | `#64D2FF` → `#0A84FF` | Data, analytics, APIs |
| **Green Teal** | `#32D74B` → `#30D158` | Health, sustainability, nature |
| **Red Orange** | `#FF453A` → `#FF9F0A` | Security, alerts, monitoring |
| **Full Spectrum** | `#FF2D55` → `#BF5AF2` → `#5E5CE6` → `#64D2FF` | Flagship projects, portfolios |

## Preview

Each skin is a pair of SVG files:
- `header-dark.svg` — for dark mode GitHub
- `header-light.svg` — for light mode GitHub

Drop them in `docs/assets/` and reference them with:

```html
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/assets/header-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="docs/assets/header-light.svg">
  <img alt="Project Name" src="docs/assets/header-dark.svg" width="700">
</picture>
```
