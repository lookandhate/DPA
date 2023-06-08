from django.db.models import Q
from django.shortcuts import render
from rest_framework import viewsets

from common.views import MultiSerializerMixin
from payment.api.serializers import PaymentMethodSerializer, DiscountSerializer, PaymentSerializer, \
    CreatePaymentMethodSerializer, CreateDiscountSerializer
from payment.models import PaymentMethod, Discount, Payment
from user.models import UserRole


# Create your views here.

class PaymentMethodViewSet(MultiSerializerMixin, viewsets.ModelViewSet):
    queryset = PaymentMethod.objects.all()
    default_serializer_class = PaymentMethodSerializer
    serializer_classes = {"create": CreatePaymentMethodSerializer}

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if user.is_anonymous: return qs.none()
        if user.role == UserRole.ADMIN: return qs
        return qs.filter(created_by=user)


class DiscountViewSet(MultiSerializerMixin, viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    default_serializer_class = DiscountSerializer
    serializer_classes = {"create": CreateDiscountSerializer}

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user

        if user.role == UserRole.ADMIN:
            return qs

        qs = qs.exclude(to_use=0)

        if user.is_anonymous:
            return qs.filter(is_for_everyone=True)
        if user.role != UserRole.ADMIN:
            return qs.filter(Q(is_for_everyone=True) | Q(user=user))


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if user.is_anonymous: return qs.none()
        if user.role == UserRole.ADMIN: return qs
        return qs.filter(created_by=user)
