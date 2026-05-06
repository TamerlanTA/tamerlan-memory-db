# Med Spa HIPAA Intake Launch Kit

#flowops #scaling #medspa #hipaa #pipeline-c #sales-kit

## Related
- [[00 - Scaling Hub]]
- [[01 - HIPAA-Safe Intake Cleanup Sprint]]
- [[../01 - Strategy/validation-hipaa-safe-intake-automation-2026-05-06]]
- [[../02 - Offers/Speed-to-Lead System]]
- [[../02 - Offers/AI Chatbot & Voice Agent]]
- [[../03 - Acquisition Pipelines/Pipeline C — Website Audit Generator]]
- [[../04 - Sales Process/Message Templates]]

## Content

## Goal

Create the first practical FlowOps sales kit for testing **HIPAA-Safe Intake + Follow-up Cleanup** against US med spas.

The goal is not to accuse prospects of legal problems. The goal is to show a concrete operational opportunity:

```text
faster lead response + cleaner intake data flow + fewer risky generic handoffs
```

## Target niche

**Primary:** med spas / aesthetic clinics in the US.

Why med spas first:
- they care about lead response and booking speed;
- they usually run paid ads and website conversion flows;
- they often use forms, booking widgets, chat, SMS, pixels, CRMs, and email marketing;
- many collect sensitive treatment interests or health-adjacent intake details;
- buying decision can be faster than traditional clinics.

## Prospect filters

Good fit:
- has online booking or consultation request form;
- offers injectables, laser, weight loss, hormone, skin, or body treatments;
- has Meta/Google/TikTok ad signals or remarketing pixels;
- has chat widget, quiz, or lead magnet;
- no clear privacy/HIPAA language near intake;
- follow-up appears manual or email-only;
- multiple locations or high-ticket services.

Bad fit:
- only phone number, no form or booking path;
- enterprise medical group with heavy IT/legal procurement;
- website is under construction;
- no reachable owner/manager/contact email;
- very small solo operator with no visible paid acquisition.

## Pipeline C search queries

Use these as the first niche query pool:

```text
med spa botox consultation booking [city]
medical spa online booking facial fillers [city]
med spa free consultation form [city]
aesthetic clinic book consultation [city]
botox clinic consultation request [city]
laser hair removal med spa booking [city]
medical weight loss med spa consultation [city]
IV therapy med spa book appointment [city]
```

Suggested first cities:
- Miami
- Austin
- Dallas
- Scottsdale
- Los Angeles
- San Diego
- Denver
- Nashville
- Atlanta
- Tampa

## Audit rubric

Score each prospect from 0-20.

| Category | Points | What to check |
|---|---:|---|
| Intake form sensitivity | 0-4 | Does the form ask treatment interest, medical concern, condition, preferred procedure, or symptoms? |
| Tracker / pixel exposure | 0-4 | Are ad pixels, analytics, chat widgets, or marketing scripts present near conversion pages? |
| Booking and follow-up gap | 0-4 | Is booking manual, delayed, email-only, or unclear after form submission? |
| Tool-stack fragmentation | 0-3 | Are there multiple disconnected tools: website form, scheduler, CRM, email, SMS, chat? |
| Privacy signal weakness | 0-3 | Is privacy/HIPAA language missing, generic, buried, or not connected to intake? |
| Commercial urgency | 0-2 | High-ticket services, paid ads, multi-location, or clear lead volume signals. |

Interpretation:
- **16-20:** strong Loom candidate, likely worth manual review.
- **12-15:** good cold email candidate.
- **8-11:** keep in CRM, lower priority.
- **0-7:** skip unless there is a unique signal.

## Audit output fields

Add these fields to the audit output for this niche:

| Field | Meaning |
|---|---|
| `med_spa_fit_score` | 0-20 score from rubric |
| `intake_data_risk_signal` | What kind of sensitive/health-adjacent data might enter the form |
| `tracking_signal` | Visible tracker/chat/analytics concern, if detectable |
| `response_gap` | What happens after the visitor submits or books |
| `safer_workflow_idea` | One concrete rebuild idea |
| `loom_hook` | First 10 seconds of Loom |
| `do_not_claim` | Guardrail text: no legal accusation or compliance promise |

## Loom structure

Target length: 90-150 seconds.

### 1. Hook

```text
Hey [Name], I took a quick look at [Med Spa] because med spas usually have two competing needs: respond to new consultation requests fast, but keep the intake path clean and controlled.
```

### 2. Specific observation

```text
I noticed your site uses [form / booking widget / chat / consultation CTA]. That is good for conversion, but it also means treatment-interest or consultation data may be moving through a few different tools.
```

### 3. Operational risk, not legal claim

```text
This is not legal advice and I am not saying anything is wrong. The operational question is: if someone asks where a consultation request went, which tools touched it, who saw it, and how follow-up happened, can the team answer that quickly?
```

### 4. Safer automated workflow

```text
The cleaner version is: form or booking request comes in, the lead is logged with source and consent details, the team gets an instant notification, the client gets a fast but controlled reply, and the CRM keeps a simple record of the handoff.
```

