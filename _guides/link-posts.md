---
title: "Link posts with the Chrome extension"
summary: "Capture a quote and its source metadata from any page and turn it into a Daring Fireball-style linked post."
description: "Use the Hiyd Chrome extension to capture selected text and page metadata as a Markdown quote post with Jekyll front matter, then wire it into a linkpost layout."
date: 2026-09-10
order: 6
---

The [Hiyd browser extension]({{ site.chrome_store_url }}) is for a specific kind
of post: the **linked list** or **quote post** — a short entry built around a
passage from someone else's page, with the title linking out to the source and a
line or two of your own commentary. If you have read Daring Fireball, you know
the format.

It is a separate tool from the iOS app, with its own Markdown output. Install it
from the **Chrome Web Store** — it works in Chrome and other Chromium browsers
(Edge, Brave, Arc, Vivaldi) and is built on Manifest V3.

## Capture a quote

1. On any web page, **select the text** you want to quote.
2. **Right-click** the selection and choose **Hiyd Capture**. (The menu item
   only appears when text is selected.)
3. A **Save** dialog opens with a suggested filename like
   `2026-09-10-the-page-title.md`. Choose where to put it — your site's `_posts`
   folder, a drafts folder, wherever.

That is the whole loop. There is no separate window and nothing is uploaded; the
file is written straight to disk. In browsers without the File System Access API,
the file downloads instead.

<div class="callout"><strong>Tip:</strong> keep the selection tight — one
paragraph is usually enough. You can trim or add an ellipsis in the file
afterwards.</div>

## What you get

The extension writes a Jekyll front matter block followed by your selection, with
every line prefixed as a Markdown blockquote:

```markdown
---
date: 2026-09-10
title: "Manton Reece: on owning your content"
cited: "Manton Reece"
link: https://example.com/own-your-content
seo: "Why your posts should live on a domain you control."
tags: indieweb, blogging
---

> If you care about your writing, you need to have your own site. Not a
> profile on someone else's platform.
```

The fields are filled from the page automatically:

| Field | Source | Notes |
| --- | --- | --- |
| `date` | Today's date | `YYYY-MM-DD` |
| `title` | The page `<title>` | Sanitised into the filename too |
| `cited` | `<meta name="author">` | The person you are quoting |
| `link` | The page URL | The canonical link to the source |
| `seo` | `<meta name="description">` | Handy as a fallback excerpt |
| `tags` | `<meta name="keywords">`, then `category` | Often empty — set your own |

Anything the page doesn't provide comes through blank; open the file and fill it
in.

## Add custom front matter

Click the extension's toolbar icon to open **Settings**. There you can add up to
**five** custom key/value pairs that are appended to every capture as string
values — for example `layout: "link"` or `author: "Sam"` (your name, as distinct
from `cited`).

Keys that clash with a built-in field (`date`, `title`, `cited`, `link`, `seo`,
`tags`) or with each other are ignored. Settings sync across your Chromium
browsers via your browser account.

## Turn it into a linked post

The captured file is a normal Jekyll post. Two small things make it a proper
link post:

**1. Write your commentary below the quote.** The blockquote is the setup; your
words are the point.

```markdown
> If you care about your writing, you need to have your own site.

Exactly right. This is why every Hiyd post is a file in *your* repo, not a
row in someone's database.
```

**2. Make the post title link to the source.** In your post layout, point the
heading at the `link` field when it is present:

{% raw %}
```liquid
<h1 class="post-title">
  {% if page.link %}
    <a href="{{ page.link }}" rel="bookmark external">{{ page.title }}</a>
    <span class="permalink">&#8203;<a href="{{ page.url }}">&#9733;</a></span>
  {% else %}
    <a href="{{ page.url }}">{{ page.title }}</a>
  {% endif %}
</h1>
```
{% endraw %}

Now any post with a `link:` renders as an outbound-linking headline with a small
"glyph" permalink back to your own page, and normal posts are unaffected. Add a
`layout: link` custom field in the extension settings if you want to style link
posts differently, or key off `page.link` in one shared layout.

## In your feed

If you publish an RSS/Atom feed, decide how link posts should behave — most
linked-list sites make the feed entry's title link to the **source**, with the
permalink to your commentary in the body. With the `link` field on the post you
have everything you need to build that in your feed template.

## Privacy

The extension collects nothing and has no servers. It reads the page you are on
only when you invoke **Hiyd Capture**, uses `storage` solely for your custom
front matter settings, and writes the Markdown file directly to the location you
pick. See the [privacy policy](/privacy/) for the full picture.
