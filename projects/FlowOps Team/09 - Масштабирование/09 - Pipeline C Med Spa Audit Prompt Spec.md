# Pipeline C Med Spa Audit Prompt Spec

#flowops #pipeline-c #medspa #hipaa #audit #n8n

## Related
- [[00 - Scaling Hub]]
- [[01 - HIPAA-Safe Intake Cleanup Sprint]]
- [[08 - Med Spa HIPAA Intake Launch Kit]]
- [[../03 - Acquisition Pipelines/Pipeline C — Website Audit Generator]]

---

## Purpose

This spec replaces the generic Pipeline C AI audit prompt when running med spa / aesthetic clinic campaigns.

Drop this into the **Audit Queue** workflow's OpenAI node in place of the default system + user prompt. Do not modify the surrounding n8n node structure — only swap the prompt content and extend the JSON output schema.

Status: **specification only**. Not yet patched into n8n workflow JSON.

---

## 1. System Prompt

```
You are a workflow analyst at FlowOps, an AI automation agency. Your job is to audit med spa and aesthetic clinic websites for operational gaps in their intake, booking, and follow-up process.

You do NOT give legal advice. You do NOT claim HIPAA compliance or HIPAA violation. You do NOT accuse anyone of breaking any law. You only analyze publicly visible website signals and describe operational cleanup opportunities.

Your output is used by FlowOps to write personalized outreach to med spa owners and managers. The goal of the outreach is to offer a free intake cleanup audit, then pitch a paid implementation sprint ($1,500–$4,000).

Tone: professional, precise, neutral. No fear-based language. No legal claims. Focus on operational efficiency, speed-to-lead, and cleaner data flow.
```

---

## 2. User Prompt (copy-paste ready)

Insert `{{scraped_website_content}}` as the variable injected from Firecrawl scrape output.

