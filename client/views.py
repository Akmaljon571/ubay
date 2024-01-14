from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import ClientModel
from .serializers import ClientSerializer


class RegisterClient(APIView):
    serializer_class = ClientSerializer

    def post(self, request, *args, **kwargs):
        serializer = ClientSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data={"message": "Created successfully", "status": status.HTTP_201_CREATED},
                            status=status.HTTP_201_CREATED)
        return Response(data={"message": serializer.errors, "status": status.HTTP_400_BAD_REQUEST},
                        status=status.HTTP_400_BAD_REQUEST)


class LoginClient(APIView):
    def get(self, request, chat_id, *args, **kwargs):
        try:
            instance = ClientModel.objects.get(chat_id=chat_id)
            serializer = ClientSerializer(instance)
            return Response(data={"data": serializer.data, "status": status.HTTP_201_CREATED})
        except ClientModel.DoesNotExist:
            return Response(data={"message": 'Client Not Found', "status": status.HTTP_404_NOT_FOUND})
