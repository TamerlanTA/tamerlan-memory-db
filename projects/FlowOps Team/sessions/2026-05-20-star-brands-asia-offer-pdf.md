# Session 2026-05-20 — Star Brands Asia Offer PDF

## Related
- [[00 - Overview]]
- [[What to Do First]]
- [[Pipeline C — Website Audit Generator]]
- [[flowops-pdf-presentations]]

## What was done
- Prepared a FlowOps-style PDF offer for Star Brands Asia using the existing `templates/flowops-pitch-deck` visual system.
- Packaged the offer around `FMCG Field Sales Control System`, not a generic AI/chatbot pitch.
- Built a 9-page A4 PDF without pricing, focused on a low-risk pilot for one branch.

## Key findings
- Public website signals used: Star Brands Asia states 21 branches in Kazakhstan, 48,989 retail outlets, 741 sales representatives, 100+ SKU, 4 production sites, and 1,800+ employees/partners.
- Best-fit offer angle: field sales control for trading representatives and supervisors: visits, shelf photos, SKU availability, store orders, issue escalation, and branch dashboards.
- Safer entry point: one branch pilot with 10-30 sales representatives before any larger rollout or ERP integration discussion.

## Artifacts
- HTML: `/Users/tamerlan/Desktop/StarBrandsAsia_FlowOps_Offer/index.html`
- PDF: `/Users/tamerlan/Desktop/StarBrandsAsia_FlowOps_Offer/StarBrandsAsia_FlowOps_Offer.pdf`
- Preview: `/Users/tamerlan/Desktop/StarBrandsAsia_FlowOps_Offer/preview/StarBrandsAsia_FlowOps_Offer.pdf.png`

## Verification
- PDF generated successfully with Chrome headless via `templates/flowops-pitch-deck/build.sh`.
- Output file size: ~868 KB.
- Page count: 9.
- Quick Look generated a thumbnail preview successfully.

## Blockers
- No private operational data from Star Brands Asia yet; all pain points are framed as hypotheses from public scale signals.
- Final scope depends on a diagnostic call with commercial/operations leadership.

## Next steps
- If outreach is planned, send a short message offering a 30-45 minute diagnostic and a pilot map for one branch.
- If they reply, ask for current visit/reporting workflow, sample supervisor report, key SKU list, and one target branch for pilot scoping.
