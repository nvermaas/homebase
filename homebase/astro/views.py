
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import MoonPhasesSerializer
from .moonphase import MoonPhase,moonphases

class MoonPhasesView(viewsets.ViewSet):
    serializer_class = MoonPhasesSerializer

    def list(self, request):
        serializer = MoonPhasesSerializer(instance=moonphases.values(), many=True)
        return Response(serializer.data)