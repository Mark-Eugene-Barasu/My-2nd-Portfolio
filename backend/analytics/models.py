from django.db import models

class PageView(models.Model):
    page       = models.CharField(max_length=200)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)
    referrer   = models.URLField(blank=True, null=True)
    visited_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-visited_at']

    def __str__(self):
        return f"{self.page} — {self.visited_at:%Y-%m-%d %H:%M}"
