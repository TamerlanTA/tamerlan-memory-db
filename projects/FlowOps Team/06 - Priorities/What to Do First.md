# 🚀 What to Do First

#flowops #priorities #action

> [!danger] The Rule
> Do not build more systems until you've used the existing framework to close your first 2–3 paying clients. Revenue first. Perfection later.
>
> *"Done is better than perfect. A working system that brings 1 client beats a perfect system that brings 0."*

---

## Priority 1 — Build the Demo Library (Week 1)

**Current status as of 2026-05-03:** still active. This is the main sales-enablement gap.

**Why first:** Every other pipeline requires a demo. Without demos, proposals are weak and response rates are low. Demos are the multiplier for everything else.

**What to build (first 5):**
- [ ] Demo 1: Speed-to-Lead System — Real Estate
- [ ] Demo 2: AI Lead Qualification Chatbot — Clinic
- [ ] Demo 3: Ops Automation — Agency Client Onboarding
- [ ] Demo 4: Jotform → CRM + Slack notification
- [ ] Demo 5: Appointment + Reminder System

**Format:** Loom 60–120 sec → full structure in [[Pipeline D — Demo Library]]

**Time to complete:** 2–3 days
**Impact:** Unlocks every other outreach pipeline immediately

---

## Priority 2 — Activate Upwork Radar (Week 1–2)

**Current status as of 2026-05-03:** prepared but not fully operationalized. A workflow JSON and clean import variant exist; next work is import, credential reconnect, Firecrawl node check/replacement, live test, and first proposal batch.

**Why second:** Upwork has the highest concentration of active buyers with explicit intent and verified payment. Fastest path to first revenue.

**What to do:**
- [x] Prepare Upwork Radar workflow concept and JSON.
- [ ] Import `upwork-radar-workflow.clean-import.json` into n8n.
- [ ] Reconnect Gmail, Google Sheets, Firecrawl, OpenAI, and Telegram credentials.
- [ ] Ensure Firecrawl community node is installed or replace it with built-in HTTP Request.
- [ ] Calibrate fit scoring criteria against real jobs.
- [ ] Send first 10–15 proposals/day from the reviewed queue.
- [ ] Refine based on response rate
- [ ] Target: 50–100 quality proposals/week within 2 weeks

**Time to complete:** 3–5 days to first proposals
**Impact:** Direct path to first Sprint client

→ Full system: [[Pipeline A — Upwork Radar]]

---

## Priority 3 — Website Audit Generator (Week 2)

**Current status as of 2026-05-03:** workflow template and runbook are prepared, but the pipeline is not yet operational. Next step is import + credential reconnect + first manual QA batch.

**Why third:** Personalized audits convert better than any generic cold email. A specific finding about THEIR business is impossible to ignore.

**What to do:**
- [ ] Choose 2–3 niche target lists (real estate, home services, med spa)
- [x] Build the audit template/workflow from [[Pipeline C — Website Audit Generator]]
- [ ] Import `pipeline-c-website-audit-generator-workflow.json` into n8n and reconnect credentials
- [ ] Run first 10-15 website QA batch and verify Airtable + Telegram outputs
- [ ] Record first 10 audit Looms
- [ ] Send 50 personalized emails/DMs per week

**Time to complete:** 1 week to first batch
**Impact:** 5–10 replies per 50 audit outreach messages

---

## Priority 4 — LinkedIn Pain Radar (Week 2–3)

**Current status as of 2026-05-03:** complete as a FlowOps pipeline. Future work is QA, first operational batch, CRM hygiene, and iteration.

**Why fourth:** Warmer leads with active, expressed pain — but requires more research time than Upwork.

**What to do:**
- [x] Build Pipeline B / LinkedIn Pain Radar.
- [x] Treat CRM integration target as available because FlowOps CRM exists.
- [ ] Run the first QA batch and verify candidate quality.
- [ ] Verify CRM writes / manual review queue fields.
- [ ] Iterate keywords and scoring based on first results.
- [ ] Maintain 100 personal touches/week once QA passes.

→ Full system: [[Pipeline B — LinkedIn Pain Radar]]

---

## Priority 5 — Close First Sprint → Pitch Retainer (Week 2–4)

**Why fifth:** The Sprint is proof. The Retainer is leverage. You can't sell the retainer without the Sprint result.

**What to do:**
- [ ] Close first Sprint client (Upwork or LinkedIn)
- [ ] Deliver exceptional work — Loom handoff + documentation
- [ ] 7 days post-delivery: pitch the retainer
- [ ] Package the three retainer tiers and present them clearly

→ Retainer pitch script: [[Pipeline E — Retainer Conversion]]
→ Tier details: [[Long-Term Partner Retainer]]

---

## 📅 Weekly Sprint Template

| Day | Focus |
|-----|-------|
| Mon | Review new Upwork jobs → send proposals |
| Tue | LinkedIn monitoring → personalized DMs |
| Wed | Record 1 demo OR audit 3 websites |
| Thu | Follow-up on all non-replies |
| Fri | Send 5–10 cold emails with audits |
| Sat | Analyze what worked → update CRM |
| Sun | Plan next week |

---

## 🎯 Month 1 Targets

| Week | Focus | Target |
|------|-------|--------|
| 1 | Demo Library | 3 demos live |
| 2 | Upwork Radar | 50 proposals sent |
| 3 | LinkedIn + Cold Email | 100 touches |
| 4 | Follow-up + close | First paid Sprint |

---

## ⚡ The 80/20 Rule

> [!success] Focus Mantra
> **80% of your time on outreach and sales. 20% on building.**
> Most people invert this — and wonder why they have no clients.

| Activity | Time |
|----------|------|
| Outreach (proposals, DMs, calls) | 60% |
| Client delivery | 25% |
| System improvement | 10% |
| Content / LinkedIn | 5% |

---

## 🔗 Related

- [[Pipeline D — Demo Library]] — Priority 1
- [[Pipeline A — Upwork Radar]] — Priority 2
- [[Pipeline C — Website Audit Generator]] — Priority 3
- [[Pipeline B — LinkedIn Pain Radar]] — Priority 4
- [[Pipeline E — Retainer Conversion]] — Priority 5
- [[Full System Architecture]] — the complete map
- [[00 - Overview]] — master hub
