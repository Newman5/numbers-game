# GitHub Copilot Instructions: Project Phases

This guide helps contributors use GitHub Copilot to work on each phase of the Chinese Number Listening Game project. Follow the instructions for each phase to maximize Copilot's assistance and keep development aligned with the roadmap.

---

## Phase 1 – Core Prototype (Complete)

- Use Copilot to:
  - Suggest HTML, CSS, and JavaScript for the basic game interface.
  - Implement audio playback for numbers 1–100.
  - Generate multiple-choice logic and scoring.
  - Add feedback sounds for correct/incorrect answers.

- Relevant files: `index.html`, `generate_audio_gtts.py`, `audio/chinese/gTTS/`

## Phase 2 – Multi-Speaker & Replay

- Use Copilot to:
  - Add support for multiple speaker folders (e.g., `gTTS`, `Taipei01`, `Shanghai01`).
  - Randomize speaker selection for each round.
  - Implement replay button and streak counter.

- Relevant files: `audio/chinese/`, game logic in `index.html`

## Phase 3 – Progress & Polish

- Use Copilot to:
  - Track local progress (accuracy per number).
  - Suggest smooth transitions, animations, and responsive design improvements.
  - Add “practice mode” for focused number ranges.

- Relevant files: `index.html`, frontend assets

## Phase 4 – Community & Expansion

- Use Copilot to:
  - Integrate new native-speaker recordings.
  - Add support for other languages (English, Japanese, Spanish).
  - Prepare for Progressive Web App (PWA) publishing.

- Relevant files: `audio/chinese/`, new language folders, PWA setup

---

## General Copilot Usage Tips

- Use Copilot for code suggestions, refactoring, and documentation.
- Review Copilot’s output for accuracy and style consistency.
- Reference the README and CONTRIBUTING guidelines for project standards.
- For new features, describe your intent in comments to guide Copilot.

---

## Future Ideas

- Use Copilot to brainstorm and prototype:
  - Voice comparison and pronunciation recording.
  - Mobile-friendly daily challenges.
  - Leaderboards and streak tracking.
  - Extensions for dates, currencies, idioms.

---

For questions or contributions, see the README and open a pull request.
