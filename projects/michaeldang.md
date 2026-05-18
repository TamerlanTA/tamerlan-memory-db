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

## Stack
- n8n
- Google Sheets
- OpenAI API
- Buffer GraphQL API

## Important Context
- Client: Michael Dang.
- Niche: premium Malta-focused advisory / luxury property / business tourism / investor relocation.
- MVP must stay simple and reliable because budget is $200.
- Buffer is the required publishing layer; avoid direct platform APIs.

## Decisions
- 2026-05-18: Use Google Sheets rather than Airtable for the MVP review queue.
- Why: cheaper, faster to hand over, and sufficient for one editorial approval flow.
- 2026-05-18: Use Buffer as the publishing layer; preferred mode is `addToQueue`, with `customScheduled` only when an exact date/time is present.
- Why: avoids direct social APIs and keeps operations inside the client's Buffer account.

## Open Tasks
- [ ] Import both workflows into the authenticated target n8n account
- [ ] Bind real Google Sheets, OpenAI, and Buffer credentials
- [ ] Paste real Buffer channel IDs into `Set Buffer Config`
- [ ] Validate Google Sheets node mappings against the live sheet
- [ ] Run live smoke tests for queue mode, custom schedule mode, and manual fallback

## Blockers
- Local n8n instance is reachable, but authenticated API access was unavailable during the 2026-05-18 pass (`/api/v1/workflows` returned 401 without `X-N8N-API-KEY`).
- Real Google Sheet ID and n8n credentials are not connected yet.
- Buffer API access / API key availability must be confirmed with the client organization owner.

## Next Steps
- Get client access and credentials.
- Import workflows into n8n.
- Test with the sample calendar row and first approved content batch.
