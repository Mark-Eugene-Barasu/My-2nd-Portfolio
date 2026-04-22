(function () {
  // ── Create button ──────────────────────────────────────────────
  const btn = document.createElement('button');
  btn.id = 'dm-toggle';
  btn.setAttribute('aria-label', 'Toggle dark mode');
  document.body.appendChild(btn);

  // ── State ──────────────────────────────────────────────────────
  const DARK_KEY = 'emkb-dark-mode';
  const POS_KEY  = 'emkb-dm-pos';

  let isDark = localStorage.getItem(DARK_KEY) === 'true';

  function applyTheme() {
    document.body.classList.toggle('dark-mode', isDark);
    btn.textContent = isDark ? '☀️' : '🌙';
    btn.setAttribute('data-tip', isDark ? 'Light mode' : 'Dark mode');
  }

  applyTheme();

  btn.addEventListener('click', function () {
    if (dragged) return; // ignore click after drag
    isDark = !isDark;
    localStorage.setItem(DARK_KEY, isDark);
    applyTheme();
  });

  // ── Restore saved position ─────────────────────────────────────
  const saved = JSON.parse(localStorage.getItem(POS_KEY) || 'null');
  if (saved) {
    btn.style.right  = 'auto';
    btn.style.bottom = 'auto';
    btn.style.left   = saved.x + 'px';
    btn.style.top    = saved.y + 'px';
  }

  // ── Drag logic (mouse + touch) ─────────────────────────────────
  let dragged = false;
  let startX, startY, startLeft, startTop;

  function getPos() {
    const r = btn.getBoundingClientRect();
    return { left: r.left, top: r.top };
  }

  function onDragStart(clientX, clientY) {
    dragged = false;
    const pos = getPos();
    startX    = clientX;
    startY    = clientY;
    startLeft = pos.left;
    startTop  = pos.top;

    btn.style.right  = 'auto';
    btn.style.bottom = 'auto';
    btn.style.left   = startLeft + 'px';
    btn.style.top    = startTop  + 'px';
    btn.style.transition = 'none';
  }

  function onDragMove(clientX, clientY) {
    const dx = clientX - startX;
    const dy = clientY - startY;
    if (Math.abs(dx) > 4 || Math.abs(dy) > 4) dragged = true;
    if (!dragged) return;

    const maxX = window.innerWidth  - btn.offsetWidth;
    const maxY = window.innerHeight - btn.offsetHeight;
    const newX = Math.min(Math.max(startLeft + dx, 0), maxX);
    const newY = Math.min(Math.max(startTop  + dy, 0), maxY);

    btn.style.left = newX + 'px';
    btn.style.top  = newY + 'px';
  }

  function onDragEnd() {
    btn.style.transition = '';
    if (dragged) {
      localStorage.setItem(POS_KEY, JSON.stringify({
        x: parseFloat(btn.style.left),
        y: parseFloat(btn.style.top)
      }));
    }
    setTimeout(() => { dragged = false; }, 0);
  }

  // Mouse
  btn.addEventListener('mousedown', e => {
    e.preventDefault();
    onDragStart(e.clientX, e.clientY);
    const move = e2 => onDragMove(e2.clientX, e2.clientY);
    const up   = ()  => { onDragEnd(); document.removeEventListener('mousemove', move); document.removeEventListener('mouseup', up); };
    document.addEventListener('mousemove', move);
    document.addEventListener('mouseup',   up);
  });

  // Touch
  btn.addEventListener('touchstart', e => {
    const t = e.touches[0];
    onDragStart(t.clientX, t.clientY);
  }, { passive: true });

  btn.addEventListener('touchmove', e => {
    const t = e.touches[0];
    onDragMove(t.clientX, t.clientY);
  }, { passive: true });

  btn.addEventListener('touchend', onDragEnd);
})();
