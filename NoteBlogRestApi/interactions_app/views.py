from django.shortcuts import render
from rest_framework import generics
from .models import Comment, Like
from .serializers import CommentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from .permissions import IsOwnerOrReadOnly
from blog_app.models import Blog

# Create your views here.
class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    # def perform_create(self, serializer):
    #     blog_id = self.kwargs.get('blog_id')
    #     blog = Blog.objects.get(id=blog_id)  # Get the blog instance based on the URL parameter
    #     serializer.save(user=self.request.user, blog=blog)

class CommentsByBlogView(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        """
        This view returns a list of all comments for a blog
        as determined by the blog_id portion of the URL.
        """
        blog_id = self.kwargs['blog_id']
        return Comment.objects.filter(blog__id=blog_id)

# Implement Delete
class CommentDeleteView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]  # Ensures only authenticated and owners can delete

    def perform_destroy(self, instance):
        instance.delete()