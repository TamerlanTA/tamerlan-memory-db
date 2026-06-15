# AMIGO MVP — Data Model

## Related
- [[overview]]
- [[technical-architecture]]
- [[candidate-intake]]
- [[integrations]]
- [[decisions]]

## Identity and access
- `users`: Telegram identity, role, active status.
- `manager_assignments`: manager-to-candidate ownership with history.
- `audit_events`: actor, action, entity, correlation ID, redacted metadata, timestamp.

## Candidate domain
- `candidates`: lifecycle status, assigned manager, contact identity, retention deadline.
- `candidate_profiles`: versioned normalized facts and completeness state.
- `candidate_preferences`: countries, roles, salary, schedule, relocation, blacklist.
- `candidate_experience`: employment records.
- `candidate_education`: education records.
- `candidate_languages`: language and proficiency.
- `candidate_certifications`: certifications and expiry.
- `candidate_consents`: consent text version and timestamp.
- `application_answers`: approved reusable answers with sensitivity and expiry.

## Documents
- `source_files`: uploaded source documents and checksums.
- `document_templates`: template type, version, locale, active status.
- `document_versions`: candidate, template, source profile version, status, storage keys.
- `generation_runs`: model, prompt version, structured input/output hashes, validation result, cost.

Document statuses:
`Draft`, `Generated`, `ValidationFailed`, `PendingApproval`, `Approved`, `Rejected`, `Superseded`.

## Employers and vacancies
- `employers`: brand, category, regions, active status.
- `career_sources`: employer, ATS type, endpoint, polling interval, connector version, health.
- `vacancies`: normalized job fields and canonical apply URL.
- `vacancy_source_snapshots`: source payload hash and retrieval timestamp.
- `vacancy_scores`: candidate, profile version, score, hard-filter result, explanation.

## Batches and applications
- `daily_batches`: candidate, date, status, target size, approved by.
- `daily_batch_items`: vacancy, rank, score, decision, rejection reason.
- `applications`: idempotency key, document version, adapter version, state, timestamps.
- `application_attempts`: attempt number, error class, retry time, redacted trace.
- `application_evidence`: screenshot/file key, confirmation URL, confirmation text hash.
- `manual_actions`: action type, instructions, owner, due time, resolution.

Batch statuses:
`Preparing`, `PendingApproval`, `Approved`, `PartiallyApproved`, `Rejected`, `Executing`, `Complete`.

Application statuses:
`Discovered`, `Scored`, `Proposed`, `Approved`, `Applying`, `Applied`, `Failed`, `NeedsAction`, `Skipped`.

## Reporting and operations
- `daily_reports`: recipient type, candidate/date, metrics, delivery status.
- `connector_runs`: counts, latency, status, error taxonomy.
- `system_alerts`: severity, source, status, resolution.
- `retention_jobs`: candidate, deadline, deletion scope, outcome.

## Core constraints
- Unique vacancy: `(career_source_id, external_id)`.
- Unique application: `(candidate_id, vacancy_id)`.
- Exactly one approved active document per candidate and document type.
- Candidate cannot enter matching without complete profile, consent, and approved CV.
- Sensitive files are referenced by storage key, never stored as database blobs.

