# AMIGO MVP — Phase 6 Execution Plan

## Related
- [[overview]]
- [[current-state]]
- [[decisions]]
- [[risks]]
- [[next-steps]]
- [[roadmap]]
- [[technical-architecture]]
- [[data-model]]
- [[integrations]]
- [[phase-5-execution-plan]]
- [[prompts]]

## Status
- Phase: Phase 6 — Applications and reporting
- Plan status: Canonical execution plan
- Created: 2026-06-30
- Rule: Future Phase 6 implementation must follow this plan in order unless Tamerlan explicitly changes the plan or a verified blocker requires a documented deviation in [[decisions]] or a session note before continuing.

## Goal
Turn Phase 5 approved or partially approved batch items into controlled application execution with duplicate prevention, explicit job states, evidence capture, manager-facing manual actions, and daily reporting.

Phase 6 is the application execution layer. It may include auto-apply only for certified, narrow, tested flows. Unsupported, risky, blocked, or ambiguous flows must become `NeedsAction` / manual deep-link tasks rather than guessed or forced submissions.

## Current Verified Context
- Phase 5 is production deployed and accepted for deterministic matching and Telegram approval.
- Phase 5 currently stops at approved or partially approved batches; it does not submit applications.
- Existing queue names already include `application.submit`, `application.manual_action`, and `report.daily`.
- Existing architecture defines `worker-applications`, `worker-reporting`, and `packages/application-adapters`, but they are not implemented/certified yet.
- Existing reliability rule: application idempotency key is `candidate_id + vacancy_id + document_version_id`.
- Existing product boundary: applications begin only after manager approval.
- Existing safety rule: CAPTCHA, OTP, assessments, account creation, video interviews, and unknown mandatory questions are never bypassed.
- Existing launch blockers include no certified application connector, no evidence trail, and no application-level duplicate prevention.
- Existing discovery catalog has many active vacancies, but source quality varies; Phase 6 must not assume every active vacancy is safely auto-applicable.

## Non-Negotiable Execution Rules
1. Do not implement Phase 6 out of order. Complete and validate each batch before starting the next batch.
2. Do not submit any real application before duplicate prevention, application state persistence, evidence handling, and manager approval checks are implemented.
3. Do not create a universal ATS auto-apply promise. Only certified adapters may submit automatically.
4. Do not bypass CAPTCHA, OTP, assessments, login walls, account creation, paywalls, video interviews, or unknown mandatory questions.
5. Do not invent candidate answers, credentials, legal status, availability, salary, documents, or cover-letter facts.
6. Do not use AI to decide whether to apply, what to answer, or whether a blocker can be skipped.
7. Do not store candidate email passwords. Applications use candidate-owned email/phone; OTP or login requirements become manager actions.
8. Do not re-apply the same candidate to the same vacancy. Enforce candidate/vacancy duplicate prevention at the database and service layers.
9. Do not apply with an unapproved or superseded CV. Each application must reference the approved document version used.
10. Do not mark a job `Applied` without timestamped evidence or a controlled manual confirmation path.
11. Do not silently drop failures. Every job must end in `Applied`, `Failed`, `NeedsAction`, or `Skipped`.
12. Do not mutate Phase 5 scoring/batch decisions except through explicit application handoff status fields added for Phase 6.
13. Do not broaden employer discovery, rewrite candidate onboarding, or redesign CV generation during Phase 6 unless it blocks a Phase 6 acceptance criterion.
14. Do not expose secrets, candidate documents, phone/email, OTPs, or full form traces in logs.
15. Any deviation from this plan must be recorded in [[decisions]] or a session note before continuing.

## Phase 6 Scope
In scope:
- application persistence schema;
- approved batch item to application job handoff;
- duplicate prevention and daily/domain caps;
- manual deep-link tasks as the first safe execution mode;
- adapter SDK and certification contract;
- one narrow certified auto-apply path only after the foundation is safe;
- evidence capture and redacted attempt logs;
- Telegram commands for application status and manager actions;
- daily manager/candidate reporting;
- tests, validation, deployment notes, and memory sync.

Out of scope:
- LinkedIn and Indeed automation;
- universal Workday, Oracle, SAP, Taleo, or custom-site auto-apply;
- CAPTCHA/OTP/login bypass;
- automatic assessments, tests, video interviews, or account creation;
- per-vacancy AI cover letters;
- storing candidate email passwords;
- mass application volume without rate limits and evidence;
- web dashboard unless Telegram becomes a blocker after Phase 6 basics work.

## Data Model Target
Add the Phase 6 persistence layer with minimal, production-safe migrations.

