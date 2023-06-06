from django.contrib.auth import get_user_model
from django.db import models

from common.models import BaseModel

UserModel = get_user_model()


class PaymentType(models.IntegerChoices):
    CASH = 1
    CARD = 2
    WALLET = 3


class PaymentMethod(BaseModel):
    name = models.CharField(max_length=50)
    card_number = models.CharField(max_length=16, null=True, blank=True)
    card_expiry = models.DateField(null=True, blank=True)
    card_cvv = models.CharField(max_length=3, null=True, blank=True)
    wallet_id = models.CharField(max_length=50, null=True, blank=True)
    payment_type = models.IntegerField(choices=PaymentType.choices, default=PaymentType.CASH)


class Discount(BaseModel):
    name = models.CharField(max_length=50)
    discount = models.IntegerField("Процент скидки")
    to_use = models.IntegerField("Сколько использований осталось")
    user = models.ForeignKey(UserModel, on_delete=models.SET_NULL,
                             verbose_name="Пользователь, на которого назначена скидка",
                             null=True,
                             related_name='user_discounts')
    is_for_everyone = models.BooleanField("Доступна ли всем?", default=False)


class Payment(BaseModel):
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE, related_name='payment_payments')
    discount = models.ForeignKey(Discount, on_delete=models.SET_NULL, null=True, blank=True,
                                 verbose_name="Скидка использованная в поездке")
    amount = models.DecimalField("Сумма платежа", max_digits=10, decimal_places=2)
    is_success = models.BooleanField("Успешен ли платеж?", default=False)