from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage
from .serializers import ContactMessageSerializer

class ContactView(APIView):

    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        ip = (
            request.META.get('HTTP_X_FORWARDED_FOR', '').split(',')[0].strip()
            or request.META.get('REMOTE_ADDR')
        )
        msg = serializer.save(ip_address=ip)

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