### `applications`
- `id`
- `candidate_id`
- `vacancy_id`
- `batch_id`
- `batch_item_id`
- `document_version_id`
- `idempotency_key`
- `application_adapter`
- `adapter_version`
- `status`: `queued`, `manual_action_required`, `applying`, `applied`, `failed`, `skipped`, `cancelled`
- `status_reason`
- `approved_by`
- `approved_at`
- `queued_at`
- `started_at`
- `finished_at`
- `last_attempt_at`
- `created_at`
- `updated_at`

Required constraints:
- unique `idempotency_key`;
- unique active application per `(candidate_id, vacancy_id)`;
- references must preserve the exact document version and batch item that caused the job.

### `application_attempts`
- `id`
- `application_id`
- `attempt_number`
- `status`
- `error_category`
- `error_message_redacted`
- `retry_after`
- `adapter_version`
- `started_at`
- `finished_at`
- `metadata`

Error categories:
- `network_error`
- `rate_limited`
- `adapter_error`
- `validation_error`
- `blocked_or_auth_required`
- `captcha_or_otp`
- `assessment_required`
- `unknown_required_question`
- `duplicate_detected`
- `manual_only`
- `unknown_error`

### `application_evidence`
- `id`
- `application_id`
- `evidence_type`: `screenshot`, `html_snapshot`, `confirmation_url`, `confirmation_text_hash`, `email_message_id`, `manual_confirmation`
- `storage_key`
- `confirmation_url`
- `confirmation_text_hash`
- `captured_at`
- `metadata`

### `manual_actions`
- `id`
- `application_id`
- `candidate_id`
- `vacancy_id`
- `action_type`: `open_deep_link`, `answer_question`, `provide_otp`, `complete_assessment`, `manual_submit`, `review_failure`
- `instructions`
- `deep_link_url`
- `status`: `open`, `resolved`, `cancelled`, `expired`
- `assigned_manager_id`
- `created_at`
- `due_at`
- `resolved_at`
- `resolution_note`

If existing schema differs during implementation, preserve local naming patterns and document the mapping in a session note.

## Application Handoff Contract
Only these Phase 5 items can enter Phase 6:
- parent batch status is `approved` or `partially_approved`;
- item decision is `approved`;
- candidate is not closed;
- candidate still belongs to the approving/assigned manager or admin override is explicit;
- candidate has exactly one active approved CV/document version;
- vacancy is still active or explicitly allowed by a freshness grace rule;
- no existing application exists for the same candidate and vacancy;
- current time respects candidate/day/domain caps.

Handoff output:
- one `applications` row per approved item;
- one idempotent queue message for `application.submit` or `application.manual_action`;
- audit event with redacted metadata;
- no real external submission during handoff itself.

## Execution Modes

### Mode 1: Manual Deep-Link Task
Default first implementation.

Behavior:
- create application row;
- create `manual_actions` row with vacancy apply URL, candidate summary, approved CV link, and instructions;
- notify manager in Telegram;
- manager completes or confirms manually;
- system records `manual_confirmation` evidence and final status.

Acceptance:
- no external form is auto-submitted;
- duplicate prevention works;
- manager can see and resolve pending actions;
- application ends in a known terminal/actionable state.

### Mode 2: Email Apply
Allowed only after foundation works.

Behavior:
- send deterministic email with approved CV attachment/link and approved candidate facts;
- no invented cover letter;
- store provider message ID and redacted evidence;
- classify bounces/failures.

Acceptance:
- sender identity, consent, attachment handling, and logs are safe;
- duplicate prevention and rate limits are active;
- email evidence is persisted.

### Mode 3: Certified ATS/Form Adapter
Allowed only after adapter certification.

Behavior:
- adapter preflight checks support;
- adapter maps known fields only;
- adapter stops on unknown mandatory questions, CAPTCHA, OTP, login, assessment, or changed form structure;
- evidence is captured before terminal status.

Acceptance:
- fixture tests cover the adapter;
- one controlled submission succeeds;
- duplicate prevention is verified;
- sensitive values are redacted from logs/screenshots where possible;
- domain rate limits are configured.

## Adapter SDK Contract
Each adapter must implement:

```text
supports(url)
preflight(context)
discoverForm(context)
mapFields(context)
uploadDocuments(context)
fillApplication(context)
submit(context)
captureEvidence(context)
```

Adapter output must include:
- status;
- external confirmation reference if any;
- confirmation URL if any;
- evidence references;
- retry classification;
- manual-action reason when blocked.

No adapter is production-enabled until certification is recorded in memory and source configuration.

## Execution Batches

