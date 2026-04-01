# GitHub Repo Standards

Quorum-approved (5 SME panel, 2026-03-26, revised 2026-03-31). The adversarial critic cut 40 proposed files down to a tiered system based on one principle: **everything is earned, not prescribed.**

## Tier 1 — Every Repo (the floor)

| File | Purpose |
|------|---------|
| `README.md` | SVG header, tagline, "Why [Name]?", quick start, variant sections, footer with repo-design-kit attribution |
| `LICENSE.md` | MIT for public, proprietary for private |
| `.gitignore` | Language-specific + hardened secrets/PII exclusions + `_memory/` |
| `CLAUDE.md` | AI assistant context: build commands, architecture, rules |
| Build manifest | `Cargo.toml` / `Package.swift` / `pyproject.toml` / `package.json` |

**That's 5 files. That's the standard.**

### README Structure (revised via Quorum 2026-03-31)

```
1. SVG Header (120px max — must not push content below fold)
2. Tagline — one technical sentence (this IS the mission statement)
3. Badges — 3-4 max (license, build, version, language)
4. Why [ProjectName]? — problem + differentiator (3-5 sentences, no adjectives)
5. Quick Start — install + run, copy-pasteable
6. [VARIANT SECTION] — depends on repo type (see below)
7. Collapsible: Architecture (optional — apps/frameworks only)
8. Collapsible: Compared to X (optional — numbers only, no adjectives)
9. Contributing — one-line link to CONTRIBUTING.md
10. License — one line
11. Footer — "Built by USER" + repo-design-kit attribution
```

### README Variants

Three template variants share a common skeleton but differ in emphasis:

| Variant | When to use | Emphasis sections |
|---------|-------------|-------------------|
| **Library** | pip/npm/cargo packages, SDKs | Usage code example, API table |
| **CLI Tool** | Command-line tools, dev tools | Usage commands, demo GIF, benchmarks |
| **Application** | Full apps, platforms, services | Deploy commands, features table, screenshot |

### What was cut (and why)

| Section | Why it was cut |
|---------|----------------|
| Separate "Mission/Goal" section | Mission belongs as the one-line tagline, not its own section |
| Separate "What Makes It Stand Out" section | Fold into "Why [Name]?" — if the problem statement doesn't convey this, it's weak |
| Star History chart | Vanity metric. Replace with "Used By" logos when earned |
| Roadmap table | Rots fast. Link to GitHub Projects instead |
| Dev Commands (build/test/lint) | Contributor content — belongs in CONTRIBUTING.md |
| Quick Start Tip (separate one-liner) | Redundant with Quick Start section |
| Collapsible Configuration | Reference docs — belongs in docs/ or man page |

### Footer Attribution

All repos using the repo-design-kit template must include in the footer:

```markdown
<p align="center"><sub>README template from <a href="https://github.com/qinnovates/repo-design-kit">repo-design-kit</a></sub></p>
```

Maintainers may remove this after initial setup, but it ships by default.

## Tier 2 — When Earned

| File | Add when... |
|------|------------|
| `.github/workflows/ci.yml` | Project has tests worth running automatically |
| `.github/workflows/vibecheck.yml` | Project accepts AI-assisted PRs (use template from `templates/vibecheck.yml`) |
| `CONTRIBUTING.md` | Project is public (use template from `templates/CONTRIBUTING.template.md`) |
| `CHANGELOG.md` | Project has users (published crate/package) |
| `SECURITY.md` | Project is published and accepts vulnerability reports |
| `docs/` folder | README exceeds 300 lines and needs splitting |
| `.github/dependabot.yml` | Project has real dependencies |
| `Dockerfile` | Project deploys as a container |

## Tier 3 — Public Repos Only (when earned)

| File | Add when... |
|------|------------|
| `.github/ISSUE_TEMPLATE/*.yml` | Public issues are enabled and getting traffic |
| `.github/PULL_REQUEST_TEMPLATE.md` | Accepting external PRs |
| `CITATION.cff` | Project is citable (research/academic) |
| "Used By" section in README | Project has real adopters (logos/links) |
| "Compared to" collapsible in README | Project has real alternatives worth comparing against |

## Private Repos — Extra Security

| Requirement | Why |
|-------------|-----|
| Branch protection on main | Prevent accidental force push |
| Signed commits | Verify authorship |
| Disable forking | Prevent data exfiltration |
| Pin GitHub Actions by SHA | Supply chain defense |
| `CODEOWNERS` | Enforce review on security-critical paths |

## The Adversarial Critic's Rule

> "Your best README (332 lines) is handcrafted. No generator built it. No generator could build it. It is good because you wrote it with intent."

> "One script. Four files. Everything else is earned, not prescribed."

Don't front-load ceremony that rots. Add files when the project earns them, not prophylactically. A repo with 4 excellent files beats one with 20 stale templates.

## The Marketing Rule (Quorum 2026-03-31)

> "The best READMEs DO market, but they market through demonstration, not declaration. Every claim is a benchmark or a code sample. The developer doesn't feel marketed to because the proof is inline."

No adjectives. No mission statements. No "what makes us special" sections. State the problem, show the differentiator with proof (benchmark, code sample, comparison table with numbers). If you need adjectives to explain why you're different, your problem statement is weak.
