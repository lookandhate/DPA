from django.shortcuts import render
from rest_framework import viewsets

from payment.api.serializers import PaymentMethodSerializer, DiscountSerializer, PaymentSerializer
from payment.models import PaymentMethod, Discount, Payment


# Create your views here.

class PaymentMethodViewSet(viewsets.ModelViewSet):
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer


class DiscountViewSet(viewsets.ModelViewSet):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer