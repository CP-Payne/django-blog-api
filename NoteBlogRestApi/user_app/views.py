from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(["POST",])
@authentication_classes([TokenAuthentication])
def logout_user(request):
    if request.user.is_authenticated:
        # Only try to delete the token if the user is authenticated
        request.user.auth_token.delete()
        return Response({'success': 'Successfully logged out.'}, status=200)
    else:
        # Handle the case where the user is not authenticated
        return Response({'error': 'You are not logged in.'}, status=400)