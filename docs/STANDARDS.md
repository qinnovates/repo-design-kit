# GitHub Repo Standards

Quorum-approved (5 SME panel, 2026-03-26). The adversarial critic cut 40 proposed files down to a tiered system based on one principle: **everything is earned, not prescribed.**

## Tier 1 — Every Repo (the floor)

| File | Purpose |
|------|---------|
| `README.md` | SVG header from theme, badges, TOC if >150 lines |
| `LICENSE.md` | MIT for public, proprietary for private |
| `.gitignore` | Language-specific + hardened secrets/PII exclusions |
| `CLAUDE.md` | AI assistant context: build commands, architecture, rules |
| Build manifest | `Cargo.toml` / `Package.swift` / `pyproject.toml` / `package.json` |

**That's 5 files. That's the standard.**

## Tier 2 — When Earned

| File | Add when... |
|------|------------|
| `.github/workflows/ci.yml` | Project has tests worth running automatically |
| `CHANGELOG.md` | Project has users (published crate/package) |
| `SECURITY.md` | Project is published and accepts vulnerability reports |
| `docs/` folder | README exceeds 300 lines and needs splitting |
| `.github/dependabot.yml` | Project has real dependencies |
| `Dockerfile` | Project deploys as a container |
| Star History chart in README | Project is public and gaining traction |

## Tier 3 — Public Repos Only (when earned)

| File | Add when... |
|------|------------|
| `CONTRIBUTING.md` | External contributors actually appear |
| `.github/ISSUE_TEMPLATE/*.yml` | Public issues are enabled and getting traffic |
| `.github/PULL_REQUEST_TEMPLATE.md` | Accepting external PRs |
| `CITATION.cff` | Project is citable (research/academic) |

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
