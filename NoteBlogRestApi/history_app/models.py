from django.db import models
from django.contrib.auth.models import User
from blog_app.models import Blog
from django.utils import timezone

# Create your models here.
class PostHistory(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(default="")

    def __str__(self):
        return f'History for {self.blog.title} at {self.created_at}'