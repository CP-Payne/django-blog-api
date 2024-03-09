from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from interactions_app.models import Comment
from blog_app.models import Blog

# Create your models here.
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read_at = models.DateTimeField(null=True, blank=True)

    def is_read(self):
        return self.read_at is not None