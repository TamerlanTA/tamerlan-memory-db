# Med Spa GTM Strategy Tracker

#flowops #scaling #gtm #medspa #strategy #metrics

## Related
- [[00 - Scaling Hub]]
- [[01 - HIPAA-Safe Intake Cleanup Sprint]]
- [[08 - Med Spa HIPAA Intake Launch Kit]]
- [[09 - Pipeline C Med Spa Audit Prompt Spec]]
- [[../03 - Acquisition Pipelines/Pipeline C — Website Audit Generator]]
- [[../05 - CRM Structure/CRM Tables]]

## Content

## Strategy hypothesis

FlowOps can get first Risk Cleanup Sprint clients by using a narrow med spa wedge:

```text
free website/intake cleanup audit -> personalized Loom -> paid 5-7 day implementation sprint
```

The pitch is not "AI automation" and not "HIPAA compliance". The pitch is:

```text
faster lead response + cleaner consultation/intake data flow + fewer messy tool handoffs
```

## Why this might work

- Med spas care about booked consultations and fast follow-up.
- Many use forms, booking tools, chat, CRM, email/SMS, pixels, and paid ads.
- The offer is specific enough to avoid sounding like generic automation.
- A free audit lowers the first-reply barrier.
- A Loom can show visible proof from the prospect's own website.

## Core operating principle

The first goal is **not** immediate revenue. The first goal is to generate enough market feedback to decide whether this wedge is real.

Primary target:

```text
50 touches -> 5 conversations -> 1 paid sprint opportunity
```

If the market does not respond, change the angle or niche quickly.

## Funnel

| Stage | Action | Target |
|---|---|---:|
| Prospecting | Pipeline C finds med spa / aesthetic clinic websites | 50 prospects |
| Scoring | Score each site 0-20 using med spa rubric | 30 score 12+ |
| Outreach | Send free audit / Loom offer | 30-50 sends |
| Loom | Record Looms only for score 16+ | 5-10 Looms |
| Reply | Get serious replies | 3-5 replies |
| Discovery | Run short calls / async audits | 2-3 conversations |
| Close | Offer implementation sprint | 1 paid sprint |

## Quality gates

Use the [[08 - Med Spa HIPAA Intake Launch Kit]] rubric:

- **16-20:** record Loom before or immediately after first reply.
- **12-15:** send email, no Loom unless they reply.
- **8-11:** CRM only / low priority.
- **0-7:** skip.

Do not spend manual Loom time on weak prospects.

## Messaging rules

Always say:
- "This is not legal advice."
- "I am not saying anything is wrong."
- "The goal is operational cleanup."
- "I can send a short free audit."

Never say:
- "HIPAA compliant."
- "You are violating HIPAA."
- "Illegal."
- "Patient data leak."
- "You are at risk."

Preferred phrase:

```text
consultation/intake data flow
```

## Success metrics

Track after each batch:

| Metric | Minimum acceptable | Strong signal |
|---|---:|---:|
| Email delivery rate | 80% | 90%+ |
| Reply rate | 3% | 8%+ |
| Serious reply rate | 1% | 4%+ |
| Loom request / permission rate | 2% | 5%+ |
| Discovery calls from 50 touches | 1 | 3+ |
| Paid sprint from 100 touches | 0-1 | 1+ |

## Stop / pivot rules

After **50 touches**:
- If 0 replies: change subject lines and first sentence.
- If replies say "not relevant": change niche or prospect filters.
- If replies say "send audit" but no calls: improve audit quality and CTA.
- If people worry about legal/HIPAA claims: soften language and remove "HIPAA" from first email.
- If only low-budget solos reply: target multi-location or higher-ticket med spas.

After **100 touches**:
- If 0 serious conversations: pause med spa campaign.
- If 3+ conversations but no close: improve sprint packaging, pricing, and proof.
- If 1 paid sprint closes: continue for another 100 touches and build a case study.

## Pivot options

If med spas are weak, test these in order:

1. **Therapy / counseling practices** — more sensitive intake, potentially stronger pain, slower sales.
2. **Dental clinics** — high lead value, appointment-driven, operationally clear.
3. **Medical weight loss clinics** — high-ticket and data-sensitive, likely strong follow-up need.
4. **Lead Consent Evidence Chain** — switch from healthcare to home services / solar lead buyers.
5. **ADA Website Defense Prep** — switch from intake risk to website remediation evidence.

## First batch plan

Cities:
- Miami
- Scottsdale
- Austin

Volume:
- 24 search queries;
- 50 normalized prospects target;
- 30 score 12+ target;
- 5-10 Loom candidates target.

Command target:

```text
/pipeline_c medspa 30
```

Manual review:
- Approve only if the email has a specific visible observation.
- Reject if the email sounds generic.
- Edit if it mentions legal claims, HIPAA compliance, violation, lawsuit, or patient data leak.
- Need Loom if score is 16+ or the prospect is high-ticket/multi-location.

## What to record in CRM

For each prospect:
- company;
- website;
- city;
- score;
- score reason;
- action route;
- email sent yes/no;
- Loom needed yes/no;
- Loom sent yes/no;
- reply status;
- objection category;
- next action;
- close outcome.

## Review cadence

After each 25 sends:
- check reply rate;
- collect objections;
- rewrite first line if needed;
- note whether prospects understand the offer.

After 50 sends:
- write a session note with metrics and recommendation:
  - continue;
  - adjust messaging;
  - change prospect filters;
  - pivot niche.

After first paid sprint:
- create case study;
- update website;
- add proof to outreach;
- build repeatable implementation checklist.

## Current status

As of 2026-05-06:
- Offer: defined.
- Launch kit: created.
- Prompt spec: created.
- Profile-link fix: local workflow JSON patched, but active n8n workflow must still be re-imported/updated.
- Campaign: not yet run.
- Market validation: not yet proven.

