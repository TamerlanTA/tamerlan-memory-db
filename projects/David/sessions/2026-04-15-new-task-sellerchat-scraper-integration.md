# Session 2026-04-15 — New Task: SellerChat → Scraper Integration

## Related
- [[projects/David/overview]]
- [[projects/David/current-state]]
- [[projects/David/next-steps]]
- [[projects/David/risks]]
- [[projects/David/decisions]]

---

## Context
Клиент David обратился повторно. Phase 1 завершена. Новая задача — другая по природе.

**Бюджет:** $300 fixed  
**Срок:** 2–2.5 дня  
**Статус договора:** Согласовано, клиент ждёт реализацию

---

## What David wants

Сейчас пользователи общаются в SellerChat. Когда пользователь отправляет номер платы (placa) или cedula (ID), SellerChat должен:
1. Распознать это как запрос поиска
2. Автоматически вызвать существующий скрапер (уже работает в n8n)
3. Получить результат по фотомультам/штрафам
4. Вернуть результат пользователю прямо в SellerChat чат

**Ключевой инсайт из чата:** David сам не уверен, умеет ли SellerChat захватить точный input пользователя и передать его наружу. Это главный вопрос для выяснения.

---

## What is already built (reuse)

| Компонент | Файл | Что умеет |
|---|---|---|
| n8n основной бот | `WhatsApp AI Bot - Fotomultas v3 con Buffer from scratch.json` | WhatsApp trigger → AI → Kommo → scrape → respond |
| n8n sub-scrape | `sub-scrape.json` | Скрапит страницы фотомульт, парсит данные, возвращает результат |
| n8n sub-save | `sub-save.json` | Сохраняет результат в Supabase |
| Reminder | `agendar-reminder.json` | Планирование напоминаний |

**Важно:** Существующий n8n бот триггерится через WhatsApp напрямую, не через Make. sub-scrape вызывается внутри основного workflow как sub-workflow.

---

## What is missing (new work)

1. **SellerChat bot flow** — настроить автоответчик/бота в SellerChat, который:
   - Детектит placa (ABC123, ABC12A) или cedula (7-10 цифр) через regex
   - Захватывает текст и отправляет webhook в Make
   
2. **Make сценарий (новый)** — отдельный от существующего (тот был для шаблонов):
   - Получить webhook от SellerChat
   - Валидировать input (placa vs cedula vs invalid)
   - Вызвать n8n скрапер (нужен webhook endpoint в n8n)
   - Ждать ответ
   - Форматировать результат
   - Отправить ответ обратно в SellerChat через API
   
3. **n8n webhook bridge** — добавить webhook trigger к существующему scraper flow:
   - Принимает: `{ plate?, id?, phone, conversation_id }`
   - Запускает sub-scrape логику
   - Возвращает результат через HTTP response в Make

---

## Key unknowns (выяснить перед реализацией)

1. **SellerChat** — может ли передать точный текст пользователя в webhook? (David не уверен)
2. **sub-scrape.json** — как именно принимает параметры сейчас? (вызывается parent workflow через internal trigger)
3. **SellerChat API** — как отправить сообщение в конкретный chat/conversation?
4. **Источники скрапинга** — SIMIT подтверждён. Medellín, Itagüí, Bello — уточнить у David какие именно нужны
5. **Формат ответа** — что именно должен видеть пользователь в SellerChat?

---

## Architecture (proposed)

```
[User in SellerChat]
  ↓ sends: "ABC123" or "1234567890"
  
[SellerChat Bot Flow]
  → regex match (placa / cedula)
  → webhook POST to Make: { input, type, phone, conversation_id, account }
  
[Make — New Scenario]
  → validate input
  → classify (plate vs ID)
  → HTTP POST to n8n webhook bridge
  
[n8n Webhook Bridge (new/modified)]
  → call sub-scrape sub-workflow
  → return structured result to Make
  
[Make — continuation]
  → format response
  → POST to SellerChat API → send message to conversation

[User in SellerChat]
  ← receives formatted result with fines/plates data
```

---

## Colombian patterns
- **Placa (вехикль):** `[A-Z]{3}[0-9]{2,3}[A-Z0-9]?` — старый ABC123, новый ABC12A
- **Cedula:** `[0-9]{7,11}` — 7-11 цифр (no letters)

---

## Blocker / Risk
- SellerChat input capture — если SellerChat не умеет передавать exact input в webhook, весь подход требует пересмотра (возможно через Zapier/Make polling SellerChat или альтернативный trigger mechanism)
- Нужен SellerChat account доступ у David (он говорит что есть у нас)

---

## Next steps before coding
1. Изучить SellerChat UI — что такое "bot flow" / "automation" / "webhook outgoing" — умеет ли захватывать user text
2. Изучить sub-scrape.json — какие именно входные параметры нужны для вызова
3. Уточнить у David: формат желаемого ответа пользователю + список источников
