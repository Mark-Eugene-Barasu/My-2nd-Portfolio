"""
Contact URL Configuration

Endpoints:
    /api/contact/  — POST to submit, GET to list (admin only)
"""

from django.urls import path
from .views import ContactView

urlpatterns = [
    path('', ContactView.as_view(), name='contact'),
]
