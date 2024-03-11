from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from blog_app.models import Blog  # Adjust the import path as necessary
from history_app.models import PostHistory  # Adjust the import path as necessary

@receiver(post_save, sender=Blog)
def create_update_blog_history(sender, instance, created, **kwargs):
    description = 'Blog post created' if created else 'Blog post updated'
    PostHistory.objects.create(
        blog=instance,
        title=instance.title,
        content=instance.content,
        user=instance.user,
        description=description,
        created_at=timezone.now()  # Ensure this uses timezone-aware datetimes
    )