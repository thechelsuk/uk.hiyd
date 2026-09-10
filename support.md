---
title: "Support"
eyebrow: "Help"
summary: "Guides, answers, and how to reach a human."
description: "Get help with Hiyd: quick start, links to the guides and FAQ, troubleshooting for the iOS app and Chrome extension, and how to report bugs or request features."
---

## Start here

- **New to Hiyd?** Read [Getting started](/guides/getting-started/).
- **Common questions** are answered in the [FAQ](/faq/).
- **All guides:** [Front matter defaults](/guides/front-matter/) ·
  [Publish to GitHub](/guides/publish-to-github/) ·
  [Shortcuts &amp; Siri](/guides/shortcuts-and-siri/) ·
  [Deep links](/guides/deep-links/).

## Quick start

**iOS app** — Install from the [App Store]({{ site.app_store_url }}) (iOS
{{ site.min_ios_version }}+), open the **Create** tab, write a title and body,
then use **••• › Save** to keep the file in iCloud Drive or **••• › Publish** to
commit it to GitHub.

**Chrome extension** — Install from the
[Chrome Web Store]({{ site.chrome_store_url }}), open a page you want to link to,
and use the extension to capture it as a Markdown link post.

## Troubleshooting

### iCloud shows "Unavailable"

Hiyd stores notes in iCloud Drive. If Settings shows iCloud as Unavailable:

1. Check **Settings › [your name] › iCloud › iCloud Drive** is on.
2. Confirm the device has a network connection and enough storage.
3. Make sure Hiyd is allowed to use iCloud Drive.

You can still use **Export** to move drafts out manually while iCloud is
unavailable.

### A post didn't publish to GitHub

- "Unable to access this repository" — re-check the username, the repository name
  on its own (no `owner/` prefix), and that the token's **Contents** permission
  is **Read and write** for that repo.
- "File already exists" — confirm the overwrite prompt, or change the filename.
- "Too large" — the GitHub Contents API path is limited to 5 MB.
- "Rate limit reached" — wait and try again.

See the [publishing guide](/guides/publish-to-github/) for the full setup.

### The app won't open or crashes

Restart the device, update to the latest iOS, then reinstall from the App Store.
If it persists, email us with your device model and iOS version.

### Chrome extension not appearing

Check it is enabled at `chrome://extensions`, pin it to the toolbar, and restart
the browser.

## Bug reports

Email <support@hiyd.uk> with "BUG REPORT" in the subject and include:

- device / browser and version
- what you did, what you expected, and what happened
- a screenshot if you have one

## Feature requests

Send ideas to <support@hiyd.uk> — a short description of the feature and the
Jekyll workflow it would help.

## Contact

| Purpose | Address |
| --- | --- |
| General support | <support@hiyd.uk> |
| Security issues | <security@hiyd.uk> |
| Privacy questions | <privacy@hiyd.uk> |
| Business enquiries | <hello@hiyd.uk> |

Typical response times: critical issues within 24 hours, general questions within
2–3 days, feature requests within a week.

## Community

- Reddit: [r/hiydapp]({{ site.social.reddit }})
- Bluesky: [@hiyd.uk]({{ site.social.bluesky }})

## Jekyll resources

- [Jekyll documentation](https://jekyllrb.com/docs/)
- [GitHub Pages with Jekyll](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll)
- [Markdown Guide](https://www.markdownguide.org/)
