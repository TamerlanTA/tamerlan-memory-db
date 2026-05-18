# Pattern — FlowOps PDF Presentations

Reusable HTML → PDF presentation system in FlowOps brand style (clean minimal, blue gradient, A4 portrait, Russian content). Used for commercial pitches, business overviews, project reports.

## Related
- [[../templates/flowops-pitch-deck/README|Template README]]
- [[../projects/industrial-climbers-flowops]] — first real usage

## Where
- **Template:** `/Users/tamerlan/Documents/TamerMemoryDB/Tamerlan Memory DB/templates/flowops-pitch-deck/`
  - `template.html` — full-fledged 14-slide HTML with all components ready
  - `README.md` — component cheat-sheet (hero, cards, pipeline, before/after, timeline, wireframe, chat, creatives, stats, pills, tables, callouts)
  - `build.sh` — one-line HTML → A4 PDF via headless Chrome (handles Cyrillic paths)

## When to use
- Коммерческое предложение клиенту FlowOps
- Бизнес-обзор / отчёт по проекту (как `speed-to-lead-business-overview.pdf`)
- Internal-документ для команды в одном стиле
- Любой A4 PDF на 8–20 слайдов с консервативной B2B-эстетикой

## Workflow
1. Скопировать `template.html` в рабочую папку проекта на Desktop.
2. Заменить контент слайдов (HTML-структура и стили готовы — меняем только текст и количество секций).
3. Собрать PDF: `bash <vault>/templates/flowops-pitch-deck/build.sh input.html output.pdf`
4. Открыть PDF, проверить визуально каждую страницу — если внизу что-то режется, сократить список / уменьшить padding / снизить размер H1.

## Why this style
- Стиль скопирован с `speed-to-lead-business-overview.pdf` (не с тёмного `FlowOps-Startup-Report.pdf`) — он лучше читается консервативной B2B-аудиторией и нормально печатается на ч/б.
- Hero — единственный тёмный слайд с навигационным градиентом, остальные белые с тонким акцентом сверху.
- Никаких эмодзи в иконках (Chrome headless рендерит непредсказуемо), только текст и SVG-цвета.
- Системные шрифты (Inter / Segoe UI / -apple-system) — не подключаем веб-шрифты, чтобы не было FOIT и потерь при печати.

## Notes / gotchas
- A4 = 794×1123px @ 96dpi. Размер страницы не менять, Chrome печатает 1:1.
- Кириллические пути в `file://` URL ломаются — `build.sh` процент-кодирует через Python.
- Переполнение страницы = низ режется молча. Лечится сокращением списков, уменьшением `padding`, фиксированной высотой плиток (`height: 138px`) вместо `aspect-ratio`.
- Localization placeholders: при работе для не-российского клиента (Алматы, Казахстан и т.д.) — сразу заменять валюту, имена, телефоны, документы (СРО → допуск ОТ, УК → КСК), уличные адреса. См. industrial-climbers-flowops для эталона.
- Для premium B2B decks не выводить агрессивный ROI слишком рано без сильного proof рядом. Сначала продавать скорость, предсказуемость, контроль и снижение хаоса; точные цены лучше оставлять для client-specific КП или поздней стадии разговора.
- Для PDF-экспорта полностью отключать тени карточек через `@media print`, а в HTML оставлять обычные мягкие `rgba`-тени. Chrome может сплющивать blur-shadow в грязные прямоугольники при печати в PDF.
