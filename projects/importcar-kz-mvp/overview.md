# ImportCar.kz MVP — Overview

## Related
- [[current-state]]
- [[decisions]]
- [[risks]]
- [[next-steps]]
- [[prompts]]

## Content
ImportCar.kz is a multi-session MVP for a Kazakhstan-focused premium car-import experience. The product began as a Kolesa-like marketplace flow and has evolved into a cinematic private-showroom prototype for importing premium cars from Korea.

Core user flow:
1. browse premium demo listings
2. open a car detail view
3. inspect the import estimate and trust/proof layer
4. compare importer partners
5. submit a lead request

Current implementation lives in `~/Desktop/importcar-kz-mvp` and uses React + TypeScript + Vite, optional Supabase lead capture, and Vercel deployment.

## Product shape
- Premium-only demo inventory inspired by Korean marketplace-style listings
- Versioned pricing-rules engine with explainability and warnings
- Trust/proof layer: auction preview, verification stages, recent proof case
- Importer comparison as concierge-partner selection
- Lead capture modal with mock fallback and optional Supabase persistence

## Live surface
- Production alias: `https://importcar-kz-mvp.vercel.app`
