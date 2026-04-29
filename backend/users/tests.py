"""
Users App Tests

Comprehensive test coverage for:
    - User registration (role validation, password strength)
    - User login (credentials, inactive accounts)
    - Profile access (authenticated only)
    - Admin-only endpoints (role-based access control)
"""

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterViewTests(APITestCase):
    """Tests for user registration endpoint."""

    def setUp(self):
        self.url = reverse('users:auth-register')
        self.valid_payload = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'StrongPass123!',
            'password_confirm': 'StrongPass123!',
            'first_name': 'Test',
            'last_name': 'User',
            'role': 'USER'
        }

    def test_register_valid_user(self):
        """Should create user and return tokens."""
        response = self.client.post(
            self.url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('tokens', response.data)
        self.assertIn('access', response.data['tokens'])
        self.assertEqual(User.objects.count(), 1)

    def test_register_password_mismatch(self):
        """Should reject when passwords don't match."""
        payload = self.valid_payload.copy()
        payload['password_confirm'] = 'DifferentPass123!'
        response = self.client.post(self.url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_admin_role_blocked(self):
        """Should prevent self-registration as ADMIN."""
        payload = self.valid_payload.copy()
        payload['role'] = 'ADMIN'
        response = self.client.post(self.url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_register_weak_password(self):
        """Should reject weak passwords."""
        payload = self.valid_payload.copy()
        payload['password'] = '123'
        payload['password_confirm'] = '123'
        response = self.client.post(self.url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class LoginViewTests(APITestCase):
    """Tests for user login endpoint."""

    def setUp(self):
        self.url = reverse('users:auth-login')
        self.user = User.objects.create_user(
            username='logintest',
            email='login@test.com',
            password='TestPass123!',
            role='USER'
        )

    def test_login_valid_credentials(self):
        """Should return tokens for valid credentials."""
        response = self.client.post(self.url, {
            'username': 'logintest',
            'password': 'TestPass123!'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('tokens', response.data)

    def test_login_invalid_password(self):
        """Should reject incorrect password."""
        response = self.client.post(self.url, {
            'username': 'logintest',
            'password': 'WrongPass123!'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_inactive_user(self):
        """Should reject login for deactivated accounts."""
        self.user.is_active = False
        self.user.save()
        response = self.client.post(self.url, {
            'username': 'logintest',
            'password': 'TestPass123!'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class ProfileViewTests(APITestCase):
    """Tests for profile endpoint."""

    def setUp(self):
        self.url = reverse('users:auth-profile')
        self.user = User.objects.create_user(
            username='profiletest',
            email='profile@test.com',
            password='TestPass123!',
            role='RECRUITER'
        )
        self.client.force_authenticate(user=self.user)

    def test_get_profile_authenticated(self):
        """Should return user profile when authenticated."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user']['username'], 'profiletest')

    def test_get_profile_unauthenticated(self):
        """Should reject unauthenticated requests."""
        self.client.force_authenticate(user=None)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class UserListViewTests(APITestCase):
    """Tests for admin-only user listing."""

    def setUp(self):
        self.url = reverse('users:user-list')
        self.admin = User.objects.create_user(
            username='admin',
            email='admin@test.com',
            password='AdminPass123!',
            role='ADMIN'
        )
        self.recruiter = User.objects.create_user(
            username='recruiter',
            email='recruiter@test.com',
            password='RecPass123!',
            role='RECRUITER'
        )

    def test_admin_can_list_users(self):
        """ADMIN should see all users."""
        self.client.force_authenticate(user=self.admin)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)

    def test_recruiter_cannot_list_users(self):
        """RECRUITER should get 403."""
        self.client.force_authenticate(user=self.recruiter)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
