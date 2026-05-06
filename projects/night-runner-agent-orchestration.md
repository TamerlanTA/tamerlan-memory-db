# Night Runner Agent Orchestration

## Related
- [[All about Agents/agent-memory]]
- [[All about Agents/routing-rules]]
- [[current-focus]]

## Current status
- Repository: `/Users/tamerlan/Desktop/night-runner`
- On 2026-05-07, Memory Preload was added before Executor in `scripts/night-runner.mjs`.
- Preload is runner-owned, read-only, and writes `.agent/reports/memory-preload.md` for Executor.
- Obsidian Memory Sync remains separate and still runs only after Final Auditor.
- On 2026-05-07, `scripts/install-agent-system.mjs` was added so the orchestration system can be installed into another existing project folder without manual copying.

## Key decisions
- Executor must not scan the Obsidian vault directly.
- Runner reads only `read_before_run` allowlisted files from configured `project_memory_dir`.
- Reviewer and Fixer should not read Obsidian or preload unless explicitly required.
- Preload uses only Node.js built-ins, caps per-file reads, caps total output, and skips unsafe/missing/non-text files.
- Installer uses only Node.js built-ins, copies only orchestration files, skips existing files unless `--force` is passed, never deletes target files, and refuses dangerous targets (`/`, home, installer repo, configured memory root).

## Changed files
- `.agent/memory-config.json`
- `.agent/state.json`
- `.agent/prompts/executor.md`
- `.agent/protocol.md`
- `.agent/README.md`
- `scripts/night-runner.mjs`
- `scripts/install-agent-system.mjs`

## Validation
- `node --check scripts/night-runner.mjs` passed.
- `node scripts/night-runner.mjs --dry-run` passed; preload skipped cleanly because `project_memory_dir` is empty.
- `node scripts/night-runner.mjs --dry-run --phase memory-preload` passed; single phase is recognized and skipped cleanly with empty `project_memory_dir`.
- `node scripts/night-runner.mjs --dry-run --no-memory` passed; both preload and sync skipped.
- `node --check scripts/install-agent-system.mjs` passed.
- `node scripts/install-agent-system.mjs --target /Users/tamerlan/Desktop/FlowOps2 --dry-run` passed; it reported 13 files that would be created and wrote nothing.

## Next steps
- For real project runs, set `.agent/memory-config.json` `project_memory_dir` to an existing project path under `memory_root`.
- Keep `read_before_run` small, usually `current-state.md`, `next-steps.md`, and `decisions.md`.
- To install into a project, first run `node scripts/install-agent-system.mjs --target <project> --dry-run`, then rerun without `--dry-run` when the target list looks correct.
