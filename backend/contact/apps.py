"""
Contact App Configuration

Django app configuration for the contact form module.
"""

from django.apps import AppConfig


class ContactConfig(AppConfig):
    """Configuration for the contact application."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contact'
    verbose_name = 'Contact Messages'
