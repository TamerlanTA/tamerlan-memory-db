---
name: Griffes Vivienne — verify git base before starting work
description: Always confirm the correct base branch/commit before starting implementation; origin/main can lag behind the real latest branch
type: feedback
---

## Related
- [[projects/AI-Powered Woven Label Generator/overview|AI-Powered Woven Label Generator]]
- [[projects/AI-Powered Woven Label Generator/decisions|project decisions]]
- [[projects/AI-Powered Woven Label Generator/risks|project risks]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-15-conversion-polish|Conversion polish session]]

Before starting any implementation on this project, verify that the working branch is based on the correct latest commit — not just `origin/main`.

**Why:** In April 2026, a full conversion polish batch was built on `origin/main` (`f51482c`), which was 6 commits behind the real latest code (`3ac2485` on `milestone4-auth-completion`). The gap contained massive changes: new domain helpers (`orderCta.ts`, `resultFlow.ts`, `generatorFlow.ts`), a rewritten `OrderPreview.tsx`, a new `BrandLogo.tsx`. All the work had to be discarded and redone on the correct base.

**How to apply:**
1. Ask the user which branch/commit represents the latest production code before starting.
2. Run `git log --oneline -10` and cross-check with the GitHub repo's active branch.
3. If in doubt, check: `git log --oneline origin/main` vs `git log --oneline origin/<feature-branch>`.
4. The real latest branch in this project may be `milestone4-auth-completion` or a later branch — not necessarily `main`.
