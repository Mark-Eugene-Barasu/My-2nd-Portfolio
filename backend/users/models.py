from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom user model with role-based access control.

    Roles:
        ADMIN     - Full access to admin panel, analytics, all contact messages
        RECRUITER - Can view public portfolio, submit contact, view own messages
        USER      - Standard registered user, limited access
    """

    ROLE_CHOICES = [
        ('ADMIN', 'Admin'),
        ('RECRUITER', 'Recruiter'),
        ('USER', 'User'),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='USER',
        help_text='Determines what the user can see and do in the portfolio'
    )

    # Track AI usage for productivity showcase
    ai_tools_used = models.JSONField(
        default=list,
        blank=True,
        help_text='List of AI tools this user leverages'
    )

    # Profile fields for recruiters/employers
    company = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_joined']
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f"{self.username} ({self.role})"

    @property
    def is_admin(self):
        """Check if user has admin privileges."""
        return self.role == 'ADMIN' or self.is_superuser or self.is_staff

    @property
    def is_recruiter(self):
        """Check if user is a recruiter."""
        return self.role == 'RECRUITER'

    def get_full_name_display(self):
        """Return formatted full name or username fallback."""
        return f"{self.first_name} {self.last_name}".strip() or self.username
