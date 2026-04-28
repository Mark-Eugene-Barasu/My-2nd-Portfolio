from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.db.models import Count
from .models import PageView
from .serializers import PageViewSerializer


class TrackPageView(APIView):
    """
    POST /api/analytics/track/ — records a page visit
    Captures user role from authenticated requests for segmentation.
    """
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request):
        serializer = PageViewSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        ip = (
            request.META.get('HTTP_X_FORWARDED_FOR', '').split(',')[0].strip()
            or request.META.get('REMOTE_ADDR')
        )

        # Determine user role for analytics segmentation
        user_role = ''
        if request.user.is_authenticated:
            user_role = request.user.role

        serializer.save(
            ip_address=ip,
            user_agent=request.META.get('HTTP_USER_AGENT', ''),
            referrer=request.META.get('HTTP_REFERER', None),
            user_role=user_role,
        )
        return Response({"detail": "tracked"}, status=status.HTTP_201_CREATED)


class PageViewStats(APIView):
    """
    GET /api/analytics/stats/ — returns view counts per page
    ADMIN only — returns full analytics with role breakdown.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if not request.user.is_admin:
            return Response(
                {"detail": "Admin access required to view analytics."},
                status=status.HTTP_403_FORBIDDEN
            )

        stats = (
            PageView.objects
            .values('page')
            .annotate(views=Count('id'))
            .order_by('-views')
        )
        total = PageView.objects.count()

        # Role-based segmentation
        by_role = (
            PageView.objects
            .values('user_role')
            .annotate(views=Count('id'))
            .order_by('-views')
        )

        return Response({
            "total_views": total,
            "by_page": list(stats),
            "by_role": list(by_role),
        })
