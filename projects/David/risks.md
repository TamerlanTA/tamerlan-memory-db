# Make-David — Risks & Blockers

## Related
- [[overview]]
- [[current-state]]
- [[decisions]]
- [[next-steps]]

---

## Active Risks

### 🔴 HIGH: Make.com scenario не создан
**Risk:** Весь Google Sheets → SellerChat flow не работает без Make.com сценария.
**Impact:** Критично — шаблонные сообщения не отправляются.
**Mitigation:** Создать сценарий в Make UI по инструкции в MAKE_SCENARIO.md.

### 🟡 MEDIUM: Hardcoded credentials в workflows
**Risk:** API ключи и URLs захардкожены в n8n workflow JSON и Apps Script.
**Impact:** Сложность поддержки, риск утечки при передаче файлов.
**Mitigation:** Вынести в environment variables / n8n credentials store.

### 🟡 MEDIUM: sub-save.json — незакрытые TODOs
**Risk:** Sticky notes с TODO в sub-save workflow могут означать незакрытые edge cases.
**Impact:** Данные фотомульт могут не сохраняться корректно в edge cases.
**Mitigation:** Пройтись по TODOs, закрыть или задокументировать.

### 🟡 MEDIUM: Нет мониторинга / алертов
**Risk:** Нет dashboard для отслеживания sent/failed сообщений.
**Impact:** Ошибки могут остаться незамеченными.
**Mitigation:** Make.com Data Store для tracking, возможно добавить email/Slack alert.

### 🟢 LOW: Масштабирование Make.com routes
**Risk:** При добавлении нового SellerChat аккаунта нужно добавлять новые routes вручную.
**Impact:** Административная нагрузка при росте команды.
**Mitigation:** Пока не критично (3 профиля), документировать процесс добавления.

### 🟢 LOW: Debounce edge cases в n8n
**Risk:** 15-секундный debounce может не покрывать все сценарии (очень быстрые / очень медленные сообщения).
**Impact:** Сообщения могут обработаться неверно.
**Mitigation:** Тестирование разных сценариев.

## Resolved Risks
_(пока нет)_
