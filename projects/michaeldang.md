# Michael Dang

## Related
- [[agent-memory]]
- [[current-focus]]
- [[routing-rules]]

## Summary
Newly started project workspace at `/Users/tamerlan/Desktop/michaeldang`.

## Goal
Define the product clearly, choose the implementation stack, and turn the empty workspace into a working first version.

## Current Status
- 2026-05-18: Created the initial repository skeleton in `/Users/tamerlan/Desktop/michaeldang`.
- 2026-05-18: Defined the actual MVP as a lean n8n AI content workflow for Michael Dang using Google Sheets, OpenAI, and Buffer.
- Added two importable workflow drafts, review-table schema, sample calendar CSV, architecture notes, testing plan, and client handover docs.
- 2026-05-18: Performed local workflow inspection and smoke-test pass; hardened error handling and Buffer fallback behavior, added setup checklist and smoke-test report.
- 2026-05-18: Prepared last-mile implementation package: credential map, live test plan, client access request, and final delivery status.
- 2026-05-21: Updated project for Bastion & Mews real client materials: final CSV/XLSX content calendar template with 6 starter rows, brand-specific content prompt, official n8n OpenAI node in Workflow 1, LinkedIn optional/pending behavior in Workflow 2, and revised setup/test/handover docs.
- 2026-05-21: Added image-generation MVP path: expanded schema to 35 columns, Workflow 1 now outputs `image_prompt` and moves rows to `Needs Image`, new Workflow 3 generates one OpenAI image per row and stores it in Google Drive, Workflow 2 attaches `image_url` to Buffer posts where supported.
- 2026-05-21: Hardened Google Drive image URL -> Buffer asset flow: Workflow 3 now writes direct Drive download URLs, docs require incognito/public fetch test, Workflow 2 writes `buffer_instagram_status = Missing Image` when Instagram lacks `image_url`, and Buffer/media failures route to manual scheduling.
- 2026-05-21: Final live acceptance prep completed. Could not import/run workflows because local n8n API requires `X-N8N-API-KEY` and no service credentials were present. Updated smoke report, final delivery status, and handover to state blocked/not handover-ready until positive + negative live tests pass.
- 2026-05-21: Added `docs/operator-live-setup-runbook.md`, a step-by-step manual n8n setup/testing checklist covering imports, credentials, placeholders, expected red warnings, test row, run order, screenshots, and Michael delivery/support message templates.
- 2026-05-23: Added Google Apps Script at `/Users/tamerlan/Desktop/michaeldang/scripts/create-google-sheets-template.gs` to create the `content_calendar`, `settings`, and `live_test_checklist` tabs with headers, starter rows, validation dropdowns, formatting, and QA checklist.
- 2026-05-23: Fixed Workflow 1 parser after live n8n run showed OpenAI producing 6 items but parse/update only handling 1 item. `Parse and Validate JSON` now loops over all OpenAI outputs and pairs each with the matching `Filter Ready to Generate` row; OpenAI system prompt also explicitly includes `image_prompt`.
- 2026-05-23: Live n8n OpenAI node showed rate-limit error (`The service is receiving too many requests from you`) because all 6 starter rows were `Ready to Generate`. Updated CSV/XLSX/App Script so only `bm-001` starts as `Ready to Generate`; rows `bm-002`..`bm-006` start as `Draft`. Runbook now warns to test one row at a time.
- 2026-05-23: Rechecked exported live Workflow 1 (`workflows/Michael Dang - 01 Content Generation.json`) after rate-limit repeated. Found live export still had old `Filter Ready to Generate` that passed all Ready rows and old single-item parser. Patched both exported-name and canonical workflow JSON: filter now hard-limits to `MAX_ITEMS_PER_RUN = 1`, trims status, and parser handles all OpenAI outputs robustly. User still must paste/update these nodes in n8n; local JSON changes do not affect already-imported workflow automatically.
- 2026-05-23: OpenAI now succeeds and returns nested `output[0].content[0].text` containing fenced JSON. Patched `Parse and Validate JSON` locally to extract that nested path and strip ```json fences before parsing. User must paste this parser code into the live n8n node.
- 2026-05-23: Full Workflow 1 recheck with n8n testing lens found remaining fragility: OpenAI can return valid-looking JSON missing `image_prompt` / arrays as strings, causing parser to mark row `Error`. Replaced parser locally with tolerant normalizer: extracts nested OpenAI output, strips fences, recovers JSON inside extra text, converts arrays/objects to Sheet-safe strings, creates fallback `image_prompt`, only hard-fails if core copy fields are missing. Local micro-test against screenshot-like output passes to `Needs Image`.


- 2026-05-25: Patched live Workflow 3 after user switched image generation to Gemini. Latest execution `8792` failed at Google Drive upload because Gemini produced binary output under an empty binary field while Drive expected `data`. Fixed live WF3: Gemini binary output now `data`, Drive upload reads `data`, Gemini node has `operation=generate` plus `aspectRatio=1:1`, image prompt explicitly requires square 1024x1024 / no horizontal composition, Drive share uses public `reader:anyone` with `allowFileDiscovery=false`, and Sheet writes direct Drive download URL. Live WF3 validates with zero errors; next manual run must verify Drive upload, public incognito URL, and actual square output.
- 2026-05-25: Local lead-generation quality pass after `bm-0062` output was polished but commercially weak. Updated `docs/content-generation-prompt.md`, both Workflow 1 exports, and Workflow 3 image prompt prep so content must include buyer triggers, Bastion & Mews credibility, soft CTA/next step, stricter 140–190 word LinkedIn target, 35–70 word Instagram enforcement, and stronger premium editorial social-ad image prompts. Parser now flags weak commercial relevance and generic trust phrasing; Workflow 3 image prompt avoids brown/generic still-life outputs and requires a clearer readiness/inspection/arrival focal point. Local JSON and code syntax checks pass; live n8n must still be updated/imported/pasted.

## Stack
- n8n
- Google Sheets
- Google Drive
- OpenAI API
- Buffer GraphQL API

## Important Context
- Client: Michael Dang.
- Brand: Bastion & Mews.
- Niche: refined 5-star boutique stays, luxury property management in Malta, business/luxury stays, owner/investor advisory, concierge operations.
- MVP must stay simple and reliable because budget is $200.
- Buffer is the required publishing layer; avoid direct platform APIs.
- OpenAI API key was shared insecurely and must be rotated before live use; never hardcode it.
- Buffer channels: Facebook/Instagram/X connected; LinkedIn pending verification.

## Decisions
- 2026-05-18: Use Google Sheets rather than Airtable for the MVP review queue.
- Why: cheaper, faster to hand over, and sufficient for one editorial approval flow.
- 2026-05-18: Use Buffer as the publishing layer; preferred mode is `addToQueue`, with `customScheduled` only when an exact date/time is present.
- Why: avoids direct social APIs and keeps operations inside the client's Buffer account.

## Open Tasks
- [ ] 2026-05-25: Finish and improve image generation automation: run one real `Needs Image` row through Workflow 3, verify OpenAI image -> Drive upload -> public direct URL -> Sheet update, then tune image prompt / quality gate if output is still generic.
- [ ] 2026-05-25: Import/paste the latest local Workflow 1 and Workflow 3 changes into live n8n, then rerun `bm-0062` or a fresh row to verify improved lead-oriented copy and stronger image output.
- [ ] Rotate OpenAI key and create/bind n8n OpenAI credential
- [ ] Create Google Sheet from `docs/bastion-mews-content-calendar-template.csv` or `.xlsx`
- [ ] Create Google Drive folder for generated images and capture folder ID
- [ ] Import workflows 1, 2, and 3 into the authenticated target n8n account
- [ ] Bind real Google Sheets, Google Drive, OpenAI, and Buffer credentials
- [ ] Paste real Facebook/Instagram/X Buffer channel IDs into `Set Buffer Config`; leave LinkedIn blank until verified
- [ ] Run first live test: 1 row through content -> image -> review -> Buffer, then expand to 3 generated rows

## Blockers
- Local n8n instance is reachable, but authenticated API access was unavailable during the 2026-05-18 pass (`/api/v1/workflows` returned 401 without `X-N8N-API-KEY`).
- Real Google Sheet ID, Google Drive folder ID, and n8n credentials are not connected yet.
- Buffer API access / API key availability must be confirmed with the client organization owner.
- Live import/execution remains untested because authenticated target n8n access and real service credentials are still missing.

## Next Steps
- Get client access and credentials.
- Import workflows into n8n.
- Test with the sample calendar row and first approved content batch.
- 2026-05-23: Quality hardening pass for Workflow 1 after live output sounded generic/salesy. Updated `docs/content-generation-prompt.md` and both Workflow 1 JSON exports with stricter Bastion & Mews voice, forbidden weak phrases, platform-specific rules, stronger image prompt requirements, `quality_flags`, and a parser-level quality gate that caps `quality_score` below 75 when forbidden phrases, generic hashtags, weak specificity, or LinkedIn/Instagram fit issues appear. Added `quality_flags` to CSV/XLSX/App Script schema and documented test rows/good-output expectations in workflow notes and smoke report.
- 2026-05-24: Second content-quality hardening pass after output still sounded like Malta travel/hotel brochure copy. Updated Workflow 1 prompt and parser gate to prohibit generic tourism language (`Malta’s unique blend`, `ideal destination`, `business and leisure`, `stunning views`, `rich cultural tapestry`, `Mediterranean pace`, etc.), reframe Bastion & Mews as a discreet premium residence operator, require operational/advisory insight in every post, require expert-observation → why-it-matters → concrete-details → calm-conclusion structure, and add `generic_tourism_language` flag capped at `quality_score <= 70`. Locally simulated bad vs good framing; bad tourism copy is flagged, good operational business-stay framing passes.
- 2026-05-24: Third content-quality pass after output became too SOP/checklist-like and images too generic. Updated Workflow 1 prompt and parser to require editorial operator prose rather than default bullets/numbered lists, added `checklist_tone` and `generic_image_prompt` quality flags, strengthened Instagram style toward short atmospheric operational lines, and required image prompts to show a preparation/operational moment (writing desk, itinerary card with no readable text, key/card, water glass, folded linen, quiet workspace, Malta limestone/heritage detail, natural light) rather than generic hotel/interior scenes. Local simulation confirms checklist/SOP copy and generic image prompts are flagged while editorial business-stay framing passes.
- 2026-05-24: Live n8n MCP patch completed for image-generation failure and image-quality direction. Workflow 3 (`izx5FsKxTOdGJsVB`) was failing because live OpenAI image node was underconfigured, Drive upload/share nodes were misconfigured, and Sheet update used the wrong update mode. Patched live Workflow 3: `gpt-image-1` image generation with binary `data`, Drive upload, public `reader:anyone` share, direct row `appendOrUpdate` by `id`, and stronger editorial/operational still-life prompt builder. Patched live Workflow 1 (`6DwmwIbWgFholDMr`): replaced deprecated OpenAI `continueOnFail`, strengthened image prompt rules, and refreshed Google Sheets schema to keep `quality_flags` / `improvement_notes` aligned. Both workflows validate with zero errors; remaining warnings are non-blocking. Next: manually run one real `Needs Image` row through Workflow 3 and verify Drive URL opens publicly.
- 2026-05-24: Attempted MCP-only execution testing for WF1 and WF3. n8n MCP cannot trigger Manual/Schedule-only workflows directly; temporarily added a webhook to WF1 for testing, but n8n Cloud blocked execution at trigger with `Execution limit reached`. Removed temporary webhook and deactivated WF1. WF1 and WF3 still validate with zero errors. Current blocker: n8n Cloud execution quota/plan limit must be cleared before real live tests can continue.
- 2026-05-24: Diagnosed WF3 latest execution `8522`: workflow showed success but skipped OpenAI because row `bm-005` had stale `image_status = Image Error`; `IF Image Prompt Valid` checked image_status and routed to error branch. Earlier `8521` failed on stale Google Sheets schema. Patched WF3 live: filter skips stale Image Error rows unless manually reset to `Ready to Generate`, prompt prep runs per item, IF checks `final_image_prompt`, OpenAI image node restored to `operation=generate` with binary output `data`, Drive upload/share restored, and WF3 validates with zero errors.
- 2026-05-24: Diagnosed WF3 execution `8524`: OpenAI image generation and Drive upload succeeded, but `Share Drive File` failed with Google Drive 400 because permission payload had empty `role/type`. Patched live share node to `reader:anyone`. Also reverted Drive upload `name` to simple expression string because resource-locator format caused uploaded files to be named `Untitled` at runtime. WF3 validates with zero errors; one non-blocking filename warning remains by design.
- 2026-05-24: Resolved recurring WF3 Share Drive File issue root cause. n8n Google Drive node validator accepted `permissionsValues` as an array, but this n8n runtime expects object shape; array patches normalized to empty `role/type`, causing repeated Google Drive 400 errors. Patched live WF3 to `permissionsUi.permissionsValues = { role: "reader", type: "anyone" }` and restored complete OpenAI image/upload params. Verified live workflow stores the corrected object shape and validates with zero errors. Keep upload filename as simple expression despite warning because resource-locator format caused `Untitled` files at runtime.
