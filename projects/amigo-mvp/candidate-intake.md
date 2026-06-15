# AMIGO MVP — Candidate Intake

## Related
- [[overview]]
- [[data-model]]
- [[prompts]]
- [[decisions]]
- [[risks]]

## Telegram workflow
Commands:
- `/candidate_new`
- `/candidate_find`
- `/candidate_edit`
- `/candidate_documents`
- `/candidate_batch`
- `/candidate_actions`
- `/candidate_close`

The intake is resumable. Every answer is persisted before the next question. Managers can skip optional fields, review a section, and replace individual values.

## Required sections

### Identity and contact
- legal first and last name;
- preferred name;
- email owned by candidate;
- phone and WhatsApp;
- date of birth when required for target roles;
- citizenship and current country/city.

### Work authorization and relocation
- passport availability and expiry;
- countries with current work authorization;
- visa sponsorship requirement;
- willingness to relocate;
- earliest start date;
- preferred and excluded countries.

### Target work
- target role families and exact titles;
- acceptable adjacent roles;
- hospitality segments;
- employment type and schedule;
- salary floor and currency;
- accommodation, meals, transport, and flight requirements.

### Experience
For every job:
- employer, location, title;
- start/end dates;
- duties;
- team or service volume;
- measurable achievements;
- reason for leaving when needed.

### Education and credentials
- education;
- hospitality, food safety, aviation, first aid, language, or role certificates;
- certificate ID and expiry where relevant.

### Languages and skills
- language proficiency;
- property-management, reservation, POS, CRM, or airline systems;
- service, sales, food, safety, and operational skills.

### Application answer bank
- salary expectations;
- notice period;
- sponsorship requirement;
- relocation confirmation;
- criminal-record declarations;
- prior employment with target brands;
- relatives at target employer;
- referral/source;
- terms and privacy consent.

Sensitive or legal declarations must be answered explicitly by the candidate. Managers cannot infer them.

### Documents
- existing CV/resume;
- profile photo only when lawful and required;
- certificates;
- passport copy only when operationally necessary and separately classified as highly sensitive.

## Validation
Document generation is blocked if:
- identity or contact is missing;
- target roles or countries are empty;
- experience dates are inconsistent;
- language level is missing;
- consent is absent;
- mandatory legal/application answers are unresolved.

## Consent record
Store:
- consent text version;
- manager who recorded consent;
- candidate confirmation channel;
- timestamp;
- allowed processing purpose;
- retention deadline.

