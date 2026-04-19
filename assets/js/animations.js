// Super Animations
gsap.registerPlugin(ScrollTrigger, MotionPathPlugin);

gsap.from('.hero h1', { duration: 1.5, y: 100, opacity: 0, ease: 'bounce.out' });
gsap.from('.hero p', { duration: 1, y: 50, opacity: 0, stagger: 0.2, delay: 0.5 });
gsap.from('.btn', { duration: 0.8, scale: 0, rotation: 180, stagger: 0.1, delay: 1 });

ScrollTrigger.batch('.card', {
  onEnter: batch => gsap.from(batch, {duration: 0.6, y: 100, opacity: 0, stagger: 0.1}),
});

gsap.to('.project-card', {
  scrollTrigger: {
    trigger: '.projects-grid',
    start: 'top bottom',
  },
  rotationY: 10,
  scale: 1.05,
  duration: 1,
  stagger: 0.1
});

document.querySelectorAll('.social-link').forEach(link => {
  link.addEventListener('mouseenter', () => gsap.to(link, {scale: 1.2, rotation: 360, duration: 0.6}));
});

