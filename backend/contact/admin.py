"""
Contact Admin Configuration

Manages ContactMessage entries in the Django admin panel.
Messages are read-only to preserve submission integrity.
"""

from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """
    Admin interface for contact form submissions.
    Provides filtering by read status and search by name/email.
    """
    list_display = ['name', 'email', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['name', 'email', 'message', 'ip_address', 'created_at']
    ordering = ['-created_at']

    def has_add_permission(self, request):
        """Prevent manual creation of contact messages."""
        return False
