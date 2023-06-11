from rest_framework import serializers
from .models import WorkProcess, WorkProcessPage


class _WorkProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkProcess
        exclude = ['page']


class WorkProcessPageSerializer(serializers.ModelSerializer):
    steps = _WorkProcessSerializer(many=True, read_only=True)

    class Meta:
        model = WorkProcessPage
        fields = '__all__'
