# FlowOps Pitch Deck — Template

A4-портретный HTML → PDF шаблон для коммерческих презентаций FlowOps в стиле `speed-to-lead-business-overview.pdf` (чистый минимализм, синий градиент, eyebrow + крупный H1, карточки со скруглениями и боковыми акцентами).

## Related
- [[../patterns/flowops-pdf-presentations]]
- [[../projects/industrial-climbers-flowops]] — реальный пример использования

## Как пользоваться

1. **Скопировать шаблон в рабочую папку проекта:**
   ```bash
   mkdir -p "~/Desktop/<Имя-Проекта>"
   cp "/Users/tamerlan/Documents/TamerMemoryDB/Tamerlan Memory DB/templates/flowops-pitch-deck/template.html" \
      "~/Desktop/<Имя-Проекта>/index.html"
   ```
2. **Заменить контент** в `index.html` (структура и стили уже готовы — только текст и количество секций).
3. **Собрать PDF** одной командой (см. `build.sh`):
   ```bash
   bash "/Users/tamerlan/Documents/TamerMemoryDB/Tamerlan Memory DB/templates/flowops-pitch-deck/build.sh" \
        "~/Desktop/<Имя-Проекта>/index.html" \
        "~/Desktop/<Имя-Проекта>/output.pdf"
   ```

## Структура файла
- **CSS-токены** в `:root`: цвета (`--blue-500`, `--ink-900`, `--navy` и т.д.), радиусы, тени, градиент.
- **Страница**: `<section class="page">` + `.frame` (отступы), верхний 8-px градиентный borderTop сам рисуется через `::before`.
- **Размер**: 794×1123px = A4 @ 96dpi. Не менять — Chrome печатает 1:1.

## Доступные компоненты

### Hero (1-й слайд, тёмный градиент)
```html
<div class="hero">
  <div class="grid-overlay"></div>
  <div class="brand">…</div>
  <div class="eyebrow">…</div>
  <h1>… <span class="accent">акцент</span></h1>
  <p class="sub">…</p>
  <div class="pills">…</div>
  <div class="footer-strip">4× stat-h</div>
</div>
```

### Eyebrow + H1 + lead (стандартный заголовок страницы)
```html
<div class="eyebrow">СЕКЦИЯ В UPPERCASE</div>
<h1>Большой заголовок<br/>с переносом по смыслу.</h1>
<p class="lead">Подзаголовок 1–2 строки.</p>
```

### Сетки
- `.grid.grid-2` / `.grid-3` / `.grid-4` — gap 14px.

### Карточки
- `.card` — белая, базовая
- `.card.tinted` — светло-голубая
- `.card.soft` — серая
- `.card.accent-l` — синяя полоса слева
  - модификаторы цвета: `.green` / `.amber` / `.rose` / `.violet`
- Внутри: `<div class="num">1</div>` + `<div class="title">…</div>` + `<div class="body">…</div>` + `<ul>…</ul>`

### Stat-цифры
```html
<div class="stat"><div class="num">30 сек</div><div class="label">До первого контакта</div></div>
```

### Pills / chips
- `<span class="pill">текст</span>` — голубой
- `<span class="pill gray">текст</span>` — серый

### Pipeline (горизонтальная цепочка шагов)
```html
<div class="pipeline">
  <div class="stepbox blue">Лид</div>
  <div class="stepbox dark">AI-звонок</div>
  <div class="stepbox">CRM</div>
</div>
```

### Callout (выноска)
- `<div class="callout">…</div>` — амбер (внимание)
- `<div class="callout blue">…</div>` — голубой (info)

### Before / After
```html
<div class="ba">
  <div class="col before"><h4>Как было</h4><ul>…</ul></div>
  <div class="col after"><h4>Как стало</h4><ul>…</ul></div>
</div>
```

### Wireframe (схема страницы / процесса)
```html
<div class="wire">
  <div class="wire-row hero-row">…</div>
  <div class="wire-row">…</div>
  <div class="wire-row cta">…</div>
</div>
```

### Timeline (4 недели / спринта)
```html
<div class="timeline">
  <div class="tl">
    <div class="wk">Неделя 1</div>
    <div class="ti">Фундамент</div>
    <ul>…</ul>
  </div>
</div>
```

### Chat bubbles (диалоги AI ↔ клиент)
```html
<div class="chat">
  <div class="bubble ai"><div class="who">AI</div>…</div>
  <div class="bubble client"><div class="who">Клиент</div>…</div>
</div>
```

### Creative tiles (рекламные плитки 3×N)
```html
<div class="creatives">
  <div class="creative c1"><span class="tag">REELS</span><div class="head">Заголовок</div></div>
</div>
```
Доступные градиенты: `c1` (navy), `c2` (sky), `c3` (slate), `c4` (green), `c5` (orange), `c6` (violet). Высота фиксированная — 138px.

### Таблицы
- `<table class="simple">` — без рамок, тонкие линии-сепараторы, header в uppercase.

### Прогресс-бары (доли бюджета и т.п.)
```html
<div class="bar-row"><div class="lbl">B2B</div><div class="bar"><span style="width: 45%"></span></div><div class="v">45%</div></div>
```

### Подпись страницы
- `<div class="pagenum">02 / 14</div>` — нижний правый угол.
- `<div class="footnote">…</div>` — серая мелкая подпись внизу со светлой линией.
- `<div class="contact-cards">2× .contact-card</div>` — контакты в финале.

## Подводные камни

1. **Переполнение A4** = низ страницы режется в PDF. Лечится:
   - сокращением `<li>` (4 пункта вместо 6),
   - уменьшением `padding`/`line-height` в карточке,
   - фиксированной высотой плитки (`height: 138px`) вместо `aspect-ratio`,
   - сокращением H1.
2. **Эмодзи** в Chrome headless рендерятся непредсказуемо. Используем только текст и SVG-цвета. В шаблоне эмодзи нет.
3. **Кириллица** работает из коробки на системных шрифтах (Inter / Segoe UI / -apple-system). Не подключаем веб-шрифты — медленнее и могут не успеть загрузиться.
4. **URL для печати** в Chrome требует процент-кодирования кириллических путей. См. `build.sh` — там это сделано через `python3 -c`.

## Что хорошо менять под каждый проект
- Hero-градиент (`.hero` background) — можно адаптировать под бренд клиента.
- Палитру в `:root` — особенно `--blue-500` / `--blue-700` / `--navy`.
- Логотип `.brand .dot` — буква и градиент.
- Кол-во и порядок слайдов — каркас одинаковый.
