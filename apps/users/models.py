from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone = models.CharField(max_length=15,
                             blank=True,
                             null=False)
    is_level = models.IntegerField(default=0, null=False)

    def __str__(self):
        return self.username
