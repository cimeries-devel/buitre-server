from django.db import models
from apps.users.models import User
from apps.users.models import Client


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

    def __str__(self):
        return self.name


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
                               blank=True)
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

    def __str__(self):
        return self.business_name


class Branch(models.Model):
    is_active = models.BooleanField(default=True)
    is_branch = models.BooleanField(default=True)
    name = models.CharField(max_length=128,
                            null=False,
                            blank=False,
                            default="no definido")
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
    users = models.ManyToManyField(User,
                                   blank=True)

    def __str__(self):
        return self.name


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


class Transfer(models.Model):
    branch_from = models.ForeignKey(Branch,
                                    related_name='from+',
                                    on_delete=models.CASCADE)
    branch_to = models.ForeignKey(Branch,
                                  related_name='to+',
                                  on_delete=models.CASCADE)
    details = models.ManyToManyField('Product', through='DetailTransfer')
    description = models.CharField(max_length=128,
                                   null=False,
                                   blank=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.branch_from.name


class DetailTransfer(models.Model):
    transfer = models.ForeignKey(Transfer,
                                 models.CASCADE,
                                 null=True,
                                 blank=False,
                                 default=0)
    product = models.ForeignKey(Product,
                                models.CASCADE)
    quantity = models.BigIntegerField(null=False,
                                      blank=False)

    def __str__(self):
        return self.product.style.name


class Sale(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             null=False)
    client = models.ForeignKey(Client,
                               on_delete=models.CASCADE,
                               null=False)
    sub_total = models.DecimalField(max_digits=18,
                                    decimal_places=2)
    exchanged_rate = models.DecimalField(max_digits=18,
                                         decimal_places=2)
    total = models.DecimalField(max_digits=18,
                                decimal_places=2)
    created = models.DateField(auto_now_add=True)
    products = models.ManyToManyField('Product', through='DetailSale')

    def __str__(self):
        return self.pk


class DetailSale(models.Model):
    sale = models.ForeignKey(Sale,
                             models.CASCADE,
                             null=False)
    product = models.ForeignKey(Product,
                                models.CASCADE,
                                null=False)
    quantity = models.BigIntegerField(null=False,
                                      blank=False)
    price = models.DecimalField(max_digits=18,
                                decimal_places=2,
                                null=False,
                                blank=False)
    sub_total = models.DecimalField(max_digits=18,
                                    decimal_places=2,
                                    null=False,
                                    blank=False)

    def __str__(self):
        return self.sale.pk
