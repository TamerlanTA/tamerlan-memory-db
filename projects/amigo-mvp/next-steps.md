# AMIGO MVP — Next Steps

## Related
- [[overview]]
- [[current-state]]
- [[risks]]
- [[decisions]]
- [[roadmap]]
- [[technical-architecture]]
- [[phase-5-execution-plan]]
- [[phase-6-execution-plan]]

## P0 — 2026-06-12 to 2026-06-14
Completed on 2026-06-15:
1. Application repository created and linked.
2. Supabase and Railway production foundation provisioned.
3. TypeScript/pnpm monorepo and CI initialized.
4. First Drizzle schema and SQL migration implemented.
5. RLS baseline and append-oriented audit logging implemented.
6. grammY webhook and manager allowlist deployed.
7. PGMQ queue and worker health processing verified.
8. Employer catalog CSV import format prepared.

## P1 — Intake ✅ COMPLETE (2026-06-16, commit d1bf79d)
- `/candidate_new`, `/candidate_find`, `/candidate_view`, `/candidate_edit`, `/candidate_close`, `/cancel` all functional
- 25-field form with age, gender, race, English level, education year, height, weight, 9 boolean experience flags
- Languages (CEFR) collected in intake and editable
- Profile completeness check implemented (`profile.ts:checkCompleteness`)
- 34 tests passing, deployed on Railway, Supabase migration applied

## P2 — Documents ✅ COMPLETE (closed 2026-06-22)
Completed foundation:
1. `worker-documents` service implemented and deployed.
2. OpenAI structured extraction path implemented with deterministic fallback mode.
3. DOCX render, Gotenberg PDF render, private Supabase Storage upload, and generation audit implemented.
4. Telegram `/candidate_documents` flow implemented with signed PDF link and approve/reject callbacks.
5. Document schema, storage bucket, and `document_generate` queue applied to production.
6. CV template/content quality upgrade completed and deployed in commit `a11145b`.
7. Controlled candidate regenerated with improved CV version `9219995e-fed0-407c-a27f-f5ee3493cd71`; status is `pending_approval`, validation errors are empty, and PDF text extraction passed.
8. Manager approval callback was verified in Telegram: document version `9219995e-fed0-407c-a27f-f5ee3493cd71` became `approved`, and candidate status became `documents`.

Residual follow-up:
1. Business/legal owner still needs to formally approve consent text v1-ru-2026-06 before pilot scale.
2. Use the new `/candidate_experience`, `/candidate_education`, `/candidate_extra`, and `/candidate_photo` flows to enrich real pilot candidates before regenerating CVs.
3. Re-upload any unsupported WebP portrait photos as JPEG/PNG when the generated CV shows `PHOTO UPLOADED - EMBEDDING FAILED`; JPEG/PNG embedding is implemented.
4. Optional: approve the latest corrected sample CV version `c20ddaa5-15a7-4aa9-9314-8db68adec1ab` or reject it after visual review.

## Phase 3.5 — CV Enrichment ✅ COMPLETE (2026-06-22, commit 3a7bd48)
Completed:
1. Added production tables for candidate photos, work experience, education, and CV extras.
2. Added Telegram manager commands `/candidate_photo`, `/candidate_experience`, `/candidate_education`, and `/candidate_extra`.
3. Updated `/candidate_view` with CV readiness warnings.
4. Updated `worker-documents` to load structured enrichment data and keep generated CVs grounded.
5. Added runbook `docs/cv-enrichment-runbook.md`.
6. Applied Supabase migration, deployed `bot-api` and `worker-documents`, refreshed Telegram webhook, and pushed commit `3a7bd48`.

Manual remaining:
1. Add real enrichment data for each pilot candidate through Telegram.
2. Regenerate and approve each enriched CV.
3. Review final portrait crop/quality in generated PDFs before approval.
4. Review and approve or reject production sample `84e1f6bf-fe95-40c8-b294-4e6e9588d3a8`.
5. Review and approve or reject compact-header production sample `689f61c4-ff82-426b-97fe-b44a7072939d`.

## Unified Candidate Onboarding ✅ DEPLOYED (2026-06-24, commit 8145245)
Completed:
1. `/candidate_new` continues after consent through experience, education, extras, portrait, and final review.
2. Repeatable add-another loops and explicit skip/no-experience paths are implemented.
3. Re-running `/candidate_new` resumes the same durable session without creating another candidate.
4. Optional separate WhatsApp is stored and used in generated CVs.
5. Standalone enrichment commands remain available.
6. Production migration, Supabase advisors, Railway deployments, webhook, and `/health` passed.

