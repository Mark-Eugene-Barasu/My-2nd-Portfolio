from django.contrib import admin
from .models import PageView

@admin.register(PageView)
class PageViewAdmin(admin.ModelAdmin):
    list_display  = ['page', 'ip_address', 'visited_at']
    list_filter   = ['page', 'visited_at']
    search_fields = ['page', 'ip_address']
    readonly_fields = ['page', 'ip_address', 'user_agent', 'referrer', 'visited_at']

    def has_add_permission(self, request):
        return False
