---
title: "Shortcuts, Siri & App Intents"
summary: "Every action Hiyd exposes to the Shortcuts app, Siri and automations."
description: "Reference for Hiyd's App Intents: Create Note, List Files, Get File Content, Search Notes and more, with example Shortcuts automations."
date: 2026-09-10
order: 4
---

Hiyd ships a set of App Intents, so you can drive it from the **Shortcuts** app,
ask **Siri**, or wire it into automations and widgets.

## Built-in phrases

Three actions are registered as App Shortcuts and work with Siri straight away:

| Say | Does |
| --- | --- |
| "Open Hiyd" | Opens the app. |
| "Create a note in Hiyd" | Opens a new note (optionally with a title and body you supply). |
| "List my Hiyd files" | Returns the files in your Archive. |

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

**Read a post back.** *Get File Content* → *Show Result* (or *Speak Text*) to
review a draft hands-free.

**Round-trip an edit.** *Get File Content* → transform the text → *Create File*
with the same name to overwrite.

## Notes

- Filenames without a `.md` or `.txt` extension get `.md` added automatically.
- If a filename already exists, **Create File** saves a numbered copy
  (`name-1.md`) rather than overwriting.
- Background actions need iCloud Drive available; if it is off, they return an
  error.
