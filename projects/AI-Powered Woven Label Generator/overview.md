# Griffes Vivienne — Full Project Memory

_Last updated: 2026-04-15_

This file is the consolidated working memory for the **AI-Powered Woven Label Generator** project for **Griffes Vivienne**.
It merges the key product, UX, architecture, AI generation, commerce, and deployment knowledge accumulated across the project so far.

---
## Related
- [[current-state]]
- [[decisions]]
- [[risks]]
- [[next-steps]]
- [[prompts]]
- [[feedback_git_base_check]]
- [[feedback_logout_pattern]]
- [[projects/AI-Powered Woven Label Generator/sessions/2026-04-15-header-refinement-and-eod-sync|Header refinement and EOD sync]]
- [[sessions/session-2026-04-15-griffes-vivienne-conversion-polish|Conversion polish session]]
## 1) Project identity

### Project name
**AI-Powered Woven Label Generator**

### Brand / client
**Griffes Vivienne**

### Core product goal
This is **not** an art generator.
The main objective is:

**AI Design → User Engagement → Premium Generation → Real Order CTA**

The application must help a user:
1. upload a logo,
2. configure a woven label through controlled parameters,
3. generate a realistic mockup,
4. unlock premium value when interest is proven,
5. convert that intent into a real manufacturing order.

### Product positioning
The app is meant to feel:
- premium,
- simple,
- conversion-focused,
- realistic enough to build trust in the physical product.

The central challenge is always the same:
**the digital output must feel close enough to the final real woven label that the user wants to order production.**

---

## 2) Locked business rules

These rules are foundational and should not be broken.

### Codification logic
**1 material + 1 color + 1 size = 1 unique code**

Examples:
- `HD_BLACK_50x20`
- `SATIN_RED_30x15`

This means the generator cannot behave like a loose creative playground.
It must be constrained by a product/domain system.

### Supported material / texture families
The system is built around controlled woven label texture families:
- **HD**
- **Satin**
- **Taffeta**
- **Cotton / BIO / HD Cotton**

### Generation must be parameter-driven
The AI must follow controlled inputs such as:
- material
- color
- size
- weave type
- grid density
- thread angle
- gloss level

### Hard constraint
The AI must **never** produce random artistic textures.
It must follow **controlled presets** and approved visual directions.

---

## 3) Original milestone structure

### Milestone 1 — Codebase Review & Generation Pipeline Stabilization
Goal:
- understand the existing MVP,
- find the generation pipeline,
- identify prompt logic,
- stabilize the AI generation behavior,
- define the project architecture.

### Milestone 2 — Domain Logic & Texture Control System
Goal:
- implement parameter configuration,
- formalize texture presets,
- improve realism and consistency,
- build controlled logic for material/color/size.

### Milestone 3 — Core Generator Interface (UX)
Goal:
- improve the main user workflow,
- parameter selection → preview → generation,
- implement **1 free generation** logic,
- improve conversion-oriented UX.

### Milestone 4 — Freemium System & Payment Integration
Goal:
- build commercial foundations,
- guest sessions,
- one free generation,
- premium gating,
- Stripe/credit system,
- account transition only when needed,
- ownership/persistence foundations.

### Milestone 5 — Conversion Workflow & Production Deployment
Goal:
- finalize the post-generation conversion flow,
- move user from result → order intent,
- prepare production-ready deployment flow,
- preserve order context,
- implement preorder capture.

---

## 4) Current overall status

### Functional status
The project is now **functionally complete from the product-flow perspective through Milestone 5**.

### Milestone 5 status
**Milestone 5 is functionally complete, with PASS WITH RISKS across batches.**

### Post-Milestone-5 polish + hotfix (2026-04-15)
Branch `claude/reverent-banzai`, commits `2a54eef` → `3c289e1`:

