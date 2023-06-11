from rest_framework import serializers
from .models import ProjectSteps, ProjectStepsPage


class _ProjectStepsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectSteps
        exclude = ['page']


class ProjectStepsPageSerializer(serializers.ModelSerializer):
    steps = _ProjectStepsSerializer(many=True, read_only=True)

    class Meta:
        model = ProjectStepsPage
        fields = '__all__'