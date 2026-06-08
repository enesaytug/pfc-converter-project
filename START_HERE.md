# START HERE — Brief for Claude Code

Copy the prompt below into Claude Code (running in this folder) to build the site.

---

## Setup (one-time)

1. Open a terminal in this folder (`pfc_website_kit/`).
2. Make sure Claude Code is installed and run `claude` from this directory so it has
   access to `PROJECT_CONTENT.md` and the `figures/` folder.
   - Claude Code docs: https://docs.claude.com/en/docs/claude-code/overview
3. Paste the prompt below.

---

## Prompt to paste into Claude Code

> Build a single-page, scroll-based project portfolio website for my power
> electronics term project. All real content (text, numbers, figure list) is in
> `PROJECT_CONTENT.md` — use ONLY the numbers and statements from that file, do
> not invent data. Figures are in `./figures/`.
>
> Requirements:
> - Plain static site: a single `index.html` plus a `style.css` and a small
>   `script.js`. No build step, no framework — it must deploy to GitHub Pages as-is.
> - Visual style: minimalist academic, navy (#0a2463 / #1b2a6b range) and white,
>   matching İTÜ. Clean serif or strong sans-serif headings, generous whitespace.
> - Layout: a sticky top nav with anchor links; a hero section with the project
>   title, authors, course, and İTÜ identity; then one scroll section per topic in
>   this order: What is PFC → Topology & Control → Component Sizing → Average Model
>   → Bode Analysis → PI Design & Re-tuning → Stability Margins → Performance (THD/PF)
>   → Limitations → MIL/SIL/PIL → Conclusion → References.
> - Each section uses concise bullet points (not walls of text) and places the
>   relevant figure(s) from `./figures/` beside or under the text. Figure-to-section
>   mapping is in the inventory table at the bottom of `PROJECT_CONTENT.md`.
> - Add smooth scroll behavior, subtle fade-in-on-scroll animations for sections
>   (IntersectionObserver), and a sticky progress indicator. Keep it lightweight.
> - Make it fully responsive (mobile-friendly: figures stack under text).
> - Include a small "key results" stat band in the hero or performance section:
>   PF ≈ 0.99, THD ≈ 4.48%, Vo = 400 V, Po = 500 W, fs = 50 kHz.
> - Put a link to download the full report PDF (placeholder href I will replace).
>
> After building, give me the exact commands to (a) preview locally and
> (b) deploy to GitHub Pages.

---

## Deploying to GitHub Pages (summary — Claude Code will give exact commands)

1. Create a new GitHub repo (e.g. `pfc-converter-project`).
2. Put `index.html` at the repo root (GitHub Pages serves root or `/docs`).
3. Push the files.
4. In the repo: **Settings → Pages → Build and deployment → Source: Deploy from a
   branch → main / root**.
5. Your site goes live at `https://<username>.github.io/pfc-converter-project/`.

Tip: keep the `figures/` folder next to `index.html` and reference images as
`figures/plant-bode.png` (relative paths) so they work on GitHub Pages.

---

## About connecting Claude Code to Canva (your other question)

You don't actually need Canva for the website — all the project content and figures
are already in this kit. But if you ever want Claude Code to read your Canva design's
content directly, you can add the Canva MCP connector to Claude Code. See:
https://docs.claude.com/en/docs/claude-code/overview (look for the MCP / connectors
section). The simplest path is still: export the Canva slides as PNG/PDF and drop
them in a folder Claude Code can read.
