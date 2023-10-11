from common.viewsets import SoloModelViewSet
from .models import Header
from .serializers import HeaderSerializer


class HeaderAPIView(SoloModelViewSet):
    queryset = Header.objects.all()
    serializer_class = HeaderSerializer
