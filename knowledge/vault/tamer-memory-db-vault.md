# Tamer Memory DB Vault

## Related
- [[agent-memory]]
- [[current-focus]]
- [[routing-rules]]
- [[decisions/tamer-memory-db-vault-repo-decisions|Tamer Memory DB vault repo decisions]]
- [[sessions/2026-04-15-vault-repo-prep|Vault repo prep]]
- [[sessions/2026-04-15-private-github-repo-created|Private GitHub repo created]]
- [[sessions/2026-05-03-vault-audit-and-cleanup|Vault audit and cleanup]]

## Summary

- Obsidian-based agent memory vault stored at `/Users/tamerlan/Documents/TamerMemoryDB/Tamerlan Memory DB`.
- This vault is the canonical continuity layer for ongoing work across sessions.
- The vault itself is infrastructure for memory management, not a client or delivery project.

## Current State

- The vault is tracked by a dedicated git repository inside the folder.
- Private GitHub repository exists: `https://github.com/TamerlanTA/tamerlan-memory-db`.
- Local branch `main` is published to `origin/main`.

## Notes

- Vault-level governance, repo setup, and maintenance should live in `knowledge`, `decisions`, `patterns`, and root `sessions`, not inside `projects/`.
- 2026-05-03 audit found that the main cleanup risk is duplicate FlowOps folders with same note names but different content; merge before deleting.
