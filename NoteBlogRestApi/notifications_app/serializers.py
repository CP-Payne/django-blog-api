from rest_framework import serializers
from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    user_fullname = serializers.SerializerMethodField()
    blog_title = serializers.SerializerMethodField()
    comment_preview = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = [
            "id",
            "user",
            "blog",
            "comment",
            "message",
            "created_at",
            "read_at",
            "user_fullname",
            "blog_title",
            "comment_preview",
        ]
        read_only_fields = ["id", "created_at", "read_at"]

    def get_user_fullname(self, obj):
        # Assuming the User model has first_name and last_name fields
        if obj.comment:
            # If comment is not null, the notification is for author, return the full name of user who made the comment
            return f"{obj.comment.user.first_name} {obj.comment.user.last_name}"
        else:
            # If comment is null, notification is for user about new blog, return author's full name
            return f"{obj.blog.user.first_name} {obj.blog.user.last_name}"

    def get_blog_title(self, obj):
        # Return the blog title if the notification is associated with a blog
        # Currently, all notifcations are related to a blog
        return obj.blog.title if obj.blog else None

    def get_comment_preview(self, obj):
        # Return the first 50 characters of the comment if the notification is associated with a comment
        return obj.comment.message[:50] + "..." if obj.comment else None
