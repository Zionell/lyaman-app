from common.viewsets import SoloModelViewSet
from .models import CertificatesPage
from .serializers import CertificatesPageSerializer


class CertificatesPageApiView(SoloModelViewSet):
    queryset = CertificatesPage.objects.prefetch_related("certs")
    serializer_class = CertificatesPageSerializer
