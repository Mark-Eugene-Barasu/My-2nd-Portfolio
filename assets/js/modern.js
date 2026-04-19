// Modern Super-Animated Portfolio JS
// GSAP 3.12+, particles.js, intense animations, dark toggle

// Core Setup
document.addEventListener('DOMContentLoaded', () => {
  initAnimations();
  initParticles();
  initDarkMode();
  initSmoothScroll();
});

// GSAP + ScrollTrigger CDN expected in HTML
function initAnimations() {
  gsap.registerPlugin(ScrollTrigger);

  // Global stagger for sections
  gsap.utils.toArray('.gsap-stagger').forEach((section) => {
    gsap.from(section.querySelectorAll('.gsap-child'), {
      duration: 0.8,
      y: 80,
      opacity: 0,
      stagger: 0.1,
      ease: 'back.out(1.7)', // Elastic bounce
      scrollTrigger: {
        trigger: section,
        start: 'top 85%',
        toggleActions: 'play none none reverse'
      }
    });
  });

  // Hero title glitch + stagger words
  const heroTitle = document.querySelector('.hero-title');
  if (heroTitle) {
    const words = heroTitle.innerHTML.split(' ');
    heroTitle.innerHTML = words.map(word => `<span class="gsap-word">${word}</span>`).join(' ');
    gsap.from('.gsap-word', {
      duration: 1,
      scale: 0,
      rotation: 180,
      opacity: 0,
      stagger: 0.05,
      ease: 'elastic.out(1,0.3)'
    });
    gsap.to(heroTitle, {
      glitch: true, // Custom via keyframes
      duration: 0.1,
      repeat: -1,
      yoyo: true,
      ease: 'power2.inOut'
    });
  }

  // Stats counters
  gsap.utils.toArray('.hero-stat strong').forEach((stat) => {
    const target = parseInt(stat.textContent);
    gsap.to(stat, {
      duration: 2,
      innerHTML: target,
      snap: { innerHTML: 1 },
      scrollTrigger: {
        trigger: stat,
        start: 'top 90%'
      },
      onUpdate: function() {
        stat.innerHTML = Math.ceil(this.targets()[0].innerHTML);
      }
    });
  });

  // Progress bars intense fill
  gsap.utils.toArray('.progress-bar').forEach((bar, i) => {
    const width = bar.style.width;
    gsap.fromTo(bar, 
      { width: 0, scaleX: 0 },
      {
        width: width,
        scaleX: 1,
        duration: 1.5,
        ease: 'power4.out',
        delay: i * 0.1,
        scrollTrigger: {
          trigger: bar.parentElement,
          start: 'top 90%'
        }
      }
    );
  });

  // Timeline chain reaction dots
  gsap.utils.toArray('.timeline-dot').forEach((dot, i) => {
    gsap.fromTo(dot, 
      { scale: 0, opacity: 0 },
      {
        scale: 1,
        opacity: 1,
        duration: 0.6,
        ease: 'elastic.out(1,0.5)',
        delay: i * 0.15,
        scrollTrigger: {
          trigger: dot.parentElement,
          start: 'top 80%'
        }
      }
    );
  });

  // Button ripples
  gsap.utils.toArray('.hero-button').forEach(btn => {
    btn.addEventListener('click', (e) => {
      const ripple = document.createElement('span');
      ripple.style.cssText = `
        position: absolute;
        width: 20px; height: 20px;
        border-radius: 50%;
        background: rgba(255,255,255,0.6);
        transform: scale(0);
        animation: ripple 0.6s linear;
        pointer-events: none;
      `;
      ripple.style.left = (e.clientX - btn.offsetLeft - 10) + 'px';
      ripple.style.top = (e.clientY - btn.offsetTop - 10) + 'px';
      btn.appendChild(ripple);
      setTimeout(() => ripple.remove(), 600);
    });
  });
}

// Particles.js - Coding theme (matrix-like)
function initParticles() {
  if (particlesJS) {
    particlesJS('particles', {
      particles: {
        number: { value: 100, density: { enable: true, value_area: 800 } },
        color: { value: ['#00f5ff', '#ff0080', '#ffff00'] },
        shape: { type: 'circle' },
        opacity: { value: 0.7, random: true },
        size: { value: 3, random: true },
        line_linked: {
          enable: true,
          distance: 150,
          color: '#00f5ff',
          opacity: 0.3,
          width: 1
        },
        move: {
          enable: true,
          speed: 4,
          direction: 'none',
          random: true,
          straight: false,
          out_mode: 'out'
        }
      },
      interactivity: {
        events: { onhover: { enable: true, mode: 'repulse' } },
        modes: { repulse: { distance: 100, duration: 0.4 } }
      },
      retina_detect: true
    });
  }
}

// Dark Mode Toggle
function initDarkMode() {
  const toggle = document.querySelector('.theme-toggle');
  if (!toggle) {
    const newToggle = document.createElement('button');
    newToggle.className = 'theme-toggle';
    newToggle.innerHTML = '🌙';
    newToggle.title = 'Toggle Theme';
    document.body.appendChild(newToggle);
    toggle = newToggle;
  }

  const currentTheme = localStorage.getItem('theme') || 'light';
  document.documentElement.setAttribute('data-theme', currentTheme);
  toggle.textContent = currentTheme === 'dark' ? '☀️' : '🌙';

  toggle.addEventListener('click', () => {
    const newTheme = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    toggle.textContent = newTheme === 'dark' ? '☀️' : '🌙';
    gsap.to('body', { duration: 0.5, backgroundColor: newTheme === 'dark' ? '#0a0a20' : '#1a1a3e' });
  });
}

// Smooth Scroll + Mobile Menu Enhance
function initSmoothScroll() {
  // Existing openNav/closeNav compatible
  window.openNav = () => {
    gsap.to('#mySidenav', { duration: 0.5, width: '280px', ease: 'power2.out' });
    gsap.to('#pageContainer', { duration: 0.3, opacity: 0.3 });
    gsap.to('#navButton', { duration: 0.3, scale: 0 });
  };

  window.closeNav = () => {
    gsap.to('#mySidenav', { duration: 0.4, width: 0, ease: 'power2.in' });
    gsap.to('#pageContainer', { duration: 0.3, opacity: 1 });
    gsap.to('#navButton', { duration: 0.3, scale: 1 });
  };

  // Lazy load images
  if ('IntersectionObserver' in window) {
    const imgObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const img = entry.target;
          img.src = img.dataset.src || img.src;
          img.classList.remove('lazy');
          imgObserver.unobserve(img);
        }
      });
    });
    document.querySelectorAll('img[data-src]').forEach(img => imgObserver.observe(img));
  }
}

// CSS @keyframes ripple (inject if needed)
const style = document.createElement('style');
style.textContent = `@keyframes ripple { to { transform: scale(4); opacity: 0; } }`;
document.head.appendChild(style);
