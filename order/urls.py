from django.urls import path
from .views import OrderListAPIView, OrderClearAPIView, OrderCountApiView

urlpatterns = [
    path('all/<int:chat_id>/', OrderListAPIView.as_view()),
    path('clear/<int:chat_id>/', OrderClearAPIView.as_view()),
    path('count/<int:id>/<str:var>', OrderCountApiView.as_view()),
]