Manual remaining:
1. Continue the existing production `awaiting_form` session by sending `/candidate_new`.
2. Complete one candidate with one experience, education, extra, and portrait.
3. Confirm `/candidate_view`, regenerate the CV, and inspect all collected data.
4. Run separate skip-photo, no-experience, and `/cancel` acceptance checks.
5. For manager `935784686`, resend the same HEIC/HEIF portrait document; native conversion is deployed and the session is still waiting at `cv_photo_upload`.
6. Rotate the Telegram bot token through BotFather because the old token appeared in historical Railway error logs, update Railway, and refresh the webhook.

## P0 — Phase 2 review remediation ✅ COMPLETE (commit e5ad6e4)
1. ✅ Non-closed filter moved to SQL WHERE in edit.ts and close.ts
2. ✅ handleCloseConfirm verifies candidateId + assignedManagerId + status != closed before UPDATE
3. ✅ Location validation already fixed in steps.ts rewrite (city.length < 1 check)

## P1 — Search and matching
Completed foundation:
1. Added employer catalog source columns and production migration `202606220001`.
2. Added idempotent catalog importer `scripts/import-employer-catalog.ts`.
3. Seeded 25 hospitality employers / career sources into production (`data/employer-catalog.seed.csv`).
4. Added normalized vacancy discovery schema in migration `202606220002`: `source_runs` and `vacancies`.
5. Added first read-only vacancy discovery vertical slice in `@amigo/vacancy-discovery`.
6. Implemented `successfactors-v1` connector for Kerzner public SuccessFactors search pages.
7. Implemented idempotent vacancy upsert by `vacancies.dedupe_key`, source run success/failure lifecycle, minimal stale marking, CLI runner, and `/source_health`.
8. Production Kerzner verification on 2026-06-26: two successful runs, 15 vacancy rows, 15 distinct dedupe keys, preserved `first_seen_at`, updated `last_seen_at`.
9. Added Phase 4B scheduled discovery path, overlap protection, error taxonomy, richer source health, `worker-vacancy-discovery`, and runbook.
10. Production connector verification on 2026-06-26: Atlantis Dubai succeeded with 3 active vacancies, Kerzner succeeded with 15 active vacancies, One&Only failed safely as `empty_result`; total `vacancies=18`, distinct `dedupe_key=18`.
11. Implemented Phase 5 locally on 2026-06-28 following [[phase-5-execution-plan]]:
    - matching schema migration draft;
    - `@amigo/matching` package;
    - hard filters, weighted scoring, explanations, duplicate suppression, daily batch preparation;
    - Telegram `/candidate_batch` review with item/whole-batch approve/reject;
    - no application submission from Phase 5;
    - full local validation passed: `pnpm check`, `pnpm test`, `pnpm build`, `pnpm format:check`.
12. Applied Supabase remote migration `202606280001` successfully on 2026-06-28; `supabase migration list` shows local and remote in sync for this migration.
13. Deployed `bot-api` with Phase 5 `/candidate_batch` on Railway after fixing Docker workspace package copying and `@amigo/matching` runtime exports.
14. Production Phase 5 data acceptance passed for candidate `61ac04f1-b04c-4f35-a324-0a8c99182109`: batch `c7c7fcb1-58a3-4f0a-bc24-e66eb8906877`, strict final result 6 primary vacancies, duplicate suppression OK, item approve/reject verified, no application submission.
15. Added regression coverage for Russian target country aliases and ISO vacancy country codes after production data revealed false `country_mismatch`.
16. Strict plan re-audit on 2026-06-28 fixed pending-batch regeneration safety: re-running prepare for an existing `pending_approval` batch preserves existing item decisions. Production verification confirmed the already approved/rejected items in batch `c7c7fcb1-58a3-4f0a-bc24-e66eb8906877` remained unchanged.
17. Strict plan re-audit on 2026-06-28 fixed role-family hard filtering: unknown non-target roles now fail unless the title explicitly contains a target role, broad F&B markers no longer make kitchen/host/stewarding roles approvable, and the production acceptance batch was regenerated to 6 strict primary items with shortage `eligible_vacancy_shortage:6/10`.

