from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.db.models import PositiveSmallIntegerField
from phonenumber_field.modelfields import PhoneNumberField


class CustomUserManager(UserManager):
    def _create_user(self, phone, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not phone:
            raise ValueError("The given phone must be set")
        email = self.normalize_email(email)
        user = self.model(phone=phone, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(phone, email, password, **extra_fields)

    def create_superuser(
            self, phone, email=None, password=None, **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(phone, email, password, **extra_fields)


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

    objects = CustomUserManager()
