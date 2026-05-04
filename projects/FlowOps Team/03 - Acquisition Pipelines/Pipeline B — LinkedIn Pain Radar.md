# 🔍 Pipeline B — LinkedIn Pain Radar

#flowops #pipeline #linkedin

> Цель: 100 персональных касаний в неделю с людьми, которые публично говорят о своей боли.

## Status

**Status as of 2026-05-03:** Pipeline B is complete.

- LinkedIn Pain Radar is now considered built for the FlowOps system.
- CRM integration target exists because the FlowOps CRM system has been created.
- Future work should treat Pipeline B as operational/ready for refinement, QA, and iteration rather than as a planning task.

**Dedupe fix as of 2026-05-04:**
- Local n8n JSON now includes persistent Airtable duplicate checking before create/notify.
- Duplicate records are skipped and logged instead of being sent again to Telegram.
- Search depth increased to reduce repeated top-5 results.
- Import/test runbook: `/Users/tamerlan/Desktop/flowopsteamPipelines/pipeline-b-linkedin-pain-radar-dedupe-runbook.md`.

---

## Логика работы

Мониторить посты и комментарии по ключевым словам → определить боль → найти профиль → проверить релевантность → сгенерировать персональное сообщение → сохранить лид → показать топ для ручной отправки.

---

## Ключевые фразы для мониторинга

**Прямые запросы:**
- "looking for automation"
- "need help with n8n / Make / Zapier"
- "recommend automation specialist"

**Сигналы боли:**
- "manual process" / "doing this manually"
- "CRM mess" / "our CRM is a disaster"
- "missed leads" / "losing leads"
- "need AI chatbot"
- "repetitive tasks"
- "wasting time on"

---

## Шаблон персонального сообщения

> "Hey [Name], saw your post about [specific problem].
>
> I build automation systems for this exact kind of ops bottleneck.
>
> Quick idea: [1 sentence конкретная идея].
>
> Worth sending a 2-min Loom?"

**Правила сообщения:**
- Всегда ссылайся на конкретный пост / конкретную боль
- Не давай длинные объяснения — только одна идея
- Заканчивай вопросом с низким порогом (Loom, а не звонок сразу)
- Никаких generic "I help businesses with automation"

---

## Структура записи в базе

| Поле | Описание |
|------|----------|
| Name | Имя человека |
| Company | Компания |
| Post URL | Ссылка на пост |
| Pain signal | Что именно написали |
| LinkedIn URL | Профиль |
| Niche | Ниша бизнеса |
| Offer match | Какой оффер подходит |
| Message draft | Черновик сообщения |
| Sent? | Да/нет |
| Response? | Ответил/нет |
| Follow-up date | Следующий шаг |

---

## Квалификация перед отправкой

Проверить перед отправкой:
- [ ] Профиль выглядит как реальный бизнес (не студент, не джуниор)
- [ ] Компания существует и работает
- [ ] Боль из поста реально решается автоматизацией
- [ ] Нет признаков, что уже работают с кем-то

---

## Связанные страницы

- [[Sales Steps]] — что делать после ответа
- [[Message Templates]] — полные шаблоны
- [[Pipeline D — Demo Library]] — демо для follow-up
- [[What to Do First]] — приоритет этого пайплайна

---

*#flowops #pipeline #linkedin*
