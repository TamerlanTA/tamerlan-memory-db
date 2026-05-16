# ImportCar.kz MVP — Next Steps

## Related
- [[overview]]
- [[current-state]]
- [[risks]]
- [[decisions]]

## Content
### Immediate — open bugs from supervisor audit
1. Fix `DealProofSection.tsx:27` — drive purchase price from `proofCase` data, not hardcoded string.
2. Add `onClick` to "Details" button in `ImporterCard.tsx:57` (expand detail panel or remove button).
3. Add `onClick` to "View sample report" button in `AuctionSheetPreview.tsx:43` or remove button.
4. Add phone format validation in `LeadForm.tsx:108` (min-length or regex before submit).
5. Resolve `Car.sourceCountry` — either remove the field or implement multi-source logic.

### Medium-term
6. Add authenticated admin access before enabling operational lead management (RLS UPDATE policy).
7. Configure a real Supabase project and apply `schema.sql` + `seed.sql` if beyond mock/demo mode.
8. Validate pricing-rules logic against real Kazakhstan import law and broker quotes.
9. Replace placeholder visuals with licensed car-specific imagery.
10. Decide next milestone: stronger demo layer vs. first real backend milestone.
