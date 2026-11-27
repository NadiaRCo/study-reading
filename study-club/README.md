# Nadia's Study Club (phone app)

The Fall 2026 Study Club as a web app you add to your phone's Home Screen.
It opens offline and keeps your progress on the phone.

## Install on iPhone
1. Open the app link in **Safari**.
2. Tap **Share**, then **Add to Home Screen**.
3. Open it from the new Study Club icon. Tap **Turn on reminders** once if you want pop-ups.

Reminders only fire while the app is open (same as on claude.ai). Your notes, ticks and quiz
answers are saved on the device you use. They don't sync between your phone and claude.ai.

## Where the content comes from
The pages here are **copies**. The source of truth is the revision repository on Nadia's Mac:

`~/Documents/Claude/Projects/uOttawa/Nadia Study Club - Repository`

Edit the Study Club there (or in the claude.ai artifacts it mirrors), then refresh the app:

```
python3 tools/sync_study_club.py
```

The script copies `index.html`, `nine-stories.html` and `bg/` in here, adds the Home Screen
tags, and stamps a new version into `sw.js` so phones pick up the change. Commit and push the result.
Don't hand-edit `index.html` or `nine-stories.html` in this folder: the next sync replaces them.

App-only files (safe to edit): `app.js`, `sw.js` (except line 1), `manifest.webmanifest`, `icons/`.
