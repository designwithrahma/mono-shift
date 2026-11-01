# MONO//SHIFT

A phase-switching browser platform game with ten levels, local score records, desktop controls, and mobile touch controls.

**Live game:** https://monoshift.designwithrahma.io

## Game idea

The player moves between Coral and Cyan phases. Only platforms matching the active phase are solid. A jump may start in one phase and require a Shift press in the air before landing on the next platform.

## Controls

| Key | Action |
|---|---|
| A / D or Arrow keys | Move |
| Space / W / Up Arrow | Jump |
| Shift / E | Change phase |
| R | Restart level |
| L / Escape | Level selection |
| F | Fullscreen |

Touch controls appear automatically on mobile screens.

## Project role and tools

- **Original concept, gameplay direction, sketches, level feedback, testing, and final decisions:** Rahmathullah / Designwithrahma
- **Development support:** [Arena AI](https://arena.ai/)
- **Code review and bug-fixing support:** ChatGPT GPT-5.6 Thinking

The project was made through an AI-assisted development process. The game idea and final project decisions came from the project owner, who also tested the finished game.

## Run locally

No build step or package installation is required.

1. Download or clone the repository.
2. Open `index.html` in a modern browser.
3. Select **Play MONO//SHIFT**.

Files:

- `index.html` contains the showcase home page.
- `game.html` contains the playable game.
- `game-design.html` contains the visual game-system breakdown.
- `assets/audio/background-calm-loop.wav` is the only external runtime media file.

## Deployment safety check

### Rate limiting

This is a static public game. It has no backend, API route, database, account system, or server-side form, so application-level rate limiting is not currently needed. Rate limiting must be added on the server if a leaderboard, login, contact form, analytics collector, or other writable API is added later.

### Secrets

The current runtime contains no API keys, tokens, passwords, `.env` files, private keys, or remote service credentials. `.gitignore` blocks common secret files from being committed.

### Input safety

The game has no free-text input, HTML form submission, URL-parameter processing, or server data. Keyboard, pointer, touch, and `localStorage` values are handled locally. Same-origin checks are used for communication between the showcase page and its embedded game pages.

### Authentication and authorization

The game is intentionally public and has no user accounts or protected data. Authentication and authorization are therefore not part of this version. They must be designed before adding private profiles, cloud saves, admin tools, or restricted content.

See [`SECURITY.md`](SECURITY.md) for the full security scope.

## Privacy

MONO//SHIFT does not send gameplay records to a server. Scores and settings stay in the browser through `localStorage`. Clearing browser storage removes them.

## Interface refinement

The responsive UI was refined using the [Unslop methodology](https://github.com/heydamir/unslop/tree/main/skills/unslop) by Damir Sokolovsky (CC BY 4.0), adapted to the existing MONO//SHIFT identity. Gameplay, level data, score records, audio and controls remain in the original game implementation.

The initial Git commit did not include four deployment files listed by its provenance manifest. This update recreates functional `.gitignore`, `.htaccess`, `.nojekyll`, and GitHub Actions configuration; their recorded hashes identify the replacements, not recovered originals.

## Repository verification

Run:

```bash
python tools/verify.py
```

The verifier checks for forbidden secret files, remote runtime requests, unsafe wildcard messaging, missing local assets, JavaScript syntax issues when Node.js is available, and SHA-256 manifest mismatches.

GitHub Actions runs the same audit on every push and pull request.

## License

This public repository is **source-available, not open source**. You may view the code and play the game for portfolio review and personal evaluation. Reuse, redistribution, resale, repackaging, removal of credit, or claims of authorship require written permission.

See [`LICENSE`](LICENSE), [`COPYRIGHT.md`](COPYRIGHT.md), and [`ATTRIBUTION.md`](ATTRIBUTION.md).
