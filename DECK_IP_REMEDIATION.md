# Presentation IP remediation

Review date: 2026-11-11. Repository: `pulkitxm/claude-directory-ppt`. Local branch: `ip-remediation-deck`, based on `c19bbd3f749848fcefb0af23bb77fdb8235a2e6e`.

The owner approved publishing this withdrawal on a dedicated review branch and creating a pull request on 2026-11-11. Branch publication is authorized; merging, deployment, history rewrites, and cache purges remain pending separate approval. No original deck or recording was uploaded as review evidence.

## Review publication

The withdrawal is published for review in [pull request 3](https://github.com/pulkitxm/claude-directory-ppt/pull/3) on `ip-remediation-deck`. The complete withdrawal checkpoint is `ea108ef24e99c07fc5aa06994657ba835d922cf1`. The remote branch contains only the two notice documents, documentation, workflow, and source checker; both disputed media-bearing artifacts are absent.

The first review run passed `verify` and skipped `deploy`: [workflow run](https://github.com/pulkitxm/claude-directory-ppt/actions/runs/43006150137). The latest Pages deployment remains the original 2026-08-24 deployment listed below. No merge, deployment, history rewrite, or cache purge was requested or performed.

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

| URL or destination | Observation on review date | Status |
| --- | --- | --- |
| `https://pulkitxm.github.io/claude-directory-ppt/` | HEAD 200, Content-Length 21,234,808, Last-Modified 2026-08-24, Cache-Control max-age=600 | Old presentation still public; replacement pending approval |
| `https://pulkitxm.github.io/claude-directory-ppt/claude-directory-deck.html` | HEAD 200, same content length and cache metadata | Old direct deck URL still public; removal pending approval |
| `https://pulkitxm.github.io/claude-directory-ppt/promo-x.mp4` | HEAD 200, Content-Length 57,042,795, same cache metadata | Recording still public; removal pending approval |
| GitHub Pages environment `github-pages` | Last successful deployment `6069409964`, source `c19bbd3f749848fcefb0af23bb77fdb8235a2e6e` | Fresh allowlisted deployment required |
| GitHub releases and tags | API returned no releases or tags | No release/tag deletion identified in this repository |
| GitHub Actions artifacts | API returned zero artifacts | Recheck before publication; do not reuse an old build |
| Source history and forks/caches | Historical HTML embeds and recording remain reachable from published Git history | Separate owner/legal review and approved history-removal plan required |

GitHub Pages has no custom domain for this repository and HTTPS enforcement is enabled. The public presentation also links the directory repository and portfolio gallery, so all three source repositories need coordinated review. The directory and portfolio edits do not update this independent Pages deployment automatically.

## Verification and pending actions

The text-only source and explicit publishing artifact checker passed. Actionlint passed for the revised workflow. Browser checks at 375px and 1440px passed: the root notice renders, no media or external-loading elements exist, and there is no horizontal overflow. The local publishing server returned 404 for `claude-directory-deck.html` and `promo-x.mp4`. These are local checks; live withdrawal remains pending approval.

1. Review the authorized withdrawal branch and pull request. Only the review publication was approved; merging and deployment remain pending. Do not attach the original recording or deck as public evidence.
2. After approved merge, explicitly dispatch the workflow with `publish=true` for the reviewed `main` revision. Configure required owner review on the `github-pages` environment where available.
3. Verify the actual root notice and 404 responses for both the old direct deck path and the standalone MP4. Verify the root response contains no embedded base64 media and no remote assets.
4. Recheck after the observed 600-second cache window; request GitHub/CDN invalidation if old bytes remain. Review cached presentation previews and any external copies separately.
5. Coordinate removal of the historical MP4 and embedded HTML payloads with the owner and appropriate licensing/legal review. An approved rewrite, if chosen, must account for contributors, branches, commit URLs, forks and caches. Do not force-push or rewrite published history automatically.

Deployment and historical cleanup remain pending approval. Branch publication does not withdraw the current live site, and local checks do not mean the live site has been remediated.
