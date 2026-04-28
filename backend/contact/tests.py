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
        self.url = reverse('contact')
        self.valid_payload = {
            'name': 'Jane Recruiter',
            'email': 'jane@techcorp.com',
            'message': 'I am impressed by your Django REST API project. Are you open to full-time roles in Cape Town?'
        }

    def test_contact_submission_public(self):
        """Anyone should be able to submit contact form."""
        response = self.client.post(
            self.url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ContactMessage.objects.count(), 1)
        msg = ContactMessage.objects.first()
        self.assertEqual(msg.name, 'Jane Recruiter')
        self.assertFalse(msg.is_read)

    def test_contact_short_message_rejected(self):
        """Messages under 10 chars should be rejected."""
        payload = self.valid_payload.copy()
        payload['message'] = 'Hi'
        response = self.client.post(self.url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_contact_short_name_rejected(self):
        """Names under 2 chars should be rejected."""
        payload = self.valid_payload.copy()
        payload['name'] = 'J'
        response = self.client.post(self.url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_contact_list_admin_only(self):
        """Only admins should see all messages."""
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

    def test_contact_list_unauthorized(self):
        """Unauthenticated users should not see messages."""
        ContactMessage.objects.create(
            name='Test', email='test@test.com', message='Test message'
        )
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
