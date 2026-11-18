---
title: "Share to Hiyd from any app"
summary: "Turn selected text or a link from Safari or any app into a new post, with the source in the front matter."
description: "Share selected text or a link to Hiyd on iPhone or iPad, and it starts a new post with the text as a quote and the link as source in the front matter."
date: 2026-11-18
order: 6
---

Hiyd appears in the iOS share sheet, so a passage you are reading can become a
post without copying and pasting. It's the iPhone and iPad counterpart to the
[Chrome extension](/guides/link-posts/).

## Share something

1. In Safari (or any app that shares text or links), select the text you want to
   quote, or just open the page.
2. Tap **Share**, then **Hiyd**. If it isn't in the row of apps, scroll to the
   end of the row and tap **More** to find it.
3. Hiyd opens on the **Create** tab with a new post ready to finish.

## What you get

| You share | Hiyd fills in |
| --- | --- |
| Selected text | The body, as a Markdown quote |
| The page's title | The post's title |
| The page's link | A `source:` field in the post's front matter |
| A link on its own | The body, as a link to the page |

Every line of the shared text is quoted, and blank lines between paragraphs get a
`>` too, so the whole passage stays one quote:

```markdown
> The first paragraph of the passage.
>
> The second paragraph.
```

Add your own commentary underneath, then save or publish as usual. The rest of
the front matter starts from your [defaults](/guides/front-matter/).

```yaml
---
title: The page's title
date: 2026-11-18
layout: post
source: https://example.com/the-article
---
```

## Using source in your theme

`source` is a plain front matter field, so your layout can read it as
`page.source`. For example, to link the title out to the page you quoted:

{% raw %}
```liquid
<h1><a href="{{ page.source | default: page.url }}">{{ page.title }}</a></h1>
```
{% endraw %}

## If Hiyd doesn't open

Occasionally iOS doesn't switch to Hiyd straight away. The share sheet then
says **Saved. Open Hiyd to finish your post.** Nothing is lost: the next time you
open Hiyd, the shared post is waiting on the **Create** tab.
