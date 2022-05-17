from django.contrib.auth.models import AbstractUser
from django.db import models


class Access(models.Model):
    name = models.CharField(max_length=64,
                            null=False,
                            blank=False)

    def __str__(self):
        return self.name


class User(AbstractUser):
    phone = models.CharField(max_length=15,
                             blank=True,
                             null=False)
    level = models.IntegerField(default=0, null=False)
    access = models.ManyToManyField(Access,
                                    blank=True)

    def __str__(self):
        return self.username


class Client(models.Model):
    trade_name = models.CharField(max_length=128,
                                  null=False,
                                  blank=False)
    document_type = models.BooleanField(default=True,
                                        null=False,
                                        unique=True)
    number_document = models.CharField(max_length=20,
                                       null=False,
                                       blank=True)

    def __str__(self):
        return self.trade_name