**Conversion polish:**
- Email capture system for guests at order boundary (`emailGate.ts`, `useGuestEmail`, `EmailCaptureModal`)
- 16 Vitest unit tests for email gate logic
- `OrderLabelsPanel` gated behind email for guests; `OrderPreview` shows known email in summary
- `BrandLogo` upgraded to use `/logo-gv.png` (actual gold logo, no CSS filter needed) + GV text fallback
- `client/public/logo-gv.png` committed to repo
- FR + EN translations for all new email capture keys

**Consistency hotfix:**
- `Account.tsx` header replaced with shared `<BrandLogo />` (was: Sparkles icon + raw translation)
- `Account.tsx` logout fixed: was calling `trpc.auth.logout` directly, never calling `clerk.signOut()` → Clerk session stayed alive. Now delegates to `useAuth.logout()` which does both steps in a `finally` block.
- Helper text under "Generate again" replaced: "Credits available..." → "Create another version of your label." (premium, universal, no credits mention)

### Final production checklist still required before sign-off
- set `ORDER_INTENT_SIGNING_SECRET`
- save `client/public/logo-gv.png` (brand logo file)
- apply DB migrations:
  - `0010_preorder_submissions.sql`
  - `0011_order_funnel_events.sql`
- verify ops access for:
  - `getRecentPreorders`
  - `getFunnelSummary`
- optionally fix unrelated failing server tests to return CI to fully green status

### Important caveat
“Functionally complete” does **not** mean every infrastructure/deployment risk is closed.
The product flow is there, but production hardening still matters.

---

## 5) Milestone 1 memory — codebase review and generation stabilization

### What this milestone was about
The objective was to understand the MVP and make the AI generation engine stable enough to build on safely.

### Main discoveries
The core system already had:
- a working AI generation pipeline,
- Nano Banana Pro / Gemini image generation integration,
- frontend pages for upload, preparation, and result,
- a database-backed app structure,
- multilingual ambitions,
- a conceptually valid product direction.

### Key technical areas identified
The project structure centered around files such as:
- `server/nanoBananaService.ts`
- `server/routers.ts`
- `server/moodboards.ts`
- `server/label/...`
- `client/src/pages/Home.tsx`
- `client/src/pages/Prepare.tsx`
- `client/src/pages/Result.tsx`
- `drizzle/schema.ts`

### Pipeline understanding
The generation pipeline was established as:
1. frontend collects logo + selected options,
2. frontend calls generation mutation,
3. server validates entitlement / generation request,
4. service constructs prompt + moodboard references,
5. Nano Banana Pro generates image,
6. output is stored and returned to frontend.

### Important architectural direction established
The project needed to move from a loose MVP into a **controlled product generator** with:
- canonical domain types,
- parameter-based generation,
- maintainable server logic,
- safer prompt composition,
- deterministic preset-driven behavior.

### Early risks found
- prompt behavior too open-ended,
- texture outputs inconsistent,
- material distinctions not strong enough,
- domain rules not formal enough,
- risk of AI drifting toward decorative or printed effects.

---

## 6) Milestone 2 memory — texture control and domain logic

This was one of the most sensitive milestones because **texture realism is the core credibility layer of the product**.

### Core objective
Transform the generator from “AI making something label-like” into “AI following controlled woven label material presets”.

### Domain direction introduced
A canonical configuration direction was established around concepts like:

```ts
{
  material: "HD",
  color: "black",
  size: "50x20",
  weave: "satin",
  density: 0.8,
  tilt: 15,
  gloss: 0.3
}
```

### Texture preset system direction
The system moved toward explicit presets such as:
- `HD_texture`
- `SATIN_texture`
- `TAFFETA_texture`
- `COTTON_texture`

Each preset conceptually contains:
- reference images,
- prompt template,
- visual constraints,
- structural parameters.

### Major texture control learnings
The client is extremely sensitive to:
- whether the label looks **woven** rather than printed,
- whether the logo is visually integrated into the weave,
- whether background and logo weaving are distinguishable in the right way,
- whether selvedges and thread direction feel physically plausible.

### Critical material-specific learnings

#### HD
Needs:
- high density,
- tight weave,
- premium structured realism,
- no fake embroidery or glossy plastic look.

