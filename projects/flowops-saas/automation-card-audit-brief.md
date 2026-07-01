# Automation Card Audit & Upgrade Brief

## Related
- [[overview]]
- [[current-state]]
- [[roadmap]]
- [[next-steps]]
- [[pipeline-catalog]]
- [[pricing]]

## Purpose
Before scaled outreach, every automation card in the FlowOps marketplace must be audited and upgraded so it feels like a real product module, not a thin automation listing. The goal is to make each card answer: who needs this, what pain it solves, why FlowOps can deploy it fast, what the buyer gets, what it costs, and why the visual system feels premium and consistent.

## Scope
- Audit all currently live automation cards in `src/lib/catalog.ts` (`25` live systems).
- Audit all roadmap/coming-soon cards (`7` announced systems) so their positioning does not conflict with live systems.
- Update marketplace cards, system detail pages, pricing references, and any stack/bundle references if price or description changes.
- Preserve the current MVP buyer flow: public audit + public system request/order + internal workspace. Do not reintroduce account/chat/deal-room into the current MVP.

## Required Agent Review Per Card
For each automation card, agents must verify and produce:

1. **Need / market usefulness**
   - Who specifically needs this automation now?
   - Is the pain urgent, frequent, and expensive enough for SMB/local service buyers?
   - Which buyer roles care most: owner, ops manager, sales manager, clinic admin, agency founder, support lead, etc.
   - Which verticals are best-fit and which should be excluded.
   - Whether this should be live, repositioned, merged into another card, moved to coming soon, or removed.

2. **Problem clarity**
   - The card must name the manual pain in concrete language.
   - Avoid generic claims like "save time" unless paired with a real workflow symptom.
   - Explain the before-state: missed leads, slow response, owner chasing updates, manual copying, duplicated work, unclear status, lost context.

3. **Expanded description**
   Current descriptions are too thin. Each card should include richer copy:
   - one sharp tagline;
   - 2–3 sentence description;
   - what triggers the workflow;
   - what the automation does step by step;
   - what the team sees after it runs;
   - what integrations are typical;
   - what is included in setup;
   - what is monitored monthly;
   - realistic deploy time;
   - best-fit industries;
   - not-for / exclusions where needed.

4. **Outcome / ROI framing**
   - Each card should include one practical outcome signal, not fake guaranteed ROI.
   - Examples: response time reduced, missed lead recovery, fewer manual handoffs, cleaner CRM, faster quote turnaround, overdue invoice recovery, fewer support escalations.
   - Use "typical value logic" rather than unsupported promises.

5. **Pricing verification**
   - Agents must research current market pricing before changing prices. Use live sources where possible: automation agencies, n8n/Make/Zapier consultants, AI automation offers, productized service pages, Upwork/Clutch-style reference ranges if needed.
   - FlowOps pricing hypothesis: because these are productized ready automation modules, setup fees can be around **30% below comparable custom-market build pricing** while monthly support stays credible.
   - Do not frame FlowOps as cheap. Frame as "productized deployment price" / "faster because the system is pre-mapped".
   - Ensure prices still leave delivery margin. If a system is genuinely complex (voice agent, CRMOS, OpsOS, dashboard), do not force an unsafe discount.

6. **Price output per card**
   - current FlowOps setup/monthly;
   - observed market custom-build range;
   - recommended FlowOps setup/monthly after productized discount;
   - complexity tier: entry / standard / complex / custom;
   - reason for price change;
   - margin/delivery risk note.

7. **Illustration requirement**
   - Every live automation card should have a small in-card illustration.
   - Style must match existing FlowOps visuals and the reference SVGs:
     - `/Users/tamerlan/Downloads/flowops-custom-workflow.svg`
     - `/Users/tamerlan/Downloads/flowops-request-to-proof-v2_1.svg`
     - `/Users/tamerlan/Downloads/flowops-request-to-proof.svg`
   - Visual language: light blue/white canvas, soft shadows, rounded workflow nodes, dotted connector paths, small icons, subtle status chips, mint/sky/peach/amber accents, no dark SaaS dashboard clichés.
   - Illustration should show the actual workflow concept, not decorative blobs.
   - Use a compact reusable component system where possible: trigger node, AI step, action node, CRM record, notification, approval, report, calendar, phone, inbox, document, chart.

8. **Card UI content standard**
   Each marketplace card should support:
   - category;
   - name;
   - tagline;
   - richer short description;
   - best-fit vertical chips;
   - trigger/action/result mini-flow;
   - integrations;
   - setup price + monthly price;
   - deploy time;
   - one "why it matters" outcome;
   - visual/illustration key.

9. **Detail page standard**
   Each `/os/[slug]` page should include:
   - problem;
   - after-state;
   - how it works;
   - example workflow;
   - integrations;
   - setup scope;
   - monthly monitoring/support;
   - before/after owner-facing example;
   - pricing;
   - request CTA.

## Pricing Direction
The new pricing direction is not "discount everything blindly." It is:

- Start from researched market custom-build price.
- If FlowOps has a repeatable productized version, price setup roughly **30% below comparable custom build**.
- Keep monthly support aligned with operational responsibility and monitoring burden.
- If a card is too custom or risky, keep it higher or mark "custom quote".
- Stacks/bundles must be recalculated after card-level price changes.

## Visual System Notes
Card illustrations should feel like mini product diagrams:
- 3–5 small nodes max inside a card.
- Use dotted connectors and directional arrows.
- Use white cards on pale blue/mint backgrounds.
- Keep text labels short enough to fit inside small cards.
- Reuse color semantics:
  - Blue = trigger/system/action
  - Mint/green = proof/live/success
  - Peach/amber = human approval/notification
  - Slate = waiting/manual logic
  - Purple/indigo = CRM/data
- Avoid heavy gradients, stock icons, large dashboard screenshots, dark themes, and generic AI sparkles.

## Suggested Agent Workflow
1. Inventory all live and coming-soon cards from `src/lib/catalog.ts`.
2. Group by category and identify duplicates/weak cards.
3. For each card, research demand and current market price references.
4. Produce a card audit table with: keep/reposition/merge/remove, target buyer, description upgrade, price recommendation, illustration concept.
5. Update memory and get approval before mass-editing catalog prices.
6. Implement catalog copy/schema/UI updates.
7. Add/generate illustrations in one consistent component/style system.
8. Run desktop/mobile visual QA on `/os`, `/os/[slug]`, `/pricing`, `/stacks`.

## Acceptance Criteria
- Every live card has a clear buyer, pain, workflow, outcome, price rationale, and illustration.
- No card feels like a generic automation service.
- Prices are internally consistent and reflect productized deployment economics.
- Cards do not overpromise ROI or imply unsupported guarantees.
- Marketplace remains premium, not cheap/Fiverr-like.
- Visuals are consistent with the FlowOps SVG reference style.
- Roadmap, pricing memory, and catalog memory stay in sync with implementation.
