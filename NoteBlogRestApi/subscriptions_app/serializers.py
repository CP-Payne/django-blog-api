from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Subscription

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'subscriber', 'author', 'is_active', 'subscribed_at', 'unsubscribed_at']
        read_only_fields = ['id', 'subscriber', 'subscribed_at', 'unsubscribed_at']

    def create(self, validated_data):
        validated_data['subscriber'] = self.context['request'].user
        return super().create(validated_data)