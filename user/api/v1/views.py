from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignUpSerializer


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
