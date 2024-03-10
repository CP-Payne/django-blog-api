from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Blog, BlogTag
from .serializer import BlogSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def view_posts(request):
    all_blogs = Blog.objects.select_related('user', 'category').prefetch_related("blogtag_set__tag").filter(is_public=True)
    serializer = BlogSerializer(all_blogs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def blog_details(request, blog_id):
    blog = Blog.objects.select_related('user', 'category').prefetch_related("blogtag_set__tag").get(pk=blog_id)
    serializer = BlogSerializer(blog)
    return Response(serializer.data)
