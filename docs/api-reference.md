# API Reference

## Base URL

```
http://127.0.0.1:8000/api
```

## Authentication

All authenticated endpoints require a Bearer token in the Authorization header:

```
Authorization: Bearer <access_token>
```

## Endpoints

### Auth

| Method | Endpoint                 | Description              | Auth     |
| ------ | ------------------------ | ------------------------ | -------- |
| POST   | `/auth/register/`        | Register new account     | Public   |
| POST   | `/auth/login/`           | Login and get tokens     | Public   |
| POST   | `/auth/logout/`          | Blacklist refresh token  | Required |
| POST   | `/auth/refresh/`         | Refresh access token     | Public   |
| GET    | `/auth/me/`              | Get current user profile | Required |
| PUT    | `/auth/me/`              | Update profile           | Required |
| POST   | `/auth/password-change/` | Change password          | Required |

### Users

| Method | Endpoint  | Description    | Auth       |
| ------ | --------- | -------------- | ---------- |
| GET    | `/users/` | List all users | Admin only |

### Contact

| Method | Endpoint    | Description            | Auth       |
| ------ | ----------- | ---------------------- | ---------- |
| POST   | `/contact/` | Submit contact message | Public     |
| GET    | `/contact/` | List all messages      | Admin only |

### Analytics

| Method | Endpoint            | Description     | Auth       |
| ------ | ------------------- | --------------- | ---------- |
| POST   | `/analytics/track/` | Track page view | Public     |
| GET    | `/analytics/stats/` | Get view stats  | Admin only |

## Request/Response Examples

### Register

**Request:**

```json
POST /api/auth/register/
{
  "username": "recruiter1",
  "email": "recruiter@example.com",
  "password": "SecurePass123!",
  "password_confirm": "SecurePass123!",
  "role": "RECRUITER",
  "first_name": "Jane",
  "last_name": "Smith"
}
```

**Response:**

```json
{
  "detail": "Account created successfully. Welcome to the portfolio!",
  "user": {
    "id": 3,
    "username": "recruiter1",
    "email": "recruiter@example.com",
    "role": "RECRUITER"
  },
  "tokens": {
    "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
  }
}
```

### Login

**Request:**

```json
POST /api/auth/login/
{
  "username": "recruiter1",
  "password": "SecurePass123!"
}
```

### Track Page View

**Request:**

```json
POST /api/analytics/track/
{
  "page": "django_project"
}
```

**Response:**

```json
{
  "detail": "tracked"
}
```

### Get Analytics Stats (Admin Only)

**Response:**

```json
{
  "total_views": 152,
  "by_page": [
    { "page": "home", "views": 89 },
    { "page": "django_project", "views": 35 }
  ],
  "by_role": [
    { "user_role": "", "views": 120 },
    { "user_role": "ADMIN", "views": 20 },
    { "user_role": "RECRUITER", "views": 12 }
  ]
}
```
