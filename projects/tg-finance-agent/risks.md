# TG Finance Agent — Risks

## Related
- [[overview]]
- [[current-state]]
- [[decisions]]
- [[next-steps]]

## Content
## Open Risks
- Real Kaspi PDF parser is improved for the tested file, but parser quality still needs manual review row-by-row across more statement layouts.
- Rules currently encode starter assumptions only; user-specific people/merchant mappings still need to be learned.
- Storage backend is still local JSON/Railway volume; this is acceptable for MVP but should move to SQLite/Supabase before multi-user or high-concurrency use.
- Need to verify how Kaspi Russian statement text represents internal transfers, ATM operations, refunds, fees, and card-to-card transfers in real PDFs.
- Current parser uses text heuristics rather than visual table coordinates; some Kaspi PDF table layouts may require table extraction or layout-aware parsing.
- Categorization rules are still starter heuristics and need validation on real monthly spending.
- `add-rule` persists learned rules to JSON; concurrent Telegram usage later will need safer storage/locking or a database.
- AI-assisted categorization is only a placeholder and intentionally returns no suggestions yet.
- Reporting has only been validated on synthetic sample data; real Kaspi months may expose edge cases in income source grouping, recurring detection, and unusual spike detection.
- Historical trend chart is implemented only when historical summaries are provided by future storage.
- Telegram bot is deployed on Railway and token is valid, but the full user flow has not been manually tested in Telegram by Tamerlan.
- Custom review button was removed and replaced with broader category buttons; expanded review UX needs live Telegram validation after the latest deployment.
- `/forgetrule` currently explains manual JSON editing; actual rule deletion is not implemented.
- n8n workflow JSON has not been imported or tested in a live n8n instance.
- Reminder CLI uses local JSON state; multi-device/server deployments will need Supabase/SQLite or another shared store.
- HTTP webhook endpoints are implemented as reusable handler contracts, not as a running HTTP server yet.
- Railway deployment exists and uses production `start` script plus `/data` volume, but needs live PDF upload validation.
- Current n8n sample uses local Execute Command; this is not suitable if the app is deployed on Railway and n8n runs elsewhere. For Railway, expose actual HTTP endpoints or run n8n in the same reachable environment.
- Real PDF categorization still produces many review items and 0 confirmed real income; PayPal/Upwork is now surfaced as probable income, but rules need user confirmation before reports are fully accurate.
- AI report/Q&A is deployed and OpenAI key is smoke-tested; the latest real Telegram PDF -> AI report flow still needs validation after parser/report fixes.
- AI analysis can improve interpretation, but deterministic extracted transaction quality and user-trained rules still matter.
- Railway logs still show npm warning `production Use --omit=dev instead`; it is non-blocking, but can be cleaned up later if desired.
- `/forgetme` resets runtime learned rules globally for the MVP, which is fine for single-user testing but should become per-user rule deletion before multi-user use.
