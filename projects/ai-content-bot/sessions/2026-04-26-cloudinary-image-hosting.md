# Session 2026-04-26 — Cloudinary Image Hosting

## Related
- [[overview]]
- [[current-state]]
- [[next-steps]]
- [[risks]]

## What was done
- Added Cloudinary signed image upload to WF-09.
- New path:
  - `Extract Image Base64`
  - `Prepare Cloudinary Upload`
  - `Upload Image to Cloudinary`
  - `Finalize Record`
- `Finalize Record` now stores Cloudinary `secure_url` into `image_url`.
- WF-11 already attaches `image_url` to Buffer via `assets.images[].url`.

## Key findings
- Cloudinary credentials found by user were enough for signed upload:
  - `cloud_name`: `drzrljg9t`
  - API key and secret are used in WF-09 Code node.
- Buffer requires a public image URL; it cannot use Gemini base64/binary directly.

## Blockers
- Security cleanup remains: Cloudinary secret is currently embedded in the workflow JSON for speed.

## Next steps
- Import WF-09 and WF-11.
- Generate a new post and verify `Posts.image_url` is populated.
- Approve one selected channel and confirm Buffer publishes with the image.
- Move Cloudinary secret into n8n credentials/env or switch to unsigned preset.
