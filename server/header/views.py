from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Header
from .serializers import HeaderSerializer


class HeaderAPIView(APIView):
    def get(self, request):
        instance = Header.load()
        serializer = HeaderSerializer(instance)
        return Response(serializer.data)
