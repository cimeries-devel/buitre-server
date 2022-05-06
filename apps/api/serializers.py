from rest_framework.serializers import ModelSerializer
from apps.store.models import Color
from apps.store.models import Sex
from apps.store.models import Size
from apps.store.models import Category
from apps.store.models import Style
from apps.store.models import Product
from apps.store.models import Company
from apps.store.models import Branch
from apps.store.models import Stock
from apps.users.models import User


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


class UserSerializers(ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'email',
                  'username')
