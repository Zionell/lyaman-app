from rest_framework import serializers
from .models import Reviews, ReviewsPage


class _ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        exclude = ['page']


class ReviewsPageSerializer(serializers.ModelSerializer):
    review = _ReviewsSerializer(many=True, read_only=True)

    class Meta:
        model = ReviewsPage
        fields = '__all__'