#### Satin
Needs:
- visible satin sheen,
- elegant but controlled light behavior,
- not too dark,
- not confused with taffeta.

A recurring issue was that satin sometimes inherited the **dark garment background** from moodboards, causing the label itself to appear too dark.

#### Taffeta
Needs:
- classic woven structure,
- visible vertical warp threads,
- realistic regularity,
- no wrong texture family contamination.

The user/client repeatedly flagged taffeta as **not matching the required texture** and emphasized that color should not be touched when the structural problem was the real issue.

#### Cotton / HD Cotton / BIO
Needs:
- more organic textile feeling,
- not fuzzy canvas,
- not porous linen,
- still controlled and premium,
- often with diagonal/twill-like realism depending on sub-style.

### Background freeze decisions
To stabilize visual consistency, approved/frozen backgrounds by material were established:
- **HD → white polished onyx**
- **Cotton → light natural wood**
- **Taffeta → laid paper (papier vergé)**
- **Satin → light grey polished concrete**

This is very important:
**backgrounds were intentionally frozen per material to reduce variation and help the AI stay visually consistent.**

### Additional color/usage logic from project memory
- Cotton should stay in a warm ecru/beige family.
- Satin should remain visually light even when colored.
- HD and Taffeta can support stronger contrast.
- Very light logo on a very light background may reduce readability.
- Dark satin backgrounds are undesirable.
- Cold/dark whites for cotton are risky.

### Structural realism constraints that became important
The generator must avoid:
- printed logo look,
- embroidered patch look,
- raised stitching look,
- padded edge look,
- fake bevel/shadow effects,
- random artistic textile noise.

The generator should favor:
- physical weave integration,
- thread-level realism,
- controlled micro-grain,
- plausible warp/weft organization,
- subtle relief from weave itself rather than fake post-processing effects.

### Broché-like logo integration principle
For HD / HD Cotton, the logo and text should often feel:
- woven distinctly from background,
- denser or tighter than the background,
- visible through weave difference,
- never like printed ink.

### Important prompt/preset approach
The system increasingly relied on:
- moodboards,
- strict negative prompting,
- material-specific prompt templates,
- structure-first prompting,
- parameter freeze for approved visual conditions.

### Determinism goal
A major project goal became:
**same input → similar controlled output**, not totally random reinterpretation.

This drove:
- preset systems,
- prompt freeze ideas,
- structured config builders,
- run tracking.

---

## 7) Milestone 3 memory — generator UX and conversion-first interface

### Objective
Make the generator UX simple, premium, and commercially sensible.

### Canonical main flow
The intended user flow became:
1. Upload logo
2. Select parameters
3. Preview / prepare
4. Generate
5. See result
6. Download / generate again / upgrade / order

### Key UX principle
The interface should feel premium and conversion-oriented, not experimental or cluttered.

### Major Milestone 3 themes
- generator state normalization,
- simpler parameter flow,
- one free generation logic,
- better result page and CTA placement,
- improved order-oriented interface behavior,
- loading UX considerations.

### Generator state architecture work
A client-side generator store was introduced to centralize:
- material,
- color,
- size,
- logo type,
- derived code/product state,
- generation success handling,
- free trial status handling.

### Free generation logic (Milestone 3 stage)
At Milestone 3 stage, the user could get:
- **1 free generation**,
- then premium gating.

Later this logic was moved to more canonical server ownership in Milestone 4.

### Result page and CTA work
The result experience became more commercial.
Notable product decisions included:
- “Generate again” as a strong primary action near the result,
- premium unlock appearing at the moment of intent,
- CTA framing toward label ordering,
- email capture deferred to the order boundary rather than interrupting early.

### Order-related UX components introduced
Work in this phase and the transition to later phases involved:
- `OrderLabelsPanel`
- `OrderPreview` page
- more structured Result page layout
- stronger post-result conversion logic

