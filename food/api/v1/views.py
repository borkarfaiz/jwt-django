from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import FoodSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from rest_framework import status

from food.models import Food


class UserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = FoodSerializer

    def list(self, request):
        queryset = Food.objects.filter(user=self.request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Food.objects.filter(user=self.request.user)
        food = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(food)
        return Response(serializer.data)

    def update(self, request, pk=None):
        queryset = Food.objects.filter(user=self.request.user)
        food = get_object_or_404(queryset, pk=pk)
        serializer = self.get_serializer(food, data=request.data)
        serializer.is_valid(raise_exception=True)
        food = serializer.save()
        content = {
            'message': f'updated {food.title}'
        }
        return Response(
            content,
            status.HTTP_200_OK
        )

    def create(self, request):
        serializer = self.get_serializer(
            data=request.data, context={'user_id': self.request.user.pk}
        )
        serializer.is_valid(raise_exception=True)
        food = serializer.save()
        content = {
            'message': 'Food Added Successfully'
        }
        return Response(
            content,
            status=status.HTTP_201_CREATED
        )
