---
title: "Publish posts to GitHub"
summary: "Create a fine-grained token, add a repository, and commit posts from your phone."
description: "Create a GitHub fine-grained access token, add a repository to Hiyd, set the folder and commit template, and publish Markdown posts from iOS."
date: 2026-09-10
order: 3
---

Hiyd can commit a finished post straight into your Jekyll repository using the
GitHub Contents API. You configure a repository once; after that, publishing is a
single action from the editor or the Archive.

## 1. Create a fine-grained personal access token

On GitHub (in a browser):

1. Go to **Settings › Developer settings › Personal access tokens › Fine-grained
   tokens**.
2. **Generate new token**. Give it a name and an expiry.
3. Under **Repository access**, choose **Only select repositories** and pick the
   one repository you will publish to.
4. Under **Permissions › Repository permissions**, set **Contents** to
   **Read and write**. Leave everything else alone.
5. Generate the token and copy it.

<div class="callout"><strong>Why fine-grained:</strong> the token can touch only
the one repository you selected, and only its file contents. If it ever leaks,
the blast radius is a single repo.</div>

## 2. Add the repository in Hiyd

**Settings › GitHub Publishing › Add**. Fill in:

| Field | Notes |
| --- | --- |
| **Name** | A label for this repo in Hiyd, with an icon and colour of your choice. |
| **GitHub Username** | The owner of the repository. |
| **Repository** | The repo name on its own, e.g. `blog`. |
| **Folder Path** | Where posts are committed. Default is `_posts`. Leave blank for the repository root. |
| **Personal Access Token** | Paste the token from step 1. |
| **Commit message template** | Default `Add {filename} via Hiyd`. Placeholders: `{filename}`, `{title}`, `{datetime}`. |

Hiyd validates the token against the repository before saving. Files are always
committed to the repository's **default branch**.

The token is stored in the iOS Keychain. It cannot be shown again or edited after
saving — to change it, remove the repository and add it back. You can store up to
**five** repositories.

## 3. Publish

From the editor's **••• › Publish**, or from a file in the **Archive**:

1. Pick the repository.
2. Hiyd checks whether a file already exists at that path. If it does, you are
   asked to confirm an **overwrite**.
3. Hiyd commits the file and shows a link to view the commit on GitHub.

Your most recent publishes are kept in a local history so you can see what went
where.

## Limits and troubleshooting

- **File size:** GitHub's Contents API is only practical for text, so Hiyd rejects
  files larger than **5 MB** before sending anything.
- **"Unable to access this repository":** check the username, the repository name
  (no owner prefix), and that the token's **Contents** permission is
  **Read and write** for that repo.
- **Rate limited:** GitHub's API has hourly limits; wait and retry.
- **Wrong branch:** Hiyd publishes to the default branch. Change the repository's
  default branch on GitHub if you need posts to land elsewhere.
