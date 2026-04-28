# 🗃️ CRM Tables

#flowops #crm #tracking

> [!abstract] System Overview
> Four interconnected tables track every prospect and client through the FlowOps pipeline. Use Airtable, Notion, or any database tool. Each record should link across tables where relevant.

---

## Table 1 — Leads

Tracks everyone who has been identified as a potential client, before any call.

| Field | Type | Notes |
|-------|------|-------|
| **Name** | Text | Full name |
| **Company** | Text | Business name |
| **Website** | URL | For audit reference |
| **Source** | Select | Upwork / LinkedIn / Cold Email / Referral / Inbound |
| **Niche** | Select | Real estate / Home services / Agency / E-commerce / Clinic / Coach / Other |
| **Pain Signal** | Long text | What they said or what we found in their setup |
| **Likely Offer** | Select | Speed-to-Lead / Ops Sprint / Chatbot / Voice Agent / Retainer |
| **Fit Score** | Number (0–10) | Based on pain clarity, budget signals, urgency |
| **Status** | Select | New / Contacted / Replied / Qualified / Called / Proposal Sent / Closed / Lost / Nurture |
| **First Contact Date** | Date | When we first reached out |
| **Last Activity** | Date | Auto-updated |
| **LinkedIn URL** | URL | Profile link |
| **Upwork Job URL** | URL | If from Upwork |
| **Notes** | Long text | Anything relevant from research or conversations |

---

## Table 2 — Opportunities

Tracks active deals — prospects who have had a discovery call or received a proposal.

| Field | Type | Notes |
|-------|------|-------|
| **Name** | Link → Leads | Linked to lead record |
| **Offer** | Select | Which offer was proposed |
| **Proposed Value** | Currency | Deal size |
| **Stage** | Select | Discovery / Proposal Sent / Negotiating / Won / Lost |
| **Discovery Call Date** | Date | When call happened |
| **Proposal Sent Date** | Date | When proposal was sent |
| **Decision Date** | Date | Expected or actual close date |
| **Pain Summary** | Long text | Core problem uncovered in discovery |
| **ROI Presented** | Text | The ROI calculation used in proposal |
| **Decision Maker** | Text | Name and role of who decides |
| **Objections Raised** | Long text | What they pushed back on |
| **Close Probability %** | Number | Your estimate |
| **Won/Lost Reason** | Text | Post-close reflection |
| **Linked Project** | Link | If won, link to active project |
| **Notes** | Long text | Follow-up actions, context |

---

## Table 3 — Messages

Tracks every outreach message sent, for A/B testing and follow-up management.

| Field | Type | Notes |
|-------|------|-------|
| **Lead** | Link → Leads | Who the message went to |
| **Channel** | Select | Upwork / LinkedIn / Email / Referral |
| **Template Used** | Select | Which template was used (links to [[Message Templates]]) |
| **Date Sent** | Date | |
| **Message Text** | Long text | Full message content |
| **Opened** | Checkbox | Did they open it? (if trackable) |
| **Replied** | Checkbox | Did they reply? |
| **Reply Sentiment** | Select | Positive / Neutral / Negative / No Reply |
| **Follow-up 1 Sent** | Date | Day 3 follow-up |
| **Follow-up 2 Sent** | Date | Day 7 follow-up |
| **Outcome** | Select | Call Booked / Not Interested / No Reply / Nurture |
| **Notes** | Text | Anything notable about the reply |

---

## Table 4 — Demos

Tracks every demo sent and its performance, to optimize which demos close deals.

| Field | Type | Notes |
|-------|------|-------|
| **Demo Name** | Text | From [[Pipeline D — Demo Library]] |
| **Offer** | Select | Which offer the demo covers |
| **Niche** | Select | Which niche it targets |
| **Loom URL** | URL | |
| **Date Created** | Date | |
| **Times Sent** | Number | Total sends |
| **Views** | Number | Total Loom views |
| **Replies After Demo** | Number | How many prospects replied after watching |
| **Calls Booked** | Number | Discovery calls attributed to this demo |
| **Deals Closed** | Number | Revenue attributed to this demo |
| **Close Rate %** | Formula | Deals Closed / Times Sent |
| **Notes** | Text | What works, what to improve |

---

## 📊 CRM Health Metrics (Weekly Review)

> [!tip] Weekly CRM Audit
> Every Monday, review these numbers to understand pipeline health:

| Metric | Target |
|--------|--------|
| New leads added this week | 50+ |
| Outreach messages sent | 50–100 |
| Reply rate | 15–25% |
| Discovery calls held | 3–7 |
| Proposals sent | 2–5 |
| Proposals closed | 1–2 |
| Retainers active | Cumulative growth |

---

## 🔗 Related

- [[Pipeline A — Upwork Radar]] → populates Leads table
- [[Pipeline B — LinkedIn Pain Radar]] → populates Leads table
- [[Pipeline C — Website Audit Generator]] → populates Leads table
- [[Pipeline D — Demo Library]] → populates Demos table
- [[Sales Steps]] → drives Opportunities table progression
- [[Message Templates]] → referenced in Messages table