### MOQ / quantity realism discussion
The client highlighted that the production logic should reflect reality more closely:
- MOQs are high,
- quantities should often be in increments like 500 or 1000,
- quantities like 1235 make little sense,
- the user should choose between:
  - sample,
  - or production quantity.

This is important for future order UX:
**the interface should match real production constraints while staying simple.**

### Loading UX discussion
A recurring issue:
image generation takes around **~1 minute** on average.

The client explicitly said the real problem is not just speed, but **what the user experiences during the wait**.

Design direction:
- make the wait feel intentional,
- avoid a “frozen” feeling,
- turn the waiting moment into a premium experience,
- reduce confusion for non-AI-native users.

This is an important unfinished UX enhancement area.

---

## 8) Milestone 4 memory — freemium, billing, ownership, and production foundation

Milestone 4 was about converting the generator from an impressive demo into a commercially usable system.

### Locked Milestone 4 product principle
**No-account entry → 1 free generation → premium unlock → account only when needed → credits/payments/history → simple internal back office → production-readiness foundation**

### What was in scope
- remove demo bypass from canonical logic,
- move free-trial enforcement to server,
- add guest sessions,
- add server-owned pricing catalog,
- add credit ledger foundation,
- add Stripe one-time checkout for credit packs,
- support guest→user continuity,
- generation ownership by guest or user,
- durable asset thinking,
- minimal account area foundations,
- admin/back-office foundation,
- production artifact/vectorization groundwork.

### Locked architecture decisions from Milestone 4
1. **Server owns freemium truth**
2. **Guest sessions are first-class**
3. **Account creation happens at monetization boundary**
4. **Stripe = one-time checkout for credit packs only**
5. **Pricing is server-owned**
6. **Credits are ledger-based**
7. **Generations can belong to guest or user**
8. **Original uploads must be preserved before rasterization**
9. **Order intent is lightweight only at this stage**
10. **Production foundation remains internal**
11. **Do not rewrite the AI generation engine** — wrap it with better ownership/persistence/entitlement systems

### Ownership model
For records that may belong to a guest or a logged-in user, the chosen direction was:
- `ownerUserId` nullable
- `ownerGuestSessionId` nullable
- exactly one should be set

This was preferred over a generic `ownerType + ownerId` approach.

### Phase structure inside Milestone 4
- Phase 1 — entitlement/ownership foundation
- Phase 1.1 — blocker stabilization
- Phase 2 — durable assets foundation
- Phase 3 — Stripe checkout + webhook
- Phase 4 — guest → user claim flow
- Phase 5 — account area completion
- Phase 6 — admin/back office v1
- Phase 7 — production-readiness foundation

### Phase 1 implemented
Implemented concepts included:
- `guest_sessions`
- `credit_packs`
- `credit_ledger_entries`
- user extension with `stripeCustomerId`
- generation ownership extension
- generation run guest support
- server-owned pricing route
- server-owned free trial enforcement
- ledger-backed balance reads
- entitlement summary path

### Phase 1 status
**PASS WITH RISKS**

### Key risks identified during Milestone 4
1. Ownership not fully canonical everywhere yet
2. Ownership exclusivity enforced in code more than DB
3. Premium spend not atomic enough with generation success
4. Overspend race condition possible
5. Ledger canonicality partial due to legacy compatibility
6. Client still had local free-trial state in some UX areas
7. Guest continuity limited if cookie is lost
8. Migration bug in schema evolution
9. Frontend balance display partly stale in places

### Critical production issue discovered
A major deployment issue occurred because production DB migrations had not been applied.

#### Root cause found
The production database was missing migration(s), including the one creating `guest_sessions`.

#### What failed
Guest session insert flow failed because the corresponding table did not exist in production.

#### Key lesson
The Vercel deployment pipeline did not automatically apply DB migrations.
This means deployment must include explicit migration handling.

### Commerce direction
The user journey remained intentionally frictionless:
- no account at the beginning,
- account only when payment/history/device continuity becomes necessary.

This is a core product decision and should stay intact unless the strategy changes.

---

