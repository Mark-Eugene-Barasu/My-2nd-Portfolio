"""
Contact App Tests

Tests for contact form submission and admin-only message listing.
"""

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import ContactMessage

User = get_user_model()


class ContactViewTests(APITestCase):
    """Tests for contact form endpoint."""

    def setUp(self):
        self.url = '/api/contact/'
        self.valid_payload = {
            'name': 'Jane Recruiter',
            'email': 'jane@techcorp.com',
            'message': 'I am impressed by your Django REST API project. Are you open to full-time roles in Cape Town?'
        }

    def test_contact_submission_unauth(self):
        """Unauthenticated should get 401."""
        response = self.client.post(
            self.url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_contact_submission_auth(self):
        """Authenticated users should submit successfully."""
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='TestPass123!',
            role='USER'
        )
        self.client.force_authenticate(user=user)
        response = self.client.post(
            self.url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ContactMessage.objects.count(), 1)
        msg = ContactMessage.objects.first()
        self.assertEqual(msg.name, 'Jane Recruiter')
        self.assertEqual(msg.user, user)
        self.assertFalse(msg.is_read)

    def test_contact_short_message_rejected(self):
        """Messages under 10 chars rejected."""
        payload = self.valid_payload.copy()
        payload['message'] = 'Hi'
        user = User.objects.create_user(
            username='short', password='pass', role='USER')
        self.client.force_authenticate(user=user)
        response = self.client.post(self.url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_contact_short_name_rejected(self):
        """Names under 2 chars rejected."""
        payload = self.valid_payload.copy()
        payload['name'] = 'J'
        user = User.objects.create_user(
            username='shortname', password='pass', role='USER')
        self.client.force_authenticate(user=user)
        response = self.client.post(self.url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_contact_list_admin_only(self):
        """Only admins see all messages."""
        admin = User.objects.create_user(
            username='admin', email='admin@test.com',
            password='AdminPass123!', role='ADMIN'
        )
        self.client.force_authenticate(user=admin)
        ContactMessage.objects.create(
            name='Test', email='test@test.com', message='Test message'
        )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_contact_list_unauth(self):
        """Unauthenticated get 401."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_contact_list_non_admin(self):
        """Non-admin gets 403."""
        user = User.objects.create_user(
            username='user', password='pass', role='USER')
        self.client.force_authenticate(user=user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
