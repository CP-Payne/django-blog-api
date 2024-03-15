from django.urls import path
from . import views

urlpatterns = [
    path("all", views.UserNotificationsView.as_view(), name="get-notifications"),
    path(
        "read/<int:notification_id>",
        views.MarkNotificationAsReadView.as_view(),
        name="read-notification",
    ),
]
