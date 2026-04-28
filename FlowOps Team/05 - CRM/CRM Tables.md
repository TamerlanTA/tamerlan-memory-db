# 🗃️ CRM Tables Structure

#flowops #crm #operations

---

## Table 1 — Leads

| Field | Type | Notes |
|-------|------|-------|
| Lead name | Text | |
| Company | Text | |
| Website | URL | |
| Source | Select | Upwork / LinkedIn / Audit / Referral / Inbound |
| Niche | Select | |
| Pain signal | Text | 1–2 sentence summary |
| Offer match | Select | Speed-to-Lead / Sprint / Chatbot / Retainer |
| Fit score | Number | 1–10 |
| Budget estimate | Number | $ |
| Contact URL | URL | Profile or job link |
| Email | Email | |
| LinkedIn | URL | |
| Status | Select | New / Contacted / In Progress / Won / Lost / Nurture |
| Next action | Text | |
| Last contacted | Date | |
| Follow-up date | Date | |
| Notes | Long text | |

---

## Table 2 — Opportunities

| Field | Type | Notes |
|-------|------|-------|
| Lead | Link | → Leads table |
| Automation opportunity | Text | |
| Problem | Text | |
| Suggested workflow | Text | |
| Tools needed | Text | |
| Estimated value | Number | Annual $ |
| Estimated build price | Number | $ |
| Retainer potential | Number | $/month |

---

## Table 3 — Messages

| Field | Type | Notes |
|-------|------|-------|
| Lead | Link | → Leads table |
| Channel | Select | Upwork / LinkedIn / Email / WhatsApp |
| Message type | Select | Proposal / DM / Cold Email / Follow-up / Retainer Pitch |
| Draft | Long text | |
| Sent? | Checkbox | |
| Response? | Select | No reply / Positive / Negative / Meeting booked |
| Follow-up date | Date | |

---

## Table 4 — Demos

| Field | Type | Notes |
|-------|------|-------|
| Demo name | Text | |
| Niche | Select | |
| Problem solved | Text | |
| Loom URL | URL | |
| Relevant offer | Link | → Offers |
| When to use | Text | Trigger context |

---

## See Also
- [[Pipeline A — Upwork Radar]]
- [[Sales Steps]]
- [[What to Do First]]
