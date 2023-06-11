from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from common.viewsets import SoloModelViewSet
from .models import WorkProcessPage
from .serializers import WorkProcessPageSerializer


class WorkProcessPageApiView(SoloModelViewSet):
    queryset = WorkProcessPage.objects.prefetch_related("steps")
    serializer_class = WorkProcessPageSerializer
