# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from user_app.models import UserProfile
from user_app.serializers import UserProfileSerializer

from .models import Subscription
from .serializers import SubscriptionSerializer


class SubscriptionToggleView(APIView):
    permission_classes = [IsAuthenticated]

    # Post toggles the subscription to active or inactive
    def post(self, request, author_id):
        subscriber = request.user
        author = get_object_or_404(User, pk=author_id)

        if subscriber == author:
            return Response({"error": "Cannot subscribe to oneself."}, status=400)

        subscription, created = Subscription.objects.get_or_create(
            subscriber=subscriber, author=author, defaults={"is_active": True}
        )

        if not created:
            subscription.is_active = (
                not subscription.is_active
            )  # Toggle is_active status
            if not subscription.is_active:
                subscription.unsubscribed_at = timezone.now()
            else:
                subscription.unsubscribed_at = None
            subscription.save()

        serializer = SubscriptionSerializer(subscription)
        return Response(serializer.data, status=200 if not created else 201)

    # The delete removes the subscription from the database
    def delete(self, request, author_id):
        subscriber = request.user
        author = get_object_or_404(User, pk=author_id)

        try:
            subscription = Subscription.objects.get(
                subscriber=subscriber, author=author, is_active=True
            )
            subscription.is_active = False
            subscription.unsubscribed_at = timezone.now()
            subscription.save()
            return Response(status=204)
        except Subscription.DoesNotExist:
            return Response({"error": "Not subscribed."}, status=404)


# Update the below to query whether to return active subscription counts, inactive subscription counts or both
class SubscriptionsCountView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        subcriptions_count = Subscription.objects.filter(subscriber=user).count()

        return Response({"subscription_count": subcriptions_count})


class SubscriptionsUserListView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        # Search active only
        # subscriptions_list = Subscription.objects.filter(user=user, is_active=True)

        subscriptions_list = Subscription.objects.filter(subscriber=user)
        authors_ids = [subscription.author.id for subscription in subscriptions_list]
        author_profiles_qs = UserProfile.objects.filter(user__id__in=authors_ids)

        author_profile_serializer = UserProfileSerializer(author_profiles_qs, many=True)
        author_profiles_data = author_profile_serializer.data
        return Response(author_profiles_data)


# Update the below to query whether to return active subscription counts, inactive subscription counts or both
# Maybe make below endpoint public
class SubscribersCountView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        subscribers_count = Subscription.objects.filter(subscriber=user).count()

        return Response({"subscribers_count": subscribers_count})
