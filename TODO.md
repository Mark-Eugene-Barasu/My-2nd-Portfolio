# Portfolio Upgrade TODO

## Phase 1 — Backend: Role-Based Authentication & API

- [ ] Update `backend/requirements.txt` (add simplejwt, extensions)
- [ ] Create `backend/users/` app (Custom User model with role field)
- [ ] Update `backend/portfolio_api/settings.py` (JWT auth, custom user model)
- [ ] Create `backend/users/serializers.py` (Register, Login, Profile)
- [ ] Create `backend/users/views.py` (RegisterView, LoginView, ProfileView, UserListView)
- [ ] Create `backend/users/urls.py` (Auth endpoints)
- [ ] Create `backend/users/admin.py` (Admin user management)
- [ ] Update `backend/portfolio_api/urls.py` (Wire users app)
- [ ] Update `backend/contact/views.py` (Add permissions, role-based access)
- [ ] Update `backend/analytics/views.py` (Admin-only stats, role-based filtering)
- [ ] Update `backend/analytics/models.py` (Add user_role field)

## Phase 2 — Frontend: Business-Focused Restructure

- [ ] Update `index.html` (Business value hero, featured projects, AI tools, remove course apps)
- [ ] Update `pages/projects/index.html` (Two-tier: Enterprise + Course Apps)
- [ ] Update `pages/projects/django_project.html` (Business value + AI badge)
- [ ] Update `pages/projects/nextjs_project.html` (Business value + AI badge)
- [ ] Update `pages/projects/spring_project.html` (Business value + AI badge)
- [ ] Update `pages/stacks.html` (Business value per stack)
- [ ] Update `pages/about.html` (Employer-focused copy)
- [ ] Update `pages/gallery.html` & `pages/socials.html` (Nav consistency)

## Phase 3 — Role-Based UI (JavaScript)

- [ ] Create `assets/js/auth.js` (JWT, login/logout, role checking)
- [ ] Create `assets/js/nav.js` (Dynamic nav based on role)
- [ ] Add login modal to all HTML pages
- [ ] Conditionally render admin-only sections

## Phase 4 — Documentation

- [ ] Rewrite root `README.md` (User + Tech docs, architecture, AI usage)
- [ ] Rewrite `backend/README.md` (Backend-specific docs)
- [ ] Create `docs/user-guide.md`
- [ ] Create `docs/tech-spec.md`
- [ ] Create `docs/api-reference.md`
- [ ] Add docstrings/comments to all backend files

## Phase 5 — Hosting & Deployment

- [ ] Add "Live & Hosted" badges to `index.html`
- [ ] Update `README.md` with deployment status
- [ ] Ensure production-ready backend settings

## Phase 6 — AI Productivity Showcase

- [ ] Add "Built with AI Augmentation" section to `index.html`
- [ ] Add AI-Assisted badges to project pages
