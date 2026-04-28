# 🔎 Pipeline B — LinkedIn Pain Radar

#flowops #pipeline #linkedin

> [!abstract] Goal
> Monitor LinkedIn for posts and comments where business owners express frustration with manual work, slow lead response, or operational chaos. Reach out with a personal, non-salesy message — 100 personal touches per week.

---

## 🔍 Keywords to Monitor

### Pain-Signal Keywords
```
"we're drowning in"
"manually doing"
"copy paste all day"
"spending hours on"
"can't keep up with"
"leads going cold"
"follow up manually"
"we miss leads"
"our team is overwhelmed"
"too much admin"
"wish this was automated"
"CRM is a mess"
"our process is broken"
```

### Trigger Phrases in Posts
```
"we hired a VA to..."
"I spend my weekends..."
"our team wastes time on..."
"we keep losing leads because..."
"anyone know a good tool for..."
"looking for help with automating..."
"tired of doing [X] manually"
```

### Job Post Signals (Company is hiring for ops problems)
```
"Operations Manager" hiring post
"Automation Specialist" job listing
"CRM Admin" or "Data Entry" role
```
> If they're hiring a human to do manual work, they're a perfect automation client.

---

## ⚙️ Automation Logic

```
LinkedIn monitoring (Phantombuster / Taplio / manual search)
         │
         ▼
Capture: post URL, author name, company, post content
         │
         ▼
AI scores post for pain relevance (0–10)
         │
         ├──► Score ≥ 7 → High priority → Add to outreach queue
         └──► Score < 7 → Skip
         │
         ▼
Research prospect: company size, industry, website, tech stack
         │
         ▼
AI generates personalized connection request + DM
         │
         ▼
Send (staggered, max 20–25 connection requests/day)
         │
         ▼
Follow-up sequence if no reply (Day 3, Day 7)
```

---

## ✉️ Message Template Strategy

**Connection Request Note (≤300 chars):**
> "Saw your post about [specific thing they said] — I help [their industry] businesses fix exactly that with automation. Would love to connect."

**First DM (after connecting):**
> "Hey [Name], I noticed you mentioned [specific pain from their post]. We've built systems that fix this for [similar businesses] — usually saves [X hrs/week or $X/mo]. Worth a quick look? Happy to send a short audit Loom."

**Follow-up (Day 3):**
> "Just wanted to bump this — if you're still dealing with [pain], I mapped out a quick fix for your setup specifically. No pitch, just ideas."

> [!warning] What NOT to Do
> - Never lead with "I'm a freelancer" or "I do automation"
> - Never paste your portfolio link in the first message
> - Never use generic templates — they must reference their specific post
> - Never connect + immediately pitch — always connect first, wait for acceptance, then message

---

## 🎯 Weekly Goal

| Metric | Target |
|--------|--------|
| Pain posts monitored | 200+ |
| Qualified prospects identified | 50 |
| Connection requests sent | 20–25/day (140–175/week) |
| Personal DMs sent | 50–100 |
| Responses received | 10–20 |
| Discovery calls booked | 3–7 |
| Sprint closes from LinkedIn | 1–2/month |

---

## 🏷️ LinkedIn Profile Optimization (Your Side)

> [!tip] Make Your Profile Do the Work
> - **Headline:** "I build AI automation systems for [niche] businesses | Speed-to-Lead · Ops Automation · AI Chatbots"
> - **Banner:** social proof stat ("Saved 50+ hrs/month for our clients")
> - **About:** Lead with their pain → your solution → proof → CTA
> - **Featured:** Loom demos, case studies, or audit examples
> - **Post 3x/week:** problems you solve, client wins, frameworks

---

## 🔗 Related

- [[Message Templates]] — LinkedIn DM full templates
- [[Pipeline A — Upwork Radar]] — complementary channel
- [[Pipeline C — Website Audit Generator]] — use audit as the LinkedIn opener
- [[CRM Tables]] — track all LinkedIn prospects here
