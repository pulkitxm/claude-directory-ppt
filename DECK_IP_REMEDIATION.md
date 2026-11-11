# Presentation IP remediation

Review and deployment date: 2026-11-11. Repository: `pulkitxm/claude-directory-ppt`. The withdrawal was squash merged into `main` as `e8609eb25f50ab55cf2979b674c78648ec939b3f`.

The owner approved review publication, merge, and deployment. The text-only withdrawal is now merged, deployed, and verified on the canonical public site. Historical content in Git history, forks, or external caches remains subject to a separate approved remediation plan. No original deck or recording was uploaded as review evidence.

## Review publication

[Pull request 3](https://github.com/pulkitxm/claude-directory-ppt/pull/3) was squash merged through Pukbot, and its remote review branch was deleted. The complete withdrawal checkpoint was `ea108ef24e99c07fc5aa06994657ba835d922cf1`; the reviewed merge is `e8609eb25f50ab55cf2979b674c78648ec939b3f`. Both disputed media-bearing artifacts are absent from the current source tree.

The required review and post-merge verification checks passed. The owner-authorized `publish=true` dispatch completed successfully in [deployment run 43009863289](https://github.com/pulkitxm/claude-directory-ppt/actions/runs/43009863289), producing GitHub Pages deployment `7708524878` from the reviewed merge. No history rewrite, force-push, or cache purge was performed.

## Scope and findings

Every tracked file in the current source tree was inspected: the README, ignore file, deployment workflow, two presentation HTML paths, and standalone promotional recording metadata. There are no other project directories. No repository license or asset-provenance record was present for the old presentation/media.

The two HTML files were byte-identical. Each embedded a 15,908,332-byte MP4 directly as base64 and two PNG payloads. They promoted preview, prompt and code access to the directory collection, including curated sets from Lexington Themes, Aceternity, Magic UI and shadcnblocks, and asserted unrestricted reuse. The presentation loaded Reveal.js from a CDN, Google Fonts, and an external portfolio portrait. The standalone promo has a different SHA-256 from the embedded MP4. Renaming the deck would not remove the embedded recording.

Risk classification: HIGH RISK for continued public distribution pending review, because the artifact embeds promotional media of the disputed collection without provenance or verified redistribution permission. This is a precautionary withdrawal. No claim is made that every frame or image infringes, and no frame-by-frame licensing clearance was performed. The prior collection's unresolved rights are not cured by its generation method or its former open-source claims.

The presentation and standalone promo are removed rather than rebuilt from the same examples. The root route is replaced with an original text-only notice; a matching 404 document explains unavailable content. No media, branding, illustrations, captured third-party source, remote fonts, external scripts, tracking or demo links remain in the new publishing artifact. No unrelated project was found or deleted.

The partial checkout did not restore the original standalone MP4 or embedded presentation into the source tree. Read-only size inspection triggered lazy hydration of historical HTML and recording blobs in local Git storage. Those bytes were never opened, served, or uploaded as evidence. Local disposable caches were cleaned during preparation; no historical remote references were changed. Local cache cleanup does not remove public historical content, and subsequent verification avoids operations that request historical blob contents or sizes.

## File evidence

Hashes preserve identity without redistributing the content.

| Original path | SHA-256 | Action |
| --- | --- | --- |
| `index.html` | `54d82ccb2703f3ffc5b91a559e77a5f819c9a7ffc483a48ba06781a1a4c0bd33` | Replaced with original review notice |
| `claude-directory-deck.html` | `54d82ccb2703f3ffc5b91a559e77a5f819c9a7ffc483a48ba06781a1a4c0bd33` | Removed from source and publishing artifact |
| `promo-x.mp4` | `747e048284a7a6a14c2d9794e079f27934ddf8ff2acbf8c8e31e46aa095e52e9` | Removed from source and publishing artifact |

| Embedded payload formerly present in each HTML | SHA-256 | Bytes |
| --- | --- | --- |
| `video/mp4` | `b904bd5001b89c66e75c6cd6aeef053793d4227b2b5e29d4abaa2a02d9ea9fef` | 15908332 |
| `image/png` | `82277913389ed17920b2056e14ca8a8277be07d9fdf1cf0ed2f29ac71cfbbad9` | 3760 |
| `image/png` | `bd96fd22cea7858624d5ce454ea55f2813ebb85ba157d5c0d54a5b92193684e8` | 3828 |

## Publishing safeguards

The former workflow uploaded the entire repository and deployed automatically on pushes to `main`. The replacement always verifies source but deploys only on an explicitly approved manual dispatch on `main` with `publish=true`. It preserves the existing Pages app-token integration without reading its secrets. The artifact is freshly constructed from an explicit allowlist containing only `index.html` and `404.html`, so source reports, scripts, Git files, old decks and media cannot be uploaded accidentally.

`scripts/check-site.py` rejects media files, the old deck path, media/loading tags, embedded base64 and CSS asset imports, validates the review notices, and constructs the allowlisted output. Checks complement manual review and do not establish legal compliance. The notices and checking code introduce no third-party assets or dependencies. No license rights are granted to historical materials by this remediation.

## Live deployment and historical content

The earlier live presentation and direct media URLs returned 200 before the withdrawal. The deployed replacement was verified at 11:12 UTC on 2026-11-11 using the canonical URLs, with and without cache-control headers and without query-string cache busting.

| URL or destination | Deployed observation | Status |
| --- | --- | --- |
| `https://pulkitxm.github.io/claude-directory-ppt/` | 200, Content-Length 1,270, Last-Modified 2026-11-11 11:11:47 UTC, Cache-Control max-age=600 | Original text-only notice verified; no embedded or remote media |
| `https://pulkitxm.github.io/claude-directory-ppt/claude-directory-deck.html` | Canonical HEAD 404, Content-Length 1,239 | Withdrawn; no old response body downloaded |
| `https://pulkitxm.github.io/claude-directory-ppt/promo-x.mp4` | Canonical HEAD 404, Content-Length 1,239 | Withdrawn; no recording downloaded |
| GitHub Pages environment `github-pages` | Successful deployment `7708524878`, source `e8609eb25f50ab55cf2979b674c78648ec939b3f` | Fresh two-file notice artifact deployed |
| GitHub releases and tags | Review API returned no releases or tags | No release/tag removal identified |
| GitHub Actions artifacts | Deployment builds only the verified two-file notice artifact | Original deck and media are not included |
| Source history and forks/external caches | Historical HTML embeds and recording remain reachable from published Git history | Separate owner/legal review and approved history-removal plan required |

Ordinary canonical cache responses also returned the new notice and both 404 outcomes, with observed Age 13 seconds. No stale original bytes were observed at this vantage. Other caches, historical URLs, forks, and external copies are not cleared by these checks.

GitHub Pages has no custom domain for this repository and HTTPS enforcement is enabled. The public presentation also links the directory repository and portfolio gallery, so all three source repositories need coordinated review. The directory and portfolio edits do not update this independent Pages deployment automatically.

## Verification and pending actions

The text-only source and explicit publishing artifact checker passed. Actionlint passed for the revised workflow. Browser checks at 375px and 1440px passed: the root notice renders, no media or external-loading elements exist, and there is no horizontal overflow. Local and deployed checks confirm the old direct deck and recording paths return 404. The successful live deployment is recorded above.

1. Review historical Git commits, forks, cached presentation previews, and external copies with the owner and appropriate licensing/legal review. Current source and live-site withdrawal does not erase historical copies.
2. If historical removal is approved separately, coordinate the MP4 and embedded HTML payload removal across contributors, branches, commit URLs, forks, and caches. Do not force-push or rewrite published history automatically.
3. Recheck other cache locations if a stale original response is reported; request a provider/CDN invalidation only when required and authorized.

Current source and the managed public Pages deployment have been remediated and verified. Only historical or external-copy review remains pending. This is an operational withdrawal record, not a legal-compliance determination. This documentation update does not change the served two-file artifact and requires no additional deployment.
