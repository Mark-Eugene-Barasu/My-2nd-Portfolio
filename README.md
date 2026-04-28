# Eugene Mark Korku Barasu — Full-Stack Portfolio

**Live Site**: [https://mark-eugene-barasu.github.io/My-2nd-Portfolio/](https://mark-eugene-barasu.github.io/My-2nd-Portfolio/)

A production-ready portfolio showcasing three full technology stacks: Python/Django, MERN/NextJS, and Java Spring Boot — with role-based authentication, analytics, and AI-augmented development.

## Features

- **Enterprise Projects**: Django REST API, NextJS Ecommerce, Spring Boot CRM
- **Role-Based Access**: ADMIN, RECRUITER, and USER roles with JWT authentication
- **AI Augmentation**: Built with ChatGPT, Claude, and Amazon Q assistance
- **Dark Mode**: Persistent theme toggle with localStorage
- **Analytics**: Page view tracking with role-based segmentation
- **Contact Form**: Backend-connected with admin-only message viewing

## Architecture

```
Frontend (HTML/CSS/JS)  ←→  Django REST API  ←→  PostgreSQL
     ↓                           ↓
  Auth.js                   JWT + Roles
  Dark Mode                 Analytics
```

## Quick Start

### Frontend

Open `index.html` in a browser or serve with any static file server.

### Backend

```bash
cd backend
# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Create .env file (see .env.example)
# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start server
python manage.py runserver
```

## Documentation

- [User Guide](docs/user-guide.md) — How to use the portfolio
- [Technical Specification](docs/tech-spec.md) — Architecture and security model
- [API Reference](docs/api-reference.md) — Endpoint documentation

## Technology Stack

| Layer    | Technologies                          |
| -------- | ------------------------------------- |
| Frontend | HTML5, CSS3, JavaScript, Font Awesome |
| Backend  | Python, Django, Django REST Framework |
| Auth     | JWT (djangorestframework-simplejwt)   |
| Database | PostgreSQL                            |
| DevOps   | WhiteNoise, Gunicorn, GitHub Pages    |

## AI Tools Used

- **ChatGPT**: Architecture design, debugging
- **Claude**: Code review, documentation
- **Amazon Q**: AWS patterns, security validation

> All AI-generated code is reviewed, tested, and understood before deployment.

## Contact

- Email: [mark0630227248@gmail.com](mailto:mark0630227248@gmail.com)
- LinkedIn: [Eugene Mark Korku Barasu](https://www.linkedin.com/in/eugene-mark-korku-barasu-5094a7220)
- GitHub: [Mark-Eugene-Barasu](https://github.com/Mark-Eugene-Barasu)

---

© 2024 Eugene Mark Korku Barasu. All rights reserved. | Umtata, South Africa
