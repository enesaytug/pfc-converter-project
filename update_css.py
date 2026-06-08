css = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

/* ===== Reset & Base ===== */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
  --bg-main: #0B0F19;
  --bg-panel: rgba(255, 255, 255, 0.03);
  --bg-panel-hover: rgba(255, 255, 255, 0.05);
  --accent: #3b82f6;
  --accent-glow: rgba(59, 130, 246, 0.5);
  --text-main: #e2e8f0;
  --text-muted: #94a3b8;
  --border-light: rgba(255, 255, 255, 0.08);
  --radius: 12px;
  --max-w: 1100px;
  --section-gap: 5rem;
}

html { scroll-behavior: smooth; font-size: 16px; }

body {
  font-family: 'Inter', system-ui, -apple-system, sans-serif;
  color: var(--text-main);
  background: var(--bg-main);
  background-image: 
    radial-gradient(circle at 15% 50%, rgba(59, 130, 246, 0.08) 0%, transparent 50%),
    radial-gradient(circle at 85% 30%, rgba(139, 92, 246, 0.08) 0%, transparent 50%);
  background-attachment: fixed;
  line-height: 1.7;
}

/* ===== Progress Bar ===== */
#progress-bar {
  position: fixed;
  top: 0; left: 0;
  height: 3px;
  width: 0%;
  background: linear-gradient(90deg, #3b82f6, #8b5cf6);
  box-shadow: 0 0 10px var(--accent-glow);
  z-index: 1000;
  transition: width 0.1s linear;
}

/* ===== Navigation ===== */
nav {
  position: sticky;
  top: 0;
  z-index: 900;
  background: rgba(11, 15, 25, 0.7);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border-bottom: 1px solid var(--border-light);
}

.nav-inner {
  max-width: var(--max-w);
  margin: 0 auto;
  padding: 0 1.5rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 60px;
}

.nav-brand {
  color: #fff;
  font-weight: 700;
  font-size: 1rem;
  letter-spacing: 0.02em;
  text-decoration: none;
  white-space: nowrap;
  flex-shrink: 0;
  background: linear-gradient(90deg, #fff, #94a3b8);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.nav-links {
  display: flex;
  gap: 0.5rem;
  list-style: none;
  overflow-x: auto;
  scrollbar-width: none;
  flex-wrap: nowrap;
}

.nav-links::-webkit-scrollbar { display: none; }

.nav-links a {
  color: var(--text-muted);
  text-decoration: none;
  font-size: 0.8rem;
  font-weight: 500;
  padding: 0.4rem 0.8rem;
  border-radius: 6px;
  white-space: nowrap;
  transition: all 0.2s;
}

.nav-links a:hover,
.nav-links a.active {
  background: var(--bg-panel);
  color: #fff;
}

/* ===== Hero ===== */
#hero {
  padding: 8rem 1.5rem 6rem;
  position: relative;
  text-align: center;
}

.hero-inner {
  max-width: 800px;
  margin: 0 auto;
}

.hero-badge {
  display: inline-block;
  background: rgba(59, 130, 246, 0.1);
  border: 1px solid rgba(59, 130, 246, 0.2);
  color: #60a5fa;
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  padding: 0.4rem 1rem;
  border-radius: 20px;
  margin-bottom: 1.5rem;
  box-shadow: 0 0 15px rgba(59, 130, 246, 0.1);
}

