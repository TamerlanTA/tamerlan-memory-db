
# Project Memory Operating Protocol

  

Primary memory vault:

`/Users/tamerlan/Documents/TamerMemoryDB/Tamerlan Memory DB`

  

## Global rule

This vault is the source of truth for continuity across sessions and across agents.

  

Before any non-trivial task:

- read the relevant memory

- identify whether the work belongs to an existing project, general knowledge, a reusable pattern, a general decision, or temporary context

  

After any significant work:

- write back concise, operational updates to the correct memory location

- do not create unnecessary project folders

- preserve continuity for future sessions and other agents

  

Do not treat every meaningful request as a new project.

  

---

  

## Memory classification rule

  

Before writing memory, classify the work into exactly one of these categories:

  

### 1. Project work

Use a project folder only if the work is clearly part of an ongoing multi-session effort with its own:

- goal

- evolving state

- decisions

- risks or blockers

- next steps

  

Examples:

- product build

- automation implementation

- milestone work

- long-running debugging stream

- ongoing client delivery

  

### 2. General reusable knowledge

If the note is useful in the future but does not belong to an ongoing project, store it in:

`knowledge/`

  

Examples:

- explanations

- technical notes

- setup instructions

- one-off research worth keeping

- reusable reference material

  

### 3. Reusable workflow, pattern, or method

If the note describes a repeatable approach, working style, prompt pattern, or method, store it in:

`patterns/` or `prompts/`

  

Examples:

- debugging patterns

- milestone review patterns

- proposal-writing patterns

- prompt templates

- handoff structures

  

### 4. General decision

If the note captures a stable operating decision not tied to one specific project, store it in:

`decisions/`

  

Examples:

- routing rules between agents

- batch-first execution rules

- memory sync conventions

- review thresholds

  

### 5. Temporary or low-value context

If the note is short-lived, casual, low-value, or not worth long-term retention, store it in:

`inbox.md`

or do not store it at all.

  

Examples:

- casual chat

- trivial questions

- low-value temporary thoughts

- one-off requests with no future reuse

  

---

  

## Project creation rule

  

Do not create a new project folder for every non-trivial request.

  

Create a new project folder only if at least one of the following is true:

- the user explicitly says this is a project

- the work will likely continue across multiple sessions

- the task has a distinct deliverable or workstream with evolving state

- the task requires tracking decisions, risks, and next steps over time

- the work is part of an ongoing client delivery or long-running build/debug effort

  

When uncertain, do not create a new project.

  

Prefer:

- `knowledge/`

- `patterns/`

- `prompts/`

- `decisions/`

- `inbox.md`

  

unless the work clearly qualifies as project work.

  

---

  

## Project size rule

  

### Small or emerging workstreams

A small or early-stage project may be tracked first as a single markdown file:

  

`/Users/tamerlan/Documents/TamerMemoryDB/Tamerlan Memory DB/projects/<project-name>.md`

  

Use this for:

- small but real workstreams

- early-stage ideas that may become larger later

- short client tasks that may or may not expand

  

### Large or ongoing projects

For large, ongoing, or complex work, use the canonical project folder structure:

  

`/Users/tamerlan/Documents/TamerMemoryDB/Tamerlan Memory DB/projects/<project-name>/`

- `overview.md`

- `current-state.md`

- `decisions.md`

- `risks.md`

- `next-steps.md`

- `prompts.md`

- `sessions/`

  

Promote a small project file into the full folder structure when the work becomes clearly:

- ongoing

- multi-session

- complex

- risk-bearing

- decision-heavy

  

---

  

## If project memory does not exist

  

### For clearly ongoing or large project work

If the relevant large-project folder or files do not exist:

1. Create the project folder

2. Create missing canonical files with concise initial content

3. Continue using that structure going forward

  

### For small or uncertain workstreams

Do not immediately create a full project folder.

Prefer creating:

- a single project markdown file, or

- a knowledge/pattern/decision note instead

  

Bias toward minimal structure first unless the need for full project continuity is obvious.

  

---

  

## Before starting any non-trivial task

  

### Step 1: Read global memory

Read:

- `/Users/tamerlan/Documents/TamerMemoryDB/Tamerlan Memory DB/agent-memory.md`

