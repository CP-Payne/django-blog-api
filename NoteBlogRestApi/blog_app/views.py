from django.shortcuts import render
from rest_framework import generics, status, permissions
from .models import Blog
from .serializer import BlogSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, IsOwner


# @api_view(['GET'])
# def view_posts(request):
#     all_blogs = Blog.objects.select_related('user', 'category').prefetch_related("blogtag_set__tag").filter(is_public=True)
#     serializer = BlogSerializer(all_blogs, many=True)
#     return Response(serializer.data)

# @api_view(['GET'])
# def blog_details(request, blog_id):
#     blog = Blog.objects.select_related('user', 'category').prefetch_related("blogtag_set__tag").get(pk=blog_id)
#     serializer = BlogSerializer(blog)
#     return Response(serializer.data)

class BlogPostCreateUpdateRetrieveView(generics.GenericAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.request.method == "GET":
            permission_classes = []
        elif self.request.method == "PUT":
            permission_classes = [permissions.IsAuthenticated, IsOwner]
        else:
            permission_classes = [permissions.IsAuthenticated]
        return [permission() for permission in permission_classes]

    def get(self, request,*args, **kwargs):
        blog_id = kwargs.get('blog_id', '')

        if blog_id:
            try:
                blog = self.queryset.get(pk=blog_id)  # Use pk=blog_id to specify the lookup field
                serializer = BlogSerializer(blog)
                return Response(serializer.data)
            except Blog.DoesNotExist:
                return Response({'error': 'Blog not found.'}, status=status.HTTP_404_NOT_FOUND)
        else:
            blogs = Blog.objects.select_related('user', 'category').prefetch_related("blogtag_set__tag").filter(is_public=True)
            serializer = BlogSerializer(blogs, many=True)
            return Response(serializer.data)
                

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        # Attempt to get the blog instance to update
        try:
            blog = self.queryset.get(pk=kwargs.get('blog_id'))
        except Blog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # Use the serializer to update the blog
        serializer = self.get_serializer(blog, data=request.data)
        if serializer.is_valid():
            if request.user.is_authenticated:
                serializer.save(user=request.user)  # Set the user to the current user
                return Response(serializer.data)
            else:
                return Response({'error': 'You must be logged in to perform this action.'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if request.user.is_authenticated:

                serializer.save(user=request.user)  # Set the user to the current user
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'You must be logged in to perform this action.'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)