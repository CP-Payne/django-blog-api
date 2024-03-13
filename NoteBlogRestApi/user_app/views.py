from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import status
from .serializers import UserRegisterSerializer
from rest_framework.permissions import AllowAny

# Create your views here.

# @api_view(["POST",])
# @authentication_classes([TokenAuthentication])
# def logout_user(request):
#     if request.user.is_authenticated:
#         # Only try to delete the token if the user is authenticated
#         request.user.auth_token.delete()
#         return Response({'success': 'Successfully logged out.'}, status=200)
#     else:
#         # Handle the case where the user is not authenticated
#         return Response({'error': 'You are not logged in.'}, status=400)

class LogoutUserView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response({'Success': 'Successfully logged out.'}, status=200)

class UserRegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user_data = UserRegisterSerializer(user).data
            return Response({
                "user": user_data,
                "message": "User successfully registered."
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)