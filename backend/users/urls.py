from django.urls import path
from .views import (
    RegisterView, LoginView, LogoutView, ProfileView,
    PasswordChangeView, UserListView, TokenRefreshView
)

urlpatterns = [
    # Authentication endpoints
    path('register/', RegisterView.as_view(), name='auth-register'),
    path('login/', LoginView.as_view(), name='auth-login'),
    path('logout/', LogoutView.as_view(), name='auth-logout'),
    path('refresh/', TokenRefreshView.as_view(), name='auth-refresh'),

    # User profile endpoints
    path('me/', ProfileView.as_view(), name='auth-profile'),
    path('password-change/', PasswordChangeView.as_view(),
         name='auth-password-change'),

    # Admin-only endpoints
    path('users/', UserListView.as_view(), name='user-list'),
]
