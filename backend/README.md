# Portfolio Backend API

Django REST API powering the portfolio website with role-based authentication, contact forms, and analytics.

## Setup

1. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

2. **Configure environment**:
   Create a `.env` file in `backend/` with:

   ```
   SECRET_KEY=your-secret-key
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   DB_NAME=portfolio_db
   DB_USER=postgres
   DB_PASSWORD=your-password
   DB_HOST=localhost
   DB_PORT=5432
   CORS_ALLOWED_ORIGINS=http://localhost:8000,http://127.0.0.1:5500
   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_HOST_USER=your-email@gmail.com
   EMAIL_HOST_PASSWORD=your-app-password
   EMAIL_RECEIVER=your-receiver@gmail.com
   ```

3. **Run migrations**:

   ```bash
   python manage.py migrate
   ```

4. **Create superuser**:

   ```bash
   python manage.py createsuperuser
   ```

5. **Run server**:
   ```bash
   python manage.py runserver
   ```

## API Overview

| App         | Endpoints          | Purpose                      |
| ----------- | ------------------ | ---------------------------- |
| `users`     | `/api/auth/*`      | JWT authentication, profiles |
| `contact`   | `/api/contact/`    | Contact form submissions     |
| `analytics` | `/api/analytics/*` | Page view tracking           |

## Apps

### users

Custom User model with role field (ADMIN, RECRUITER, USER). Provides:

- Registration & login with JWT
- Profile management
- Password change
- Admin-only user listing

### contact

Stores contact form submissions. Features:

- Public submission (no auth required)
- Admin-only message listing
- User association for authenticated submitters
- Email notification on submission

### analytics

Tracks page views for portfolio analytics. Features:

- Public tracking endpoint
- Role segmentation (captures user role if authenticated)
- Admin-only statistics endpoint with page/role breakdowns

## Role-Based Permissions

| Role      | Can View Admin | Can View Analytics | Can View All Messages |
| --------- | -------------- | ------------------ | --------------------- |
| ADMIN     | Yes            | Yes                | Yes                   |
| RECRUITER | No             | No                 | Own messages only     |
| USER      | No             | No                 | Own messages only     |

## Management Commands

```bash
# Create admin user
python manage.py createsuperuser

# Run development server
python manage.py runserver

# Run tests (when added)
python manage.py test
```
