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
