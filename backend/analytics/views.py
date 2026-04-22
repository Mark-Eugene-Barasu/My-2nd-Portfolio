from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count
from .models import PageView
from .serializers import PageViewSerializer

class TrackPageView(APIView):
    """POST /api/analytics/track/  — records a page visit"""

    def post(self, request):
        serializer = PageViewSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        ip = (
            request.META.get('HTTP_X_FORWARDED_FOR', '').split(',')[0].strip()
            or request.META.get('REMOTE_ADDR')
        )
        serializer.save(
            ip_address=ip,
            user_agent=request.META.get('HTTP_USER_AGENT', ''),
            referrer=request.META.get('HTTP_REFERER', None),
        )
        return Response({"detail": "tracked"}, status=status.HTTP_201_CREATED)


class PageViewStats(APIView):
    """GET /api/analytics/stats/  — returns view counts per page"""

    def get(self, request):
        stats = (
            PageView.objects
            .values('page')
            .annotate(views=Count('id'))
            .order_by('-views')
        )
        total = PageView.objects.count()
        return Response({"total_views": total, "by_page": list(stats)})