```
You are auditing a med spa or aesthetic clinic website for FlowOps.

Website content:
---
{{scraped_website_content}}
---

Company name (if known): {{company_name}}
Website URL: {{website}}
City: {{city}}

TASK:
Analyze the website content and score this med spa as a potential FlowOps client for a HIPAA-Safe Intake + Follow-up Cleanup Sprint.

Use the following scoring rubric (total: 0–20 points):

1. Intake form sensitivity (0–4):
   Does the site collect treatment interest, condition concern, procedure preference, weight, medical history, symptoms, or any health-adjacent information in a form, quiz, or booking widget? Score 4 if clearly present. Score 2-3 if likely but not fully visible. Score 0-1 if no form or clearly only name/email.

2. Tracker / pixel exposure (0–4):
   Are there visible signals of ad pixels (Meta, Google, TikTok), analytics scripts, chat widgets (Intercom, Drift, LiveChat), or remarketing tools on or near intake/booking pages? Score 4 if multiple trackers clearly present near intake. Score 2-3 if some signals visible. Score 0-1 if no signals.

3. Booking and follow-up gap (0–4):
   Is booking manual (call-only, email-only), delayed (no instant confirmation), or unclear after form submission? Is there no visible instant-response or automation signal? Score 4 if clearly manual/delayed. Score 2-3 if partial automation visible. Score 0-1 if strong automated booking clearly visible.

4. Tool-stack fragmentation (0–3):
   Are multiple disconnected tools visible? (e.g. a third-party booking widget + separate form + chat + CRM reference + SMS opt-in). Score 3 if 3+ disconnected tools visible. Score 2 if 2 tools visible. Score 1 if 1 visible. Score 0 if none detectable.

5. Privacy signal weakness (0–3):
   Is HIPAA, privacy, or data handling language missing from intake pages, forms, or near booking CTAs? Is privacy policy generic, buried, or not linked near intake? Score 3 if no visible privacy signal near intake. Score 2 if generic or buried. Score 1 if partial language visible. Score 0 if clear, specific privacy language is present near intake.

6. Commercial urgency (0–2):
   Does the site show paid ad signals, high-ticket services ($500+), multiple locations, or clear lead volume activity (testimonials volume, blog activity, offer promotions)? Score 2 if strong. Score 1 if moderate. Score 0 if weak.

After scoring, determine the recommended action:
- 16–20: Loom candidate (record personalized Loom video)
- 12–15: Cold email candidate
- 8–11: CRM only, low priority
- 0–7: Skip

Write the output as a single valid JSON object matching this exact schema. Output ONLY the JSON object. No explanation, no preamble, no markdown code fences.

{
  "company_name": "string",
  "website": "string",
  "city": "string",
  "niche": "string — must be one of: Med Spa, Aesthetic Clinic, Medical Weight Loss, IV Therapy Clinic, Laser Clinic, Hormone Clinic, or Mixed Aesthetic",
  "med_spa_fit_score": integer between 0 and 20,
  "score_reasoning": "string — 2–4 sentences explaining the score across the 6 rubric dimensions",
  "intake_data_risk_signal": "string — describe exactly what sensitive or health-adjacent data the site appears to collect and through which mechanism (form, quiz, chat, booking widget)",
  "tracking_signal": "string — list any visible trackers, pixels, chat tools, or analytics tools found on or near intake/booking pages. Write 'None detected' if nothing visible.",
  "response_gap": "string — describe what appears to happen after a visitor submits a form or booking request. Is it clear? Manual? Automated? Unknown?",
  "tool_stack_fragmentation": "string — list the distinct tools or systems visible on the site. Include booking, forms, chat, CRM hints, SMS opt-ins, and payment tools.",
  "privacy_signal_weakness": "string — describe the privacy or HIPAA language situation on the site: missing, generic, buried, or adequate. Cite exactly where it appears or doesn't.",
  "commercial_urgency": "string — describe signals of paid acquisition, high-ticket services, multiple locations, or lead volume",
  "safer_workflow_idea": "string — one concrete operational improvement: what would a cleaner intake → response → CRM path look like for this specific site?",
  "bottleneck": "string — the single biggest operational gap on this site that FlowOps could fix",
  "opportunity_1": "string — first automation/cleanup opportunity for this site",
  "opportunity_2": "string — second automation/cleanup opportunity for this site",
  "opportunity_3": "string — third automation/cleanup opportunity for this site",
  "loom_hook": "string — first 10 seconds of a Loom script, personalized to this site. Must open with an observation, not a claim. Example: 'Hey [Name], I took a quick look at [Company] because med spas usually have two competing needs...'",
  "loom_script": "string — full 90–150 second Loom script with 5 sections: Hook / Specific Observation / Operational question (not legal claim) / Safer workflow idea / CTA. Keep it neutral and operational. Do not claim HIPAA violation or compliance.",
  "cold_email_subject": "string — one subject line, under 8 words, curious not alarming. Examples: 'Quick intake idea for [Company]' or 'Question about [Company]'s consultation flow'",
  "cold_email_body": "string — personalized cold email body using the specific observation from the audit. 4–6 sentences. Must include the safe language guardrail. End with a Loom offer or question. Do NOT include a subject line in this field.",
  "linkedin_dm": "string — short LinkedIn DM, 3–4 sentences. Conversational. Reference a specific site observation. Offer a 2-min Loom.",
  "follow_up_1": "string — first follow-up message if no reply, reference a specific site observation, offer the Loom or free audit",
  "follow_up_2": "string — second and final follow-up, close the loop, offer to send a free cleanup audit",
  "recommended_action": "string — must be exactly one of: Loom Candidate, Email Candidate, CRM Only, Skip",
  "do_not_claim": "string — write the exact safe-language disclaimer sentence to include in all outreach for this prospect. Must include: not legal advice, not saying anything is wrong, operational cleanup only.",
  "implementation_sprint_angle": "string — 1–2 sentences describing how to frame the paid sprint for this specific prospect after the free audit. Reference their specific bottleneck."
}
```

---

## 3. JSON Output Schema (for n8n OpenAI node)

Use with `response_format: { type: "json_object" }` in the OpenAI Chat node.

Required fields and types:

