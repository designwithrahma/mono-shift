# Security Policy

## Current scope

MONO//SHIFT is a static client-side game. This release has:

- no backend or writable API
- no database
- no user accounts
- no authentication session
- no payment system
- no remote analytics or trackers
- no free-text user input
- no runtime dependency on third-party JavaScript

## Deployment checklist

### Rate limiting

Not applicable to the current static build because there is no server endpoint to abuse. Add server-side rate limiting before introducing login, cloud saves, leaderboards, forms, uploads, or analytics ingestion.

### Secret handling

No secret is required to run this project. Do not place API keys or passwords in HTML, JavaScript, Git history, or client-side environment variables. Client-side code is public to every visitor.

The repository ignores `.env`, private key, certificate, credential, and generated archive patterns. Before every release, run `python tools/verify.py` and review the Git diff.

### Input handling

The current inputs are keyboard, pointer, touch, browser storage, and same-origin iframe messages. There is no user-supplied HTML or server submission. Message sources and origins are checked before data is accepted, and numeric settings are clamped to expected ranges.

### Authentication and authorization

Not applicable to this public version. If accounts or private data are added, authentication alone is not enough. Every protected server action must also verify authorization for the requested resource.

## Browser protections

The pages use a restrictive Content Security Policy that blocks remote connections and object embedding. A DreamHost `.htaccess` file adds response headers when Apache supports them. GitHub Pages ignores `.htaccess`, so the in-page CSP remains the portable baseline.

## Reporting a problem

Do not publish a working exploit or secret in a public issue. Contact the project owner through the official Designwithrahma website or use a private GitHub security advisory when available.