18. Manual Telegram click-through on 2026-06-29 found and fixed callback handling for `/candidate_batch`: callbacks were reaching production, but old/retried callback query ids and Markdown parsing failures made the buttons appear unresponsive. `bot-api` redeployed with safe early callback answers and plain-text batch summaries.
19. Tamerlan retried `/candidate_batch` after the fix; the button worked and the 2026-06-29 batch became `approved` with 6 strict primary vacancies and shortage `eligible_vacancy_shortage:6/10`.
20. Candidate Юля Иванова Иванов (`ресепшионист`, target countries ОАЭ/Катар/Бахрейн) returned `0/10`. Production diagnosis showed no active front-office/receptionist vacancies in target countries in the current catalog. Russian receptionist aliases were added to front-office taxonomy so future matching is correct, but the current shortage remains real until the catalog includes receptionist/front-office vacancies in UAE/Qatar/Bahrain or the candidate's target roles/countries are widened.
21. Vacancy discovery coverage was expanded on 2026-06-30 by adding `workday-v1` and enabling it in `worker-vacancy-discovery` alongside `successfactors-v1`. Four Seasons Workday produced 100 active/upserted vacancies; production reached 345 total vacancies, 200 active, 145 stale, and 221 distinct apply URLs.
22. All seeded discovery sources were activated on 2026-06-30. `worker-vacancy-discovery` now runs all connector ids (`successfactors-v1`, `workday-v1`, `marriott-careers-v1`, `accor-careers-v1`, `oracle-cx-v1`, `taleo-v1`, `ihg-careers-v1`, `generic-careers-v1`) and logs `checkedSourceCount=31`. Production totals after manual discovery are 533 vacancies, 388 active, 145 stale, and 399 distinct apply URLs.
23. `/approved_vacancies` was added and deployed on 2026-06-30 to show approved vacancies per candidate and flag duplicate approved `vacancy_id` values across approved/partially approved batches.
24. Phase 5 batch preparation timeout found in production logs was fixed and deployed on 2026-06-30: `persistPreparedBatch()` now persists only primary/reserve approvable scores, not every rejected vacancy score, so large active catalogs do not cause statement timeouts while creating a manager-facing batch.
25. `/ops_status` was added and deployed on 2026-07-01 as the compact real-time operations command: sources, active/total vacancies, distinct active apply URLs, new/refreshed vacancies today, source runs, connector breakdown, and latest failed sources.
26. 2026-07-01 shortage diagnosis confirmed that `0/10` candidate batches can be real under current hard filters: production had 386 active vacancies overall, but 0 active Qatar/Doha vacancies for `официант + Катар` and 0 active Gulf receptionist/front-office matches for `ресепшионист + ОАЭ/Катар/Бахрейн`.

Next:
1. Follow [[phase-6-execution-plan]] exactly. Batch 0 audit through Batch 8 QA/production readiness are locally complete.
2. Phase 6 migrations `202606300001_phase6_applications.sql` and `202607010001_manual_actions_open_unique.sql` are applied to production; direct DB verification confirms tables, queues, queue depth 0, and 0 duplicate open manual-action groups.
3. `bot-api` deployment `2e2d57e5-a522-42ab-9073-e99eb452904e` and `worker-applications` deployment `c501d034-40a9-4a50-b928-1bc50032e732` are live on Railway.
4. Controlled production handoff on batch `7c580a24-8e0e-4b1a-b22a-0e0999e09869` created 4 application jobs/manual tasks; 2 stale vacancies were safely skipped; re-run created 0 duplicate apps.
5. Manual Telegram evidence acceptance is complete for manual deep-link mode: production has 8 `applied` applications and 8 `manual_confirmation` evidence rows. Continue using `/application_report` during pilot operations.
6. Rotate the Railway token shared in chat after deploy verification.
7. Before any production auto-submit, wire `email-apply-v1` to an explicitly configured email sender/source-level enable flag, verify duplicate prevention/rate limits, and record one controlled submission or approved dry-run evidence.
7. Manually test `/approved_vacancies` in Telegram, then use its duplicate report before Phase 6 production handoff.
8. Confirm product/business approval for current scoring strictness and shortage behavior (`6/10` primary for the first accepted candidate).
9. Keep the original One&Only umbrella endpoint visible as `empty_result` until a stable umbrella URL is found.
10. Continue expanding employer catalog from 31 toward 100 approved brands after scoring/matching safety rules are live.
11. Certify and harden the newly activated best-effort sources: replace fragile HTML parsing with dedicated APIs/parsers where available, especially Rixos/Accor 404, Jumeirah Oracle CX empty result, IHG network failures, and generic sources blocked by 403/410.
12. Improve location extraction for best-effort generic vacancies so matching can safely use more of the newly ingested rows instead of relying only on title/apply URL.
13. Rotate secrets exposed in operational logs/chats: at minimum Railway token and Telegram bot token; review OpenAI and Supabase service-role keys as well.
14. Use `/ops_status` during daily operations before interpreting `0/10` batches; if totals are healthy but a candidate returns `0/10`, inspect the candidate's exact role+country intersection before relaxing filters.
15. Expand or repair sources specifically for Qatar/Bahrain and front-office/waiter roles before expecting narrow candidates to consistently receive 5-10 eligible vacancies.
16. Source expansion from 31 to 85 is production-deployed. Monitor `worker-vacancy-discovery` logs and `/ops_status`; the scheduler now reports `checkedSourceCount=85`.
17. Re-run `/candidate_supply` and `/candidate_batch` in Telegram after the 85-source expansion:
    - expected now: Юля Иванова Иванов 10 primary + 10 reserve;
    - Жанибек Иванов 10 primary + 10 reserve;
    - Тамерлан Тог 1 strict primary + 10 reserve after today's already-approved вакансии are excluded.
