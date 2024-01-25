from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('card/', include('card.urls')),
    path('client/', include('client.urls')),
    path('order/', include('order.urls')),
]

