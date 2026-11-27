# Study Reader

> This repo also holds **Nadia's Study Club** as a Home Screen app, in [`study-club/`](study-club/).
> With GitHub Pages on, it lives at `https://nadiarco.github.io/study-reading/study-club/`.

A free, Speechify-style "read along" app for university readings.

- Open a **PDF, Word (.docx) or text file**, or paste text.
- It reads aloud and **highlights each word** as it's spoken, with the current sentence shaded.
- **Tap any word** to start reading from there. Speed goes from 0.5× to 3×.
- **Focus mode** fades everything except the sentence being read.
- **Skip citations**: leaves out things like (Smith, 2019) and [12] when reading aloud.
- Remembers your place in every reading.
- Shows page markers from the original PDF, so you can match the page numbers in class.
- **Study guide** (when opened inside Claude): Claude reads the article and writes the context, a summary,
  key terms defined, key arguments, reasoning, evidence and suggested next steps. You can listen to the guide too.
  Outside Claude, the button copies the reading with instructions to paste into a Claude chat.
- Keyboard: Space = play/pause, ←/→ = previous/next sentence, +/− = speed.

## How it works

It's one HTML file with no server and no account. Speech uses the voices built into
your device (Web Speech API), so it costs nothing. PDFs are read with pdf.js and Word
files with mammoth.js. Both load from cdnjs. Nothing you open leaves your device.

## Better voices

- **iPhone/iPad/Mac:** Settings → Accessibility → Spoken Content (Read & Speak on Mac) → Voices.
  Download an "Enhanced" or "Premium" voice, then choose it in the app's settings.
- **Android/Chrome:** the "Google" voices are usually the most natural.
- **Windows/Edge:** the "Online (Natural)" voices are excellent.

## Limitations

- Scanned PDFs (photos of pages) have no text layer. Convert them first, for example
  by opening them with Google Docs in Google Drive.
- Phones may stop speaking when the screen locks. The app keeps the screen awake
  while playing, where the browser allows it.

## Run it

Open `index.html` in a browser, or host it free on GitHub Pages
(Settings → Pages → deploy from the `main` branch).
