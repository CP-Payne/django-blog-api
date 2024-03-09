from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=255)
    is_active = models.BooleanField(default=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    unsubscribed_at = models.DateTimeField(null=True, blank=True)

    def is_subscribed(self):
        return self.is_active and self.unsubscribed_at is None