18. Decide product policy for the daily minimum: count approved reserve items toward the 5/day target, or require 5 strict primary items. If strict primary is required for narrow Qatar-only waiter candidates, either widen target countries/roles or add more Qatar-specific source/API coverage.
19. Clean up source health: replace or disable generic sources returning 403/404/410/empty results, and prefer dedicated API/connectors over generic HTML parsing.
20. Add guardrails for query-level sources: review location inference and avoid over-trusting broad Workday/Marriott/Accor query labels when individual vacancy location conflicts with the query.
21. Rotate the temporary Railway token shared in chat after deploy verification.
22. Re-test `/candidate_batch` and `/application_handoff`; repeated identical messages should stop after the `update_id` dedupe/webhook-timeout fix.
23. Start pilot operations for the first 2-3 real candidates: daily `/candidate_supply`, `/candidate_batch`, manager approval, `/application_handoff`, `/manual_actions`, `/application_report`.
24. Next automation layer decision is recorded in [[decisions]] as D-018: build certification-gated `email-apply-v1`/adapter readiness first, with dry-run/feature-flag runtime support and adapter eligibility reporting; do not enable live sending until source-level enablement, sender configuration, rate limits, duplicate prevention, and controlled evidence review are complete.
25. Before implementing live `email-apply-v1`, find or add real mailto/email-apply sources; production check on 2026-07-03 found 0 active `mailto:` vacancies and all 85 sources have `application_adapter = null`.
26. `email-apply-v1` dry-run worker support and `/adapter_eligibility` are implemented and deployed. Use `/adapter_eligibility` after approving a batch to inspect manual/email/future-adapter split before handoff.
27. Workday preflight foundation is implemented locally:
    - `workday-form-v1` supports `*.myworkdayjobs.com`;
    - it requires `runtime.htmlSnapshot`;
    - it stops on CAPTCHA/OTP/login/account creation/assessment/video/unknown required fields;
    - it hashes preflight evidence and never live-submits;
    - `/adapter_eligibility` now reports Workday approved items as `preflight-capable`.
28. Next safe automation step: add a browser preflight worker for Workday/Four Seasons:
    - open the approved apply URL in a controlled browser session;
    - capture sanitized HTML snapshot/screenshot evidence;
    - run `workday-form-v1` classification;
    - store evidence and route each application to `ready_for_autofill` or manual `NeedsAction`;
    - keep submit disabled.
29. After browser preflight is accepted, add Workday dry-run autofill for one allowlisted Four Seasons source:
    - fill only mapped/stored candidate fields;
    - upload the approved CV;
    - pause before submit;
    - capture evidence for manager review.
30. Only after one controlled manager-reviewed Workday dry-run and one controlled live submission, consider live Workday submit behind source allowlist, per-domain daily caps, duplicate checks, and explicit runtime flag.
31. Parallel safe automation step: source-quality/adapter targeting pass for email-capable sources:
    - find real hospitality sources with `mailto:` or explicit email-apply instructions;
    - mark only those sources with `application_adapter = email-apply-v1`;
    - run one dry-run handoff and verify `confirmation_text_hash` evidence plus manual action;
    - only after review, wire a real sender behind explicit env flag and source allowlist.

## P1 — Applications and reports
1. Define the adapter SDK and fixture contract.
2. Certify the first hosted-form adapters.
3. Implement email apply.
4. Add `NeedsAction` handling for CAPTCHA, OTP, assessments, and unknown questions.
5. Store confirmation evidence and send daily manager/candidate reports.

## Required owner inputs
- Telegram bot and initial manager ID: provided and configured.
- Supabase, Railway, and OpenAI: provided/provisioned and configured.
- Hospitality CV template: draft v1 created; team approval still required.
- Employer catalog: Codex is authorized to assemble the first 100 target brands.
- Candidate consent: draft v1 created; business/legal approval and privacy contact still required.

## Immediate execution order
1. Complete the unified `/candidate_new` manual Telegram acceptance pass.
2. Collect/enrich pilot candidate CV facts through unified onboarding or standalone Phase 3.5 commands.
3. Run `/candidate_batch` manually in Telegram for UX acceptance, then decide whether to close the existing pending batch or regenerate.
4. Continue monitoring `worker-vacancy-discovery` scheduled runs and `/source_health` as the source count grows.
5. Continue expanding employer catalog from 31 toward 100 approved brands.

## Two-person working split
- **Tamerlan:** approve business rules, provide or create service accounts and secrets, approve the CV template, consent text, target employer scope, and pilot candidates.
- **Codex:** initialize and implement the repository, database, bot, workers, tests, CI, documentation, and project-memory updates.
- **Joint checkpoints:** approve schema before production migration, approve the first end-to-end candidate flow, certify application adapters, and make the July 5 launch decision.
