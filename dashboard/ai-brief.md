# Morning Brief 2026-05-25

## Today
- Закончить image-generation контур в [[projects/michaeldang|Michael Dang]]: реальный `Needs Image` row -> OpenAI image -> Drive upload -> public URL -> Sheet update.
- Довести [[projects/upwork-auto-response-system|Upwork Auto Response System]] до рабочего состояния для себя: P0 guardrails, real dry-run E2E, затем controlled live submit.
- Спроектировать и внедрить AI-assisted улучшение калькулятора [[projects/importcar-kz-mvp/overview|ImportCar.kz / EMcar]] без поломки deterministic pricing baseline и `calc:sanity`.
- После первого завершённого блока обновить [[My-tasks]] и relevant project memory, чтобы dashboard не расходился с фактическим состоянием.

## Risks
- [[projects/michaeldang|Michael Dang]] всё ещё зависит от live n8n quota/credential state и ручной проверки реального image row.
- [[projects/upwork-auto-response-system|Upwork Auto Response System]] нельзя включать на live auto-submit до P0 guardrails: connectivity, Connects accounting, min budget gate, field verification, Telegram notification.
- AI layer в [[projects/importcar-kz-mvp/overview|ImportCar.kz / EMcar]] может ухудшить точность, если заменить deterministic rules; безопаснее добавлять его как advisory/explanation/confidence layer.
- В [[My-tasks]] много направлений; сегодня лучше закрывать один блок за раз, иначе три крупных проекта останутся наполовину открытыми.

## Recommendations
- Начать с [[projects/michaeldang|Michael Dang]], потому что там самый узкий validation loop: один row, один image, один Drive URL.
- Для Upwork сначала закрыть guardrails и dry-run evidence; live submit делать только один и только после проверки результата.
- Для EMcar зафиксировать architecture decision: rules engine остаётся source of truth, AI добавляет уточнение/объяснение/коррекционный слой с логированием.
- В конце каждого блока сразу помечать статус в [[My-tasks]], иначе dashboard быстро станет неточным.

## Activity
- Today: новая очередь дня записана в [[My-tasks]]: Michael Dang image generation, Upwork auto-response, EMcar AI calculator.
- Week: завершены ImportCar QA hardening и production activation prep; собран и переработан local Memory Dashboard; за неделю добавлено 90 новых FlowOps leads и 2 prospect audits по `Completed-in-a-week.md`.
- Month: основной рабочий контур держится вокруг [[projects/FlowOps Team/00 - Overview|FlowOps Team]], [[projects/importcar-kz-mvp/overview|ImportCar.kz]], memory/agent infrastructure и коммерческих materials для outreach.