```json
{
  "company_name": "string",
  "website": "string",
  "city": "string",
  "niche": "string",
  "med_spa_fit_score": "integer",
  "score_reasoning": "string",
  "intake_data_risk_signal": "string",
  "tracking_signal": "string",
  "response_gap": "string",
  "tool_stack_fragmentation": "string",
  "privacy_signal_weakness": "string",
  "commercial_urgency": "string",
  "safer_workflow_idea": "string",
  "bottleneck": "string",
  "opportunity_1": "string",
  "opportunity_2": "string",
  "opportunity_3": "string",
  "loom_hook": "string",
  "loom_script": "string",
  "cold_email_subject": "string",
  "cold_email_body": "string",
  "linkedin_dm": "string",
  "follow_up_1": "string",
  "follow_up_2": "string",
  "recommended_action": "string",
  "do_not_claim": "string",
  "implementation_sprint_angle": "string"
}
```

**In n8n:** set the OpenAI node to parse the response as JSON. Use a downstream `Set` node to extract each field as `{{ $json.company_name }}`, `{{ $json.med_spa_fit_score }}`, etc.

---

## 4. Quality Gate Rules

Insert an `If` node after the OpenAI output parse. Route based on `med_spa_fit_score`:

| Score | Action | Route |
|------:|--------|-------|
| 16–20 | Loom Candidate | → Telegram card + Airtable write (priority: HIGH) |
| 12–15 | Email Candidate | → Telegram card + Airtable write (priority: MEDIUM) |
| 8–11 | CRM Only | → Airtable write only, no Telegram card (priority: LOW) |
| 0–7 | Skip | → Airtable log only (status: SKIPPED) |

In n8n, use two `If` nodes in sequence:
- If `med_spa_fit_score >= 16` → Loom branch
- Else if `med_spa_fit_score >= 12` → Email branch
- Else if `med_spa_fit_score >= 8` → CRM only branch
- Else → Skip/log branch

---

## 5. Cold Email Template (generated from audit)

The `cold_email_body` field in the AI output is already personalized. Use this static wrapper when composing the final Gmail message:

```
Subject: {{ cold_email_subject }}

Hi [Name],

{{ cold_email_body }}

Tamerlan
FlowOps
https://www.flowops.agency
https://www.linkedin.com/in/tamerlan-togysbayev-855a8526b
https://www.upwork.com/freelancers/tamerlantog
```

**Guardrail check before send:** verify `cold_email_body` does NOT contain:
- "HIPAA compliant" or "HIPAA compliance"
- "violating" or "illegal" or "lawsuit"
- "patient data" (use "intake data" or "consultation request data")
- "you are at risk" (frame as "this is worth cleaning up")

If any flagged phrase appears, reject and re-prompt or manually edit before approving in Telegram.

---

## 6. Telegram Review Card Format

```
🏥 MED SPA AUDIT — {{ company_name }}

🌆 {{ city }} | {{ niche }}
🔗 {{ website }}

📊 Score: {{ med_spa_fit_score }}/20
📋 Action: {{ recommended_action }}

📌 Bottleneck:
{{ bottleneck }}

🚨 Intake Signal:
{{ intake_data_risk_signal }}

📡 Tracker Signal:
{{ tracking_signal }}

⚡ Response Gap:
{{ response_gap }}

💡 Safer Workflow Idea:
{{ safer_workflow_idea }}

📬 Email Subject:
{{ cold_email_subject }}

📝 Score Reasoning:
{{ score_reasoning }}

---
[✅ Approve + Send] [🎥 Need Loom] [✏️ Edit Needed] [❌ Reject]
```

**Note:** Keep the card under ~600 characters above the divider. If fields are long, truncate to first sentence with `...`.

In n8n, build the card text in a `Set` node using expression mode:

```
🏥 MED SPA AUDIT — {{ $json.company_name }}

🌆 {{ $json.city }} | {{ $json.niche }}
🔗 {{ $json.website }}

📊 Score: {{ $json.med_spa_fit_score }}/20
📋 Action: {{ $json.recommended_action }}

📌 Bottleneck:
{{ $json.bottleneck }}

🚨 Intake Signal:
{{ $json.intake_data_risk_signal }}

📡 Tracker Signal:
{{ $json.tracking_signal }}

⚡ Response Gap:
{{ $json.response_gap }}

💡 Safer Workflow Idea:
{{ $json.safer_workflow_idea }}

📬 Email Subject:
{{ $json.cold_email_subject }}

📝 Score Reasoning:
{{ $json.score_reasoning }}
```

---

## 7. Airtable Field Mapping

