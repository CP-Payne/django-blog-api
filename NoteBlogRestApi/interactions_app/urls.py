from django.urls import path, include
from . import views

urlpatterns = [
    path('comment/add', views.CommentCreateView.as_view(), name="post-comment"),
    path('comment/list/<int:blog_id>', views.CommentsByBlogView.as_view(), name="get-comments"),
    path('comment/delete/<int:comment_id>', views.CommentDeleteView.as_view(), name="delete-comments"),
    path('like/<int:blog_id>/toggle-like', views.ToggleLikeView.as_view(), name='toggle-like'),
    path('like/<int:blog_id>', views.BlogLikesCountView.as_view(), name="blog-likes"),
]