### Batch 0: Baseline Audit and Phase 6 Lock
Objective:
- Confirm repo state, Phase 5 handoff semantics, existing queue contracts, current schema, and validation commands before coding.

Actions:
- Inspect `packages/contracts/src/queues.ts`.
- Inspect `packages/db/src/schema.ts`.
- Inspect `packages/matching/src/store.ts`.
- Inspect `apps/bot-api/src/intake/batch.ts`.
- Inspect current migrations.
- Confirm no existing application tables already exist.
- Confirm validation commands in `package.json`.

Validation:
- No code changes unless the audit finds a stale memory mismatch.

Exit criteria:
- Exact files and gaps are known.
- Any mismatch with this plan is documented before implementation starts.

### Batch 1: Schema and Contracts
Objective:
- Add application persistence and typed contracts without submitting anything externally.

Actions:
- Add migration for `applications`, `application_attempts`, `application_evidence`, and `manual_actions`.
- Add Drizzle schema/types.
- Add status/error constants and queue payload schemas.
- Add indexes and uniqueness for idempotency.
- Add append-only audit events for handoff and status transitions.

Validation:
- Typecheck.
- Migration reviewed as non-destructive.
- Unit tests for idempotency key generation and status transitions.

Exit criteria:
- Application jobs can be represented safely in the DB.

### Batch 2: Approved Batch Handoff
Objective:
- Convert approved Phase 5 batch items into idempotent application jobs.

Actions:
- Implement a service that reads approved/partially approved batches and approved items.
- Enforce handoff preconditions.
- Create one application row per eligible approved item.
- Skip duplicates with explicit `skipped` or no-op behavior, never duplicate rows.
- Enqueue only queue messages; do not submit external applications.
- Add Telegram/admin command if useful, for example `/application_handoff`.

Validation:
- Tests for approved, partially approved, rejected, pending, duplicate, closed candidate, superseded document, inactive vacancy.
- Tests prove handoff does not submit applications.

Exit criteria:
- Phase 5 approved items become Phase 6 jobs exactly once.

### Batch 3: Manual Deep-Link Execution
Objective:
- Provide the first safe operational execution mode.

Actions:
- Implement `manual_actions` creation for unsupported or manual-first applications.
- Add Telegram manager UI to list open manual actions by candidate.
- Include apply URL, approved CV signed link, candidate facts summary, and clear action buttons.
- Add resolution actions: confirm applied, mark failed, mark skipped, request follow-up.
- Persist manual confirmation evidence.

Validation:
- Tests for manager ownership, stale callbacks, status transitions, signed link generation, redaction.
- Manual Telegram checklist prepared.

Exit criteria:
- Managers can execute and resolve application tasks without hidden automation.

### Batch 4: Application Worker Foundation
Objective:
- Add worker skeleton and deterministic state machine.

Actions:
- Add `apps/worker-applications` following existing worker patterns.
- Read `application.submit` and `application.manual_action`.
- Load application context, candidate, vacancy, document version, and adapter/source config.
- Route unsupported adapters to manual actions.
- Implement retries only for retryable technical failures.
- Record attempts and audit events.

Validation:
- Unit/integration tests for worker message handling, ack-after-transaction behavior, retry classification, terminal states.
- Local build/check/test.

Exit criteria:
- Worker can process jobs to `manual_action_required`, `skipped`, `failed`, or adapter-ready path without unsafe submission.

### Batch 5: Adapter SDK and Certification Harness
Objective:
- Create the adapter interface and test harness before enabling any auto-apply.

Actions:
- Add `packages/application-adapters`.
- Define context, field mapping, evidence, and error taxonomy.
- Add fixture format for HTML/form snapshots and expected mapping behavior.
- Add certification checklist in docs or memory.
- Add a `manual-deep-link-v1` adapter as the safe default.

Validation:
- Tests for adapter support detection, unknown required fields, blocked controls, evidence contract, redaction.

Exit criteria:
- Future adapters have a strict contract and cannot silently submit outside certification.

### Batch 6: First Narrow Certified Submission Path
Objective:
- Implement only one narrow auto-submit path if a safe target is chosen and certification requirements are met.

Allowed choices:
- email apply, if a source exposes a safe application email or controlled recipient;
- one specific employer/form adapter with stable fields and controlled test submission.

Actions:
- Pick exactly one target.
- Build fixture tests first.
- Implement preflight, field mapping, document upload/attachment, submit, evidence capture.
- Stop safely on unknown fields/protective controls.
- Enable through source-level config only after certification.

