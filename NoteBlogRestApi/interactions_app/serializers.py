from rest_framework import serializers
from .models import Like, Comment
from django.contrib.auth.models import User
from blog_app.models import Blog


class CommentSerializer(serializers.ModelSerializer):
    #user = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    user_fullname = serializers.SerializerMethodField()
    blog = serializers.PrimaryKeyRelatedField(queryset=Blog.objects.all(), required=True)
    class Meta:
        model = Comment
        fields = ['id','blog', 'message', 'user_fullname', 'created_at']
        read_only_fields = ['id','user', 'created_at']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)

    def get_user_fullname(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"