.hero-title {
  font-size: clamp(2rem, 5vw, 3.5rem);
  font-weight: 800;
  line-height: 1.1;
  margin-bottom: 1rem;
  letter-spacing: -0.02em;
  color: #fff;
  background: linear-gradient(180deg, #ffffff 0%, #cbd5e1 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.hero-subtitle {
  font-size: 1.1rem;
  color: var(--text-muted);
  margin-bottom: 2.5rem;
}

.hero-meta {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 1rem 2.5rem;
  font-size: 0.9rem;
  color: var(--text-muted);
  margin-bottom: 3rem;
}

.hero-meta span strong { color: #fff; font-weight: 600; }

/* ===== Stats Band ===== */
.stats-band {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 1px;
  background: var(--border-light);
  border-radius: var(--radius);
  overflow: hidden;
  margin: 0 auto;
}

.stat-item {
  background: var(--bg-main);
  padding: 1.5rem 1rem;
  text-align: center;
  position: relative;
}

.stat-item::before {
  content: '';
  position: absolute;
  inset: 0;
  background: var(--bg-panel);
  transition: opacity 0.3s;
  opacity: 0;
}

.stat-item:hover::before { opacity: 1; }

.stat-value {
  font-size: 1.5rem;
  font-weight: 800;
  color: #fff;
  letter-spacing: -0.02em;
  position: relative;
  z-index: 1;
}

.stat-label {
  font-size: 0.7rem;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-top: 0.3rem;
  position: relative;
  z-index: 1;
}

.hero-actions {
  margin-top: 3rem;
  display: flex;
  justify-content: center;
  gap: 1rem;
  flex-wrap: wrap;
}

.btn-primary, .btn-secondary {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.8rem 1.5rem;
  border-radius: 8px;
  font-size: 0.9rem;
  font-weight: 600;
  text-decoration: none;
  transition: all 0.2s;
  cursor: pointer;
  border: 1px solid transparent;
}

.btn-primary {
  background: var(--accent);
  color: #fff;
  box-shadow: 0 4px 15px var(--accent-glow);
}

.btn-primary:hover { 
  background: #2563eb; 
  transform: translateY(-2px); 
  box-shadow: 0 6px 20px var(--accent-glow);
}

.btn-secondary {
  background: var(--bg-panel);
  color: #fff;
  border-color: var(--border-light);
}

.btn-secondary:hover { 
  background: var(--bg-panel-hover); 
  transform: translateY(-2px); 
}

/* ===== Sections ===== */
.section {
  padding: var(--section-gap) 1.5rem;
  opacity: 0;
  transform: translateY(20px);
  transition: opacity 0.6s ease-out, transform 0.6s ease-out;
}

.section.visible {
  opacity: 1;
  transform: none;
}

.section-inner {
  max-width: var(--max-w);
  margin: 0 auto;
}

.section-header {
  margin-bottom: 2.5rem;
}

.section-tag {
  display: inline-block;
  font-size: 0.75rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--accent);
  margin-bottom: 0.5rem;
}

.section-title {
  font-size: clamp(1.5rem, 3vw, 2.2rem);
  font-weight: 800;
  color: #fff;
  line-height: 1.2;
}

.divider {
  width: 60px;
  height: 4px;
  background: var(--accent);
  border-radius: 2px;
  margin-top: 1rem;
  box-shadow: 0 0 10px var(--accent-glow);
}

/* ===== Content grid ===== */
.content-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  align-items: start;
}

.content-grid.wide-text { grid-template-columns: 1.2fr 1fr; }
.content-grid.wide-fig  { grid-template-columns: 1fr 1.2fr; }
.content-grid.single    { grid-template-columns: 1fr; max-width: 800px; margin: 0 auto; }

/* ===== Bullet lists ===== */
.point-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.point-list li {
  padding-left: 1.5rem;
  position: relative;
  color: var(--text-main);
  font-size: 1rem;
  line-height: 1.6;
}

.point-list li::before {
  content: '✦';
  position: absolute;
  left: 0;
  color: var(--accent);
  font-size: 0.8rem;
  top: 0.25rem;
}

