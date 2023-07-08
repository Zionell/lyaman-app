from common.viewsets import SoloModelViewSet
from .models import ReviewsPage
from .serializers import ReviewsPageSerializer


class ReviewsPageApiView(SoloModelViewSet):
    queryset = ReviewsPage.objects.prefetch_related("review")
    serializer_class = ReviewsPageSerializer
