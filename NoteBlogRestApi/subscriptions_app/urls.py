from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token
#router = DefaultRouter()
#router.register(r'blog-list', blog_details )

urlpatterns = [
  path("subscribe/<int:author_id>", views.SubscriptionToggleView.as_view(), name="toggle-subscription"),
  path("count", views.SubscriptionsCountView.as_view(), name="subscriptions-count"),
  path("subscribers/count", views.SubscribersCountView.as_view() , name="subscriptions-count"),
  path("get-subscriptions", views.SubscriptionsUserListView.as_view() , name="list-subscriptions"),
]
