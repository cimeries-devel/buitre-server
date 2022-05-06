from django.contrib import admin
from apps.store.models import Color
from apps.store.models import Sex
from apps.store.models import Size
from apps.store.models import Category
from apps.store.models import Style
from apps.store.models import Product
from apps.store.models import Company
from apps.store.models import Branch
from apps.store.models import Stock


# Register your models here.
admin.site.register(Color)
admin.site.register(Sex)
admin.site.register(Size)
admin.site.register(Category)
admin.site.register(Style)
admin.site.register(Product)
admin.site.register(Company)
admin.site.register(Branch)
admin.site.register(Stock)
