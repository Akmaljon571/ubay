from rest_framework import serializers

from .models import CardModel


class CardSerializer(serializers.ModelSerializer):
    image_field = serializers.ImageField(required=False)

    class Meta:
        model = CardModel
        fields = "__all__"