- `/Users/tamerlan/Documents/TamerMemoryDB/Tamerlan Memory DB/current-focus.md` when relevant

- `/Users/tamerlan/Documents/TamerMemoryDB/Tamerlan Memory DB/routing-rules.md` when relevant

  

### Step 2: Classify the work

Decide whether this task belongs to:

- an existing project

- general knowledge

- a reusable pattern/prompt

- a general decision

- temporary context

  

### Step 3: Read the relevant memory

If it is project work:

  

#### For large project folders, read:

- `overview.md`

- `current-state.md`

- `decisions.md`

- `risks.md`

- `next-steps.md`

  

Also read the most recent relevant session notes from that project's `sessions/` folder when available.

  

#### For small single-file projects:

Read that project markdown file.

  

If it is not project work, read the most relevant existing note(s) in:

- `knowledge/`

- `patterns/`

- `prompts/`

- `decisions/`

  

Do not begin substantial work until the relevant state is understood.

  

---

  

## After completing significant work

  

First, write memory back to the correct category.

  

### If the work belongs to a large project

Always:

1. Create or update a short session note in the project's `sessions/` folder

2. Record:

- what was done

- key findings

- blockers

- next steps

  

Additionally update project files as needed:

- Update `current-state.md` if the actual project status changed

- Update `decisions.md` if an important decision was made or confirmed

- Update `risks.md` if a new risk/blocker appeared or an old one was resolved

- Update `next-steps.md` if priorities or immediate actions changed

- Update `prompts.md` only when a prompt is genuinely reusable

- Update `overview.md` only when the fundamental understanding of the project changed

  

### If the work belongs to a small single-file project

Update that project file with:

- current status

- key decisions

- blockers

- next steps

  

### If the work is general reusable knowledge

Write or update a note in:

`knowledge/`

  

### If the work is a reusable pattern or prompt

Write or update a note in:

`patterns/` or `prompts/`

  

### If the work is a general operating decision

Write or update a note in:

`decisions/`

  

### If the work is temporary or low-value

Write only to:

`inbox.md`

or do not persist it.

  

---

  

## Writing rules

- Keep notes concise, concrete, and operational

- Prefer markdown

- Do not overwrite important historical context

- Preserve continuity for future sessions and other agents

- Do not store trivial chat or low-value casual questions in project memory

- Optimize notes for fast onboarding by another agent

- Prefer a few strong notes over many weak ones

- Avoid memory spam

- When uncertain, store less, not more

  

---

  

## Session note naming

Use descriptive filenames such as:

`YYYY-MM-DD-short-topic.md`

  

Examples:

- `2026-04-15-header-refinement-and-eod-sync.md`

- `2026-04-15-kommo-payment-tag-debug.md`

  

---

  

## Daily maintenance rule

At the end of a meaningful work block or at the end of the day, synchronize memory for the relevant category.

  

### For large projects

Ensure:

- session notes are written

- `current-state.md` reflects reality

- `risks.md` reflects current blockers and residual risks

- `next-steps.md` reflects the true immediate priorities

  

### For small projects

Ensure the single project file reflects:

- current status

- open blockers

- next steps

  

### For non-project work

Only update the relevant knowledge/pattern/decision note if the result is truly worth keeping.

  

---

  

## Sync commands

  

If the user asks for:

### "memory sync"

- update the relevant memory location

- if project work: write a concise session note and update current-state, risks, and next-steps if needed

- if non-project work: update the appropriate knowledge/pattern/decision note if relevant

  

### "handoff sync"

- prepare memory so another agent can continue immediately without rereading the full chat

- include essential progress, decisions, blockers, changed files if relevant, and next steps

- write a concise handoff-oriented session note if this is project work

- for non-project work, update the correct note only if the result is reusable

  

### "end-of-day sync"

- perform a full daily memory update for the relevant category

- for project work, ensure current-state, risks, and next-steps reflect reality

- write a concise end-of-day session note for project work

- avoid creating new project folders during end-of-day sync unless the work clearly qualifies as a true project

  

---

  

## Memory graph rule

  

When reading or writing memory in Obsidian:

- preserve and expand meaningful wikilinks

- do not create isolated notes when a real connection exists

- do not create artificial links just to increase graph density

- every project session note must link to the project's core notes

