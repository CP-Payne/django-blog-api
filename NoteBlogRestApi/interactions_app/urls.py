from django.urls import path, include
from . import views

urlpatterns = [
    path('comment/add', views.CommentCreateView.as_view(), name="post-comment"),
    path('comment/list/<int:blog_id>', views.CommentsByBlogView.as_view(), name="get-comments"),
]