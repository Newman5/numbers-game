# GitHub Copilot Instructions: Project Phases

This guide helps contributors use GitHub Copilot to work on each phase of the Chinese Number Listening Game project. Follow the instructions for each phase to maximize Copilot's assistance and keep development aligned with the roadmap.

---

## Phase 1 – Core Prototype 

- Use Copilot to:

  - Add feedback sounds for correct/incorrect answers.

- Relevant files: `index.html`, `generate_audio_gtts.py`, `audio/chinese/gTTS/`

## Phase 2 – Multi-Speaker & Replay

- Use Copilot to:
  - Add support for multiple speaker folders (e.g., `gTTS`, `Taipei01`, `Shanghai01`).
  - Create UI elements for speaker selection.
  - include a Randomize speaker selection option.
  - implement functionality to replay audio clips.
  - implement a timer for each question and a scoring system based on response time.
  - Implement a countdown timer visible to the user and calculate score based on how quickly they answer.
  - make the game have a start screen and an end screen showing final score and stats.
  - make the game responsive for mobile devices.
  - make the gave have a progress bar showing how many questions have been answered out of the total.
  - make the game have levels of difficulty (e.g., easy: 1-10, medium: 1-50, hard: 1-100).
  - make the game have a time limit for each question (e.g., 10 seconds) and a time limit for the whole game (e.g., 5 minutes).
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