## 9) Milestone 5 memory — conversion workflow and preorder/order bridge

Milestone 5 focused on the post-generation conversion funnel.
Its goal was not to build full manufacturing operations, but to close the critical gap between a generated result and a real order intent.

### Product perspective
Milestone 5 made the product feel like a real business funnel instead of just a generator.

### Batch-by-batch progress

#### Batch 1 — canonical generator domain/state foundation
Status: **PASS WITH RISKS**

Implemented:
- canonical generator domain/state foundation,
- pure typed eligibility/completeness helpers,
- derived selectors,
- unit tests.

#### Batch 2 — centralized typed generator flow model
Status: **PASS WITH RISKS**

Implemented:
- centralized typed generator flow model,
- shared route guards,
- flow controller hook wired to auth and credit balance,
- focused transition tests.

#### Batch 3 — result-state routing and view modeling
Status: **PASS WITH RISKS**

Implemented:
- typed result-state view model,
- centralized Result state router,
- Result page refactored to be flow-driven.

#### Batch 4 — Order Labels CTA gating
Status: **PASS WITH RISKS**

Implemented:
- typed Order Labels CTA view model,
- centralized CTA gating from result/flow state,
- lightweight CTA analytics hooks,
- routing to order-preview or credits based on readiness/lock state.

#### Batch 5 — durable Result → OrderPreview handoff
Status: **PASS WITH RISKS**

Implemented:
- typed `OrderIntentDraft` contract,
- localStorage persistence with TTL,
- durable handoff from Result to OrderPreview,
- hardened OrderPreview recovery and guards.

#### Batch 6 — backend-backed order intent bridge
Status: **PASS WITH RISKS**

Implemented:
- minimal backend-backed order intent bridge,
- signed token validation,
- authoritative `/order-preview` integrity checks,
- local fallback preservation.

#### Batch 7 — preorder submission contract
Status: **PASS WITH RISKS**

Implemented:
- minimal pre-order submission contract,
- audit persistence via `preorder_submissions`,
- idempotent backend submission behavior,
- actionable OrderPreview submit UX,
- conversion analytics for preview-to-preorder.

#### Batch 8 — confirmation and funnel ops visibility
Status: **PASS WITH RISKS**

Implemented:
- pre-order confirmation receipt UX,
- recent preorders ops read endpoint,
- funnel summary path,
- backend funnel event tracking.

### Milestone 5 conclusion
**Milestone 5 is functionally complete from the product-flow perspective.**

### What this means in product terms
The system can now move a user through:
- generation,
- result,
- CTA,
- order preview,
- preorder submission,
- confirmation,
- internal tracking.

This is a major product milestone because it closes the “cool output but no real order path” gap.

---

## 10) Current canonical UX workflow

As of current project memory, the intended canonical user journey is:

1. **Upload logo**
2. **Select parameters**
   - material
   - color
   - size
   - potentially other controlled visual settings
3. **Prepare / preview**
4. **Generate**
5. **Receive 1 free generation** (guest flow allowed)
6. **Review result**
7. **Generate again / unlock premium if needed**
8. **Move toward Order Labels CTA**
9. **Open Order Preview**
10. **Submit preorder intent**
11. **See confirmation**
12. **Internal ops can review funnel and preorder records**

### Important UX philosophy
- registration should not appear before value is shown,
- friction should appear only when user intent is strong,
- premium lock should feel like a natural next step, not punishment,
- order CTA should appear when trust is highest.

---

## 11) AI generation strategy memory

### Model / provider direction
The project uses **Nano Banana Pro** through Google AI Studio / Gemini image generation infrastructure.

### Core strategy
This is **controlled material transfer**, not open artistic generation.

### Typical prompt philosophy
The generator should:
- use the uploaded logo as geometry,
- use approved reference images as material guidance,
- transfer texture/light/material feel,
- keep structure realistic,
- avoid copying textual content from references,
- behave like a textile design renderer.

### Moodboard strategy
Moodboards are important because they provide:
- material identity,
- lighting character,
- structural cues,
- realism anchors.

