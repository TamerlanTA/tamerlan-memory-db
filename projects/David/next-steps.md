# Make-David — Next Steps

## Related
- [[overview]]
- [[current-state]]
- [[risks]]
- [[decisions]]

---

## Immediate Priorities

### 1. 🔴 Создать Make.com сценарий
- Открыть MAKE_SCENARIO.md как гайд
- Создать Custom Webhook модуль
- Настроить Filter → Router → 6 routes (David+Derecho, David+Radicado, Lilia+Derecho, Lilia+Radicado, Lyan+Derecho, Lyan+Radicado)
- Создать Data Stores: `sellerchat_sent_templates`, `sellerchat_failed_templates`
- Подключить SellerChat connections для каждого аккаунта
- Протестировать с одним Google Sheet

### 2. 🟡 Закрыть TODOs в sub-save.json
- Открыть n8n, найти sticky notes с TODO
- Определить что именно не реализовано
- Реализовать или задокументировать как known limitation

### 3. 🟡 Провести safe rollout
- Начать с 1 тестового David spreadsheet
- Проверить end-to-end: cell edit → Apps Script → Make → SellerChat → WhatsApp delivered
- Проверить дедупликацию (отредактировать одну строку дважды)
- Расширить на остальные sheets после подтверждения

### 4. 🟢 Документировать SellerChat template variables
- Уточнить у David какие переменные используются в шаблонах
- Обновить MAKE_SCENARIO.md с маппингом переменных

### 5. 🟢 Мониторинг
- Добавить Slack/Email alert при сбоях в Make.com error handler
- Настроить Data Store review для failed messages

## Future / Backlog
- Вынести credentials из hardcode в environment variables
- Автоматизировать добавление новых профилей/аккаунтов
- Добавить dashboard для tracking message delivery