### 5. CTA

```text
I can map this in a short paid cleanup audit, or rebuild the intake/follow-up workflow in a 5-7 day sprint. If helpful, I can send a simple one-page version of what I would change.
```

## Cold email 1

Subject options:
- `Quick intake idea for [Company]`
- `Question about [Company]'s consultation flow`
- `Small med spa intake cleanup idea`

```text
Hi [Name],

I was looking at [Company]'s website and noticed [specific observation: e.g. the consultation form / booking widget / treatment request flow].

For med spas, the tricky part is usually balancing speed and control: new consultation requests need a fast reply, but the intake data should not be scattered across random forms, chat tools, email threads, and CRM notes.

This is not legal advice, but I help clinics clean up that workflow: map where the request goes, tighten the handoffs, and automate the response + CRM update path.

Worth sending you a quick 2-min Loom with what I noticed?

Tamerlan
FlowOps
```

## Cold email 2, stronger pain angle

Subject options:
- `Can your team trace a consultation request?`
- `Small workflow question`

```text
Hi [Name],

Quick question: if a new consultation request comes through [Company]'s site, can your team quickly see:

- where the lead came from;
- which tool captured it;
- who followed up;
- what message was sent;
- whether the request made it into the CRM?

I build simple intake/follow-up systems for med spas so new leads get answered quickly without the data trail becoming messy.

Happy to record a short Loom showing the workflow I would clean up on your site.

Worth sending?

Tamerlan


```

## LinkedIn DM

```text
Hey [Name], I took a quick look at [Company]'s consultation flow.

Med spas usually have a tricky ops problem: you want fast replies to new treatment inquiries, but the data trail can get messy across forms, booking tools, chat, email, and CRM.

I build cleanup sprints for that intake/follow-up path. Worth sending a 2-min Loom with what I noticed?
```

## Follow-up 1

```text
Hey [Name],

Just following up. One small thing I noticed: [specific observation].

The fix is usually not a full new system. It is a cleaner handoff from intake -> instant team alert -> controlled reply -> CRM record.

Still happy to send the 2-min Loom.
```

## Follow-up 2

```text
Hey [Name],

Closing the loop here. I am testing a small cleanup audit for med spas: mapping the consultation request flow and showing where response time or data handoffs can be tightened.

If that is useful, I can send the quick audit. If not, no worries.
```

## Paid audit offer

Use after a reply.

```text
Perfect. The light version is a paid cleanup audit.

I review the consultation/intake path, identify where data and follow-up handoffs get messy, and send:

- a simple data-flow map;
- 3-5 cleanup opportunities;
- one recommended safer workflow;
- a short Loom walkthrough;
- a sprint quote if you want me to implement it.

It is $500 fixed and usually takes 48 hours.
```

## Sprint offer

Use after audit or strong discovery call.

```text
The sprint version is 5-7 working days.

I rebuild the intake/follow-up workflow around your existing tools:

- consultation request captured cleanly;
- source and consent/context stored;
- instant team notification;
- fast controlled reply to the prospect;
- CRM record updated;
- follow-up sequence created;
- Loom handoff and simple SOP.

For this kind of setup, the sprint usually lands between $1,500 and $4,000 depending on tools and channels.
```

## Discovery questions

Ask these before quoting implementation:

- Where do new consultation requests currently arrive?
- What form, booking, chat, CRM, and SMS/email tools do you use?
- Who follows up with new inquiries?
- How fast does the first reply usually go out?
- Do you run paid ads to the consultation page?
- Do you store treatment interests or medical-adjacent notes in the CRM?
- Do you already have approved privacy/HIPAA language from counsel?
- Do you have a BAA-capable form/CRM/SMS provider, or should we only map options?

## Implementation concept

Default architecture:

```text
Website form / booking request
-> intake parser
-> source + context log
-> CRM record
-> internal notification
-> controlled first reply
-> booking/follow-up task
-> audit trail dashboard
```

Possible tools:
- Airtable or HubSpot for CRM/logging;
- HIPAA-capable form/booking provider where needed;
- Gmail/Google Workspace only if appropriate for the client's setup;
- SMS only through approved provider/client account;
- n8n/Make for workflow glue;
- OpenAI only for non-sensitive classification unless client has approved architecture.

## Guardrails

Always say:
- "This is not legal advice."
- "I am not saying your current setup is violating anything."
- "The goal is to clean up the operational data flow."
- "Use counsel-approved privacy/HIPAA language."

Never say:
- "I will make you HIPAA compliant."
- "Your site is illegal."
- "You are leaking patient data."
- "AI will handle patient data" unless the architecture has been explicitly approved.

## First run checklist

- [ ] Pick 3 cities.
- [ ] Run 8-12 searches per city.
- [ ] Filter to 30-50 prospects.
- [ ] Score with the 0-20 rubric.
- [ ] Send emails only to score 12+.
- [ ] Record Looms only for score 16+.
- [ ] Track replies in FlowOps CRM.
- [ ] After 50 sends, review reply rate and objections.

