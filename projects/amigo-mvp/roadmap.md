c# AMIGO MVP — Roadmap

## Related
- [[overview]]
- [[current-state]]
- [[decisions]]
- [[risks]]
- [[next-steps]]
- [[technical-architecture]]

## Phase 1 — Foundation, 12–14 June
Goal: deployable backend foundation.

Deliverables:
- monorepo, CI, development and staging environments;
- database schema, RLS, private storage, audit log;
- Telegram webhook, manager authorization, health commands;
- PGMQ queues, cron schedules, worker contracts;
- employer catalog schema and initial import format.

Acceptance:
- migrations run from zero;
- unauthorized Telegram users are rejected;
- a queued test job is processed once and audited;
- private candidate file cannot be accessed without a signed URL.

## Phase 2 — Candidate intake, 15–18 June
Goal: manager can create a complete candidate record in Telegram.

Deliverables:
- resumable Russian intake;
- candidate ownership and search;
- preferences, experience, languages, visa, relocation, and answer bank;
- source-document upload and consent record;
- profile completeness and validation report.

Acceptance:
- interrupted intake resumes at the correct field;
- manager can edit any section without restarting;
- required missing data blocks document generation.

## Phase 3 — Document pipeline, 19–21 June
Goal: approved English DOCX/PDF package.

Deliverables:
- structured translation/generation prompt;
- source-field grounding and validation;
- versioned CV template;
- Docxtemplater generation and Gotenberg PDF conversion;
- approve, reject, and regenerate actions.

Acceptance:
- every generated statement maps to stored facts;
- manager approval activates exactly one document version;
- old application records preserve their original document version.

## Phase 4 — Vacancy ingestion, 22–25 June
Goal: normalized current vacancy inventory.

Deliverables:
- curated catalog of 100–200 employers;
- Greenhouse-read, Lever-read, and generic feed connectors;
- first certified hospitality enterprise-site connector;
- normalization, deduplication, expiry, and connector health.

Acceptance:
- repeated runs create no duplicate vacancies;
- removed/expired roles stop entering new batches;
- connector failures produce alerts without blocking other employers.

## Phase 5 — Matching and approval, 26–28 June
Goal: deterministic daily vacancy batches.

Deliverables:
- role taxonomy and synonym dictionaries;
- hard filters;
- weighted score and explanation;
- daily 5–10 vacancy batch plus reserves;
- batch approve/reject Telegram actions.

Acceptance:
- identical inputs produce identical scores;
- hard-filter failures cannot be approved accidentally;
- prior applications and employer blacklists are excluded.

## Phase 6 — Applications and reporting, 29 June–2 July
Goal: supported applications execute and produce evidence.

Deliverables:
- adapter SDK and first certified adapters;
- email apply;
- domain rate limits, retries, idempotency;
- `NeedsAction` workflow;
- manager and candidate daily reports.

Acceptance:
- all attempts reach a known state;
- successful applications have confirmation evidence;
- transient failures retry with backoff;
- CAPTCHA and OTP never trigger automated bypass.

## Phase 7 — Pilot QA, 3–4 July
Goal: safe launch readiness for 10 candidates.

Deliverables:
- full E2E and failure-injection tests;
- 10 complete candidate profiles;
- at least 50 real or controlled application attempts;
- security, retention, restore, and queue recovery tests;
- P0/P1 defect closure.

Acceptance:
- no duplicate applications;
- no ungrounded document facts;
- at least 90% of attempts are classified correctly;
- launch blockers in [[risks]] are cleared.

## Phase 8 — Controlled launch, 5 July
Goal: activate 10 candidates.

Operations:
- stagger candidate batch times;
- monitor queue lag, connector failures, and domain responses;
- hold unsupported connectors disabled;
- publish launch review and 30-candidate go/no-go.

## Phase 9 — Scale to 30, 6–12 July
Goal: activate the waitlist without architectural changes.

Deliverables:
- browser worker concurrency tuning;
- domain backpressure and proxy decision;
- 300-attempt/day load test;
- additional certified employer adapters;
- manager SLA for `NeedsAction`;
- operations dashboard specification if Telegram limits are reached.

