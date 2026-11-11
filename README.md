# UI experiment presentation review

The earlier presentation and promotional recordings are withdrawn from this source tree during an asset and licensing review. The site now contains only an original text notice with system fonts. It loads no external libraries, fonts, images, videos, frames, or tracking scripts.

The presentation promoted the UI experiment collection in [the source repository](https://github.com/pulkitxm/claude-directory). Its review is coordinated with the collection and the portfolio gallery. Public previews do not grant redistribution rights, and generated implementations can still involve third-party rights.

Run `python3 scripts/check-site.py` to validate the notice, then `python3 -m http.server 4175 --directory site` to preview the publishing artifact. The checker builds `site` from an explicit two-file allowlist. The previous deck URL and `promo-x.mp4` are absent from that artifact.

Publishing requires review, owner approval, and a manually dispatched deployment with `publish=true`. No deployment is triggered by a push. See [the remediation report](DECK_IP_REMEDIATION.md) for pending live-site and history actions. Passing checks does not establish legal compliance.
