from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
#router = DefaultRouter()
#router.register(r'blog-list', blog_details )

urlpatterns = [
    path('blogs/', views.BlogPostCreateUpdateRetrieveView.as_view(), name="blog-list"),
    path('blogs/<int:blog_id>', views.BlogPostCreateUpdateRetrieveView.as_view(), name="blog-details"),
    #path('create/', views.BlogPostCreateUpdateRetrieveView.as_view(), name='blog-create'),
    #path('update/<int:pk>', views.BlogPostCreateUpdateRetrieveView.as_view(), name='blog-update'),
    #path('', include(router.urls))
]