- every core project note must include a `## Related` section linking to other core project notes

- prefer stable canonical filenames so links remain durable

  

---

  

## Obsidian linking rules

  

All memory files should use Obsidian wikilinks when there is a real relationship.

  

Prefer:

- a small number of strong, meaningful links

- durable canonical links

- clear graph structure over noisy graph inflation

  

### For large projects

Files inside the same project folder should link to related local notes using relative wikilinks such as:

- `[[overview]]`

- `[[current-state]]`

- `[[decisions]]`

- `[[risks]]`

- `[[next-steps]]`

- `[[prompts]]`

  

### Required linking behavior for project session notes

Every project session note must include links to:

- `[[overview]]`

- `[[current-state]]`

- `[[next-steps]]`

  

Add links to:

- `[[decisions]]`

- `[[risks]]`

- `[[prompts]]`

  

when relevant.

  

### Required linking behavior for core project notes

Every core project note should include a `## Related` section near the top with links to the other relevant core project notes.

  

Recommended examples:

  

#### For `overview.md`

- `[[current-state]]`

- `[[decisions]]`

- `[[risks]]`

- `[[next-steps]]`

- `[[prompts]]`

  

#### For `current-state.md`

- `[[overview]]`

- `[[decisions]]`

- `[[risks]]`

- `[[next-steps]]`

  

#### For `decisions.md`

- `[[overview]]`

- `[[current-state]]`

- `[[risks]]`

- `[[next-steps]]`

  

#### For `risks.md`

- `[[overview]]`

- `[[current-state]]`

- `[[decisions]]`

- `[[next-steps]]`

  

#### For `next-steps.md`

- `[[overview]]`

- `[[current-state]]`

- `[[risks]]`

- `[[decisions]]`

  

#### For `prompts.md`

- `[[overview]]`

- `[[current-state]]`

- `[[next-steps]]`

  

### Linking rule for small projects

If using a single-file project note, add meaningful wikilinks to:

- relevant global notes

- relevant knowledge/pattern/decision notes

- related project notes if truly connected

  

### Linking rule for non-project notes

For notes in:

- `knowledge/`

- `patterns/`

- `prompts/`

- `decisions/`

  

add wikilinks only when there is a real conceptual relationship.

  

Examples:

- a reusable debugging method can link to a project where it was applied

- a global routing decision can link to `[[agent-memory]]` or `[[routing-rules]]`

- a knowledge note can link to a relevant pattern note

  

Do not force links where there is no meaningful relationship.

  

### Link creation rule

When creating a new note, always add wikilinks to the most relevant existing notes.

When updating a note, preserve existing useful wikilinks and add missing ones if the note is insufficiently connected.

  

### Naming rule

Inside a large project folder, prefer stable canonical filenames:

- `overview.md`

- `current-state.md`

- `decisions.md`

- `risks.md`

- `next-steps.md`

- `prompts.md`

  

Session notes should also link back to the project core notes so they appear in the graph.

  

---

  

## Note structure rule

  

### Core project notes

Core project notes should normally begin with:

  

```md

# Note Title

  

## Related

- [[overview]]

- [[current-state]]

- [[decisions]]

- [[risks]]

- [[next-steps]]

  

## Content

...

  

Adjust the Related links to match the actual note type.

  

Project session notes

  

Project session notes should normally begin with:

  

# Session YYYY-MM-DD — Short Topic

  

## Related

- [[overview]]

- [[current-state]]

- [[next-steps]]

  

## What was done

- ...

  

## Key findings

- ...

  

## Blockers

- ...

  

## Next steps

- ...

  

Add [[decisions]], [[risks]], or [[prompts]] when relevant.

  

⸻

  

Anti-sprawl rule

  

Do not create:

• a new project folder for casual work

• duplicate notes with overlapping purpose

• many tiny notes when one stable note is enough

• empty placeholder files without a clear reason

  

Prefer:

• updating an existing relevant note

• using knowledge/, patterns/, prompts/, or decisions/

• a single-file project for early-stage work

• a full project folder only for clearly ongoing project work

  

⸻

  

Default bias

  

When uncertain:

1. do not create a new project folder

2. do not store trivial context

3. prefer updating existing notes

4. prefer fewer, stronger notes

5. preserve graph quality and continuity