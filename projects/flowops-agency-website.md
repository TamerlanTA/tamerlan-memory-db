# FlowOps Agency Website

## Related
- [[agent-memory]]
- [[FlowOps promo video scene system]]

## Current status
- 2026-04-26: Published the `FlowOps2` rebrand to GitHub production branch `main` for `https://github.com/TamerlanTA/FlowOps`. Commit: `d0c9d99` (`Launch FlowOps command-center rebrand`).
- Vercel project `flowops` built the new `main` commit successfully. Deployment `dpl_2ZrnYgHabX4VRyvMVrDUZW76UhmN` reached `READY` and aliases include `www.flowops.agency`, `flowops-orpin.vercel.app`, and `flowops-git-main-tamertt931-8560s-projects.vercel.app`.
- Deployment was done from a clean temporary worktree at `/tmp/flowops-main-worktree` because `/Users/tamerlan/Desktop/PC/FlowOps` remained on dirty branch `milestone4-auth-completion`.
- 2026-04-26: Created a new full-rebrand implementation in `/Users/tamerlan/Desktop/FlowOps2` rather than continuing to mutate `/Users/tamerlan/Desktop/PC/FlowOps`. The new site keeps FlowOps content/offer only, but replaces the visual system with a new dark command-center portfolio aesthetic inspired by the user's two GitHub references.
- New `FlowOps2` build uses a single custom client experience (`components/FlowOpsRebrand.tsx`) with fixed glass nav, full-screen canvas engine/orbit scene, interactive workflow prompt, live architecture preview, stack strip, problems, services, cases, method, proof, and contact sections.
- Preserved the old lead capture contract by copying `/api/contact`, `/api/sendLead`, `lib/lead.ts`, and Telegram/Google Sheets/SendGrid integration helpers into `FlowOps2`; the UI posts to `/api/contact` with the same schema.
- 2026-04-26: Upgraded `/Users/tamerlan/Desktop/PC/FlowOps` homepage from a standard agency landing page into an interactive premium AI Automation System Builder experience.
- Hero now uses a live builder: user enters an automation request, UI immediately shows a fallback/generated system map, then calls `/api/analyze-system` for AI-backed structured architecture when `OPENAI_API_KEY` is available.
- Added deterministic fallback analyzer for common automation keywords: WhatsApp, email, CRM, leads, Shopify, orders, Google Sheets, Airtable, Notion, ClickUp, Slack, invoices, scraping, reporting, dashboard, support, and customer messages.
- Preserved existing lead form submission pipeline (`/api/sendLead` → Telegram, Google Sheets, email) and added prefill from generated system request/summary.
- Added six interactive Real Systems cards: WhatsApp AI Bot, WhatsApp AI Bot + CRM Sync, Lead Research Automation Pipeline, Social Media Video Automation Pipeline, Jotform to ClickUp Operations System, AI Label Generator Order Flow.
- Added How We Think section and updated final CTA/SEO positioning around systems, not random automations.
- 2026-04-26: Restyled the new builder toward the user's monochrome reference screenshots (`IMG_7326.jpg`, `IMG_7327.jpg`, `IMG_7328.jpg`): black framed stage, compact centered pill nav, white CTA, grayscale mesh/silk background, softer horizon arc, reduced cyan/violet SaaS look, and monochrome workflow/result cards.
- 2026-04-26: Added a second polish pass focused on interaction quality: staged system-generation states, living idle graph, edge labels/particles, node type badges/hover states, mobile compact flow preview, executive-style result panel, case modal tools + “Build something similar” prefill CTA, monochrome Real Systems cards, updated contact copy, and updated metadata title/description.
- 2026-04-26: Added a GitHub-reference effects pass inspired by `mohitvirli.github.io` and `ThreeJS_Portfolio`: lightweight canvas automation-engine orbit layer, pointer-responsive hero stage tilt/spotlight, portal/depth hover treatment for workflow nodes and case cards, scan highlights for glass panels, and command-bar polish. No new heavy animation/3D dependencies were added.
- 2026-04-26: Addressed reported hydration mismatch warning by adding root `suppressHydrationWarning` on `html`/`body` for extension-injected attributes and fixing Navbar hash-route active comparison (`/#cases`) to compare only the pathname.

## Key decisions
- User explicitly asked for a full rebrand and to reuse only the old site's information; therefore the old visual components were not reused in `FlowOps2`.
- GitHub clone/download of the two reference repos stalled on network, so the `FlowOps2` implementation adapted the referenced effect direction from the known pattern: canvas orbit/data particles, horizon grid, scan-panel hover, portal-like cards, and command-panel workflow UI.
- `FlowOps2` remains a compact single-page site for now, with old multi-page routes intentionally not recreated unless requested.
- Treat this as a small project note for now, not a full project folder, unless the agency website becomes a larger ongoing redesign/build stream.
- Avoided React Flow or large new dependencies; implemented a custom HTML/SVG-style workflow renderer with existing React, Tailwind, and lucide-react.
- API route always returns a valid `SystemPlan`; OpenAI failure or missing key falls back silently to deterministic local planning.
- Used OpenAI Responses API with structured JSON schema via direct `fetch`, avoiding a new SDK dependency.
- For the reference-style pass, kept the interactive builder and lead prefill behavior intact instead of replacing the page with a static portfolio-like hero.
- Continued avoiding heavy animation libraries; polish uses existing React state plus CSS transitions/keyframes for performance.
- For the GitHub-reference pass, adapted visual techniques instead of copying the repos directly: 2D canvas approximates orbit/ring/data movement, CSS handles portal/depth hover, and pointer CSS variables provide a “camera” feel without Three.js/GSAP runtime cost.

