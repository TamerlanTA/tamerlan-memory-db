# 📡 Pipeline A — Upwork Radar

#flowops #pipeline #upwork

> [!abstract] Goal
> Monitor Upwork in near-real-time for high-intent job posts matching our services. Automatically score and prioritize them. Send 50–100 **quality, personalized proposals per week**.

---

## 🔍 Keyword Groups to Monitor

### Group 1 — Automation Core
```
"automation" + "Make.com" OR "n8n" OR "Zapier"
"workflow automation"
"business automation"
"process automation"
"automate my business"
"automation consultant"
```

### Group 2 — AI/Chatbot
```
"AI chatbot"
"voice agent"
"Voiceflow"
"chatbot build"
"AI assistant"
"GPT integration"
"OpenAI API"
"conversational AI"
```

### Group 3 — CRM & Lead Systems
```
"CRM automation"
"lead follow-up automation"
"speed to lead"
"HubSpot automation"
"GoHighLevel"
"lead nurturing"
"sales automation"
```

### Group 4 — Ops & Integration
```
"Airtable automation"
"Notion automation"
"Zapier expert"
"Make.com expert"
"API integration"
"webhook"
"data sync"
"no-code automation"
```

---

## ⚙️ Automation Logic

```
Upwork RSS Feed / API → Triggered every 30 min
         │
         ▼
Parse job title + description + budget + client history
         │
         ▼
AI Scoring Engine (0–100)
         │
         ├──► Score ≥ 70 → High Priority → Slack alert + add to proposal queue
         ├──► Score 40–69 → Medium → Add to review list
         └──► Score < 40 → Skip
         │
         ▼
For High Priority: AI drafts personalized proposal
         │
         ▼
Review → Edit → Submit (human in the loop)
```

---

## 📊 Fit Score Criteria

| Signal | Weight | Notes |
|--------|--------|-------|
| Keywords match core offer | 25 | Speed-to-Lead / Chatbot / Ops Sprint |
| Budget $500+ | 20 | Filter out low-budget jobs |
| Client has payment verified | 15 | Reduces no-show risk |
| Client has >70% hire rate | 15 | They actually hire |
| Posted < 6 hours ago | 10 | Fresh = higher visibility |
| Job description has clear pain | 10 | Not just "build a zap" |
| Fixed-price preferred | 5 | Better for scope control |

**Max Score: 100**
- 70–100: Auto-alert + priority proposal
- 40–69: Queue for manual review
- 0–39: Skip

---

## 📋 Output Fields (per job)

| Field | Source |
|-------|--------|
| Job Title | Scraped |
| Client Budget | Scraped |
| Client Hire Rate % | Scraped |
| Post Time | Scraped |
| Fit Score | AI calculated |
| Match Keywords | AI extracted |
| Suggested Offer | AI mapped |
| Draft Proposal | AI generated |
| Status | Manual update |

---

## ✍️ Proposal Template Structure

```
Hook (1 sentence): Reference their specific pain/situation
Problem reframe (1 sentence): Show you understand the deeper issue
Proof (1–2 sentences): Relevant experience or result
CTA (1 sentence): Low friction next step
Optional: Loom link or audit offer
```

> [!tip] Proposal Length Sweet Spot
> 100–180 words. Long enough to show expertise. Short enough to actually get read. Never use bullet points in proposals.

---

## 🎯 Weekly Goal

| Metric | Target |
|--------|--------|
| Jobs monitored/week | 500+ |
| High-priority proposals sent | 50–100 |
| Response rate | 15–25% |
| Discovery calls booked | 5–10 |
| Sprint closes from Upwork | 2–4/month |

---

## 🔗 Related

- [[Message Templates]] — Upwork proposal full template
- [[Pipeline D — Demo Library]] — attach relevant demo to proposals
- [[Discovery Call Script]] — for calls booked through Upwork
- [[Speed-to-Lead System]] · [[Ops Automation Sprint]] · [[AI Chatbot & Voice Agent]] — offers to match to jobs
