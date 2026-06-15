# AMIGO MVP — Technical Architecture

## Related
- [[overview]]
- [[current-state]]
- [[decisions]]
- [[risks]]
- [[data-model]]
- [[integrations]]
- [[roadmap]]

## Stack
- Runtime: Node.js LTS, TypeScript, pnpm workspaces.
- Bot: grammY in webhook mode with conversations and inline keyboards.
- API: Fastify, Zod, OpenAPI.
- Database: Supabase Postgres with Drizzle ORM and SQL migrations.
- Files: private Supabase Storage buckets.
- Queues: Supabase Queues/PGMQ.
- Scheduling: Supabase Cron.
- Automation: Playwright Chromium workers.
- Documents: Docxtemplater and private Gotenberg/LibreOffice service.
- LLM: OpenAI GPT-5.4 mini structured output.
- Hosting: Railway Pro for API, workers, and Gotenberg.
- Monitoring: Sentry, JSON logs, health endpoints, Telegram alert chat.
- Tests: Vitest, integration fixtures, Playwright.

## Repository shape
```text
apps/
  bot-api/
  worker-ingestion/
  worker-documents/
  worker-matching/
  worker-applications/
  worker-reporting/
packages/
  db/
  contracts/
  bot-ui/
  connectors/
  application-adapters/
  document-templates/
  observability/
```

## Runtime data flow
1. Telegram webhook validates the manager and persists each workflow transition.
2. Candidate completion enqueues a document job.
3. Approved documents activate scheduled vacancy matching.
4. Ingestion workers poll employer endpoints and upsert normalized vacancies.
5. Matching workers apply hard filters and scoring, then create a daily batch.
6. Manager approval creates idempotent application jobs.
7. Application workers run the correct certified adapter.
8. Results and evidence are persisted before Telegram notifications are sent.
9. Reporting workers aggregate daily metrics by candidate and manager.

## Queue names
- `document.generate`
- `vacancy.ingest`
- `vacancy.match`
- `batch.prepare`
- `application.submit`
- `application.manual_action`
- `report.daily`
- `retention.delete`

Each message contains `job_id`, `correlation_id`, entity ID, attempt count, and schema version. Workers acknowledge only after the database transaction commits.

## Reliability rules
- Application idempotency key: `candidate_id + vacancy_id + document_version_id`.
- No automatic retry for validation errors, CAPTCHA, OTP, assessments, or unsupported fields.
- Network and 429 errors use exponential backoff with jitter.
- Every connector has a circuit breaker and independent health state.
- Domain concurrency and requests-per-minute are configurable.
- Browser screenshots and final URL are retained as application evidence.

## Security
- Telegram ID allowlist plus `admin`, `manager`, and `viewer` roles.
- Managers access only assigned candidates unless granted admin scope.
- RLS enabled on all candidate-facing tables.
- Files use private buckets and short-lived signed URLs.
- Browser session secrets are encrypted using AES-256-GCM.
- Encryption keys and service credentials exist only in Railway secrets.
- Audit events are append-only for identity, document, approval, and application actions.
- Logs redact email, phone, passport, token, and document contents.

## Budget guardrails
- Supabase Pro: approximately USD 25/month.
- Railway Pro minimum: USD 20/month plus measured usage.
- OpenAI documents: target below USD 10/month for pilot.
- Remaining budget covers browser runtime, Sentry, and optional proxy use.
- Alert at 70% and stop non-critical generation at 90% of monthly budget.

## Scale trigger
Move from PGMQ to dedicated Redis/BullMQ only if measured queue latency, job throughput, or scheduling requirements cannot meet the scale-to-30 gates. Do not add Redis preemptively.

