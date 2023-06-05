from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(UserModel, null=True, on_delete=models.SET_NULL)

    class Meta:
        abstract = True
