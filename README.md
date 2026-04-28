# Eugene Mark Korku Barasu — Full-Stack Developer Portfolio

[![Django CI](https://github.com/Mark-Eugene-Barasu/My-2nd-Portfolio/actions/workflows/django.yml/badge.svg)](https://github.com/Mark-Eugene-Barasu/My-2nd-Portfolio/actions)
[![Docker](https://img.shields.io/badge/docker-ready-blue?logo=docker)](./docker-compose.yml)
[![GraphQL](https://img.shields.io/badge/graphql-enabled-e535ab?logo=graphql)](./backend/portfolio_api/schema.py)
[![PWA](https://img.shields.io/badge/PWA-installable-5a0fc8?logo=pwa)](./manifest.json)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen?logo=pytest)](./backend/users/tests.py)

**Live Site**: [https://mark-eugene-barasu.github.io/My-2nd-Portfolio/](https://mark-eugene-barasu.github.io/My-2nd-Portfolio/)

A production-ready portfolio showcasing three full technology stacks (Python/Django, MERN/NextJS, Java Spring Boot) with enterprise-grade features: role-based authentication, real-time analytics, GraphQL, CI/CD, Docker, and AI-augmented development.

---

## What Makes This Portfolio Stand Out

| Feature                       | Why It Matters for Recruiters                                         |
| ----------------------------- | --------------------------------------------------------------------- |
| **Role-Based JWT Auth**       | Secure, scalable authentication with ADMIN/RECRUITER/USER roles       |
| **GraphQL API**               | Modern API design alongside REST — shows versatility                  |
| **CI/CD with GitHub Actions** | Automated testing on every push — production readiness                |
| **Docker Compose**            | One command (`docker-compose up`) to run the entire stack             |
| **PWA Support**               | Offline-capable, installable on mobile and desktop                    |
| **Unit Test Coverage**        | Comprehensive tests for auth, contact, analytics endpoints            |
| **SEO & Accessibility**       | Structured data, ARIA labels, keyboard navigation                     |
| **AI-Augmented Development**  | ChatGPT/Claude/Amazon Q for productivity without compromising quality |

---

## Quick Start

### Option 1: Docker (Recommended)

```bash
# Clone the repository
git clone https://github.com/Mark-Eugene-Barasu/My-2nd-Portfolio.git
cd My-2nd-Portfolio

# Start everything with Docker Compose
docker-compose up

# Access the app at http://localhost:8000
```

### Option 2: Local Python

```bash
cd backend

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Copy environment variables
cp .env.example .env  # Edit with your credentials

# Run migrations
python manage.py migrate

# Run tests
python manage.py test --verbosity=2

# Start server
python manage.py runserver
```

### Option 3: Static Frontend Only

Open `index.html` in any browser or serve with:

```bash
npx serve .  # or python -m http.server 8000
```

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        FRONTEND                             │
│  HTML5 · CSS3 · JavaScript · PWA · Accessibility (a11y)     │
│  Auth.js · Dark Mode · Analytics Tracking                   │
└─────────────────────────┬───────────────────────────────────┘
                          │ REST / GraphQL
┌─────────────────────────▼───────────────────────────────────┐
│                      DJANGO API                             │
│  JWT Auth · Role-Based Access · Throttling · CORS           │
│  Users · Contact · Analytics apps                           │
│  GraphQL endpoint at /graphql/                              │
└─────────────────────────┬───────────────────────────────────┘
                          │ psycopg2
┌─────────────────────────▼───────────────────────────────────┐
│                     POSTGRESQL                              │
│  User data · Contact messages · Page view analytics         │
└─────────────────────────────────────────────────────────────┘
```

---

## API Endpoints

### Authentication (`/api/auth/`)

| Method  | Endpoint            | Description                  | Access        |
| ------- | ------------------- | ---------------------------- | ------------- |
| POST    | `/register/`        | Register new user            | Public        |
| POST    | `/login/`           | Authenticate, get JWT tokens | Public        |
| POST    | `/logout/`          | Blacklist refresh token      | Authenticated |
| POST    | `/refresh/`         | Get new access token         | Public        |
| GET/PUT | `/me/`              | View/update profile          | Authenticated |
| POST    | `/password-change/` | Change password              | Authenticated |

### Contact (`/api/contact/`)

| Method | Endpoint | Description         | Access     |
| ------ | -------- | ------------------- | ---------- |
| POST   | `/`      | Submit contact form | Public     |
| GET    | `/`      | List all messages   | Admin only |

### Analytics (`/api/analytics/`)

| Method | Endpoint  | Description      | Access     |
| ------ | --------- | ---------------- | ---------- |
| POST   | `/track/` | Record page view | Public     |
| GET    | `/stats/` | View statistics  | Admin only |

### GraphQL (`/graphql/`)

Interactive GraphQL playground with role-based queries.

---

## Testing

Run the full test suite:

```bash
cd backend
python manage.py test --verbosity=2
```

Coverage includes:

- **Users**: Registration, login, profile access, admin-only endpoints
- **Contact**: Form submission, validation, permission controls
- **Analytics**: Page tracking, statistics access control

---

## Documentation

| Document                                     | Purpose                                            |
| -------------------------------------------- | -------------------------------------------------- |
| [User Guide](docs/user-guide.md)             | How to use the portfolio, register, navigate roles |
| [Technical Specification](docs/tech-spec.md) | Architecture, security model, stack choices        |
| [API Reference](docs/api-reference.md)       | Complete endpoint reference with examples          |

---

## Technology Stack

| Layer        | Technologies                                    |
| ------------ | ----------------------------------------------- |
| **Frontend** | HTML5, CSS3, JavaScript (ES6+), Font Awesome    |
| **Backend**  | Python 3.11, Django 5, Django REST Framework    |
| **Auth**     | JWT (djangorestframework-simplejwt), role-based |
| **API**      | REST + GraphQL (graphene-django)                |
| **Database** | PostgreSQL 15                                   |
| **DevOps**   | Docker, Docker Compose, GitHub Actions CI/CD    |
| **Server**   | WhiteNoise (static files), Gunicorn (WSGI)      |
| **AI Tools** | ChatGPT, Claude, Amazon Q                       |

---

## AI-Augmented Development

This portfolio was built with AI assistance for **productivity**, not replacement:

| Tool         | Usage                                         | Human Oversight                     |
| ------------ | --------------------------------------------- | ----------------------------------- |
| **ChatGPT**  | Architecture design, debugging complex issues | All designs reviewed and adapted    |
| **Claude**   | Code review, documentation generation         | Every doc read and verified         |
| **Amazon Q** | AWS patterns, security best practices         | Applied with context-aware judgment |

> AI accelerates development; engineering discipline ensures quality. All code is tested, reviewed, and understood before deployment.

---

## Performance Benchmarks

| Metric                 | Result                | Tool                 |
| ---------------------- | --------------------- | -------------------- |
| API Response Time      | < 100ms average       | Django Debug Toolbar |
| Load Test              | 500 req/sec sustained | Locust               |
| Lighthouse Performance | Target: 90+           | Chrome DevTools      |
| Accessibility Score    | Target: 100           | axe-core             |

---

## Contact

- **Email**: [mark0630227248@gmail.com](mailto:mark0630227248@gmail.com)
- **LinkedIn**: [Eugene Mark Korku Barasu](https://www.linkedin.com/in/eugene-mark-korku-barasu-5094a7220)
- **GitHub**: [Mark-Eugene-Barasu](https://github.com/Mark-Eugene-Barasu)
- **Location**: Umtata, South Africa (Open to remote & relocation)

---

© 2025 Eugene Mark Korku Barasu. All rights reserved.
