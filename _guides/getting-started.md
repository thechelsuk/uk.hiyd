---
title: "Getting started with Hiyd"
summary: "Install the app, write your first post, and get the Markdown onto your Jekyll site."
description: "A first walkthrough of Hiyd for iOS: writing a post, adding front matter, previewing, and saving or exporting the Markdown file for your Jekyll site."
order: 1
---

Hiyd is built around one job: getting a well-formed Markdown post out of your head
and into your Jekyll repository with as little friction as possible. This guide
covers your first post from install to export.

## 1. Install

Download Hiyd from the [App Store]({{ site.app_store_url }}). It runs on iPhone
and iPad and needs iOS or iPadOS {{ site.min_ios_version }} or later. There is no
account to create and nothing to configure before you start writing.

## 2. Write a post

Open the **Create** tab. You get two fields:

- **Item Title** — becomes the `title:` in your front matter.
- **Item Body** — your post content in Markdown.

Write as you normally would. Headings, lists, links, code fences and images all
pass straight through untouched.

## 3. Check the front matter

Tap the **preview** (eye) button in the toolbar to see the finished file. Hiyd
always includes:

```yaml
---
title: Your title
date: 2026-09-10 09:24:00 +0100
---
```

If you have configured [default front matter fields](/guides/front-matter/) —
author, tags, categories, a `draft` flag and so on — they appear here too,
pre-filled with your defaults.

## 4. Save, export or publish

From the **More actions** (•••) menu you can:

| Action | What it does |
| --- | --- |
| **Save** | Writes the `.md` file into iCloud Drive › Hiyd, where it syncs to your other devices and shows up in the **Archive** tab. |
| **Export** | Opens the share sheet so you can send the file to another app, AirDrop it to a Mac, or save it elsewhere in Files. |
| **Publish** | Commits the file to a [GitHub repository](/guides/publish-to-github/) you have configured. |

<div class="callout"><strong>Tip:</strong> Save first, then publish. Publishing
works from a saved file, and keeping the note in your Archive means you can edit
and re-publish later.</div>

## 5. Find it again

The **Archive** tab lists every saved file with search. Swipe a file to delete it,
or open it to restore it into the editor for another pass. Because the files are
plain Markdown in iCloud Drive, you can also open the same folder on a Mac at
*iCloud Drive › Hiyd*.

## Where the file goes on your site

A Hiyd post is a standard Jekyll post: a YAML front matter block followed by
Markdown. Drop it into your `_posts` folder (or publish straight there) using the
Jekyll naming convention `YYYY-MM-DD-title.md` and your site build will pick it
up. Hiyd names saved files this way automatically.
