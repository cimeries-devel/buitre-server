from django.db import models
from apps.users.models import User


class Color(models.Model):
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=16,
                            null=False,
                            blank=False)

    def __str__(self):
        return self.name


class Sex(models.Model):
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=16,
                            null=False,
                            blank=False)

    def __str__(self):
        return self.name


class Size(models.Model):
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=16,
                            null=False,
                            blank=False)

    def __str__(self):
        return self.name


class Category(models.Model):
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=32,
                            null=False,
                            blank=False)


class Style(models.Model):
    code = models.CharField(max_length=32,
                            null=False,
                            blank=False)
    name = models.CharField(max_length=64,
                            null=False,
                            blank=False)
    price = models.DecimalField(max_digits=16,
                                decimal_places=2)
    seller_price = models.DecimalField(max_digits=16,
                                       decimal_places=2)
    tag_price = models.DecimalField(max_digits=16,
                                    decimal_places=2)
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 null=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    is_active = models.BooleanField(default=True)
    color = models.ForeignKey(Color,
                              on_delete=models.CASCADE,
                              null=False)
    sex = models.ForeignKey(Sex,
                            on_delete=models.CASCADE,
                            null=False)
    size = models.ForeignKey(Size,
                             on_delete=models.CASCADE,
                             null=False)
    codebar = models.CharField(max_length=128,
                               null=False,
                               blank=False)
    style = models.ForeignKey(Style,
                              on_delete=models.CASCADE,
                              null=False)

    def __str__(self):
        return self.style.name


class Company(models.Model):
    business_name = models.CharField(max_length=128,
                                     null=False,
                                     blank=False)
    trade_name = models.CharField(max_length=128,
                                  null=False,
                                  blank=False)
    website = models.CharField(max_length=64,
                               null=False,
                               blank=True)
    logo = models.ImageField(upload_to='media')
    description = models.CharField(max_length=128,
                                   null=False,
                                   blank=True)
    exchanged_rate = models.DecimalField(max_digits=5,
                                         decimal_places=2,
                                         null=False,
                                         default=3.80)


class Branch(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=16,
                             null=False,
                             blank=True)
    urbanization = models.CharField(max_length=64,
                                    null=False,
                                    blank=False)
    fiscal_address = models.CharField(max_length=64,
                                      null=False,
                                      blank=False)
    company = models.ForeignKey(Company,
                                on_delete=models.CASCADE,
                                null=False)
    products = models.ManyToManyField('Product', through='Stock')
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.company.trade_name


class Stock(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                null=False)
    branch = models.ForeignKey(Branch,
                               on_delete=models.CASCADE,
                               null=False)
    quantity = models.BigIntegerField(null=False,
                                      blank=False)

    def __str__(self):
        return "{0} - {1}".format(self.quantity,
                                  self.product.style.name)
