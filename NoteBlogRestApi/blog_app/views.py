from django.shortcuts import render
from django.http import JsonResponse
from .models import Blog, BlogTag

# Create your views here.
def view_posts(request):
    #blogs = Blog.objects.select_related('user', 'category').all()
    blogs = Blog.objects.select_related('user', 'category').prefetch_related("blogtag_set__tag").all()
    blogs_data = []
    for blog in blogs:
        
        blog_tags = BlogTag.objects.filter(blog=blog)

        tags = [blog_tag.tag.tag_name for blog_tag in blog_tags]
        blogs_data.append({
            'id': blog.id,
            'title': blog.title,
            'content': blog.content,
            'created_at': blog.created_at,
            'updated_at': blog.updated_at,
            'name': blog.user.first_name,  # Assuming 'username' is the field name in the User model
            'surname': blog.user.last_name,
            'category_name': blog.category.category_name,
            'tags': tags,
        })

    data = {
        "Blogs": blogs_data
    }
    return JsonResponse(data)


def blog_details(request, blog_id):
    blog = Blog.objects.select_related('user', 'category').prefetch_related("blogtag_set__tag").get(pk=blog_id)
    blog_data = []
    blog_tags = BlogTag.objects.filter(blog=blog)

    tags = [blog_tag.tag.tag_name for blog_tag in blog_tags]
    blog_data.append({
        'id': blog.id,
        'title': blog.title,
        'content': blog.content,
        'created_at': blog.created_at,
        'updated_at': blog.updated_at,
        'name': blog.user.first_name,  # Assuming 'username' is the field name in the User model
        'surname': blog.user.last_name,
        'category_name': blog.category.category_name,
        'tags': tags,
    })

    data = {
        "Blog": blog_data
    }
    return JsonResponse(data)