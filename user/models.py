from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import PositiveSmallIntegerField
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class UserRole(models.IntegerChoices):
    USER = 1, "Пользователь"
    DRIVER = 2, "Водитель"
    ADMIN = 3, "Администратор"


class User(AbstractUser):
    # Names
    first_name = models.CharField("Имя", max_length=32, default="", blank=True)
    middle_name = models.CharField(
        "Отчество", max_length=32, default="", blank=True
    )
    last_name = models.CharField(
        "Фамилия", max_length=32, default="", blank=True, db_index=True
    )

    # Personal
    birth_date = models.DateField("Дата рождения", null=True, blank=True)

    # Contacts
    email = models.EmailField(
        "Электронная почта", blank=True, null=True, db_index=True
    )
    phone = PhoneNumberField("Номер телефона", unique=True, db_index=True)

    # Code for auth
    code = models.CharField(
        "Код для верификации по номеру телефона",
        max_length=4,
        null=True,
        blank=True,
    )

    role = PositiveSmallIntegerField(choices=UserRole.choices, default=UserRole.USER)

    USERNAME_FIELD = "phone"
