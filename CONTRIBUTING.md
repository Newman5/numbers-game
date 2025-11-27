# 🤝 Contributing Guidelines

Thank you for your interest in improving the **Chinese Number Listening Game**!
This project thrives on collaboration from learners, developers, and especially native Chinese speakers who can contribute authentic voice recordings.

---

## 🗣️ Audio Contributions

We are currently seeking **native Mandarin Chinese speakers** to record numbers 1–100 for listening comprehension training.

### 🎙️ Recording Requirements

* **Voice:** Clear, natural Mandarin pronunciation.

* **Format:** MP3 files, 44.1 kHz or higher.

* **One file per number:** Name files `1.mp3`, `2.mp3`, … `100.mp3`.

* **Folder naming:**

  ```bash
  audio/chinese/Speaker_YourName/
  ```

  Example: `audio/chinese/Speaker_LiMing/`

* **Environment:** Quiet background, minimal echo, no background music.

* **Style:** Speak naturally, as if in everyday use (not overly slow or robotic).

* **Volume:** Consistent levels across all recordings.

### 🧾 Optional Metadata

Include a small `info.txt` file in your folder:

```bash
Name: Li Ming
Region: Beijing, China
Accent: Standard Mandarin
Recording Device: iPhone 14
Date: 2025-11-10
License: CC BY 4.0
```

---

## 💻 Developer Contributions

We welcome developers, designers, and learners to help expand the project.

### Areas to Contribute

* Front-end improvements (UI, animations, responsive design)
* Audio handling enhancements (playback, progress tracking)
* Adding multi-speaker randomization logic
* Language expansions (add folders for English, Japanese, etc.)
* Documentation improvements and translations

### Copilot & Agent Coding Guidelines

* Write code as simply as possible; avoid complex structures.
* Use patterns and techniques suitable for novice coders.
* Add clear, helpful comments for collaborators.
* Prioritize readability and ease of contribution.
* When in doubt, choose clarity over cleverness.

### Setup Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/chinese-number-game.git
   cd chinese-number-game
   ```
2. Generate default audio (optional):

   ```bash
   pip install gtts
   python generate_audio_gtts.py
   ```
3. Open `index.html` in your browser and play the game locally.

---

## 📬 Submitting Contributions

1. Fork the repository and create a new branch.
2. Add your new audio or code changes.
3. Commit with clear messages.
4. Submit a pull request.

All pull requests will be reviewed for quality and naming consistency.

---

## 🧾 Licensing

By contributing audio or code, you agree to license your work under:

* **Audio:** Creative Commons Attribution 4.0 (CC BY 4.0) unless otherwise stated.
* **Code and documentation:** MIT License.

This ensures that all learners can freely access and improve upon the work.

---

Thank you for helping make language learning accessible, authentic, and fun! 🌍
