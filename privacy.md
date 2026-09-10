---
title: "Privacy Policy"
eyebrow: "Legal"
summary: "What Hiyd does and does not collect, and where your content lives."
last_updated: "10 September 2026"
description: "Hiyd's privacy policy: no accounts, no analytics in the app, content stored in your own iCloud Drive, and GitHub contacted only when you choose to publish."
---

Hiyd ("we", "our", "us") makes the Hiyd iOS app and the Hiyd Chrome extension.
This policy explains what happens to your information when you use them and this
website.

## The short version

- **No account.** There is nothing to sign up for.
- **No analytics or tracking in the app.** We do not measure how you use Hiyd.
- **Your content stays yours.** Posts are stored in *your* iCloud Drive and on
  your device, not on our servers — we have none.
- **We contact one external service, GitHub, and only when you ask us to** by
  publishing a post.

## What the iOS app stores, and where

- **Your posts** are saved as `.md` files in your iCloud Drive, in the folder
  *iCloud Drive › Hiyd*. Apple syncs that folder between your devices. We cannot
  see its contents.
- **Settings** (appearance, default front matter fields, the biometric-lock
  preference) are stored locally on the device via the system preferences store.
- **GitHub personal access tokens**, if you add a repository for publishing, are
  stored in the **iOS Keychain**. They are not synced to us and cannot be
  displayed again after you save them.

## When Hiyd connects to the internet

The app works offline for writing, previewing, saving and exporting. It makes a
network request in one situation only:

- **Publishing to GitHub.** When you choose **Publish**, Hiyd sends the single
  Markdown file you are publishing, and your commit message, to
  `api.github.com`, authenticated with the token you provided. This is a direct
  connection between your device and GitHub. GitHub's handling of that request is
  covered by [GitHub's Privacy Statement](https://docs.github.com/site-policy/privacy-policies/github-general-privacy-statement).

Hiyd does not send your content anywhere else, and does not contact us at all.

## The Chrome extension

The extension captures the page you are on so you can turn it into a Markdown link
post. It stores its working data in your browser's local storage. It does not
send your data to us or to third parties.

## This website

`hiyd.uk` is a static site hosted on GitHub Pages. It uses
[Ahrefs Web Analytics](https://ahrefs.com/web-analytics), a cookieless analytics
script that records aggregate page views without profiling individual visitors or
setting tracking cookies. Server request logs are handled by GitHub Pages and
Cloudflare as our hosting and CDN providers.

## Children

Hiyd is not directed at children and collects no personal information from anyone,
so no information is collected from children.

## Your rights

Because we hold no personal data about you, there is nothing for us to provide,
correct or delete. Your posts are under your control in iCloud Drive; you can
edit or delete them at any time in Hiyd or the Files app.

## Changes

We may update this policy. Material changes will be noted here with a new "last
updated" date.

## Contact

Questions about privacy: <privacy@hiyd.uk>
