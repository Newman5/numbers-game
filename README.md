# 🎷 Chinese Number Listening Game

A simple HTML5 web game to train your **listening fluency for numbers in Mandarin Chinese** (1 – 100).
Press **Start**, hear a number, and choose the correct answer.
Earn points for correct answers, lose points for wrong ones — and listen again until you get it right!

---

## 🧠 Why This Game Matters

Numbers are everywhere — prices, dates, times, addresses — but they’re deceptively hard to catch in fast, tonal speech.
This project helps you internalize how Mandarin numbers **sound** in different voices, tones, and pacing.

Understanding multiple speakers is essential because:

* Tone and rhythm vary between regions and individuals.
* Real-world listening rarely matches textbook pronunciation.
* Training your ear on a **variety of speakers** builds real comprehension, not rote memory.

---

## 🌿 Project Phases

### **Phase 1 – Core Prototype (✅ Complete)**

* Simple HTML5 + JavaScript.
* Plays audio for numbers 1 – 100.
* Four multiple-choice answers.
* Points and feedback sounds.

### **Phase 2 – Multi-Speaker & Replay**

* Add support for multiple speaker folders (e.g., `gTTS`, `Taipei01`, `Shanghai01`).
* Randomly select a speaker for each round.
* Add replay button and streak counter.

### **Phase 3 – Progress & Polish**

* Local progress tracking (accuracy per number).
* Smooth transitions, animations, and responsive design.
* Optional “practice mode” for focused ranges.

### **Phase 4 – Community & Expansion**

* Collect diverse native-speaker recordings.
* Add other languages (English, Japanese, Spanish…).
* Publish as a simple Progressive Web App (PWA).

---

## 🗂️ Folder Structure

```txt
chinese-number-game/
│
├── index.html
├── generate_audio_gtts.py
└── audio/
    └── chinese/
        ├── gTTS/            # auto-generated voices
        │   ├── 1.mp3 … 100.mp3
        ├── Speaker_Taipei01/  # future contributor set
        ├── Speaker_Shanghai01/
        └── fx/
            ├── correct.mp3
            └── wrong.mp3
```

---

## 🤉 Tech Overview

* **Frontend:** HTML + CSS + Vanilla JavaScript
* **Audio Generation:** [`gTTS`](https://pypi.org/project/gTTS/) (free Google Text-to-Speech)
* **Hosting:** any static host — GitHub Pages or Cloudflare Pages

---

## 🤝 Contributing (Chinese speakers wanted!)

We’d love native Chinese speakers to contribute voice recordings of numbers 1–100.
The goal is to capture **natural variation** in pronunciation, tone, and pacing.

### 🎤 How to Contribute Audio

1. Record yourself clearly saying the numbers 1 – 100 in Mandarin.

   * Each number should be a **separate MP3** (e.g., `1.mp3`, `2.mp3`, …).
   * Speak naturally — tone and rhythm as you would in conversation.
2. Name your folder as:

   ```bash
   audio/chinese/Speaker_YourName/
   ```

3. Add your files there and open a **pull request**.
   If you prefer to share files privately, reach out via the repo’s contact email.

### 🌟 Recording Tips

* Record in a quiet space.
* Avoid background music or compression.
* Consistent volume helps future learners.
* Optional: include metadata file like `info.txt` with your region and accent.

---

## 🧪 For Developers

Generate the initial gTTS set:

```bash
pip install gtts
python generate_audio_gtts.py
```

Then open `index.html` in your browser and play!

---

## 🩴 Future Ideas

* Add voice comparison / pronunciation recording.
* Create mobile-friendly daily challenges.
* Build leaderboards or streak tracking.
* Extend to other learning domains (dates, currencies, idioms).

---

### 🌏 License & Credits

This project is open-source and educational.
Audio by contributors remains under their chosen license (default CC BY 4.0 unless noted).  See [LICENSE.md](LICENSE.md)

### Todo

* repeat number sound
* a running list of correct and incorrect answers - streaks and common mistakes - toggle to see the last one or a long list of past answers
