# This is my second Portfolio website
## [Please check it out here](https://mark-eugene-barasu.github.io/My-2nd-Portfolio/)

It has a toggle effect
How the toggle button works
🌙 Moon icon = currently in light mode, click to go dark

☀️ Sun icon = currently in dark mode, click to go light

Drag anywhere — click and hold to drag it to any corner or position on screen

Position is saved — localStorage remembers where you dragged it, so it stays there across page loads

Theme is saved — localStorage also remembers your dark/light preference, so it persists as you navigate between pages

Touch support — works on mobile too

backend/
├── manage.py
├── requirements.txt
├── setup.bat          ← run this to install everything
├── .env               ← fill in your secrets
├── README.md
├── portfolio_api/     ← Django project
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── contact/           ← contact form app
│   ├── models.py      ← saves messages to PostgreSQL
│   ├── serializers.py ← validates input
│   ├── views.py       ← saves + sends email
│   ├── urls.py
│   └── admin.py       ← manage messages in admin panel
└── analytics/         ← page tracking app
    ├── models.py
    ├── serializers.py
    ├── views.py       ← track visits + stats
    ├── urls.py
    └── admin.py


cd backend
venv\Scripts\activate
python manage.py runserver
