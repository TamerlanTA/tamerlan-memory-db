# Session 2026-04-15 — Vault structure audit and reclassification

## Related
- [[knowledge/vault/tamer-memory-db-vault|Tamer Memory DB Vault]]
- [[decisions/tamer-memory-db-vault-repo-decisions|Vault repo decisions]]
- [[sessions/2026-04-15-vault-repo-prep|Vault repo prep]]
- [[sessions/2026-04-15-private-github-repo-created|Private GitHub repo created]]
- [[projects/AI-Powered Woven Label Generator/overview|AI-Powered Woven Label Generator]]

## Done

- Audited the vault structure against the updated memory protocol.
- Confirmed that `projects/Tamer Memory DB` was wrongly classified as a project.
- Reclassified vault-level material into:
  - `knowledge/vault/tamer-memory-db-vault.md`
  - `decisions/tamer-memory-db-vault-repo-decisions.md`
  - root `sessions/` for historical setup notes
- Moved the Griffes Vivienne conversion polish note from root `sessions/` into the project session folder.
- Reclassified reusable Griffes-specific lessons from project-local `feedback_*` notes into `patterns/`.
- Updated wikilinks so the Obsidian graph stays connected after the move.

## Findings

- The project area should be reserved for genuine delivery/client projects with canonical project structure.
- Vault governance and reusable operating guidance fit better in `knowledge`, `decisions`, `patterns`, and root `sessions`.
- Root `sessions/` is appropriate for vault-level maintenance history when the work is not tied to a client project.

## Next

- Continue using `projects/` only for real ongoing projects.
- Prefer `patterns/` for reusable engineering lessons and `knowledge/` for vault-level reference material.
