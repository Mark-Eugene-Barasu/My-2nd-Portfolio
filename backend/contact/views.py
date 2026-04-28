from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage
from .serializers import ContactMessageSerializer


class ContactView(APIView):
    """
    POST /api/contact/ — Submit a contact message (public)
    GET  /api/contact/ — List messages (ADMIN only)
    """
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        ip = (
            request.META.get('HTTP_X_FORWARDED_FOR', '').split(',')[0].strip()
            or request.META.get('REMOTE_ADDR')
        )

        # Associate with authenticated user if available
        user = request.user if request.user.is_authenticated else None
        msg = serializer.save(ip_address=ip, user=user)

        try:
            send_mail(
                subject=f"Portfolio Contact: {msg.name}",
                message=(
                    f"Name:    {msg.name}\n"
                    f"Email:   {msg.email}\n"
                    f"Message:\n{msg.message}\n\n"
                    f"Sent at: {msg.created_at:%Y-%m-%d %H:%M} SAST"
                ),
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_RECEIVER],
                fail_silently=True,
            )
        except Exception:
            pass  # message is already saved to DB

        return Response(
            {"detail": "Message received! I'll get back to you soon."},
            status=status.HTTP_201_CREATED
        )

    def get(self, request):
        """
        List all contact messages. Restricted to ADMIN users.
        """
        if not request.user.is_authenticated or not request.user.is_admin:
            return Response(
                {"detail": "Admin access required to view messages."},
                status=status.HTTP_403_FORBIDDEN
            )

        messages = ContactMessage.objects.all().order_by('-created_at')
        serializer = ContactMessageSerializer(messages, many=True)
        return Response({
            "count": messages.count(),
            "messages": serializer.data
        })
