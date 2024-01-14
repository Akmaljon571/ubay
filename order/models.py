from django.db import models

from client.models import ClientModel
from card.models import CardModel


class OrderModel(models.Model):
    user = models.ForeignKey(ClientModel, on_delete=models.CASCADE, db_column='chat_id')
    card = models.ForeignKey(CardModel, on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)
