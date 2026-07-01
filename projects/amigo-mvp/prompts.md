# AMIGO MVP — Prompts

## Related
- [[overview]]
- [[current-state]]
- [[candidate-intake]]
- [[technical-architecture]]
- [[next-steps]]
- [[phase-6-execution-plan]]

## Prompt policy
- Prompts operate only on stored candidate facts.
- Output must follow a versioned JSON schema.
- Missing facts return `null` or a clarification item.
- The model must not infer employers, dates, metrics, certifications, legal status, or language level.
- Generation temperature stays low.
- Every generated field stores its source field IDs.
- Prompt and model versions are recorded in `generation_runs`.

## Candidate normalization prompt
Purpose: translate Russian intake into professional English without changing meaning.

Required output:
```json
{
  "professional_summary": {
    "text": "",
    "source_field_ids": []
  },
  "experience": [
    {
      "source_experience_id": "",
      "title": "",
      "employer": "",
      "dates": "",
      "bullets": [
        {
          "text": "",
          "source_field_ids": []
        }
      ]
    }
  ],
  "skills": [],
  "languages": [],
  "clarifications": []
}
```

System instruction:
```text
You are preparing an English hospitality CV from verified candidate records.
Translate and improve clarity, but preserve every factual claim.
Never invent metrics, responsibilities, dates, employers, systems, certificates,
language levels, work authorization, or achievements.
When a useful fact is missing, add a clarification instead of filling the gap.
Return only data that matches the supplied JSON schema.
```

## Validation prompt
Purpose: compare generated content with source facts.

Output:
```json
{
  "valid": true,
  "unsupported_claims": [],
  "contradictions": [],
  "missing_critical_facts": [],
  "language_issues": []
}
```

Any unsupported claim blocks manager approval until removed or supported by a new source fact.

## Reusable text blocks
The application answer bank uses deterministic templates for:
- availability;
- relocation;
- sponsorship;
- salary;
- notice period;
- referral source;
- privacy consent.

No per-vacancy cover-letter generation is included in MVP.

## Phase 6 agent kickoff prompt
Use this prompt for any coding agent starting Phase 6 work:

```md
Read AMIGO MVP memory first:
- overview.md
- current-state.md
- decisions.md
- risks.md
- next-steps.md
- roadmap.md
- technical-architecture.md
- data-model.md
- integrations.md
- phase-6-execution-plan.md

You are implementing Phase 6 only. Follow [[phase-6-execution-plan]] in order and do not skip batches.

Start with the next incomplete batch from the plan. Do not implement universal ATS auto-apply. Do not submit real applications until duplicate prevention, application persistence, evidence handling, worker state handling, and manager approval checks are implemented and validated. CAPTCHA, OTP, assessments, login/account creation, and unknown mandatory questions must become NeedsAction/manual tasks.

Before editing, inspect the files named in the current batch. Preserve unrelated changes. After implementation, report changed files, validation commands, evidence, residual risks, and memory updates.
```
