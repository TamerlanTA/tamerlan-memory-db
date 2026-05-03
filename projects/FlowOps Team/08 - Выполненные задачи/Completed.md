# Выполненные задачи

## Related
- [[../00 - Overview]]
- [[../03 - Pipelines/Pipeline A — Upwork Radar]]
- [[../05 - CRM Structure/Airtable CRM Build Spec]]
- [[../05 - CRM Structure/CRM Automation Plan]]

## Список
- **Upwork Radar** — подготовлен n8n workflow JSON для мониторинга Upwork, скоринга, генерации предложения, валидации, отправки в Telegram и записи в Google Sheets.
- **CRM система FlowOps** — создана CRM система; дальнейшие задачи должны идти от состояния "CRM существует", а не "нужно создать базу".
- **Pipeline B — LinkedIn Pain Radar** — завершён; считать готовым к операционному использованию, QA и дальнейшей итерации.
- **Pipeline C — Website Audit Generator workflow template** — подготовлены локальные `pipeline-c-website-audit-generator-workflow.json` и `pipeline-c-website-audit-generator-runbook.md`; это draft-only workflow, не полная operational completion.
- **Pipeline C v2 — automated website audit machine templates** — подготовлены import-ready workflow файлы для multi-niche Firecrawl prospecting, AI audit queue, Telegram approve buttons, Gmail send after approve, WF-06 router patch, and runbook.
- **Pipeline C v2 — выполнен operationally end-to-end** — подтверждён рабочий n8n pipeline: Telegram command запускает prospecting, Firecrawl автоматически ищет сайты, нормализация/дедуп/скрейп работают, Audit Queue пишет `Leads`/`Audits`/`Messages`/`Automation Logs`, Telegram карточки приходят с approve-кнопками, `Approve + Send` отправляет Gmail через native Gmail node, остальные кнопки логируют без отправки. Запуск переведён с расписания на `/pipeline_c` и `/audit_sites` через WF-06 без второго Telegram Trigger.

## Пока не считаем завершенным
- CRM QA/валидация, production-safe automation wiring, отчётность и data hygiene.
- Pipeline C больше не считать незавершенным build-task. Открытым остается только campaign operations: регулярные ручные запуски через Telegram, мониторинг reply rate, улучшение niche/query rotation и copy, Loom только для сильных лидов или `Need Loom`.
