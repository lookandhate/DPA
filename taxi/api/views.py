from django.db.models import Q
from rest_framework import viewsets

from taxi.api.serializers import RideSerializer
from taxi.models import Ride
from user.models import UserRole


class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.is_anonymous:
            return qs.none()
        if self.request.user.role == UserRole.ADMIN:
            return qs
        if self.request.user.role == UserRole.DRIVER:
            return qs.filter(Q(driver=self.request.user) | Q(created_by=self.request.user))
        return qs.filter(created_by=self.request.user)
