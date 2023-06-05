from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import DecimalField


class LatitudeField(DecimalField):
    """
    Override for set base max_digits, decimal_places and default values for coordinates
    """

    def __init__(
            self,
            verbose_name="Широта",
            name=None,
            max_digits=18,
            decimal_places=15,
            **kwargs,
    ):
        kwargs["validators"] = [
            MinValueValidator(-90),
            MaxValueValidator(90),
        ]
        super().__init__(
            verbose_name,
            name,
            max_digits,
            decimal_places,
            **kwargs,
        )


class LongitudeField(DecimalField):
    """
    Override for set base max_digits, decimal_places and default values for coordinates
    """

    def __init__(
            self,
            verbose_name="Долгота",
            name=None,
            max_digits=18,
            decimal_places=15,
            **kwargs,
    ):
        kwargs["validators"] = [
            MinValueValidator(-180),
            MaxValueValidator(180),
        ]
        super().__init__(
            verbose_name, name, max_digits, decimal_places, **kwargs
        )
