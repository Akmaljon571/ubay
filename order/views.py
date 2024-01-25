from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from client.models import ClientModel
from card.models import CardModel
from .models import OrderModel
from .serializers import OrderSerializer, OrderAllSerializer


class OrderListAPIView(APIView):
    def get(self, request, chat_id, *args, **kwargs):
        all_data = OrderModel.objects.all()

        if not all_data.exists():
            return Response(data={"data": [], "status": status.HTTP_200_OK}, status=status.HTTP_200_OK)

        try:
            a = ClientModel.objects.get(chat_id=chat_id)
        except:
            return Response(data={"message": "Chat Not Found", "status": status.HTTP_404_NOT_FOUND},
                            status=status.HTTP_404_NOT_FOUND)
        serializer_data = OrderAllSerializer(all_data, many=True).data

        filter_data = [item for item in serializer_data if item['user'] == a.id]

        return Response(data={"data": filter_data, "status": status.HTTP_200_OK}, status=status.HTTP_200_OK)


class OrderClearAPIView(APIView):
    def delete(self, request, chat_id, *args, **kwargs):
        try:
            a = ClientModel.objects.get(chat_id=chat_id)
        except:
            return Response(data={"message": "Chat Not Found", "status": status.HTTP_404_NOT_FOUND},
                            status=status.HTTP_404_NOT_FOUND)

        OrderModel.objects.filter(user=a.id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderCountApiView(APIView):
    def increment_count(self, order_instance):
        order_instance.count += 1
        order_instance.save()

    def decrement_count(self, order_instance):
        if order_instance.count > 0:
            order_instance.count -= 1
            order_instance.save()

    def put(self, request, id, var, *args, **kwargs):
        try:
            order_instance = OrderModel.objects.get(id=id)
        except OrderModel.DoesNotExist:
            return Response(data={"message": "Order not found", "status": status.HTTP_404_NOT_FOUND},
                            status=status.HTTP_404_NOT_FOUND)
        if var == 'add':
            self.increment_count(order_instance)
            return Response(data={"message": "Order updated successfully", "status": status.HTTP_200_OK},
                            status=status.HTTP_200_OK)
        elif var == 'remove':
            self.decrement_count(order_instance)
            return Response(data={"message": "Order updated successfully", "status": status.HTTP_200_OK},
                            status=status.HTTP_200_OK)
        else:
            return Response(data={"message": "Var Bad Request", "status": status.HTTP_400_BAD_REQUEST},
                            status=status.HTTP_400_BAD_REQUEST)


class OrderCreateAPIView(APIView):
    def post(self, request, chat_id, card_id, *args, **kwargs):
        try:
            client = ClientModel.objects.get(chat_id=chat_id)
            card = CardModel.objects.get(id=card_id)

            order_data = {
                'user': client.pk,
                'card': card.pk,
                'count': 1
            }

            serializer = OrderSerializer(data=order_data)
            if serializer.is_valid():
                serializer.save()
                return Response(data={"message": "Order created successfully", "status": status.HTTP_201_CREATED},
                                status=status.HTTP_201_CREATED)
            else:
                return Response(data={"message": "Invalid data", "errors": serializer.errors,
                                      "status": status.HTTP_400_BAD_REQUEST},
                                status=status.HTTP_400_BAD_REQUEST)
        except ClientModel.DoesNotExist:
            return Response(data={"message": "Client not found", "status": status.HTTP_404_NOT_FOUND},
                            status=status.HTTP_404_NOT_FOUND)

        except CardModel.DoesNotExist:
            return Response(data={"message": "Card not found", "status": status.HTTP_404_NOT_FOUND},
                            status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(data={"message": str(e), "status": status.HTTP_500_INTERNAL_SERVER_ERROR},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
