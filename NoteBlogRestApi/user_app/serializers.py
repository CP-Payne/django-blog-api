from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile

class UserRegisterSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'password_confirm']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        password = self.validated_data['password']
        password_confirm = self.validated_data['password_confirm']

        if password != password_confirm:
            raise serializers.ValidationError({"Error": "Passwords do not match"})

        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({"Error": "Email already exists"})

        account = User(email=self.validated_data['email'], username=self.validated_data['username'],first_name=self.validated_data['first_name'], last_name=self.validated_data['last_name'] )
        account.set_password(password)
        account.save()

        return account


class UserProfileSerializer(serializers.ModelSerializer):
    user_fullname = serializers.SerializerMethodField();
    class Meta:
        model= UserProfile
        fields=["user_fullname", "bio", "profession"]
        #read_only_fields = ['id', 'user']

    def get_user_fullname(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"