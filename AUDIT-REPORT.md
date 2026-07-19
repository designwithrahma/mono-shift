# MONO//SHIFT Release Audit

Audit date: 2026-07-19

## Result

The GitHub showcase package passed the included static security and integrity checks.

## Security review

- **Rate limiting:** Not applicable to this release because the project has no backend, API, database, uploads, login, or writable server route.
- **Secrets:** No `.env` file, API key, token, password, certificate, private key, or remote-service credential was found in the repository.
- **Input safety:** No free-text form, user HTML, URL-parameter processing, or server submission exists. Runtime input is limited to keyboard, pointer, touch, browser storage, and same-origin iframe messages.
- **Message safety:** Parent and iframe messages validate both the sending window and same-origin source when hosted. Local `file://` mode uses the required wildcard fallback because local files have an opaque origin.
- **Authentication and authorization:** Not applicable because this release is a public static game with no accounts or protected data.
- **Runtime network access:** No `fetch`, XMLHttpRequest, WebSocket, EventSource, beacon, Axios, or remote HTTP resource exists in the runtime pages.
- **Dynamic code:** No `eval()` or `new Function()` use was found.
- **Browser policy:** Runtime pages include a restrictive Content Security Policy. DreamHost deployments also receive Apache security headers through `.htaccess` when supported.

## Repository review

- Showcase home page is now `index.html`.
- Playable game is `game.html`.
- Game design page is `game-design.html`.
- Nested delivery ZIP files and duplicate legal files were removed from the repository.
- `.gitignore` blocks common secrets, keys, editor files, logs, dependencies, and generated archives.
- GitHub Actions runs `tools/verify.py` on pushes and pull requests.
- Local links and runtime asset paths passed verification.
- Inline JavaScript passed syntax validation.
- SHA-256 hashes in `PROVENANCE-MANIFEST.json` match the delivered files.

## Copyright and attribution review

- Copyright language now covers the project owner's original and protectable contributions instead of claiming that every AI-assisted output is entirely human-authored.
- `ATTRIBUTION.md` records the owner's concept, direction, testing, and final decisions.
- Arena AI is disclosed as development support.
- ChatGPT GPT-5.6 Thinking is disclosed as code-review and bug-fixing support.
- The repository uses a source-available proprietary license, not an open-source license.
- The audio file's hash and embedded metadata were verified. Legal ownership of an asset cannot be proven only from metadata or a hash, so the documents describe the project-owner claim without treating the technical record as legal proof.

## Recheck command

```bash
python tools/verify.py
```

This audit is a technical review, not legal advice or a guarantee against every possible vulnerability.
