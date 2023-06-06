from rest_framework import viewsets

from taxi.api.serializers import RideSerializer
from taxi.models import Ride


class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer

