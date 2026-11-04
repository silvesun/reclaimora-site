# Reclaimora support website

Bilingual static support website for Reclaimora, published by GitHub Pages from `main` at the repository root.

- Home: https://silvesun.github.io/reclaimora-site/
- Support: https://silvesun.github.io/reclaimora-site/support.html
- Privacy: https://silvesun.github.io/reclaimora-site/privacy.html
- English: https://silvesun.github.io/reclaimora-site/en/
- Feedback: https://github.com/silvesun/reclaimora-site/issues/new/choose

Maintainer: [silvesun](https://github.com/silvesun). Feedback is public and requires a GitHub account to post. Never request private files, account information, full paths or unredacted scan records.

## Local preview and validation

```bash
python3 scripts/check_site.py
python3 -m http.server 8765 --bind 127.0.0.1
```

No build dependencies, JavaScript, analytics, remote fonts or forms. All assets are hosted here. Screenshots are captured from the actual app using fictional data. Keep both languages consistent with the shipping app; moving files to Trash does not immediately free space, restoration is conditional, and Photos library recovery is managed by Photos.

Update `privacy.html` and `en/privacy.html` together whenever data handling changes. GitHub Pages/Issues have their own data processing, separate from the offline app. Pushes to `main` trigger GitHub Pages publication and the static link check workflow. No App Store download URL is advertised until a live listing is confirmed.
