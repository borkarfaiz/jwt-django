from rest_framework import serializers
from food.models import Food


class FoodSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(source='user.pk', required=False)

    def create(self, validated_data):
        food = Food.objects.create(
            user_id=self.context.get('user_id'),
            title=validated_data['title'],
            description=validated_data['description']
        )
        return food

    class Meta:
        model = Food
        fields = ['user_id', 'id', 'title', 'description']
