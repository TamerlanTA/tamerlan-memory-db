# Session 2026-06-22 — Partner-Approved CV Correction

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]
- [[risks]]

## What was done
- Read the production correction request from the attached pasted text.
- Reworked worker document data from generic fields into grounded blocks:
  - `header`;
  - `photo`;
  - `about_me`;
  - `personal_info`;
  - `experience[]`;
  - `education[]`;
  - `languages[]`;
  - `other[]`.
- Updated DOCX template generation so layout order is:
  - photo placeholder;
  - candidate name;
  - target role;
  - personal/contact info;
  - ABOUT ME;
  - EXPERIENCE;
  - EDUCATION;
  - LANGUAGES;
  - ADDITIONAL INFORMATION / OTHER only when grounded data exists.
- Removed `Hospitality Strengths`, unsupported skills, and pseudo-experience such as `Hospitality readiness profile`.
- Added `PHOTO REQUIRED` placeholder. Missing photo does not fail generation.
- Updated OpenAI schema and prompt to prohibit invented skills, employers, experience, certificates, software, courses, achievements, dates, education names, and responsibilities.
- Added grounding in `groundCvData()`:
  - strips ungrounded generated experience when no stored `work_experience` exists;
  - strips ungrounded `other`;
  - normalizes unsafe/too-short About Me output back to deterministic grounded fallback.
- Updated tests for:
  - About Me below header;
  - no Hospitality Strengths;
  - exact EXPERIENCE title;
  - no fake readiness profile;
  - missing photo report without failure;
  - honest entry-level CV;
  - real work experience rendering from stored facts.
- Deployed `worker-documents` to Railway.
- Regenerated controlled candidate CV.

## Key findings
- The earlier CV quality improvement still violated partner rules by inferring skills and creating pseudo-experience.
- Current candidate schema does not yet store real workplaces or candidate photo, so the corrected CV honestly shows:
  - `PHOTO REQUIRED`;
  - `No formal work experience recorded yet.`
- Final generated sample document version: `c20ddaa5-15a7-4aa9-9314-8db68adec1ab`, status `pending_approval`, validation errors `[]`.
- PDF text extraction verified:
  - PHOTO REQUIRED;
  - Tamerlan Tog / Waiter;
  - ABOUT ME below header;
  - EXPERIENCE;
  - no Hospitality Strengths;
  - no fake experience;
  - no unsupported Additional Information.
- PNG visual verification was also done from `/tmp/amigo-tamerlan-grounded-cv-final.pdf`.

## Blockers
- Real work experience storage/intake is not implemented yet.
- Candidate photo upload/storage/rendering is not implemented yet.
- Current `work_experience` is wired as an empty JSON placeholder in the worker until schema/intake support is added.

## Next steps
- Add candidate photo upload/storage support.
- Add structured work experience intake/storage.
- Then regenerate CVs with real photo and real experience data.
