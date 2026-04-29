"""
Analytics App Tests

Tests for page view tracking and statistics.
"""

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import PageView

User = get_user_model()


class TrackPageViewTests(APITestCase):
    """Tests for page view tracking endpoint."""

    def setUp(self):
        self.url = '/api/analytics/track/'
        self.valid_payload = {
            'page': '/projects/django_project.html'
        }

    def test_track_valid_page_public(self):
        """Unauth should get 401."""
        response = self.client.post(
            self.url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_track_valid_page_auth(self):
        """Auth users track successfully."""
        user = User.objects.create_user(
            username='trackuser',
            email='track@test.com',
            password='TestPass123!',
            role='USER'
        )
        self.client.force_authenticate(user=user)
        response = self.client.post(
            self.url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PageView.objects.count(), 1)
        view = PageView.objects.first()
        self.assertEqual(view.page, '/projects/django_project.html')
        self.assertEqual(view.user_role, 'USER')

    def test_track_missing_page(self):
        """Missing page rejected."""
        user = User.objects.create_user(
            username='miss', password='pass', role='USER')
        self.client.force_authenticate(user=user)
        response = self.client.post(self.url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class PageViewStatsTests(APITestCase):
    """Tests for analytics statistics endpoint."""

    def setUp(self):
        self.url = '/api/analytics/stats/'
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

        # Create sample data
        PageView.objects.create(page='/projects/', user_role='ADMIN')
        PageView.objects.create(page='/about.html', user_role='RECRUITER')
        PageView.objects.create(page='/projects/', user_role='')

    def test_admin_can_view_stats(self):
        """Admin gets full statistics."""
        self.client.force_authenticate(user=self.admin)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('total_views', response.data)
        self.assertEqual(response.data['total_views'], 3)

    def test_non_admin_forbidden(self):
        """Non-admins get 403."""
        self.client.force_authenticate(user=self.recruiter)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_stats_unauth(self):
        """Unauth gets 401."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
