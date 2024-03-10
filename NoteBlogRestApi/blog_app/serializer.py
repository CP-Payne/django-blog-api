from rest_framework import serializers
from .models import Tag, Blog, BlogTag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['tag_name']


class BlogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    snippet = serializers.CharField()
    author_name = serializers.CharField(source='user.first_name')
    author_surname= serializers.CharField(source='user.last_name')
    content = serializers.CharField()
    category = serializers.CharField(source='category.category_name')
    created_at = serializers.DateTimeField()
    is_public = serializers.BooleanField()
    tags = serializers.SerializerMethodField()

    

    
    def get_tags(self, obj):
        blog_tags = BlogTag.objects.filter(blog=obj)
        # Extract the tag names through the tag relationship
        tags = [blog_tag.tag.tag_name for blog_tag in blog_tags]  # Correct way to access tag_name
        return tags

# class BlogSerializer(serializers.ModelSerializer):
#     tags = serializers.SerializerMethodField()
#     name = serializers.CharField(source='user.first_name')
#     surname = serializers.CharField(source='user.last_name')
#     category_name = serializers.CharField(source='category.category_name')

#     class Meta:
#         model = Blog
#         fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'name', 'surname', 'category_name', 'tags', 'is_public']

#     def get_tags(self, obj):
#         blog_tags = BlogTag.objects.filter(blog=obj)
#         # Extract the tag names through the tag relationship
#         tags = [blog_tag.tag.tag_name for blog_tag in blog_tags]  # Correct way to access tag_name
#         return tags