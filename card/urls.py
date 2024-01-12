from django.urls import path

from .views import CardAllView, CardOneView

urlpatterns = [
    path('<int:pk>', CardOneView.as_view()),
    path('', CardAllView.as_view()),
]
