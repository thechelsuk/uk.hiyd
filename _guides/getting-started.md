---
title: "Getting started with Hiyd"
summary: "Install the app, write your first post, and get the Markdown onto your Jekyll site."
description: "A first walkthrough of Hiyd for iOS: writing a post, adding front matter, previewing, and saving or exporting the Markdown file for your Jekyll site."
date: 2026-09-10
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
pass straight through untouched. While you type in the body, the bar above the
keyboard formats the selected text: bold, italic, code, link, heading, list and
quote. With a keyboard attached to an iPad, **⌘B**, **⌘I**, **⌘K** and **⌘E** do
bold, italic, link and code.

Your draft is kept as you go, so if you leave the app, or iOS closes it, the post
is still there when you come back.

## 3. Check the front matter

Tap the **preview** (eye) button in the toolbar to see the finished file. On iPad,
and on the iPhone Duo when it's unfolded, the preview sits beside the editor and
updates as you type. Hiyd always includes:

```yaml
---
title: Your title
date: 2026-09-10
---
```

If you have configured [default front matter fields](/guides/front-matter/) —
author, tags, categories, a `draft` flag and so on — they appear here too,
pre-filled with your defaults. Open **Front Matter** under the body to change them
for this post.

## 4. Save, export or publish

From the **More actions** (•••) menu you can:

| Action | What it does |
| --- | --- |
| **Save** | Writes the `.md` file into iCloud Drive › Hiyd, where it syncs to your other devices and shows up in the **Archive** tab. With iCloud Drive off, it's saved on your device instead (Files › On My iPhone › Hiyd) and moves into iCloud Drive when you turn it on. |
| **Export** | Opens the share sheet so you can send the file to another app, AirDrop it to a Mac, or save it elsewhere in Files. |
| **Publish** | Commits the file to a [GitHub repository](/guides/publish-to-github/) you have configured. |

<div class="callout"><strong>Tip:</strong> Save first, then publish. Publishing
works from a saved file, and keeping the note in your Archive means you can edit
and re-publish later.</div>

## 5. Find it again

The **Archive** tab lists every saved file with search, and you can pull the list
down to refresh it. Tap a file to preview it, or open it in the editor for another
pass. Swipe right to publish, edit or preview, and swipe left to delete or share.
Touch and hold a file for every action, including **Duplicate**. Because the files
are plain Markdown in iCloud Drive, you can also open the same folder on a Mac at
*iCloud Drive › Hiyd*.

## Where the file goes on your site

A Hiyd post is a standard Jekyll post: a YAML front matter block followed by
Markdown. Drop it into your `_posts` folder (or publish straight there) using the
Jekyll naming convention `YYYY-MM-DD-title.md` and your site build will pick it
up. Hiyd names saved files this way automatically.
