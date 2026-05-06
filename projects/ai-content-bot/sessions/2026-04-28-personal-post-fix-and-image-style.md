# Session 2026-04-28 — Personal Post Fix + Image Style

## Related
- [[projects/David/overview]]
- [[projects/David/current-state]]
- [[projects/David/next-steps]]
- [[projects/David/decisions]]
- [[projects/David/risks]]

## What was done

### Root cause of wrong personal post generation (FOUND + FIXED)

Three compounding bugs:

**Bug 1 — Route Telegram Update regex missed "Create a post."**
- Old regex: `/^(create|write...)\s+(мне\s+)?(пост|post)(?:\s|$)/i`
- "Create a post. [content]" has "a" between "create" and "post" → regex didn't match
- Message fell through to AI Agent instead of direct create_post route

**Bug 2 — AI Agent tool schema had no `text` field**
- When routed via AI Agent → `create_post` toolWorkflow, agent summarized user's story into a short topic
- "Please forgive me. I fired 4 people. Was paid $3,350." → became something like "automation case"
- Full personal context lost entirely

**Bug 3 — WF-09 Resolve Topic didn't handle toolWorkflow format**
- toolWorkflow sends: `{ query: { some_input: '{"topic":"...","chat_id":"..."}' } }`
- Resolve Topic was reading `input.text` and `input.topic` which were `undefined` at top level
- `rawText = ''`, `requested = ''` → personal narrative detection never fired (length > 50 check fails)
- Resolve Topic matched a generic Topics sheet row → GPT-4o generated generic content

### Fixes applied

**WF-06 Route Telegram Update** — new regex:
```js
/^(create|write|...)\s+(?:(?!post\b|пост\b)\w+\s+){0,2}(пост|post)(?:[.\s,!?]|$)/i
```
Handles: "Create a post.", "Write me a post", "create a post about X", etc.

**WF-06 Tool: Create Post schema** — added `text` field:
```json
"text": { "description": "Full verbatim user message. CRITICAL: if user shared a personal story, case, money figures — copy ENTIRE message verbatim, do not summarize." }
```

**WF-09 Resolve Topic** — toolWorkflow format unwrapping at top:
```js
const rawInput = $('When Called by WF-06').first().json;
let input;
if (rawInput.query?.some_input) {
  try { input = JSON.parse(rawInput.query.some_input); } catch(e) { input = rawInput; }
} else { input = rawInput; }
```

### Image style fix

Previous style was too "professional/boring" (cream+navy, barely any visual interest). New direction: **bold confidence with editorial discipline** — scroll-stopping but not chaotic. Key changes:
- Hero headline now 45-60% of image height (was 30-45%)
- Allow 1-2 accent colors (was strictly 1 muted only)
- Accent colors now RICHER: slate-blue (#5C7AA8), warm coral (#D4715A), amber (#C9933C) instead of just muted teal
- Small ALL CAPS label at top (CASE STUDY / AUTOMATION NOTE)
- For PERSONAL_CASE: dominant number/quote in filled accent-colored box
- Explicit: "if image looks like blank wall with tiny text, reject it"

## Blockers
- TELEGRAM_BOT_TOKEN still hardcoded as placeholder in WF-09 `Prepare Gemini Body` — must replace after import
- Images not tested yet with new style prompt

## Next steps
1. Import WF-06 and WF-09 into n8n (both changed)
2. Replace TELEGRAM_BOT_TOKEN in Prepare Gemini Body node
3. Test: "Create a post. Please forgive me. I fired 4 people, made $3,350"
   - Expected: post_mode=personal_case, first-person voice, real numbers
   - Expected image: big $3,350 in accent-colored box, cream background, bold navy headline
4. Test: general chat ("What do you think about Claude 4?") → natural response, no tool call
5. Test: photo + caption → image-to-image via Gemini
