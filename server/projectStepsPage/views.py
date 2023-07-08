from common.viewsets import SoloModelViewSet
from .models import ProjectStepsPage
from .serializers import ProjectStepsPageSerializer


class ProjectStepsApiView(SoloModelViewSet):
    queryset = ProjectStepsPage.objects.prefetch_related("steps")
    serializer_class = ProjectStepsPageSerializer
