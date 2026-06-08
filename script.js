/* ===== Progress bar ===== */
const progressBar = document.getElementById('progress-bar');
window.addEventListener('scroll', () => {
  const scrolled = window.scrollY;
  const total = document.documentElement.scrollHeight - window.innerHeight;
  progressBar.style.width = total > 0 ? (scrolled / total * 100) + '%' : '0%';
}, { passive: true });

/* ===== Fade-in on scroll ===== */
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });

document.querySelectorAll('.section').forEach(s => observer.observe(s));

/* ===== Active nav link ===== */
const sections = document.querySelectorAll('.section[id]');
const navLinks = document.querySelectorAll('.nav-links a[href^="#"]');

const navObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const id = entry.target.getAttribute('id');
      navLinks.forEach(a => {
        a.classList.toggle('active', a.getAttribute('href') === '#' + id);
      });
    }
  });
}, { threshold: 0.35 });

sections.forEach(s => navObserver.observe(s));

/* ===== Graceful missing figure handling ===== */
document.querySelectorAll('.fig-wrap img').forEach(img => {
  img.addEventListener('error', function () {
    this.closest('.fig-wrap').classList.add('fig-missing');
    this.style.display = 'none';
    const ph = document.createElement('div');
    ph.className = 'fig-placeholder';
    ph.innerHTML = `<span>Figure not yet available</span><small>${this.getAttribute('alt') || ''}</small>`;
    ph.style.cssText = 'padding:2.5rem 1rem;text-align:center;color:#9aa5be;font-size:0.8rem;display:flex;flex-direction:column;gap:0.35rem;align-items:center;min-height:120px;justify-content:center;';
    this.closest('.fig-wrap').prepend(ph);
  });
});
