# AMIGO MVP — Integrations and Connector Strategy

## Related
- [[overview]]
- [[technical-architecture]]
- [[data-model]]
- [[risks]]
- [[roadmap]]

## Employer catalog
Each employer entry records:
- brand and parent group;
- hospitality segment;
- target regions;
- career page URL;
- ATS type and tenant identifier;
- vacancy connector and version;
- application adapter and version;
- polling schedule;
- last successful run;
- certification and health state.

Initial catalog target: 100–200 hotels, resort groups, restaurant groups, airlines, and hospitality operators.

## Discovery connectors

### Greenhouse
Use public Job Board GET endpoints to retrieve published jobs when the board token is known. Do not assume submission API access: employer-owned authentication is required.

### Lever
Use public postings endpoints for published jobs. Hosted application forms remain the default submission path unless authorized credentials exist.

### Generic feeds
Support documented JSON endpoints, RSS, sitemap discovery, and stable server-rendered career listings.

### Enterprise career sites
Workday, Oracle Recruiting, SAP SuccessFactors, Taleo, and custom portals are implemented employer-by-employer. Their recruiter APIs are not treated as public candidate submission APIs.

## Normalized vacancy contract
```text
source
source_tenant
external_id
employer
title
role_family
country
city
employment_type
salary_min/max/currency/period
language_requirements
experience_requirements
description
posted_at
expires_at
apply_url
connector_type/version
```

## Deduplication
1. Exact `(source, tenant, external_id)`.
2. Canonical apply URL.
3. Hash of normalized employer, title, location, and posting date.

## Application adapter contract
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

Adapter output:
- status;
- external confirmation reference;
- confirmation URL;
- evidence;
- retry classification;
- manual-action reason.

## Certification
An adapter is enabled only after:
- fixture tests cover known field variants;
- one controlled submission succeeds;
- duplicate prevention is verified;
- CAPTCHA and unknown questions stop safely;
- screenshots and logs redact sensitive values;
- domain rate limits are configured.

## Matching
Hard filters:
- country and excluded regions;
- role family;
- relocation and sponsorship;
- language;
- minimum experience;
- contract type;
- blacklist;
- vacancy age;
- previous application.

Weighted score:
- role/title match: 30;
- experience/seniority: 20;
- country/relocation: 15;
- language: 10;
- hospitality segment: 10;
- schedule/contract: 5;
- salary: 5;
- freshness: 5.

Thresholds:
- 70–100: primary batch;
- 55–69: reserve;
- below 55: reject.

## Research references
- Greenhouse Job Board API: https://developers.greenhouse.io/job-board.html
- Greenhouse API overview: https://support.greenhouse.io/hc/en-us/articles/10568627186203-Greenhouse-API-overview
- Lever Postings API: https://github.com/lever/postings-api
- Oracle Recruiting REST: https://docs.oracle.com/en/cloud/saas/human-resources/farws/
- SAP JobApplication API: https://help.sap.com/docs/successfactors-platform/sap-successfactors-api-reference-guide-odata-v2/jobapplication
- Playwright: https://playwright.dev/
- Telegram Bot API: https://core.telegram.org/bots/api
- Supabase PGMQ: https://supabase.com/docs/guides/database/extensions/pgmq
- Gotenberg: https://gotenberg.dev/

