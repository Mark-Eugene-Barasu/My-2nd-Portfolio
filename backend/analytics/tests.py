"""
Analytics App Tests

Tests for page view tracking and statistics.
"""

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import PageView

User = get_user_model()


class TrackPageViewTests(APITestCase):
    """Tests for page view tracking endpoint."""

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('analytics:track')
        self.valid_payload = {
            'page': '/projects/django_project.html'
        }

    def test_track_valid_page_public(self):
        """Anonymous users should track page views."""
        response = self.client.post(
            self.url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PageView.objects.count(), 1)
        view = PageView.objects.first()
        self.assertEqual(view.page, '/projects/django_project.html')
        self.assertEqual(view.user_role, '')

    def test_track_missing_page(self):
        """Missing page should be rejected."""
        response = self.client.post(self.url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_track_authenticated_user_role(self):
        """Authenticated users should have role captured."""
        user = User.objects.create_user(
            username='roleuser',
            email='role@test.com',
            password='TestPass123!',
            role='RECRUITER'
        )
        self.client.force_authenticate(user=user)
        response = self.client.post(
            self.url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PageView.objects.first().user_role, 'RECRUITER')


class PageViewStatsTests(APITestCase):
    """Tests for analytics statistics endpoint."""

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('analytics:stats')
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
        """Admin should get full statistics."""
        self.client.force_authenticate(user=self.admin)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('total_views', response.data)
        self.assertIn('by_page', response.data)
        self.assertIn('by_role', response.data)
        self.assertEqual(response.data['total_views'], 3)

    def test_non_admin_forbidden(self):
        """Non-admins should get 403."""
        self.client.force_authenticate(user=self.recruiter)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_stats_aggregation(self):
        """Verify stats aggregation logic."""
        self.client.force_authenticate(user=self.admin)
        response = self.client.get(self.url)
        by_page = {item['page']: item['views']
                   for item in response.data['by_page']}
        self.assertEqual(by_page['/projects/'], 2)
        self.assertEqual(by_page['/about.html'], 1)
