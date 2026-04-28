"""
Analytics Admin Configuration

Manages PageView entries in the Django admin panel.
Page views are read-only to preserve analytics integrity.
"""

from django.contrib import admin
from .models import PageView


@admin.register(PageView)
class PageViewAdmin(admin.ModelAdmin):
    """
    Admin interface for page view analytics.
    Provides filtering by page and visit time.
    """
    list_display = ['page', 'ip_address', 'user_role', 'visited_at']
    list_filter = ['page', 'visited_at']
    search_fields = ['page', 'ip_address']
    readonly_fields = ['page', 'ip_address', 'user_agent',
                       'referrer', 'user_role', 'visited_at']

    def has_add_permission(self, request):
        """Prevent manual creation of page view records."""
        return False