### Why this matters
Without strong reference conditioning, the AI drifts too easily into:
- generic fabric,
- print-like outcomes,
- decorative embellishment,
- wrong material family.

### Negative prompt / anti-drift strategy
The project repeatedly relied on explicit exclusions against:
- embroidery,
- stitched outline,
- patch effect,
- applique,
- canvas/linen/burlap textures when not desired,
- fuzzy weave,
- oversized weave cells,
- random macro fibers,
- fake relief effects.

### Core generation philosophy
The system should act like a **parameterized textile mockup engine**.

---

## 12) Tech stack memory

### Frontend
- React / Next.js direction for product architecture discussions
- In implementation memory, React + TypeScript-based app structure is central
- Tailwind CSS / modern component system

### Backend
- Node.js
- tRPC-like routing
- server-side business logic around generation, entitlement, credits, and order flows

### Database
- Drizzle ORM
- MySQL/TiDB-style schema references in some earlier deliverable memory
- migrations critical to deployment correctness

### Payments
- Stripe planned/implemented as one-time credit-pack checkout foundation

### AI generation
- Nano Banana Pro / Google AI Studio / Gemini image preview class model

### Storage / assets
- output persistence and asset ownership became a major architecture theme in Milestone 4+

### Deployment
- Vercel is an important deployment target used in project flow
- deployment must handle migrations explicitly

---

## 13) Important files and conceptual modules remembered

These are the most relevant project areas repeatedly referenced across the work:

### Backend / server
- `server/nanoBananaService.ts`
- `server/routers.ts`
- `server/moodboards.ts`
- `server/label/types.ts`
- `server/label/constants.ts`
- `server/label/texturePresets.ts`
- `server/label/buildLabelConfig.ts`
- `server/label/generateLabelCode.ts`
- `server/label/buildGenerationPrompt.ts`
- `server/label/mapLegacyTextureType.ts`
- `server/_core/index.ts`

### Frontend / client
- `client/src/pages/Home.tsx`
- `client/src/pages/Prepare.tsx`
- `client/src/pages/Result.tsx`
- `client/src/pages/Credits.tsx`
- `client/src/pages/Account.tsx`
- generator domain/store files
- order preview / order CTA related components

### Database / schema / migrations
- `drizzle/schema.ts`
- milestone-related SQL migrations
- preorder-related migrations:
  - `0010_preorder_submissions.sql`
  - `0011_order_funnel_events.sql`

### Tests mentioned in project memory
- `server/texturePresets.test.ts`
- `server/nanoBananaService.helpers.test.ts`
- `server/generation.test.ts`
- server/auth and service-level tests

---

## 14) Runtime / infrastructure issues encountered during the project

### 1. Missing production migrations
This caused runtime failures in guest flow.

### 2. Deployment pipeline gaps
Vercel deployment did not automatically handle DB migration application.

### 3. Environment variable issues
The project encountered missing or misconfigured env values during development and deployment.

### 4. Generation latency
Average generation time around ~1 minute created UX risk.

### 5. AI quota / rate issues
There were mentions of Gemini / image-model quota constraints in project memory.

### 6. Frontend/runtime inconsistency risks
Some UI state originally relied too much on local state before server-owned entitlement became more canonical.

---

## 15) Commerce / conversion strategy memory

### Product philosophy
The app must earn the user’s trust first, then monetize.

### Intended commercial flow
- one free generation for proof of value,
- premium generations or premium outputs gated,
- credits / one-time pricing packs,
- account creation only when actually necessary,
- order CTA presented when emotional/product intent is high.

### Why this matters
The product is selling not just a mockup, but confidence in manufacturing.
So conversion depends on:
- realism,
- frictionless first interaction,
- premium feel,
- clear next step to order real labels.

### Back office need
The client also highlighted a future need for a **simple back office** to manage:
- generations,
- users/leads,
- payments/credits,
- potentially production issues.

---

## 16) Things explicitly considered out of scope at earlier stages

