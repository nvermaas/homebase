
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import MoonPhasesSerializer
from .my_moon.moon import get_new_moons

class MoonPhasesView(viewsets.ViewSet):
    serializer_class = MoonPhasesSerializer

    # override the list method to be able to plug in my moonphase business logic
    def list(self, request):
        # read the year from the request: .../moonphases/?year=2018
        year = self.request.query_params['year']

        # call to the business logic that returns a list of moonphase
        my_moonphases = get_new_moons(int(year))
        serializer = MoonPhasesSerializer(instance=my_moonphases, many=True)

        # add some extra structure to the json response
        numphases = len(my_moonphases)
        data = {'numphases' : numphases, 'phasedata' : serializer.data}
        return Response(data)