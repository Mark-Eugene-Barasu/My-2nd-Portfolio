# Technical Specification

## Architecture Overview

```
┌─────────────────┐      ┌──────────────────┐      ┌─────────────────┐
│   Frontend      │      │   Django REST    │      │   PostgreSQL    │
│   (HTML/CSS/JS) │◄────►│   API Backend    │◄────►│   Database      │
│                 │      │                  │      │                 │
│ - Dark mode     │      │ - JWT Auth       │      │ - Users         │
│ - Animations    │      │ - Role-based     │      │ - Contact msgs  │
│ - Auth.js       │      │   access         │      │ - Analytics     │
└─────────────────┘      └──────────────────┘      └─────────────────┘
```

## Technology Stack

### Frontend

- HTML5, CSS3, JavaScript (ES6+)
- Font Awesome 6.4.0
- Inter font family
- Custom dark mode with localStorage persistence
- GSAP animations (on about page)

### Backend

- Python 3.11
- Django 5.0.4
- Django REST Framework 3.15.1
- djangorestframework-simplejwt 5.3.1
- django-cors-headers 4.3.1
- PostgreSQL (via psycopg2-binary)
- WhiteNoise for static files
- Gunicorn for WSGI server

### DevOps

- Git / GitHub
- Environment-based configuration (django-environ)
- SMTP email backend

## Security Model

1. **Authentication**: JWT tokens with 60-minute access / 7-day refresh lifetime
2. **Authorization**: Role-based access control (ADMIN, RECRUITER, USER)
3. **CORS**: Whitelisted origins only
4. **Rate Limiting**: 30 requests/hour anonymous, 100/hour authenticated
5. **Token Blacklist**: Refresh tokens blacklisted on logout

## Database Schema

### users.User (Custom User)

- username, email, first_name, last_name
- role (ADMIN/RECRUITER/USER)
- company, title, ai_tools_used (JSON)

### contact.ContactMessage

- user (FK, nullable)
- name, email, message
- ip_address, is_read, created_at

### analytics.PageView

- page, ip_address, user_agent, referrer
- user_role, visited_at

## API Endpoints

See `api-reference.md` for full endpoint documentation.
