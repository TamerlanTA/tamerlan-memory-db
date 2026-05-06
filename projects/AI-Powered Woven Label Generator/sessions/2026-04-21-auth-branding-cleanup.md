# Session 2026-04-21 — Auth Branding Cleanup

## Related
- [[projects/David/overview]]
- [[projects/David/current-state]]
- [[projects/David/next-steps]]
- [[projects/David/risks]]

## What was done
- Audited the Clerk login path and confirmed `/sign-in` was rendering the raw Clerk `<SignIn />` component on a blank app background.
- Added a shared Clerk branding helper with Griffes Vivienne logo, colors, support email, and FR/EN localized auth copy.
- Moved `ClerkProvider` under `LanguageProvider` so Clerk auth text can follow the current app language.
- Reworked `/sign-in` into a minimal Griffes Vivienne branded page using the existing `AppHeader`, legal footer, and restrained client-space copy.
- Added focused tests for the Clerk branding helper.

## Key findings
- The unbranded experience was code-side: no `appearance` or `localization` was passed to Clerk, so Clerk could fall back to default project/dashboard identity such as "My Application".
- Some Clerk surfaces may still depend on Clerk Dashboard application settings, especially hosted/account-portal surfaces outside embedded React components.

## Blockers
- None in code.

## Next steps
- In Clerk Dashboard, confirm the application name/logo are set to Griffes Vivienne for any hosted/account-portal surfaces that do not read the embedded React appearance/localization.
- Browser-check `/sign-in` in FR and EN with a real Clerk publishable key.