Validation:
- Fixture tests.
- One controlled submission or dry-run evidence depending on target.
- Duplicate prevention verified.
- Logs redacted.

Exit criteria:
- One certified path can submit or send safely; all other paths remain manual.

### Batch 7: Reporting and Operational Visibility
Objective:
- Report application progress to managers and candidates.

Actions:
- Add daily report aggregation for applications.
- Add Telegram command/status view for candidate application outcomes.
- Summarize applied, needs action, failed, skipped, duplicates prevented, and shortage.
- Keep candidate-facing reports simpler than manager reports.
- Add queue/source/adapter health fields where useful.

Validation:
- Tests for report counts and status grouping.
- Manual Telegram output review.

Exit criteria:
- Managers can understand daily execution state without reading logs.

### Batch 8: QA, Production Readiness, and Memory Sync
Objective:
- Validate Phase 6 before pilot use.

Actions:
- Run full validation:
  - `CI=true pnpm check`
  - `CI=true pnpm test`
  - `CI=true pnpm build`
  - `CI=true pnpm format:check`
- Apply migration only after review.
- Deploy only the completed safe slice.
- Verify health endpoints, worker logs, queue depth, Telegram commands, and one controlled flow.
- Update [[current-state]], [[next-steps]], [[risks]], and session notes.

Exit criteria:
- Build/tests pass or failures are documented with owner and next step.
- Changed files are listed.
- No secrets are exposed.
- Application jobs produce terminal/actionable statuses.
- Memory reflects actual evidence, not assumptions.

## Acceptance Criteria
Phase 6 is complete only when:
- approved Phase 5 items create idempotent application jobs;
- duplicate applications are prevented for `(candidate_id, vacancy_id)`;
- every application references the exact approved document version used;
- jobs reach `Applied`, `Failed`, `NeedsAction`, or `Skipped`;
- manual actions are visible and resolvable in Telegram;
- no unsupported form is auto-submitted;
- protective controls become `NeedsAction`;
- at least one execution mode is production accepted;
- evidence is persisted for applied/confirmed applications;
- daily manager/candidate reports summarize outcomes;
- full validation commands pass or documented failures are explicitly accepted;
- memory is updated with actual completion evidence.

## Risk Register
| Risk | Evidence | Impact | Mitigation | Owner | Status |
|---|---|---|---|---|---|
| Phase 6 drifts into unsafe universal auto-apply | Enterprise ATS forms vary and no adapter is certified | Candidate reputation and legal/compliance risk | Start with manual deep-link tasks; certify one narrow adapter at a time | Codex + Tamerlan | Open |
| Duplicate applications | Phase 5 approval can happen across days and sources overlap by apply URL | Candidate reputation damage | DB uniqueness, idempotency key, prior application checks, duplicate report before handoff | Codex | Open |
| Missing evidence for claimed applications | No application evidence tables exist yet | Cannot audit success/failure | Implement evidence persistence before real submission | Codex | Open |
| Login/OTP/CAPTCHA blocks automation | Known ATS risk | Automation failure or unsafe bypass temptation | Route to `NeedsAction`; no bypass | Codex + Manager | Open |
| Form fields require facts not in profile | Candidate data may be incomplete | Wrong or invented answers | Use deterministic answer bank only; unknown mandatory fields become manager actions | Codex + Manager | Open |
| Application worker sends too many requests | Daily target can scale to 300 attempts | Blocking/rate-limit risk | Domain caps, retry backoff, slow defaults, manual-first rollout | Codex | Open |
| Secrets or PII leak in logs/evidence | Application forms contain personal data | Critical privacy risk | Redaction, private storage, signed URLs, no passwords, no raw full traces in logs | Codex | Open |

## Manual Acceptance Checklist
- Run `/approved_vacancies` for the pilot candidate before handoff.
- Confirm no duplicate approved `vacancy_id` values for the candidate.
- Create Phase 6 jobs from one approved or partially approved batch.
- Re-run handoff and confirm no duplicate applications are created.
- Confirm each application references the approved CV document version.
- Confirm unsupported adapters create manual actions, not submissions.
- Open manual action in Telegram and verify instructions/deep link/CV link.
- Resolve one manual action as applied and confirm evidence is recorded.
- Resolve one manual action as failed/skipped and confirm final state.
- Confirm manager ownership restrictions on callbacks.
- Confirm logs redact sensitive fields.
- Confirm queue depth returns to zero after controlled run.

## Next Action
Start Batch 0: audit current repo state, Phase 5 handoff semantics, queue contracts, schema, bot batch implementation, and validation commands. Do not start schema implementation until Batch 0 findings are known and no blocker contradicts this plan.
