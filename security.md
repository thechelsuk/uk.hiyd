---
title: "Security"
eyebrow: "Legal"
summary: "How Hiyd is built to be safe, and how to report a vulnerability."
last_updated: "10 September 2026"
description: "Hiyd's security model: local-first storage in iCloud Drive, GitHub tokens in the iOS Keychain, minimal network surface, and how to report a security issue."
---

Hiyd is designed to keep its attack surface small. This page describes how it
works and how to report a problem.

## Architecture

- **Local-first.** Writing, previewing, saving and exporting happen entirely on
  your device. Posts are stored as files in your iCloud Drive.
- **One outbound connection.** The app contacts a single external service —
  `api.github.com` — and only when you publish a post. There is no Hiyd server,
  telemetry endpoint or third-party SDK phoning home.
- **No accounts.** There are no credentials for us to lose.

## Credential handling

- **GitHub personal access tokens** are stored in the **iOS Keychain**. They are
  write-once from your perspective: after saving, a token cannot be displayed or
  edited — you remove and re-add the repository to change it.
- We recommend **fine-grained** tokens scoped to a single repository with
  **Contents: Read and write** and nothing else, so a compromised token affects
  only that repo.

## Platform protections

- Runs inside the iOS application sandbox.
- Optional **biometric lock** (Face ID / Touch ID / passcode) gates app launch.
- Distributed through the App Store and the Chrome Web Store, both of which review
  submissions. The Chrome extension uses Manifest V3 with minimal permissions.

## Reporting a vulnerability

Please report security issues privately:

- **Email:** <security@hiyd.uk> with "SECURITY" in the subject.
- **GitHub:** open a private advisory at
  <https://github.com/thechelsuk/uk.hiyd/security/advisories/new>.

Include reproduction steps and an impact assessment if you can. Please give us a
reasonable window to fix the issue before any public disclosure.

### What to expect

- Acknowledgement within **48 hours**.
- An initial assessment within **1 week**.
- A target of **30 days** to resolve serious issues, with updates along the way.

## Your part

Keep your device OS current, use a device passcode and biometrics, install apps
only from official stores, and review generated content before you publish it.
