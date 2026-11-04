# Reclaimora support website

English-only support website for Reclaimora’s planned United States App Store launch. Published with GitHub Pages from `main` at the repository root.

- Home: https://silvesun.github.io/reclaimora-site/
- Support URL: https://silvesun.github.io/reclaimora-site/support.html
- Privacy Policy URL: https://silvesun.github.io/reclaimora-site/privacy.html
- Feedback: https://github.com/silvesun/reclaimora-site/issues/new/choose

The old `/en/index.html`, `/en/support.html` and `/en/privacy.html` URLs continue to serve English content. The root URLs are canonical. There are no Chinese pages or language switches.

Maintainer: [silvesun](https://github.com/silvesun). Posting feedback requires a GitHub account. Issues are public: never include private files, account information, full paths or unredacted scan records.

## Preview and checks

```bash
python3 scripts/check_site.py
python3 -m http.server 8765 --bind 127.0.0.1
```

No build dependencies, JavaScript, analytics, remote fonts or forms. Screenshots show the actual app with fictional data. File cleanup moves files to Trash and does not immediately free space; restoration is conditional. Photos manages library recovery in Recently Deleted.

Keep the root and `/en/` pages consistent. GitHub Pages and Issues process requests separately from the offline app, as explained in the privacy policy. No App Store download link is advertised until the listing is confirmed live.

App Store Connect distribution must be set separately to United States only, with English (U.S.) as the primary language. Publishing this website does not change storefront availability or the app’s in-app language support.
