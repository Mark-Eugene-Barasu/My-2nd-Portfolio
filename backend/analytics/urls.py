"""
Analytics URL Configuration

Endpoints:
    /api/analytics/track/  — POST to record a page visit
    /api/analytics/stats/  — GET view statistics (admin only)
"""

from django.urls import path
from .views import TrackPageView, PageViewStats

urlpatterns = [
    path('track/', TrackPageView.as_view(), name='track'),
    path('stats/', PageViewStats.as_view(), name='stats'),
]
