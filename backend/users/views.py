from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

from .serializers import (
    UserSerializer, RegisterSerializer, LoginSerializer,
    ProfileUpdateSerializer, PasswordChangeSerializer
)

User = get_user_model()


def get_tokens_for_user(user):
    """Generate JWT refresh and access tokens for a user."""
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class RegisterView(APIView):
    """
    POST /api/auth/register/

    Register a new user with role-based access.
    Available roles: USER, RECRUITER (ADMIN cannot self-register).
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            tokens = get_tokens_for_user(user)

            return Response({
                'detail': 'Account created successfully. Welcome to the portfolio!',
                'user': UserSerializer(user).data,
                'tokens': tokens
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """
    POST /api/auth/login/

    Authenticate user and return JWT tokens.
    Includes user role for frontend permission handling.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            tokens = get_tokens_for_user(user)

            return Response({
                'detail': f'Welcome back, {user.username}!',
                'user': UserSerializer(user).data,
                'tokens': tokens
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    """
    POST /api/auth/logout/

    Blacklist refresh token to prevent reuse.
    Requires valid refresh token in request body.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            if not refresh_token:
                return Response(
                    {'detail': 'Refresh token is required.'},
                    status=status.HTTP_400_BAD_REQUEST
                )

            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(
                {'detail': 'Successfully logged out.'},
                status=status.HTTP_200_OK
            )
        except Exception:
            return Response(
                {'detail': 'Invalid or expired token.'},
                status=status.HTTP_400_BAD_REQUEST
            )


class ProfileView(APIView):
    """
    GET  /api/auth/me/     - Get current user profile
    PUT  /api/auth/me/     - Update current user profile
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Return authenticated user's profile data."""
        serializer = UserSerializer(request.user)
        return Response({
            'user': serializer.data,
            'permissions': {
                'is_admin': request.user.is_admin,
                'is_recruiter': request.user.is_recruiter,
                'can_view_admin': request.user.is_admin,
                'can_view_analytics': request.user.is_admin,
                'can_view_all_messages': request.user.is_admin,
            }
        })

    def put(self, request):
        """Update authenticated user's profile."""
        serializer = ProfileUpdateSerializer(
            request.user,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response({
                'detail': 'Profile updated successfully.',
                'user': UserSerializer(request.user).data
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordChangeView(APIView):
    """
    POST /api/auth/password-change/

    Change authenticated user's password.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PasswordChangeSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = request.user

        # Verify old password
        if not user.check_password(serializer.validated_data['old_password']):
            return Response(
                {'old_password': ['Current password is incorrect.']},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Set new password
        user.set_password(serializer.validated_data['new_password'])
        user.save()

        # Generate new tokens since password changed
        tokens = get_tokens_for_user(user)

        return Response({
            'detail': 'Password changed successfully.',
            'tokens': tokens
        })


class UserListView(APIView):
    """
    GET /api/users/

    List all registered users. ADMIN only.
    Used for admin dashboard user management.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Role-based access control
        if not request.user.is_admin:
            return Response(
                {'detail': 'You do not have permission to view all users. Admin access required.'},
                status=status.HTTP_403_FORBIDDEN
            )

        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response({
            'count': users.count(),
            'users': serializer.data
        })


class TokenRefreshView(APIView):
    """
    POST /api/auth/refresh/

    Refresh access token using refresh token.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        from rest_framework_simplejwt.serializers import TokenRefreshSerializer

        serializer = TokenRefreshSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
