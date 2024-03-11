from rest_framework import serializers
from .models import Tag, Blog, BlogTag, Category

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['tag_name']


# class BlogSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField()
#     snippet = serializers.CharField()
#     author_name = serializers.CharField(source='user.first_name')
#     author_surname= serializers.CharField(source='user.last_name')
#     content = serializers.CharField()
#     category = serializers.CharField(source='category.category_name')
#     created_at = serializers.DateTimeField()
#     is_public = serializers.BooleanField()
#     tags = serializers.SerializerMethodField()

    

    
#     def get_tags(self, obj):
#         blog_tags = BlogTag.objects.filter(blog=obj)
#         # Extract the tag names through the tag relationship
#         tags = [blog_tag.tag.tag_name for blog_tag in blog_tags]  # Correct way to access tag_name
#         return tags

# class BlogSerializer(serializers.ModelSerializer):
#     tags = serializers.SerializerMethodField()
#     name = serializers.CharField(source='user.first_name')
#     surname = serializers.CharField(source='user.last_name')
#     category_name = serializers.CharField(source='category.category_name')

#     class Meta:
#         model = Blog
#         fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'name', 'surname', 'category_name', 'tags', 'is_public']
#         read_only_fields = ['created_at', 'updated_at', 'name', 'surname']
        
#     def get_tags(self, obj):
#         blog_tags = BlogTag.objects.filter(blog=obj)
#         # Extract the tag names through the tag relationship
#         tags = [blog_tag.tag.tag_name for blog_tag in blog_tags]  # Correct way to access tag_name
#         return tags

class BlogSerializer(serializers.ModelSerializer):
    tags = serializers.ListField(child=serializers.CharField(), write_only=True, required=False)
    tags_display = serializers.SerializerMethodField(read_only=True)  # For displaying tags
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), required=False, allow_null=True)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'snippet', 'content', 'created_at', 'updated_at', 'user', 'category', 'is_public', 'tags', 'tags_display']
        read_only_fields = ['created_at', 'updated_at', 'user', 'tags_display']

    def get_tags_display(self, instance):
        blog_tags = BlogTag.objects.filter(blog=instance)
        # Extract the tag names through the tag relationship
        tags = [blog_tag.tag.tag_name for blog_tag in blog_tags]  # Correct way to access tag_name
        return tags

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        blog = Blog.objects.create(**validated_data)
        blog.save()
        for tag_name in tags_data:
            tag, created = Tag.objects.get_or_create(tag_name=tag_name)
            BlogTag.objects.create(blog=blog, tag=tag)
        return blog

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', None)
        if tags_data is not None:
            # Clear existing tags
            instance.blogtag_set.all().delete()
            for tag_name in tags_data:
                tag, created = Tag.objects.get_or_create(tag_name=tag_name)
                BlogTag.objects.create(blog=instance, tag=tag)
        
        # Update other fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        return instance