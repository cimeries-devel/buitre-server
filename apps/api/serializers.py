from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from apps.store.models import Color
from apps.store.models import Sex
from apps.store.models import Size
from apps.store.models import Category
from apps.store.models import Style
from apps.store.models import Product
from apps.store.models import Company
from apps.store.models import Branch
from apps.store.models import Stock
from apps.store.models import Transfer
from apps.store.models import DetailTransfer
from apps.users.models import User
from apps.users.models import Access


class ColorSerializers(ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class SexSerializers(ModelSerializer):
    class Meta:
        model = Sex
        fields = '__all__'


class SizeSerializers(ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'


class CategorySerializers(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class StyleSerializers(ModelSerializer):
    class Meta:
        model = Style
        fields = '__all__'


class ProductSerializers(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CompanySerializers(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class BranchSerializers(ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'


class StockSerializers(ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'


class DetailTransferSerializers(ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')

    class Meta:
        model = DetailTransfer
        fields = ('transfer',
                  'product',
                  'quantity',
                  'product_name')


class TransferSerializers(ModelSerializer):
    details = DetailTransferSerializers(source='detailtransfer_set', many=True)

    class Meta:
        model = Transfer
        fields = ('id',
                  'branch_from',
                  'branch_to',
                  'description',
                  'details')


class UserSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'email',
                  'password',
                  'last_login',
                  'username',
                  'first_name',
                  'last_name',
                  'phone',
                  'is_active',
                  'is_staff',
                  'level',
                  'access')


class AccessSerializers(ModelSerializer):
    class Meta:
        model = Access
        fields = '__all__'
