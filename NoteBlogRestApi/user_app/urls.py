from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token
#router = DefaultRouter()
#router.register(r'blog-list', blog_details )

urlpatterns = [
  path("login", obtain_auth_token, name="login"),
  # path("logout", views.logout_user, name="logout"),
  path("logout", views.LogoutUserView.as_view(), name="logout"),
  path("register", views.UserRegisterView.as_view(), name="user-register") 
]
