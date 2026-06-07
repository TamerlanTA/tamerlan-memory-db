# Next Steps

## Related
- [[overview]]
- [[current-state]]
- [[risks]]
- [[decisions]]

## Immediate
1. Решить, фиксируем ли текущую **light editorial Vysota** визуальную систему или возвращаемся к прежней **dark cinematic premium B2B** памяти; после решения синхронизировать `DESIGN.md` и `[[decisions]]`.
2. Discovery-неделя с клиентом (по плану слайда 13 деки): собрать контент, реквизиты, параметры lead-пайплайна (см. `[[risks]]`).

## Контент и дизайн
3. Финализировать токены под фирстиль клиента, если у него есть. Иначе оставить токены деки.
4. Написать тексты для всех 10 секций на ru-RU, акцент B2B/Алматы.
5. Заменить заглушки секций реальным контентом и медиа.

## Квиз
6. Описать матрицу расчёта (тип работ × этажность × площадь × срочность → коридор цены ₸).
7. Реализовать движок квиза: 5 шагов, прогресс-бар, локальный расчёт, финальный экран с ценой + формой контакта.

## Backend
8. `/api/lead`: контракт скопировать из FlowOps2 `/api/contact`, добавить Airtable insert + Telegram alert бригадиру.
9. ENV: `AIRTABLE_API_KEY`, `AIRTABLE_BASE_ID`, `AIRTABLE_TABLE_ID`, `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`.

## Деплой и инфра
10. Создать Vercel-проект из `TamerlanTA/SummitSolutions`, привязать домен (после выбора с клиентом — см. `[[risks]]`).
11. SEO: ru-метаданные, JSON-LD LocalBusiness (Алматы), `sitemap.ts`, `robots.ts`.
12. Подключить простую аналитику (Plausible / Vercel Analytics) и UTM-пропагацию из таргета.
