from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Subscription(models.Model):
    subscriber = models.ForeignKey(User, related_name='subscriptions', on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name='subscribers', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    unsubscribed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('subscriber', 'author')

    def is_subscribed(self):
        return self.is_active and self.unsubscribed_at is None