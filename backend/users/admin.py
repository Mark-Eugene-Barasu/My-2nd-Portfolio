from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Custom admin configuration for User model.
    Provides role-based user management interface.
    """

    # Fields displayed in the user list page
    list_display = [
        'username', 'email', 'first_name', 'last_name',
        'role', 'company', 'is_active', 'date_joined'
    ]

    # Filters for the sidebar
    list_filter = ['role', 'is_active', 'is_staff', 'date_joined']

    # Searchable fields
    search_fields = ['username', 'email', 'first_name', 'last_name', 'company']

    # Default ordering
    ordering = ['-date_joined']

    # Fieldsets for add/change forms
    fieldsets = UserAdmin.fieldsets + (
        ('Portfolio Role', {
            'fields': ('role', 'company', 'title', 'ai_tools_used'),
            'description': 'Role-based access control for the portfolio website'
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Portfolio Role', {
            'fields': ('role', 'company', 'title'),
        }),
    )

    # Actions for bulk operations
    actions = ['make_admin', 'make_recruiter', 'make_user', 'deactivate_users']

    @admin.action(description='Make selected users ADMIN')
    def make_admin(self, request, queryset):
        """Bulk action to set role to ADMIN."""
        updated = queryset.update(role='ADMIN')
        self.message_user(request, f'{updated} user(s) promoted to Admin.')

    @admin.action(description='Make selected users RECRUITER')
    def make_recruiter(self, request, queryset):
        """Bulk action to set role to RECRUITER."""
        updated = queryset.update(role='RECRUITER')
        self.message_user(request, f'{updated} user(s) set to Recruiter.')

    @admin.action(description='Make selected users USER')
    def make_user(self, request, queryset):
        """Bulk action to set role to USER."""
        updated = queryset.update(role='USER')
        self.message_user(request, f'{updated} user(s) set to standard User.')

    @admin.action(description='Deactivate selected users')
    def deactivate_users(self, request, queryset):
        """Bulk action to deactivate users."""
        updated = queryset.update(is_active=False)
        self.message_user(request, f'{updated} user(s) deactivated.')