These were intentionally deferred from Milestone 4 and largely beyond the immediate scope unless revisited:
- full manufacturing order management,
- shipping/taxes/invoicing PDFs,
- ERP/fulfillment integration,
- subscription billing,
- customer self-serve payment method portal,
- advanced CRM automation,
- rich DAM/studio,
- full production workflow with roles/SLA/vendor routing,
- complex permissions.

This matters because the architecture was intentionally kept lean enough to reach conversion readiness without overbuilding.

---

## 17) Approved / important product decisions that should be remembered

### Decision: account creation is delayed
Do **not** force signup before first value is shown.

### Decision: server owns commercial truth
Client-side state should not be trusted for entitlement.

### Decision: guest sessions are important
Anonymous users are a first-class part of the commercial funnel.

### Decision: textures must be controlled
No random artistic interpretation.

### Decision: approved backgrounds are frozen by material
This is part of output consistency.

### Decision: order intent in early commercial flow stays lightweight
The system should capture order intent and preorder context before building a massive operations system.

### Decision: conversion flow is as important as generation quality
A beautiful image without a next-step system is not enough.

---

## 18) What is currently safest to say about project completion

### Completed at a functional/product-flow level
- Milestone 1 foundations
- Milestone 2 domain/texture control direction
- Milestone 3 core UX flow
- Milestone 4 freemium/commercial ownership foundation
- Milestone 5 conversion/preorder flow

### Still requiring production hardening / validation
- final env configuration,
- final DB migrations in production,
- ops endpoint verification,
- CI cleanup,
- texture quality validation in remaining edge cases,
- possible UX polish for loading state,
- possible further visual refinement on specific textures like taffeta/satin depending on latest client validation.

---

## 19) Recommended next practical focus

Given current memory, the smartest next focus after functional completion is:

### 1. Production sign-off hardening
- env audit (`ORDER_INTENT_SIGNING_SECRET` must be set)
- migration audit — apply `0010_preorder_submissions.sql` + `0011_order_funnel_events.sql` in production
- endpoint permission audit (`getRecentPreorders`, `getFunnelSummary`)
- CI cleanup

### 2. Visual QA pass on textures
Particularly confirm:
- satin consistency,
- taffeta structure fidelity,
- cotton realism,
- final approved outputs against manufacturing expectations.

### 3. Loading UX improvement
Because 1-minute waits are a known conversion risk.

### 4. Deployable ops readiness
Make sure internal preorder visibility and funnel summary are truly usable in production.

### 5. Logo file
Save brand logo to `client/public/logo-gv.png` — BrandLogo component references it, falls back to "GV" text until present.

---

## 20) Short milestone summary for fast orientation

### Milestone 1
Understood MVP, stabilized pipeline direction, identified prompt/texture/domain architecture.

### Milestone 2
Built controlled texture/material/domain logic direction; frozen backgrounds and realism constraints became crucial.

### Milestone 3
Built stronger generator UX, free generation flow, better result experience, early order/CTA direction.

### Milestone 4
Built guest sessions, server-side entitlement logic, commercial foundation, credits/payments/account-transition architecture.

### Milestone 5
Built conversion flow from result → CTA → order preview → preorder submission → confirmation → internal funnel tracking.

---

## 21) Sources used for this consolidated memory

This consolidated memory was reconstructed from:
- project working memory already tracked in conversation context,
- the uploaded Milestone 4 memory file,
- the uploaded deliverable/overview file,
- project progress tracked across milestones.

Important source files used for grounding:
- `MILESTONE_4_MEMORY.md`
- `DELIVERABLE_V2.0_EN.md`

---

## 22) Final canonical reminder

This project should always be treated as a **production-oriented, conversion-focused, parameter-driven woven label generator**, not as a generic AI image tool.

Whenever adding features, evaluate them by:
- complexity,
- conversion impact,
- architectural compatibility.

The safest long-term rule remains:

**Preserve realism, preserve control, preserve conversion flow, do not break the architecture.**
