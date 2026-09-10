---
title: "Deep links (the hiyd:// URL scheme)"
summary: "Open pages, pre-fill the editor and jump to a saved file from any app."
description: "Reference for Hiyd's hiyd:// URL scheme: create, archive and settings links, pre-filling a note with title and body, and opening a saved file for editing."
order: 5
---

Hiyd registers the `hiyd://` URL scheme. A deep link works anywhere iOS makes URLs
tappable — Notes, Messages, a widget, or the Shortcuts **Open URLs** action.

## Navigation links

| Link | Opens |
| --- | --- |
| `hiyd://create` | The Create tab |
| `hiyd://archive` | The Archive tab |
| `hiyd://settings` | The Settings tab |

## Pre-fill a new note

| Link | Result |
| --- | --- |
| `hiyd://create?title=My%20Note` | Create tab with the title filled in |
| `hiyd://create?title=My%20Note&body=Note%20content%20here` | Create tab with title and body filled in |

Encode spaces as `%20` and other characters with standard percent-encoding.

## Open a saved file

| Link | Result |
| --- | --- |
| `hiyd://file?filename=example.md` | Opens the Archive and selects that file |
| `hiyd://file?filename=example.md&restore=true` | Opens that file in the editor, ready to edit |

Replace `example.md` with the exact filename as it appears in your Archive.

## Where to use them

- **Notes / Messages:** paste the link and tap it.
- **Shortcuts:** add an **Open URLs** action with the deep link.
- **Widgets:** configure a widget link to jump straight to Create or a specific
  file.
- **Home Screen:** wrap a deep link in a Shortcut and add that Shortcut to your
  Home Screen for a one-tap "new post" button.

Inside Hiyd, **Settings › Deep Links** lists every link and copies one to the
clipboard when you tap it.
