from django.urls import path

from .views import RegisterClient, LoginClient

urlpatterns = [
    path('register/', RegisterClient.as_view()),
    path('login/<int:chat_id>', LoginClient.as_view()),
]
