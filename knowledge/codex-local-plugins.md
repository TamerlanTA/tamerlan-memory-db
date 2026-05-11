# Codex Local Plugins

## Related
- [[agent-memory]]
- [[routing-rules]]
- [[vault/tamer-memory-db-vault|Tamer Memory DB Vault]]

## Installed Plugins

### browser-harness
- Installed on `2026-05-11` from `https://github.com/browser-use/browser-harness`.
- Local editable repo: `/Users/tamerlan/Developer/browser-harness`.
- Global command: `/Users/tamerlan/.local/bin/browser-harness` via `uv tool install -e .`.
- Codex global skill symlink: `/Users/tamerlan/.codex/skills/browser-harness/SKILL.md` -> `/Users/tamerlan/Developer/browser-harness/SKILL.md`.
- Connected using Way 2 from `install.md`: Chrome launched with a dedicated profile at `/Users/tamerlan/.browser-harness/chrome-profile` and remote debugging port `9222`.
- Because another Chrome process was already bound on `127.0.0.1:9222`, use `BU_CDP_URL=http://localhost:9222` for harness commands so macOS resolves to the working IPv6 DevTools listener.
- Verified with `browser-harness --doctor`: Chrome running, daemon alive, one active connection, active page `https://github.com/browser-use/browser-harness`.
- Optional checks still fail until needed: `profile-use installed` and `BROWSER_USE_API_KEY set` are only for Browser Use cloud/profile sync.

### Obsidian Skills
- Installed on `2026-04-15` from `https://github.com/kepano/obsidian-skills`.
- Local plugin path: `/Users/tamerlan/plugins/obsidian`.
- Local marketplace file: `/Users/tamerlan/.agents/plugins/marketplace.json`.
- Marketplace name: `obsidian-skills`.
- Plugin name: `obsidian`.

## Notes

- Upstream repo ships Claude-oriented metadata in `.claude-plugin/`.
- Local install was adapted for Codex by creating `/Users/tamerlan/plugins/obsidian/.codex-plugin/plugin.json`.
- Installed repo contents include Obsidian-related skills such as `obsidian-markdown`, `obsidian-bases`, `json-canvas`, `obsidian-cli`, and `defuddle`.
- Restart Codex to ensure the newly installed local plugin is discovered in a fresh session.
