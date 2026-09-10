---
title: "Front matter defaults"
summary: "Set the YAML fields every new note should start with — author, tags, categories, flags."
description: "How to configure default YAML front matter fields in Hiyd: Text, List and Boolean field types, reordering, the reserved title and date fields, and the YAML output."
order: 2
---

Every Jekyll post starts with a YAML front matter block. Hiyd can pre-fill that
block for you so you are not retyping `author:` and `tags:` on every post.

## Reserved fields

`title` and `date` are always included and cannot be removed or renamed:

- `title` comes from the **Item Title** field in the editor.
- `date` is set when you create the file, in the format
  `2026-09-10 09:24:00 +0100`.

## Adding your own fields

Go to **Settings › Front Matter › Manage Front Matter Fields** and tap **+**. Each
field has a **key** (the YAML name) and a **value type**:

| Type | Use for | YAML output |
| --- | --- | --- |
| **Text** | Single line — `author`, `layout`, `category` | `author: Sam` |
| **List** | Multiple items — `tags`, `categories` | `tags: [jekyll, ios, writing]` |
| **Boolean** | True/false flags — `draft`, `published`, `comments` | `draft: false` |

Enter the default value you want new notes to start with. For a List field, type
the items separated by commas; Hiyd formats them as a YAML array.

## Reordering and removing

In the field list, **drag** the handle to reorder fields — they appear in your
front matter in that order. **Swipe** a field to delete it. **Delete All Fields**
clears everything back to just `title` and `date`.

## Example

With default fields `author` (Text), `tags` (List) and `draft` (Boolean = false),
a new note previews as:

```yaml
---
title: Hello, world
date: 2026-09-10 09:24:00 +0100
author: Sam
tags: [jekyll, ios]
draft: false
---
```

Edit any value per-post before you save — the defaults are just a starting point.

<div class="callout"><strong>Note:</strong> field keys must be unique, and you
cannot reuse the reserved names <code>title</code> or <code>date</code>.</div>
