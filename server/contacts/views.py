from django.shortcuts import render
from rest_framework import generics

from .models import Contacts
from .serializers import ContactsSerializer


class ContactsApiView(generics.ListAPIView):
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
