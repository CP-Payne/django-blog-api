from django.db.models.signals import post_save
from django.dispatch import receiver
from blog_app.models import Blog
from interactions_app.models import Comment
from notifications_app.models import Notification
from subscriptions_app.models import Subscription


@receiver(post_save, sender=Comment)
def create_comment_notification(instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.blog.user,
            blog=instance.blog,
            comment=instance,
            message=f"User {instance.user} commented on your blog post: {instance.blog.title}",
        )


@receiver(post_save, sender=Blog)
def create_blog_notification(instance, created, **kwargs):
    if created:
        # Get active subscriptions for the blog's author
        subscriptions = Subscription.objects.filter(
            author=instance.user, is_active=True
        )

        for subscription in subscriptions:
            Notification.objects.create(
                user=subscription.subscriber,
                blog=instance,
                message=f"Author {instance.user} has released a new blog post: {instance.title}",
            )
