from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import CardModel
from .serializers import CardSerializer


class CardAllView(ListCreateAPIView):
    queryset = CardModel.objects.all()
    serializer_class = CardSerializer


class CardOneView(RetrieveUpdateDestroyAPIView):
    queryset = CardModel.objects.all()
    serializer_class = CardSerializer
