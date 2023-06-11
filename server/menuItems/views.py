from django.shortcuts import render
from rest_framework import generics

from .models import MenuItems
from .serializers import MenuItemsSerializer


class MenuItemsApiView(generics.ListAPIView):
    queryset = MenuItems.objects.all()
    serializer_class = MenuItemsSerializer
