from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Notification
from .serializers import NotificationSerializer
from django.utils import timezone


class UserNotificationsView(APIView):
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):
        notifications = Notification.objects.filter(user=request.user)
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)


class MarkNotificationAsReadView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, notification_id):
        notification = Notification.objects.filter(
            id=notification_id, user=request.user
        ).first()
        if notification:
            if notification.read_at is None:
                notification.read_at = timezone.now()
                notification.save()
            return Response({"status": "Notification marked as read"})

        return Response({"error": "Notification not found"}, status=404)
