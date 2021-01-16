from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignUpSerializer

from django.contrib.auth.models import User


class SignUpAPIView(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        message = {'message': f'{user.username} registered successfully'}
        return Response(
            message,
            status=status.HTTP_201_CREATED
        )

from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated

class ListUsers(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)