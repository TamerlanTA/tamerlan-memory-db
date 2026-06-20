# Inbox

## Related
- [[agent-memory]]
- [[current-focus]]

Operational capture note for future triage items.

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