### `Leads` table — existing fields + new med spa fields

| Airtable Field | Source | Notes |
|---|---|---|
| Company | `company_name` | Existing field |
| Website | `website` | Existing field |
| Niche | `niche` | Set to med spa sub-niche value |
| City | `city` | New field — add if not present |
| Status | `recommended_action` | Map: Loom Candidate → Hot, Email Candidate → Warm, CRM Only → Cold, Skip → Skipped |
| Priority | derived from score | HIGH if 16+, MEDIUM if 12–15, LOW if 8–11 |

### `Audits` table — existing fields + new med spa fields

| Airtable Field | Source | Notes |
|---|---|---|
| Bottleneck | `bottleneck` | Existing field |
| Opportunity 1 | `opportunity_1` | Existing field |
| Opportunity 2 | `opportunity_2` | Existing field |
| Opportunity 3 | `opportunity_3` | Existing field |
| Fit Score | `med_spa_fit_score` | Existing field — use med spa score |
| Score Reasoning | `score_reasoning` | New field — add if not present |
| Intake Data Risk Signal | `intake_data_risk_signal` | New field |
| Tracking Signal | `tracking_signal` | New field |
| Response Gap | `response_gap` | New field |
| Tool Stack Fragmentation | `tool_stack_fragmentation` | New field |
| Privacy Signal Weakness | `privacy_signal_weakness` | New field |
| Commercial Urgency | `commercial_urgency` | New field |
| Safer Workflow Idea | `safer_workflow_idea` | New field |
| Loom Hook | `loom_hook` | New field |
| Loom Script | `loom_script` | New field (long text) |
| Implementation Sprint Angle | `implementation_sprint_angle` | New field |
| Do Not Claim | `do_not_claim` | New field — for reviewer reference |

### `Messages` table — existing fields

| Airtable Field | Source | Notes |
|---|---|---|
| Email Subject | `cold_email_subject` | Existing field |
| Email Body | `cold_email_body` | Existing field |
| LinkedIn DM | `linkedin_dm` | Existing field |
| Follow-up 1 | `follow_up_1` | Existing field |
| Follow-up 2 | `follow_up_2` | Existing field |

### New Airtable fields to create

Add these to the `Audits` table before running the first med spa batch:

| Field Name | Type |
|---|---|
| Score Reasoning | Long text |
| Intake Data Risk Signal | Long text |
| Tracking Signal | Single line text |
| Response Gap | Long text |
| Tool Stack Fragmentation | Long text |
| Privacy Signal Weakness | Long text |
| Commercial Urgency | Single line text |
| Safer Workflow Idea | Long text |
| Loom Hook | Long text |
| Implementation Sprint Angle | Long text |
| Do Not Claim | Long text |

Add to `Leads` table:

| Field Name | Type |
|---|---|
| City | Single line text |
| Priority | Single select: HIGH / MEDIUM / LOW |

---

## 8. Safe Language Guardrails

### What the AI must always include

The `do_not_claim` field must contain a sentence like:

> "This is not legal advice, and I am not saying your current setup is violating any regulation. The goal is an operational cleanup: faster lead response, cleaner intake data handoffs, and fewer generic tool touchpoints."

### What the AI must never output

Blocklist — reject or re-prompt if any of these appear in `cold_email_body`, `linkedin_dm`, `loom_script`, or `loom_hook`:

- "HIPAA compliant" / "HIPAA compliance"
- "you are violating" / "illegal" / "not compliant"
- "patient data" (use "intake data" or "consultation request data")
- "leak" / "leaking data"
- "lawsuit" / "fine" / "penalty" / "OCR"
- "you are at risk of" (frame as "worth cleaning up")
- "AI will handle patient data" or "AI processes health records"

### n8n guardrail node

After parsing the AI JSON output, add a `Code` node that checks for blocklisted phrases in `cold_email_body` and `loom_script`. If found, set a field `guardrail_flag = true` and route to a Telegram alert instead of the normal approval card.

