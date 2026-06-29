# Inbox

## Related
- [[agent-memory]]
- [[current-focus]]

Operational capture note for future triage items.

## 2026-06-26 — Parallels Desktop cleanup
- Removed Parallels Desktop and Windows VM artifacts from the Mac.
- Deleted main VM `/Users/tamerlan/Parallels/Windows 11.pvm` (~51 GB), Parallels app shortcuts, user Library caches/preferences/containers/keychain remnants, `/Applications/Parallels Desktop.app`, `/Library/Parallels`, `/Library/Preferences/Parallels`, and `/Library/Logs/parallels.log`.
- Verification: no Parallels processes remain; `/Applications` and `/Library` searches found no Parallels Desktop artifacts; remaining `parallelstore` search hits are unrelated Google API/Python/node_modules files.
- Disk availability on `/` increased from ~111 GiB to ~163 GiB.

## 2026-06-26 — Mac disk cleanup and storage analysis
- Performed safe cleanup after Parallels removal: user caches, npm/pip/pnpm/Homebrew caches, Chrome on-device model cache, `.dmg` installers in Downloads, Notion Service Worker/cache storage, VS Code cached VSIXs, and Codex temp/old logs.
- Did not delete user documents/projects/photos/videos, games, Minecraft/Steam data, Docker data, Claude VM bundle, LM Studio models, WhatsApp/Telegram media, or application bundles without explicit approval.
- Final observed free space: `df -h /` showed ~175 GiB free; APFS container showed ~187.7 GB free. APFS values may fluctuate with purgeable/swap space.
- Largest remaining areas: `~/Library` ~70 GB, `~/Documents` ~19 GB, `~/Desktop` ~17 GB, `~/Pictures` ~8.2 GB, `~/.lmstudio` ~7.3 GB, `/Applications` ~53 GB.
- Large optional cleanup candidates needing user approval: `/Applications/DaVinci Resolve` ~9.8 GB, `/Applications/The Forest.app` ~7.1 GB, `~/Documents/1video.fcpbundle` ~7.2 GB, Claude VM rootfs ~5.5 GB, LM Studio model ~5 GB, Docker.raw ~3.6 GB, `~/Desktop/Альпинисты` ~7 GB, `~/Documents/Adeal` ~4.3 GB, WhatsApp backup/media and Telegram media caches.

## 2026-06-26 — Packet Tracer d2.pka VLAN task
- Helped complete one-off Cisco Packet Tracer assignment `/Users/tamerlan/Downloads/d2.pka`.
- Final topology passed Packet Tracer check: Activity Results showed `Congratulations Guest! You completed the activity.`
- Key fix sequence: configured Router1 subinterfaces for VLAN 2/3, Switch0 VLAN/trunk ports, Multilayer Switch0 VLAN 4/5 SVIs with `ip routing`, Switch1/Switch2 access/trunk ports, then corrected PC IP settings.
- Final PC addressing: PC0 `192.168.2.10/24 gw 192.168.2.1`; PC1 `192.168.3.10/24 gw 192.168.3.1`; PC2 `192.168.4.10/24 gw 192.168.4.1`; PC3 `192.168.5.10/24 gw 192.168.5.1`; PC4 `192.168.4.20/24 gw 192.168.4.1`; PC5 `192.168.5.20/24 gw 192.168.5.1`.
- Important correction: Switch2 ports needed PC4 on VLAN 4 and PC5 on VLAN 5. File was saved; disk modification time confirmed as `2026-06-26 10:11:35`.
- Defense prep should focus on `Practice 3 – VLAN Technology 1.pdf` and `Practice 5 - L3 Switch and Router.pdf`: access vs trunk ports, VLAN vs subnet, 802.1Q tagging, router-on-a-stick subinterfaces, L3 switch SVIs, `ip routing`, default gateways, and ping-based troubleshooting.

## 2026-06-19 — Computer Networks Practice 1 Lab Defense
- Built one-off Cisco Packet Tracer / IOS lab deliverables in `/Users/tamerlan/Desktop/comp-net/`.
- Output files: `Practice_1_Lab_Defense_Togysbayev_Tamerlan.docx`, `Practice_1_Lab_Defense_Togysbayev_Tamerlan.pdf`, `lab1-defense-report.md`, and `lab1-defense-commands.txt`.
- Lab content: switch/router/PC configuration for Practice 1 Defense from user photos; switch hostname `Tamerlan`, router hostname `Togysbayev`, LAN `172.16.30.0/24`.
- Note: instructor username is represented as `instructor` and should be replaced if the teacher requires their exact username.

## 2026-06-18 — Excel laboratory work deliverables
- Built one-off Excel lab deliverables in `outputs/019eba6d-2222-7532-a606-ae934df05248/`.
- Lab #1 file: `Laboratory work_1_Togysbayev_Tamerlan.xlsx`.
- Lab #2 file: `Laboratory work_2_Togysbayev_Tamerlan.xlsm`.
- Lab #2 source data is on worksheet `Financials`; automated output is on `Summary` and `Report`.
- Verification: `.xlsm` contains `xl/vbaProject.bin`; Microsoft Excel opened it with `hasVBA=true`; macros `PrepareFinancialData`, `CreateQuarterlySummary`, `GenerateFinancialCharts`, `ForecastNextQuarter`, and `GenerateReportSummary` ran successfully on a test copy. `RunScenarioAnalysis` is intentionally interactive and should be run manually because it uses `InputBox`.
- Follow-up fix: rebuilt Lab #2 buttons to reference full module-qualified macro names like `FinancialAutomation.PrepareFinancialData` after Excel reported it could not run workbook-level `PrepareFinancialData`. Verified module-qualified macros run successfully in Excel on a test copy.

## 2026-06-18 — Upwork Telegram Automation call prep
- Prepared for an Upwork call with Diana about a `Telegram Automation & Funnel Developer` role posted 2026-06-16.
- Positioning to reuse: Tamerlan should sell a Telegram revenue/funnel system, not just a bot: entry point -> qualification -> segmentation -> follow-up -> CRM sync -> conversion tracking -> optimization.
- Relevant proof points: FlowOps automation agency, Telegram bots/command centers, AI qualification, CRM integrations, webhook/API systems, analytics dashboards, approval flows, and long-term optimization mindset.
- Constraint: Tamerlan is not fully confident in spoken English; future prep should include short, simple English scripts and recovery phrases.

## 2026-04-30 — Team task import JSON
- `/Users/tamerlan/Desktop/flowopsteamPipelines/team-tasks-import.json` is not an n8n workflow export: it has no `nodes` / `connections` and uses custom type `team_tasks_import`.
- Imported its Aslanbek pricing-section task locally to `/Users/tamerlan/Documents/TamerMemoryDB/Tamerlan Memory DB/My-Team/Aslanbek/tasks/TASK-2026-04-30-pricing-section.json`.
- If this should run through n8n later, create a real n8n workflow wrapper instead of importing this JSON directly.

## 2026-06-04 — Allur / BAIC tender CPL comparison
- Built one-off Excel comparison for Allur / BAIC agency tender: `/Users/tamerlan/Downloads/DanMedia_Allur_BAIC_Comparative_CPL.xlsx`.
- Sources used: local Dan Media PDF/XLSX, Holy Media PDF/XLSX, Netpeak PDF, and TDS Google Slides/Sheet links.
- Workbook frames Dan Media as recommended winner via decision score (CPL + commission + channel fit + analytics/CRM + evidence clarity), while noting TDS has lower indicative CPL but mixed KPI/currency definitions that need validation.
- Later the same day, translated the workbook UI/content into Russian in-place and verified formulas/rendered sheet previews successfully.
