from rest_framework import serializers
from .models import Certificates, CertificatesPage


class _CertificatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificates
        exclude = ['page']


class CertificatesPageSerializer(serializers.ModelSerializer):
    certs = _CertificatesSerializer(many=True, read_only=True)

    class Meta:
        model = CertificatesPage
        fields = '__all__'
