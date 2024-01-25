from rest_framework import serializers

from card.serializers import CardSerializer
from .models import OrderModel


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = "__all__"


class OrderAllSerializer(serializers.ModelSerializer):
    card = CardSerializer()  # Nested CardSerializer

    class Meta:
        model = OrderModel
        fields = "__all__"
