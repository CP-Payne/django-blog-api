from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    profession = models.CharField(max_length=100, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

