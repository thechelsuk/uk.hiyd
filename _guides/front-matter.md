---
title: "Front matter defaults"
summary: "Set the YAML fields every new note should start with — author, tags, categories, flags."
description: "How to configure default YAML front matter fields in Hiyd: Text, List and Boolean field types, reordering, and the reserved title and date fields."
date: 2026-09-10
order: 2
---

Every Jekyll post starts with a YAML front matter block. Hiyd can pre-fill that
block for you so you are not retyping `author:` and `tags:` on every post.

## Reserved fields

`title` and `date` are always included and cannot be removed or renamed:

- `title` comes from the **Item Title** field in the editor.
- `date` is the day you create the file, in the format `2026-09-10`. Editing a
  post later keeps its original date.

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
date: 2026-09-10
author: Sam
tags: [jekyll, ios]
draft: false
---
```

## Front matter for each post

The defaults are a starting point. In the editor, open **Front Matter** under the
body to see this post's fields as YAML, and change, add or remove any of them for
this post only. Your defaults in Settings stay as they are.

When you open a saved post to edit it, Hiyd keeps that post's own front matter,
whatever your defaults are now. Changing a default never rewrites posts you have
already written.

<div class="callout"><strong>Note:</strong> field keys must be unique, and you
cannot reuse the reserved names <code>title</code> or <code>date</code>.</div>
