from django.db import models

class ContactMessage(models.Model):
    name       = models.CharField(max_length=100)
    email      = models.EmailField()
    message    = models.TextField()
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    is_read    = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} <{self.email}> — {self.created_at:%Y-%m-%d %H:%M}"
