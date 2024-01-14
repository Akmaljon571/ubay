from django.db import models


class ClientModel(models.Model):
    chat_id = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    def __str__(self):
        return self.username
