"""
Portfolio API URL Configuration.

Root endpoints:
    /admin/          - Django admin dashboard (user management, analytics)
    /api/auth/       - Authentication (register, login, logout, profile)
    /api/users/      - User management (admin-only)
    /api/contact/    - Contact form submissions
    /api/analytics/  - Page view tracking and statistics

For recruiters:
    All endpoints return JSON. Authentication uses JWT Bearer tokens.
    See docs/api-reference.md for detailed usage examples.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include(('users.urls', 'users'), namespace='users')),
    path('api/contact/', include(('contact.urls', 'contact'), namespace='contact')),
    path('api/analytics/', include(('analytics.urls',
         'analytics'), namespace='analytics')),
]
