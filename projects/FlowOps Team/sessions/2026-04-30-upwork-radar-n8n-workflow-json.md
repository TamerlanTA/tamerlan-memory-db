# Session 2026-04-30 - Upwork Radar n8n Workflow JSON

## Related
- [[../00 - Overview]]
- [[../03 - Pipelines/Pipeline A — Upwork Radar]]
- [[../03 - Acquisition Pipelines/Pipeline A — Upwork Radar]]
- [[../05 - CRM Structure/CRM Tables]]

## What was done
- Created importable n8n workflow JSON at `/Users/tamerlan/Desktop/flowopsteamPipelines/upwork-radar-workflow.json`.
- Workflow implements Gmail Upwork `New job alert` trigger -> URL extraction -> Google Sheets dedup -> Firecrawl scrape -> OpenAI scoring -> OpenAI proposal generation -> proposal validation -> Telegram send -> Google Sheets append.
- Added placeholders only: Gmail, Firecrawl, OpenAI HTTP Header Auth, Telegram, Google Sheets, Sheet ID, Telegram chat ID.
- Updated OpenAI scoring and proposal nodes from generic HTTP Request nodes to official n8n OpenAI nodes: `@n8n/n8n-nodes-langchain.openAi`, resource `text`, operation `message`, `jsonOutput: true`.
- Strengthened `OpenAI Generate Proposal` prompt with the full operational proposal rules and expanded `Validate Proposal` into a deterministic gate for closing block order, word counts, specialist positioning, banned phrases, markdown symbols, concrete timeline, concrete budget, generic questions, and signature.
- Rebuilt proposal prompt around FlowOps positioning adapted for Upwork solo-freelancer positioning: first-person Tamerlan, no agency/team language, business outcomes over tools, offer mapping to Speed-to-Lead / Ops Automation Sprint / AI Chatbot.
- Updated Telegram output to send only `proposal_full` inside an HTML `<pre>` block for copy-friendly Telegram behavior. Short version and one-liner are no longer generated for Telegram.
- Fixed proposal validator false positive where banned phrase `our team` matched client-facing phrase `your team`; banned phrases now use regex boundaries. Prompt now explicitly requires a specialist phrase in the relevance paragraph.
- Relaxed `Validate Proposal` formatting checks after live n8n error: closing block now tolerates harmless whitespace variations while preserving required order/signature/link, and markdown detection only flags markdown markers at line starts or bold markers instead of any `>` character.
- Updated Telegram message format again: plain metadata first (`Score`, `Title`, `Budget`, `Connects`, `URL`), followed by only the full proposal inside an HTML `<pre>` block for easy copying.
- Fixed another live `Validate Proposal` false negative for timeline detection. Validator now accepts numeric durations, word-number durations (`two weeks`), timeline phrases like `within/about/around/complete/deliver`, and calendar dates. Prompt now asks the model to use exact `Estimated time: X days/weeks` wording.
- Fixed `Invalid regular expression flags` in `Validate Proposal` by removing unsupported/dangerous regex literal patterns and converting the calendar-date check to `new RegExp(...)`; local `node --check` now passes for the validator code.
- Added `Quiet Hours Gate` after Gmail Trigger. It stops processing between 02:00 and 09:00 Asia/Almaty by returning no items.
- Reworked proposal prompt for conversion/readability after live output felt too dense. New structure is preview-first: standalone greeting, short hook max 22 words, short relevance paragraph, exactly 3 compact bullets, `Estimated time:` line, `Investment:` line, then required closing. Validator now accepts 95-170 body words and enforces first content paragraph <=22 words.
- After live validation was too strict, moved proposal body word count and first-paragraph length checks from hard errors to `proposal_quality_warnings`. Hard validation now focuses on critical rules only, while prompt still asks for a separate hook paragraph and lighter 95-170 word body.

## Key findings
- The local workspace folder was empty before this workflow file was created.
- Existing memory already defined this as FlowOps Team Pipeline A - Upwork Radar, so no new project folder was created.
- Firecrawl community node is used as requested: `@mendable/n8n-nodes-firecrawl.firecrawl`.
- OpenAI now uses official n8n OpenAI credentials via `openAiApi` with placeholder `REPLACE_WITH_OPENAI_CREDENTIAL_ID`.
- Proposal compliance is enforced by validation after generation. If the model drifts, the workflow stops before Telegram/Sheets instead of treating the draft as ready.
- External Upwork proposal research reinforced: strong first lines, personalization, client-problem focus, relevant proof, concise/scannable copy, hidden-instruction compliance, and clear CTA/question.

## Blockers
- Workflow was JSON-validated locally, but not imported into a live n8n instance yet.
- User must configure credentials, `REPLACE_WITH_GOOGLE_SHEET_ID`, `REPLACE_WITH_TELEGRAM_CHAT_ID`, and create the `Upwork Radar` sheet columns.
- If n8n does not have the Firecrawl community node installed, replace it with HTTP Request `POST https://api.firecrawl.dev/v2/scrape`.

## Next steps
- Import `upwork-radar-workflow.json` into n8n.
- Set credentials and placeholders.
- Run manual test with a real Upwork Gmail alert.
- Confirm Google Sheets dedup and append behavior.
- Confirm proposal validation does not reject good drafts too aggressively.
- If validation is too strict in live runs, tune the deterministic `Validate Proposal` Code node rather than weakening the proposal prompt.
- Test Telegram rendering on mobile/desktop and confirm the `<pre>` block copy action copies only the full proposal.
- Re-import the workflow JSON or manually update the `OpenAI Generate Proposal` prompt and `Validate Proposal` Code node in n8n after validator changes.
- Important: the current quiet-hours gate skips items during 02:00-09:00. If jobs from that window must be processed after 09:00 instead of skipped, redesign trigger as scheduled Gmail search + dedup rather than Gmail Trigger + drop gate.
