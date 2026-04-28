from rest_framework import serializers
from .models import PageView


class PageViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageView
        fields = ['id', 'page', 'user_role', 'visited_at']
        read_only_fields = ['id', 'user_role', 'visited_at']
