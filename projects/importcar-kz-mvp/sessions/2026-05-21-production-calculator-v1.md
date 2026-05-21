# Session 2026-05-21 — Production Calculator v1 built

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[decisions]]

## Что было сделано

Полностью реализован Production Calculator v1 (v0.1 roadmap milestone).

### Изменения

**`src/components/BottomNav.tsx`**
- Tab type изменён: `'calculator' | 'catalog' | 'favorites' | 'request'`
- Порядок вкладок: Калькулятор (первый, дефолт) / Каталог / Избранное / Заявка
- IconPerson заменена на IconDocument для вкладки Заявка

**`src/App.tsx`**
- Default tab изменён с `'catalog'` на `'calculator'`
- Import ProfileScreen → RequestScreen
- `'profile'` → `'request'` в render

**`src/components/RequestScreen.tsx`** (новый файл)
- Переименованный ProfileScreen с обновлённым заголовком "Заявки"
- Пустое состояние теперь ссылается на "калькулятор или каталог"

**`src/components/CalculatorScreen.tsx`** (полная замена)
- Новые поля: Страна покупки (Korea/Japan/UAE/USA), Город доставки (Алматы/Астана/Шымкент/Другой)
- Trust strip: ✓ Бесплатно / ✓ 30 секунд / ✓ Без регистрации
- CTA кнопка "Рассчитать стоимость" — reveal-on-click UX
- Result card: тёмно-зелёный hero с большим KZT итогом + ≈ USD
- 7 строк разбивки (карPriceKzt, доставка, таможня, утиль, брокер, регистрация, комиссия)
- Explainability accordion "Как рассчитана стоимость" (возраст, объём, тип, ставка, версия правил, warnings)
- Disclaimer: "Расчёт является предварительным и не является публичной офертой..."
- Lead capture: ссылка на авто (optional), имя, телефон, город, комментарий
- CTA: "Получить точный расчёт" + "Написать в WhatsApp"
- Calculation snapshot сохраняется в metadata JSONB при submit

**`supabase/schema.sql`** (migration добавлена в конец)
- `car_id` и `importer_id` стали nullable (для calculator leads)
- Добавлены `metadata jsonb` и `source text default 'catalog'`

**`src/components/AdminLeads.tsx`**
- Select включает `metadata` колонку
- Calculator leads показывают CalcContext: страна, год, объём, тип, город доставки, версия правил, ссылка на авто, warnings

**`src/App.css`**
- Добавлены стили для всех новых элементов: `.calcV2Header`, `.calcV2Title`, `.calcV2TrustStrip`, `.calcCtaBtn`, `.calcResultV2`, `.calcResultV2Hero`, `.calcResultV2Total`, `.calcResultV2Approx`, `.calcExplainPanel`, `.calcExplainBody`, `.calcExplainRow`, `.calcDisclaimerV2`, `.calcLeadCapture`, `.calcLeadForm`, `.calcLeadActions`, `.calcWaBtn`, `.calcLeadSuccess`, `.adminCalcContext`

## Проверено

- `npm run lint` — чисто
- `npm run build` — чисто (460 kB)
- Preview: calculator открывается первым, все поля работают, результат появляется после клика, explainability разворачивается, lead form отображается корректно, Заявка вкладка работает

## Next steps (из next-steps.md)

v0.1 Production Calculator фактически завершён (все 8 задач выполнены).
Следующий блок: v0.3 Supabase Auth или immediate fixes (WhatsApp номер, desktop top-nav).
