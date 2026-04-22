from django.urls import path
from .views import TrackPageView, PageViewStats

urlpatterns = [
    path('track/', TrackPageView.as_view(), name='track'),
    path('stats/', PageViewStats.as_view(), name='stats'),
]
