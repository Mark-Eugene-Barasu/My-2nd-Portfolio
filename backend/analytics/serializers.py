from rest_framework import serializers
from .models import PageView

class PageViewSerializer(serializers.ModelSerializer):
    class Meta:
        model  = PageView
        fields = ['id', 'page', 'visited_at']
        read_only_fields = ['id', 'visited_at']
