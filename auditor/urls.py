from django.urls import path
from .views import socket_list

urlpatterns = [
    path('', socket_list, name='socket_list'),
]