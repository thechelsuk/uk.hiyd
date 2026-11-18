---
title: "Shortcuts, Siri & App Intents"
summary: "Every action Hiyd exposes to the Shortcuts app, Siri and automations."
description: "Reference for Hiyd's App Intents: Create Note, Publish Post, List Files, Get File Content, Search Notes and more, with example Shortcuts automations."
date: 2026-09-10
order: 4
---

Hiyd ships a set of App Intents, so you can drive it from the **Shortcuts** app,
ask **Siri**, or wire it into automations and widgets.

## Built-in phrases

Four actions are registered as App Shortcuts and work with Siri straight away:

| Say | Does |
| --- | --- |
| "Open Hiyd" | Opens the app. |
| "Create a note in Hiyd" | Opens a new note (optionally with a title and body you supply). |
| "List my Hiyd files" | Returns the files in your Archive. |
| "Publish a post with Hiyd" | Asks which post and which site, then publishes it. |

## All available actions

Add these from the Shortcuts app by searching for **Hiyd**:

| Action | Parameters | Returns | Opens app |
| --- | --- | --- | --- |
| **Create Note** | Title, Body (both optional) | — | Yes |
| **Create File** | Filename, Content | The created file | No |
| **List Files** | Limit (optional) | List of files | No |
| **Get File** | Filename | The file (with content and modified date) | No |
| **Get File Content** | Filename | The file's text | No |
| **Search Notes** | Search query | Matching files | No |
| **Publish Post** | Post, Site, Overwrite (off by default) | The file's GitHub link | No |
| **Open Page** | Create / Archive / Settings | — | Yes |
| **Open File** | Filename, "Restore to Editor" toggle | — | Yes |

Actions that don't open the app run in the background, so you can chain them with
other Shortcuts actions.

## Example automations

**Daily journal entry.** *Create File* with the filename built from a formatted
**Current Date** (`yyyy-MM-dd`) plus `-journal.md`, and content from an
"Ask for Input" action. Saves straight to your Archive without opening Hiyd.

**Share sheet to draft.** A Shortcut that takes the Safari page as input, formats
a Markdown link, and calls *Create Note* with that as the body.

**Publish from anywhere.** *Create File* to save a post, then *Publish Post* with
that file and your site. Add it to a Home Screen Shortcut for one-tap publishing.

**Read a post back.** *Get File Content* → *Show Result* (or *Speak Text*) to
review a draft hands-free.

**Round-trip an edit.** *Get File Content* → transform the text → *Create File*
with the same name to overwrite.

## Notes

- Filenames without a `.md` or `.txt` extension get `.md` added automatically.
- If a filename already exists, **Create File** saves a numbered copy
  (`name-1.md`) rather than overwriting.
- With iCloud Drive off, background actions read and save posts on your device
  instead.

## Checks before publishing

**Publish Post** runs without you looking at the post first, so Hiyd checks it
and stops with the reason if anything is wrong. It won't publish a post that:

- is empty, or larger than 5 MB
- has no front matter, or no `title` or `date`
- has a `date` Jekyll can't read (use `YYYY-MM-DD`, optionally with a time)
- has a front matter line that isn't valid YAML
- is going into a `_posts` folder without a date at the start of its filename

It also won't replace a file that's already on GitHub unless you turn
**Overwrite** on.
