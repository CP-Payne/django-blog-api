from django.urls import path
from . import views

urlpatterns = [
    path('view-posts/', views.view_posts, name="view_posts"),
    path('blog-details/<int:blog_id>', views.blog_details, name="blog_details")
]
