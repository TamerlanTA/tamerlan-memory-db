# AMIGO MVP — Overview

## Related
- [[current-state]]
- [[decisions]]
- [[risks]]
- [[next-steps]]
- [[roadmap]]
- [[technical-architecture]]
- [[data-model]]
- [[candidate-intake]]
- [[integrations]]
- [[prompts]]
- [[../../knowledge/notion-office-operating-system|Notion Office Operating System]]

## Product
AMIGO is a manager-led Telegram system for preparing international hospitality candidates, finding suitable vacancies, approving daily application batches, submitting applications, and reporting results.

The first target markets are the Maldives, Asia, the Middle East, and Europe. Initial candidate roles are in hotels, resorts, restaurants, airlines, and related hospitality businesses.

## Goal
Launch a controlled pilot for 10 candidates by **2026-07-05**, then immediately support 30 active candidates from the existing waitlist.

Each active candidate should receive:
- an approved English CV package;
- deterministic vacancy matching;
- 5–10 approved application attempts per day when enough suitable vacancies exist;
- a concise daily progress report.

## Users
- **Admin:** manages access, infrastructure settings, employers, and connector activation.
- **Manager:** collects candidate data, approves documents, reviews daily vacancy batches, and handles exceptions.
- **Candidate:** provides source data and receives progress reports; no self-service dashboard in MVP.

The pilot assumes 2–5 managers. Every candidate has an assigned manager.

## Core workflow
1. A manager creates a candidate in Telegram.
2. A step-by-step Russian intake collects facts, preferences, documents, and standard application answers.
3. An LLM translates and structures approved facts into an English profile.
4. Template-based document generation produces DOCX and PDF CV files.
5. The manager reviews and approves the document version.
6. The system ingests vacancies from a curated catalog of 100–200 employers.
7. Hard filters and weighted rules rank vacancies without AI.
8. The manager approves a daily batch of 5–10 vacancies.
9. Supported adapters submit applications; unsupported steps enter a manual-action queue.
10. The manager receives an operational report and the candidate receives a simplified report.

## MVP boundaries
Included:
- Telegram-only manager workflow;
- Russian intake and English documents;
- LLM-assisted document preparation;
- curated employer catalog;
- deterministic ingestion, filtering, scoring, and selection;
- hosted-form browser automation and email applications;
- audit evidence and daily reporting.

Excluded:
- LinkedIn and Indeed automation;
- CAPTCHA or anti-bot bypass;
- automatic tests, assessments, or video interviews;
- invented answers to application questions;
- universal Workday, Oracle, SAP, or Taleo support;
- candidate-facing web dashboard;
- per-vacancy AI cover letters.

## Success criteria
- Ten candidates are active by 2026-07-05.
- Documents contain no facts absent from the candidate profile.
- Matching is reproducible for identical input.
- Duplicate applications are prevented.
- Every attempt ends as `Applied`, `Failed`, `NeedsAction`, or `Skipped`.
- Every successful application has timestamped evidence.
- The system can process 30 candidates and up to 300 attempts per day after launch.
- Personal data is deleted 90 days after candidate closure.

## Notion
- Project: https://app.notion.com/p/3793e026e92f813f838be7212aa1d8a5
- Office: https://app.notion.com/p/3753e026e92f8008a797d3446e02752c

