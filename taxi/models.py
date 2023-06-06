from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import DecimalField

from common.model_fields import LongitudeField, LatitudeField
from common.models import BaseModel
from payment.models import PaymentMethod

# Create your models here.

UserModel = get_user_model()


class Ride(BaseModel):
    driver = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='driver_rides')
    departure_longitude = LongitudeField("Долгота старта")
    departure_latitude = LatitudeField("Широта старта")

    arriving_longitude = LongitudeField("Долгота точки назначения")
    arriving_latitude = LatitudeField("Широта точки назначения")

    total_price = DecimalField("Цена поездки", decimal_places=2, max_digits=20)

    time_in_road = models.IntegerField("Время в пути")

    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, related_name='payment_method_rides', null=True)

    discount = models.ForeignKey("payment.Discount", on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name="Скидка использованная в поездке")
