from django.db import models


class CardModel(models.Model):
    title = models.CharField(max_length=255)
    image = models.TextField()
    price = models.CharField(max_length=255)
    desc = models.TextField()

    def __str__(self):
        return self.title
