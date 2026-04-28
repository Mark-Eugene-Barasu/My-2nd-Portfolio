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



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),       # JWT authentication
    path('api/contact/', include('contact.urls')),  # Contact form
    path('api/analytics/', include('analytics.urls')),  # Analytics tracking
]
