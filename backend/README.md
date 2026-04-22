# Portfolio Backend — Django REST API

Full backend for Eugene Mark Korku Barasu's portfolio website.

## Tech Stack
- Python 3.11 + Django 5
- Django REST Framework
- PostgreSQL
- django-cors-headers
- Gunicorn + WhiteNoise (production)

## Features
| Endpoint | Method | Description |
|---|---|---|
| `/api/contact/` | POST | Save contact message + send email |
| `/api/analytics/track/` | POST | Record a page view |
| `/api/analytics/stats/` | GET | Get view counts per page |
| `/admin/` | GET | Django admin dashboard |

---

## Setup

### 1. Prerequisites
- Python 3.11+
- PostgreSQL installed and running
- A Gmail account with an [App Password](https://myaccount.google.com/apppasswords)

### 2. Create the PostgreSQL database
```sql
CREATE DATABASE portfolio_db;
```

### 3. Configure environment variables
Edit `.env` and fill in your values:
```
SECRET_KEY=your-django-secret-key
DB_PASSWORD=your-postgres-password
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-gmail-app-password
EMAIL_RECEIVER=your-email@gmail.com
```

### 4. Run setup (Windows)
```bash
cd backend
setup.bat
```

### 5. Start the server
```bash
venv\Scripts\activate
python manage.py runserver
```

Server runs at: http://127.0.0.1:8000

---

## Django Admin
Visit http://127.0.0.1:8000/admin/ to:
- Read all contact messages
- Mark messages as read
- View page analytics

---

## Production Deployment (Render / Railway)
1. Set `DEBUG=False` in `.env`
2. Add your domain to `ALLOWED_HOSTS`
3. Add your frontend URL to `CORS_ALLOWED_ORIGINS`
4. Run `python manage.py collectstatic`
5. Use `gunicorn portfolio_api.wsgi` as the start command

---

## API Usage Examples

### Send a contact message
```bash
curl -X POST http://127.0.0.1:8000/api/contact/ \
  -H "Content-Type: application/json" \
  -d '{"name":"John","email":"john@example.com","message":"Hello Eugene!"}'
```

### Track a page view
```bash
curl -X POST http://127.0.0.1:8000/api/analytics/track/ \
  -H "Content-Type: application/json" \
  -d '{"page":"home"}'
```

### Get analytics stats
```bash
curl http://127.0.0.1:8000/api/analytics/stats/
```