.point-list li strong { color: #fff; font-weight: 600; }

/* ===== Figures ===== */
.fig-block {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.fig-wrap {
  background: var(--bg-panel);
  border-radius: var(--radius);
  overflow: hidden;
  border: 1px solid var(--border-light);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  transition: transform 0.3s, border-color 0.3s;
}

.fig-wrap:hover {
  transform: translateY(-5px);
  border-color: rgba(59, 130, 246, 0.3);
}

.fig-wrap img {
  width: 100%;
  height: auto;
  display: block;
  object-fit: contain;
  background: #fff; /* Keep background white for PDFs converted to images, so they are legible */
}

.fig-caption {
  font-size: 0.8rem;
  color: var(--text-muted);
  padding: 0.8rem 1rem;
  background: rgba(0,0,0,0.2);
  border-top: 1px solid var(--border-light);
  font-style: italic;
  text-align: center;
}

/* ===== Highlight / Callout Box ===== */
.highlight-box {
  background: rgba(59, 130, 246, 0.05);
  border: 1px solid rgba(59, 130, 246, 0.2);
  border-radius: var(--radius);
  padding: 1.5rem;
  font-size: 0.95rem;
  margin-top: 1.5rem;
  position: relative;
  overflow: hidden;
}

.highlight-box::before {
  content: '';
  position: absolute;
  top: 0; left: 0; width: 4px; height: 100%;
  background: var(--accent);
}

.highlight-box h4 {
  font-size: 0.85rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: #60a5fa;
  margin-bottom: 1rem;
}

.kv-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
}

.kv-item { display: flex; flex-direction: column; gap: 0.2rem; }
.kv-label { font-size: 0.75rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.05em; }
.kv-value { font-size: 1.05rem; font-weight: 600; color: #fff; }

/* ===== Results pill band ===== */
.results-pills {
  display: flex;
  flex-wrap: wrap;
  gap: 0.8rem;
  margin-top: 1.5rem;
}

.pill {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: var(--bg-panel);
  border: 1px solid var(--border-light);
  border-radius: 20px;
  padding: 0.4rem 1rem;
  font-size: 0.85rem;
  color: var(--text-main);
  transition: background 0.2s;
}

.pill:hover { background: var(--bg-panel-hover); }
.pill strong { color: #60a5fa; }

/* ===== Callouts ===== */
.callout {
  border-left: 4px solid;
  padding: 1rem 1.2rem;
  border-radius: 0 var(--radius) var(--radius) 0;
  font-size: 0.95rem;
  margin-top: 1.5rem;
  background: var(--bg-panel);
}

.callout-warn { border-color: #f59e0b; }
.callout-info { border-color: #3b82f6; }
.callout-success { border-color: #10b981; }

.callout strong { display: block; margin-bottom: 0.4rem; color: #fff; }

/* ===== Comparison badges ===== */
.badge-row {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-top: 1.5rem;
}

.badge {
  border-radius: var(--radius);
  padding: 1rem 1.2rem;
  font-size: 0.9rem;
  background: var(--bg-panel);
  border: 1px solid var(--border-light);
  border-left: 4px solid;
}

.badge-mil  { border-left-color: #3b82f6; }
.badge-sil  { border-left-color: #10b981; }
.badge-pil  { border-left-color: #f59e0b; }

.badge strong { 
  display: block; 
  font-size: 0.8rem; 
  text-transform: uppercase; 
  letter-spacing: 0.05em; 
  margin-bottom: 0.3rem; 
  color: #fff;
}

/* ===== References ===== */
.ref-list {
  list-style: none;
  counter-reset: ref-counter;
  display: flex;
  flex-direction: column;
  gap: 1rem;
  max-width: 800px;
}

.ref-list li {
  counter-increment: ref-counter;
  padding-left: 3rem;
  position: relative;
  font-size: 0.95rem;
  color: var(--text-muted);
  line-height: 1.6;
}

.ref-list li::before {
  content: '[' counter(ref-counter) ']';
  position: absolute;
  left: 0;
  top: 0;
  color: var(--accent);
  font-weight: 600;
  background: var(--bg-panel);
  padding: 0.2rem 0.6rem;
  border-radius: 4px;
  font-size: 0.8rem;
}

/* ===== Footer ===== */
footer {
  background: rgba(0,0,0,0.3);
  border-top: 1px solid var(--border-light);
  color: var(--text-muted);
  text-align: center;
  padding: 3rem 1.5rem;
  font-size: 0.9rem;
  margin-top: 4rem;
}

footer a { color: var(--accent); text-decoration: none; }
footer a:hover { text-decoration: underline; }

/* ===== Responsive ===== */
@media (max-width: 900px) {
  .content-grid,
  .content-grid.wide-text,
  .content-grid.wide-fig {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 768px) {
  .stats-band { grid-template-columns: repeat(3, 1fr); }
  .stats-band .stat-item:nth-child(4),
  .stats-band .stat-item:nth-child(5) { grid-column: span 1; }
  .nav-brand { display: none; }
  .kv-grid { grid-template-columns: 1fr; }
  .hero-meta { flex-direction: column; gap: 0.5rem; }
}

@media (max-width: 480px) {
  :root { --section-gap: 3.5rem; }
  .stats-band { grid-template-columns: repeat(2, 1fr); }
  .stats-band .stat-item:last-child { grid-column: span 2; }
}
"""
with open("style.css", "w") as f:
    f.write(css)
print("Updated style.css")
