# 🌐 Pipeline C — Website Audit Generator

#flowops #pipeline #cold-outreach #audit

> [!abstract] Goal
> Automatically generate personalized website audits for target businesses, identifying specific automation opportunities visible from the outside. Use the audit as a hyper-personalized cold outreach opener that proves expertise before asking for anything.

---

## 🎯 Target Niches

| Niche | Why They Work |
|-------|--------------|
| Real estate agencies | Websites with contact forms, listings — easy to audit |
| Home services (HVAC, roofing, plumbing) | Slow response time is industry-wide known pain |
| Med spas & dental clinics | Booking systems often broken or manual |
| Law firms & financial advisors | Lead response is typically poor |
| Marketing agencies | Usually have no automation in their own ops |
| E-commerce stores | Abandoned cart, follow-up — easy wins to spot |
| Coaches & consultants | No CRM, manual booking, no follow-up |

---

## 🔍 What to Analyze (Publicly Visible)

### Lead Capture
- [ ] Does the site have a contact form?
- [ ] Is there a chatbot/live chat widget?
- [ ] Is there a clear CTA above the fold?
- [ ] Is there a lead magnet (ebook, free audit, etc.)?
- [ ] Is there a booking widget (Calendly, etc.)?

### Follow-Up Signals
- [ ] Do they have a newsletter signup?
- [ ] Is there any automation visible (pop-up timing, exit intent)?
- [ ] Do they respond to Google Reviews publicly?

### Speed & Response
- [ ] How fast does the contact form respond? (test with a dummy lead)
- [ ] Is there a 24/7 presence or just business hours?

### Tech Stack (via BuiltWith or Wappalyzer)
- [ ] What CRM are they using?
- [ ] What email platform?
- [ ] Any automation tools visible (Zapier, Make, etc.)?
- [ ] Any booking system?

---

## ⚙️ Automation Logic

```
Target list (company name + website + niche) in Airtable/Google Sheets
         │
         ▼
Scraper visits website → captures forms, CTAs, tech stack, chatbot presence
         │
         ▼
AI analyzes data → generates 3 specific automation opportunities
         │
         ▼
Generates personalized Loom script OR written audit summary
         │
         ▼
Opener message drafted (email or LinkedIn)
         │
         ▼
Outreach sent → track opens/replies
```

---

## 📝 Audit Output Template

```
Business: [Company Name]
Website: [URL]
Audit Date: [Date]

TOP 3 AUTOMATION OPPORTUNITIES:

1. [Specific finding]: "Your contact form doesn't have instant follow-up. 
   Leads likely wait hours before hearing from you. A Speed-to-Lead 
   system would cut that to under 60 seconds."

2. [Specific finding]: "No booking widget visible — prospects who want 
   to talk have to call during business hours. An embedded Calendly + 
   AI pre-qualification would convert more browsers to booked calls."

3. [Specific finding]: "No chatbot or FAQ automation on site. Given 
   [niche] typically gets the same 5 questions repeatedly, a trained 
   AI chatbot would free up significant team time."

ESTIMATED MONTHLY VALUE: $[X,XXX] in recovered time/revenue
```

---

## ✉️ Opener Messages

**Cold Email Subject Lines:**
- "Quick audit of [Company] — 3 things I noticed"
- "Found something on [Company]'s website"
- "[Name], I ran your site through our automation scanner"

**Email Body:**
> "Hi [Name],
>
> I ran [Company]'s website through our automation audit tool and noticed a few things that are probably costing you leads every week.
>
> Specifically: [ONE specific finding with detail].
>
> I put together a quick 2-minute Loom showing exactly what I mean and what a fix looks like. Would it be useful to send it over?
>
> — [Your name]"

**LinkedIn version:**
> "Hey [Name] — I audited [Company]'s site and spotted [specific thing]. Most [niche] businesses I work with don't realize how many leads they're losing at that stage. Happy to share a quick Loom if it would be helpful."

---

## 🎯 Weekly Goal

| Metric | Target |
|--------|--------|
| Audits generated | 50–100/week |
| Outreach messages sent | 50–100/week |
| Response rate | 10–20% |
| Calls booked | 3–7/week |

---

## 🔗 Related

- [[Message Templates]] — Cold email and LinkedIn audit opener
- [[Pipeline D — Demo Library]] — attach niche demo to audit outreach
- [[Speed-to-Lead System]] — most common finding from audits
- [[AI Chatbot & Voice Agent]] — second most common finding
- [[Discovery Call Script]] — for calls booked via audit outreach
