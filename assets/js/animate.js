(function () {

  /* ── Preloader ─────────────────────────────────────── */
  const pre = document.createElement('div');
  pre.id = 'preloader';
  pre.innerHTML = `<div class="preloader-inner"><div class="preloader-logo">EMKB</div><div class="preloader-bar"></div></div>`;
  document.body.prepend(pre);
  window.addEventListener('load', () => {
    setTimeout(() => pre.classList.add('hidden'), 900);
    setTimeout(() => pre.remove(), 1500);
  });

  /* ── Scroll Reveal ─────────────────────────────────── */
  function initReveal() {
    const selectors = [
      '.project-card', '.skill-item', '.stack-card',
      '.card', '.sidebar-card', '.about-text',
      '.about-img', '.contact-form', '.section-title',
      '.content > div', '.stacks-container > div'
    ];
    selectors.forEach((sel, si) => {
      document.querySelectorAll(sel).forEach((el, i) => {
        if (el.closest('#preloader')) return;
        el.classList.add('reveal');
        if (si % 3 === 1) el.classList.add('from-left');
        else if (si % 3 === 2) el.classList.add('from-right');
        else el.classList.add('from-scale');
      });
    });

    const io = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          e.target.classList.add('visible');
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.12 });

    document.querySelectorAll('.reveal').forEach(el => io.observe(el));
  }

  /* ── Typing Effect on hero h1 ──────────────────────── */
  function initTyping() {
    const h1 = document.querySelector('.hero-content h1');
    if (!h1) return;
    const text = h1.textContent;
    h1.textContent = '';
    h1.classList.add('typing-cursor');
    let i = 0;
    const type = () => {
      if (i < text.length) {
        h1.textContent += text[i++];
        setTimeout(type, 55);
      } else {
        h1.classList.remove('typing-cursor');
      }
    };
    setTimeout(type, 1000);
  }

  /* ── Canvas Particles ──────────────────────────────── */
  function initParticles() {
    const hero = document.querySelector('.hero, .page-hero, .project-hero');
    if (!hero) return;
    const canvas = document.createElement('canvas');
    canvas.id = 'particles-canvas';
    canvas.style.cssText = 'position:absolute;inset:0;pointer-events:none;z-index:0;opacity:0.35;';
    hero.style.position = 'relative';
    hero.prepend(canvas);

    const ctx = canvas.getContext('2d');
    let W, H, dots = [];

    function resize() {
      W = canvas.width  = hero.offsetWidth;
      H = canvas.height = hero.offsetHeight;
    }
    resize();
    window.addEventListener('resize', resize);

    for (let i = 0; i < 55; i++) {
      dots.push({
        x: Math.random() * W, y: Math.random() * H,
        r: Math.random() * 2.5 + 0.5,
        dx: (Math.random() - 0.5) * 0.5,
        dy: (Math.random() - 0.5) * 0.5,
        a: Math.random()
      });
    }

    function draw() {
      ctx.clearRect(0, 0, W, H);
      dots.forEach(d => {
        ctx.beginPath();
        ctx.arc(d.x, d.y, d.r, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(255,255,255,${d.a})`;
        ctx.fill();
        d.x += d.dx; d.y += d.dy;
        if (d.x < 0 || d.x > W) d.dx *= -1;
        if (d.y < 0 || d.y > H) d.dy *= -1;
      });
      requestAnimationFrame(draw);
    }
    draw();
  }

  /* ── Counter Animation ─────────────────────────────── */
  function initCounters() {
    document.querySelectorAll('[data-target]').forEach(el => {
      const raw = el.getAttribute('data-target');
      const num = parseInt(raw);
      if (isNaN(num)) { el.textContent = raw; return; }
      const suffix = raw.replace(/[0-9]/g, '');
      let current = 0;
      const step = Math.ceil(num / 40);
      const io = new IntersectionObserver(entries => {
        if (!entries[0].isIntersecting) return;
        io.disconnect();
        const tick = () => {
          current = Math.min(current + step, num);
          el.textContent = current + suffix;
          if (current < num) requestAnimationFrame(tick);
        };
        tick();
      }, { threshold: 0.5 });
      io.observe(el);
    });
  }

  /* ── Card 3D Tilt ──────────────────────────────────── */
  function initTilt() {
    document.querySelectorAll('.project-card, .stack-card').forEach(card => {
      card.addEventListener('mousemove', e => {
        const r  = card.getBoundingClientRect();
        const x  = e.clientX - r.left - r.width  / 2;
        const y  = e.clientY - r.top  - r.height / 2;
        const rx = (-y / r.height * 10).toFixed(2);
        const ry = ( x / r.width  * 10).toFixed(2);
        card.style.transform = `perspective(800px) rotateX(${rx}deg) rotateY(${ry}deg) translateY(-8px) scale(1.02)`;
      });
      card.addEventListener('mouseleave', () => {
        card.style.transform = '';
      });
    });
  }

  /* ── Ripple on buttons ─────────────────────────────── */
  function initRipple() {
    document.querySelectorAll('.btn, .btn-primary, .cta, .hero-button').forEach(btn => {
      btn.addEventListener('click', function (e) {
        const r   = this.getBoundingClientRect();
        const rip = document.createElement('span');
        const size = Math.max(r.width, r.height);
        rip.style.cssText = `
          position:absolute; border-radius:50%;
          width:${size}px; height:${size}px;
          left:${e.clientX - r.left - size/2}px;
          top:${e.clientY - r.top  - size/2}px;
          background:rgba(255,255,255,0.3);
          transform:scale(0); animation:rippleAnim 0.6s ease-out forwards;
          pointer-events:none;
        `;
        this.style.position = 'relative';
        this.style.overflow = 'hidden';
        this.appendChild(rip);
        setTimeout(() => rip.remove(), 700);
      });
    });

    if (!document.getElementById('ripple-style')) {
      const s = document.createElement('style');
      s.id = 'ripple-style';
      s.textContent = '@keyframes rippleAnim{to{transform:scale(2.5);opacity:0}}';
      document.head.appendChild(s);
    }
  }

  /* ── Navbar scroll shrink ──────────────────────────── */
  function initNavScroll() {
    const header = document.querySelector('header');
    if (!header) return;
    window.addEventListener('scroll', () => {
      if (window.scrollY > 60) {
        header.style.padding    = '0.4rem 0';
        header.style.boxShadow  = '0 4px 30px rgba(0,0,0,0.2)';
      } else {
        header.style.padding    = '1rem 0';
        header.style.boxShadow  = '0 2px 20px rgba(0,0,0,0.1)';
      }
    });
  }

  /* ── Feature list items stagger ───────────────────── */
  function initFeatureList() {
    document.querySelectorAll('.feature-list li').forEach((li, i) => {
      li.style.opacity = '0';
      li.style.transform = 'translateX(-20px)';
      li.style.transition = `opacity 0.4s ease ${i * 0.08}s, transform 0.4s ease ${i * 0.08}s`;
      const io = new IntersectionObserver(entries => {
        if (entries[0].isIntersecting) {
          li.style.opacity = '1';
          li.style.transform = 'translateX(0)';
          io.disconnect();
        }
      }, { threshold: 0.3 });
      io.observe(li);
    });
  }

  /* ── Init all ──────────────────────────────────────── */
  document.addEventListener('DOMContentLoaded', () => {
    initReveal();
    initTyping();
    initParticles();
    initCounters();
    initTilt();
    initRipple();
    initNavScroll();
    initFeatureList();
  });

})();
