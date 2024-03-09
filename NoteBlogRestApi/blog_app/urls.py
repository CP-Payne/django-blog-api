from django.urls import path
from . import views

urlpatterns = [
    path('view-blog/', views.blog_list, name="blog_post")
]