## Validation
- Production deploy validation: Vercel deployment for commit `d0c9d995b4565718bc4ae0277c3d9b0c609de0e0` is `READY`; Vercel fetch of `https://flowops-orpin.vercel.app` returned HTTP 200 and contained the new command-center rebrand HTML.
- Clean `main` worktree validation before push: `npm run lint` passed and `npm run build` passed.
- `FlowOps2`: `npm run lint` passed cleanly.
- `FlowOps2`: `npm run build` passed cleanly; routes generated: `/`, `/api/contact`, `/api/sendLead`, `/robots.txt`, `/sitemap.xml`.
- `FlowOps2`: Dev server ran at `http://localhost:3002`.
- `FlowOps2`: Chrome headless screenshots checked desktop `1440x1100` and mobile `390x844`; desktop hero/canvas/command panel rendered correctly. Mobile hero initially overflowed, then was adjusted with mobile type/action/layout constraints and `overflow-x: hidden`.
- `FlowOps2`: `/api/contact` smoke test with invalid payload returned expected schema field errors.
- `npm run lint` passed with one existing warning in `components/Services.tsx` about a missing hook dependency.
- `npm run build` passed.
- Dev server ran at `http://localhost:3001` because port 3000 was already in use.
- Playwright screenshot fallback verified desktop and mobile hero rendering plus desktop Real Systems section.
- API smoke check against `/api/analyze-system` returned valid fallback JSON for a Shopify → ClickUp → Slack reporting request.
- Reference-style pass validation: `npm run lint` passed with the same pre-existing `components/Services.tsx` warning, `npm run build` passed, Playwright Chrome screenshots checked desktop `1440x1100` and mobile `390x844`, and `/api/analyze-system` returned valid fallback JSON for a WhatsApp → CRM → Slack reporting request.
- Interaction polish validation: `npm run lint` passed with the same pre-existing `components/Services.tsx` warning, `npm run build` passed, Playwright Chrome screenshots checked desktop `1440x1100` and mobile `390x844`, and `/api/analyze-system` returned valid fallback JSON for WhatsApp → Kommo CRM → Slack.
- GitHub-reference effects validation: `npm run lint` passed with the same pre-existing `components/Services.tsx` warning, `npm run build` passed, Playwright Chrome screenshots checked desktop `1440x1100`, mobile `390x844`, and desktop Real Systems section. `/api/analyze-system` returned valid JSON for “Qualify WhatsApp leads and update Kommo CRM”.
- Hydration warning fix validation: `npm run lint` passed with the same pre-existing `components/Services.tsx` warning and `npm run build` passed after the Navbar nullable pathname type fix.

## Residual risks
- `/Users/tamerlan/Desktop/PC/FlowOps` is still the old local dirty `milestone4-auth-completion` worktree; production `main` was updated through `/tmp/flowops-main-worktree`. If future local edits should start from production, switch/clone from `main` carefully instead of continuing from the dirty milestone branch.
- `FlowOps2`: Mobile Chrome headless screenshot did not visibly show the hamburger button even after CSS adjustments; main content/CTA rendered, but manual browser check is recommended before deployment.
- `FlowOps2`: Valid contact submission was not smoke-tested because production env variables for Telegram, Google Sheets, and SendGrid may be absent locally; invalid-payload validation path was verified.
- `FlowOps2`: Reference repos were not fully cloned due network stalls, so no direct code/assets were copied from them.
- Computer Use browser interaction could not complete because macOS Accessibility/Screen Recording permissions were still pending.
- Modal click-through was not fully browser-automated due missing local `@playwright/test`; visual/API checks covered the main risks.
- Existing lint warning in `components/Services.tsx` remains unrelated to this work.
- `test-results/.last-run.json` remains untracked from a failed temporary Playwright test attempt; deletion needs explicit user confirmation.

## Next steps
- Manually open `https://www.flowops.agency` and `https://flowops-orpin.vercel.app` to check final visual behavior on real desktop/mobile browsers.
- Decide whether to clean up or archive the old dirty `milestone4-auth-completion` local worktree after confirming production is good.
- Open `http://localhost:3002` manually in Chrome/Safari and check mobile nav/hamburger behavior, hero CTA scroll, prompt editing, and contact form layout.
- If the new rebrand direction is approved, decide whether `FlowOps2` replaces `/Users/tamerlan/Desktop/PC/FlowOps` or should be deployed as a separate project.
- If closer fidelity to the GitHub references is needed, retry cloning/downloading the reference repos and consider adding a real Three.js layer only if performance remains acceptable.
- Manually click through hero input, Real Systems modal, and Get this system built CTA in the browser once Computer Use permissions or normal browser access is available.
- Set `OPENAI_API_KEY` in production if AI-generated architecture should be used instead of deterministic fallback.
- Consider a later polish pass for the dedicated `/cases` page so it visually matches the new Real Systems section.
- If continuing the reference direction, consider making downstream sections (`RealSystems`, contact, services) more monochrome so the whole page matches the new hero/nav system.
- Optional next polish: make older reused sections (`Problems`, `Solutions`, `Services`, `TechStack`, `RoiCalculator`, footer) fully match the monochrome command-center aesthetic; dedicated `/cases` still uses older styling.
- Optional next polish: if the user wants closer fidelity to the GitHub refs, add real `@react-three/fiber` scenes only for one isolated hero layer, after confirming performance budget and asset direction.
