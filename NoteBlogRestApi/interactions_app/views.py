from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import Comment, Like
from .serializers import CommentSerializer, LikeSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from .permissions import IsOwnerOrReadOnly
from blog_app.models import Blog
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status

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
    
    def get_object(self):
        comment_id = self.kwargs.get('comment_id')
        return get_object_or_404(Comment, id=comment_id)

    def perform_destroy(self, instance):
        instance.delete()

class ToggleLikeView(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def post(self, request, blog_id, format=None):
        user = request.user
        blog = get_object_or_404(Blog, pk=blog_id)

        like, created = Like.objects.get_or_create(user=user, blog=blog)

        if not created:
            like.delete()
            return Response({'status': 'unliked'}, status=status.HTTP_204_NO_CONTENT)

        serializer = LikeSerializer(like)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class BlogLikesCountView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, blog_id, format=None):
        blog = get_object_or_404(Blog, pk=blog_id)
        likes_count = Like.objects.filter(blog=blog).count()
        return Response({"likes_count": likes_count})