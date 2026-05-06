# Make-David — Next Steps

## Related
- [[projects/David/overview]]
- [[projects/David/current-state]]
- [[projects/David/risks]]
- [[projects/David/decisions]]

---

## Phase 1 — DONE ✅
Google Sheets → Make → SellerChat template sending. Завершено.

---

## Phase 2 — SellerChat Scraper Integration (ACTIVE)

**Goal:** User sends plate/ID в SellerChat → автоматически получает данные фотомульт обратно в чат.  
**Budget:** $300 | **Deadline:** 2–2.5 дня | **Status:** Agreed, в работе

### Шаг 1 — Исследование (сделать первым)
- [ ] Изучить SellerChat bot flow / automation — умеет ли передавать exact user text в webhook?
- [ ] Открыть sub-scrape.json и понять точный API/входные параметры для вызова
- [ ] Уточнить у David: список источников (SIMIT + какие ещё?) + желаемый формат ответа

### Шаг 2 — SellerChat Bot Flow
- [ ] Создать bot flow в SellerChat для аккаунта David
- [ ] Настроить regex detectors: placa (ABC123/ABC12A) + cedula (7-11 цифр)
- [ ] Настроить outgoing webhook → Make, payload: `{ input, type, phone, conversation_id, account }`

### Шаг 3 — n8n Webhook Bridge
- [ ] Добавить webhook trigger в n8n (или создать новый workflow)
- [ ] Принимает: `{ plate?, id?, phone, conversation_id }`
- [ ] Вызывает существующую sub-scrape логику
- [ ] Возвращает структурированный результат через HTTP response

### Шаг 4 — Make Scraper Scenario (новый, отдельный от Phase 1)
- [ ] Custom webhook endpoint
- [ ] Input validation + классификация (placa vs cedula vs invalid)
- [ ] HTTP call → n8n webhook bridge
- [ ] Форматирование ответа
- [ ] SellerChat API call → отправить ответ в conversation

### Шаг 5 — Error handling & testing
- [ ] Timeout handling (скрапер не ответил)
- [ ] No result found
- [ ] Source blocked / anti-bot
- [ ] Invalid input (не placa и не cedula)
- [ ] End-to-end тест с реальным номером

### Шаг 6 — Production rollout
- [ ] Тест с David аккаунтом
- [ ] При необходимости — Lilia и Lyan аккаунты

---

## Критический вопрос

**Умеет ли SellerChat захватить exact input пользователя и передать его в webhook?**  
Если НЕТ → нужна альтернативная архитектура (polling, другой trigger механизм).  
Этот вопрос решается на Шаге 1 перед любым кодингом.