```javascript
const blocklist = [
  'hipaa compliant', 'hipaa compliance', 'you are violating', 'illegal',
  'not compliant', 'patient data', 'leaking data', 'lawsuit', 'fine',
  'penalty', 'ocr investigation', 'you are at risk of'
];

const textToCheck = [
  $json.cold_email_body,
  $json.loom_script,
  $json.loom_hook,
  $json.linkedin_dm
].join(' ').toLowerCase();

const flagged = blocklist.filter(phrase => textToCheck.includes(phrase));

return [{
  json: {
    ...$json,
    guardrail_flag: flagged.length > 0,
    guardrail_phrases: flagged
  }
}];
```

---

## 9. First Test Run Plan — Miami, Scottsdale, Austin

### Search queries per city

Run 8 queries per city = 24 total searches.

**Miami:**
```
med spa botox consultation booking Miami
medical spa online booking facial fillers Miami FL
med spa free consultation form Miami
aesthetic clinic book consultation Miami
laser hair removal med spa booking Miami
medical weight loss med spa consultation Miami
IV therapy med spa book appointment Miami
hormone therapy med spa consultation Miami
```

**Scottsdale:**
```
med spa botox consultation booking Scottsdale
medical spa online booking facial fillers Scottsdale AZ
med spa free consultation form Scottsdale
aesthetic clinic book consultation Scottsdale
laser hair removal med spa booking Scottsdale
medical weight loss med spa consultation Scottsdale
IV therapy med spa book appointment Scottsdale
hormone therapy med spa consultation Scottsdale
```

**Austin:**
```
med spa botox consultation booking Austin
medical spa online booking facial fillers Austin TX
med spa free consultation form Austin
aesthetic clinic book consultation Austin
laser hair removal med spa booking Austin
medical weight loss med spa consultation Austin
IV therapy med spa book appointment Austin
hormone therapy med spa consultation Austin
```

### Expected output targets

| Metric | Target |
|---|---|
| Raw domains found | 50–80 |
| After dedupe | 30–60 |
| After scrape (successful) | 20–40 |
| After AI audit | 20–40 |
| Score 16+ (Loom) | 3–8 |
| Score 12–15 (Email) | 5–12 |
| Score 8–11 (CRM only) | 5–15 |
| Score 0–7 (Skip) | rest |

### Success criteria for first run

- At least 5 Telegram approval cards with score 12+
- At least 2 score 16+ Loom candidates
- No guardrail flags triggered
- At least 10 emails sent after approval
- Track replies for 5 business days

### How to trigger

Send to Telegram bot:
```
/pipeline_c med_spa miami scottsdale austin
```

Or if the workflow does not yet support city/niche overrides via Telegram command, manually configure the search query array in the `Prospecting` workflow's `Set` node before triggering `/pipeline_c`.

---

## 10. n8n Implementation Notes

### Where to patch

1. **Audit Queue workflow** (`pipeline-c-v2-audit-queue-workflow.json`):
   - Replace the system prompt in the OpenAI Chat node.
   - Replace the user prompt with the med spa version above.
   - Add `response_format: { type: "json_object" }` if not already set.
   - Add the guardrail `Code` node between OpenAI output and the Telegram card node.
   - Extend the Airtable `Create Record` nodes with the new fields.

2. **Prospecting workflow** (`pipeline-c-v2-prospecting-workflow.json`):
   - Replace or extend the niche/city query arrays with the med spa queries above.
   - Add a `city` tag to each search result so it flows through to the audit output.

3. **Approval Handler workflow** (`pipeline-c-v2-approval-handler-workflow.json`):
   - No changes needed unless adding new callback types.

### Do not change

- WF-06 Telegram router — it must remain the only active Telegram Trigger.
- Gmail send logic — send only after `Approve + Send` callback, same as current.
- Airtable dedupe logic — domain/company dedupe must stay in place.

### Test before live run

1. Paste 3 sample scraped med spa pages into the prompt manually in OpenAI Playground.
2. Verify all 28 JSON fields are present and populated correctly.
3. Verify `recommended_action` matches the score tier.
4. Verify no guardrail phrases appear.
5. Then import the prompt into n8n and do a dry-run with `Execute Node` on the OpenAI node before running the full workflow.

---

*Last updated: 2026-05-06*
*Status: Specification complete. Not yet patched into n8n workflow JSON.*
*Next step: Patch pipeline-c-v2-audit-queue-workflow.json and pipeline-c-v2-prospecting-workflow.json*
