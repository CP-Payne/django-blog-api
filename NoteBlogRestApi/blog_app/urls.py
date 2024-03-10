from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
#router = DefaultRouter()
#router.register(r'blog-list', blog_details )

urlpatterns = [
    path('view-posts/', views.view_posts, name="view_posts"),
    path('blog-details/<int:blog_id>', views.blog_details, name="blog_details")
    #path('', include(router.urls))
]
