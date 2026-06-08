# PromAlp — Current State

## Related
- [[overview]]
- [[decisions]]
- [[risks]]
- [[next-steps]]

---

## Сайт (promalp-site)
- Статус: в разработке, см. [[../promalp-site/current-state]]
- Стек: Next.js 14 + Vercel + Airtable + Telegram alert

## Видео (обновлено 2026-06-02)
- Статус: **АНАЛИЗ ЗАВЕРШЁН → готов к монтажу**
- iPhone: 36 клипов MOV (9:16, 60fps) + DJI: 69 клипов MP4 (16:9, 30fps) = 105 файлов
- **5 объектов**: Купол (OBJ-1), ЖК Бежевый (OBJ-2), ЖК Серый (OBJ-3), ЖК Золотой (OBJ-4), Magnum ТРЦ (OBJ-5)
- **ТОП кадры**: IMG_4835 (дети в окне🏆), IMG_4824 (вид сверху), IMG_4821 (портрет улыбка), IMG_4858/4861 (горы), dji601_22 (двое на синем фасаде)
- **Стратегия готова**: `video-strategy-output/` — 5 файлов (каталог, лучшие моменты, 10 рекл. сценариев, 15 органических, ТЗ монтажёра, промпт след. агента)
- **Не хватает**: «после»-кадров (чистый фасад), активной мойки, документов (Допуск ОТ)
- **⚠️ NB**: Уточнить у Айдоса разрешение Magnum на публикацию кадров с их объектом
- **Production briefs готовы**: `first-5-video-briefs/` — 8 файлов с точными монтажными картами
- **Remotion полный проект**: `/Users/tamerlan/Desktop/promalp-video/` — 5 compositions ✅
  - Ad01DirtyFacade (720f, 24s), Ad02HeightTrust (660f, 22s), Ad03CommercialObjects (705f, 23.5s)
  - Oc01KidsOrganic (660f, 22s) ⚠️ blur детей, Oc02MountainsTrust (810f, 27s)
  - Все compositions: typecheck ✅, bundle ✅, compositions CLI ✅
  - Shared компоненты в src/components/ и src/styles/theme.ts
  - Рендер через `npm run render:ad01` ... `npm run render:all`
- **⚠️ Обязательно перед публикацией**: проверить blur детей в OC-01 в Remotion Studio
- **Следующий шаг**: 1) Добавить музыку, 2) Проверить QA-чеклист, 3) Рендерить, 4) Уточнить тексты у Айдоса

## Маркетинг
- Статус: не начат
- Зависит от: готового видео + запущенного сайта

## Notion Office (обновлено 2026-06-08)
- Зонтичный проект добавлен в Notion Office:
  - https://app.notion.com/p/3793e026e92f8188ab77f0b511aa78b6
- Статус: Active; health: Yellow; priority: P1.
- Зафиксированы 8 фаз:
  - site MVP foundation and video analysis completed;
  - discovery blocked by client inputs;
  - video production and site activation in progress;
  - Instagram, ads, and optimization not started.
- Добавлены только подтверждённые задачи и blockers from memory; speculative 15-post and expanded CRM plans are not treated as immediate launch blockers.
