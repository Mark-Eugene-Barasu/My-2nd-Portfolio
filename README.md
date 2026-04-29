# Eugene Mark Korku Barasu — Full-Stack Developer Portfolio 🚀

[![Django CI](https://github.com/Mark-Eugene-Barasu/My-2nd-Portfolio/actions/workflows/django.yml/badge.svg)](https://github.com/Mark-Eugene-Barasu/My-2nd-Portfolio/actions)
[![Docker](https://img.shields.io/badge/docker-ready-blue?logo=docker)](docker-compose.yml)
[![GraphQL](https://img.shields.io/badge/graphql-enabled-e535ab?logo=graphql)](backend/portfolio_api/schema.py)
[![PWA](https://img.shields.io/badge/PWA-installable-5a0fc8?logo=pwa)](manifest.json)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen?logo=pytest)](backend/)

**Live Site**: [mark-eugene-barasu.github.io/My-2nd-Portfolio](https://mark-eugene-barasu.github.io/My-2nd-Portfolio/)

Production-ready portfolio showcasing Django REST APIs, role-based auth, CI/CD, PWA, and more. Open to full-time/contract roles.

## 📁 Project Structure

```
second_protfolio/
├── index.html                        # 🎯 Main homepage
├── README.md                         # 📖 This guide
├── resume/                           # 📄 CV download
│   └── CV of Eugene Mark Korku Barasu.pdf
├── assets/                           # 🎨 Media & styles
├── backend/                          # 🐍 Django API
├── pages/                            # 📄 HTML pages
├── docs/                             # 📚 Documentation
└── .github/workflows/                # 🤖 CI/CD
```

## ✨ All Features

| Feature                  | Description               | Location/Trigger                |
| ------------------------ | ------------------------- | ------------------------------- |
| **Resume Download**      | Instant PDF CV            | Hero button (`resume/CV...pdf`) |
| **Responsive Design**    | Mobile-first, all devices | All pages                       |
| **Dark Mode**            | Toggle theme              | JS + CSS                        |
| **Smooth Animations**    | Fade-ins, hovers          | Scroll-triggered                |
| **PWA Install**          | Offline, app-like         | Chrome/Edge menu                |
| **Contact Form**         | Backend-powered           | `#contact`, Django API          |
| **Role-Based Auth**      | JWT ADMIN/RECRUITER/USER  | Login modal → API               |
| **Page Analytics**       | Tracks visits, roles      | JS → `/api/analytics/track/`    |
| **GraphQL API**          | Modern queries            | `localhost:8000/graphql/`       |
| **Unit Tests**           | 100% coverage             | `python manage.py test`         |
| **CI/CD Pipeline**       | Auto-test on push/PR      | GitHub Actions                  |
| **SEO Optimized**        | Schema.org, OG tags       | `<head>` meta                   |
| **Accessibility**        | ARIA, keyboard nav        | WCAG compliant                  |
i| **Project Case Studies** | Detailed breakdowns       | `pages/projects/`               |

## 🚀 Quick Start

### Frontend Live Preview

```bash
start index.html
```

### Full Stack

```cmd
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## 🔑 Navigation Guide

| Action   | Path/Button                     |
| -------- | ------------------------------- |
| Resume   | Hero "Resume"                   |
| Projects | "View Projects"                 |
| Contact  | "Hire Me"                       |
| Backend  | `backend/manage.py`             |
| API Docs | `docs/api-reference.md`         |
| Tests    | `backend/python manage.py test` |

## 🛠 API Endpoints

**Auth** `/api/auth/register/`, `/login/`
**Contact** `/api/contact/` (public POST)
**Analytics** `/api/analytics/stats/` (admin GET)

## 📱 Demo Features

1. **Hero CTA**: Resume + Projects + Contact
2. **Dark Mode Toggle**: JS-powered
3. **Login Modal**: JWT demo
4. **Contact Form**: Real Django backend
5. **PWA**: Install button in browser

## 🎯 Recruiter Fast Track

```
1. index.html → See live portfolio
2. Resume button → Download CV
3. backend/ → Full-stack skills
4. Tests/CI → Production quality
```

---

**mark0630227248@gmail.com** | Umtata, SA

© 2025 Eugene Mark Korku Barasu
