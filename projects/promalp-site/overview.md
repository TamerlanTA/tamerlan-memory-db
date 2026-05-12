# Промальп-сайт (Алматы) — Overview

## Related
- [[current-state]]
- [[decisions]]
- [[risks]]
- [[next-steps]]
- [[prompts]]
- [[../industrial-climbers-flowops|FlowOps pitch]]
- [[../flowops-agency-website]]

## Что это
Веб-сайт для бригады промышленных альпинистов в Алматы. Реализация «Слота 1» (Attraction → Speed-to-Lead) из системы FlowOps, описанной в пресейл-деке `[[../industrial-climbers-flowops]]`: сайт + квиз → AI-обзвон (Vapi/Retell) → CRM Airtable → follow-up WhatsApp/Telegram.

Сайт — главная точка конверсии трафика с органики и таргета. Лид уходит в Airtable + Telegram-алерт бригадиру в течение секунд.

## Цели
- Конверсия посетителя в заявку через интерактивный квиз (5 шагов, ~5 минут).
- B2B-доверие: «Допуск ОТ», страховка, кейсы, отзывы УК/КСК.
- Расчёт стоимости прямо в квизе по матрице (тип работ × этажность × площадь × срочность).
- Передача лида в Airtable + мгновенный Telegram-алерт бригадиру (Айдос).

## Целевая аудитория
- B2B: КСК / управляющие компании, бизнес-центры, ЖК (примеры из деки: ЖК «Жетысу», БЦ Esentai Tower).
- B2C: владельцы квартир в высотках — герметизация швов, окраска фасадов, мытьё окон, антиобледенение.
- Регион: Алматы и пригороды.

## Стек
- Next.js 14 (App Router) + TypeScript + Tailwind CSS — повторяет FlowOps2.
- Деплой: Vercel.
- Lead pipeline: API route → Airtable + Telegram alert (контракт переиспользуем из FlowOps `/api/contact`).
- Локализация: ru-RU, цены в ₸, телефоны +7 707, документы РК (Допуск ОТ вместо СРО, КСК вместо УК).

## Корневой каталог
`/Users/tamerlan/Desktop/promalpsite`
