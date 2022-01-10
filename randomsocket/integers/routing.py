from django.urls import path
from .consumers import WSConsumer
ws_urlpatterns= [
    path('integers/',WSConsumer.as_asgi())
]