from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
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
from .serializers import ColorSerializers
from .serializers import SexSerializers
from .serializers import SizeSerializers
from .serializers import CategorySerializers
from .serializers import StyleSerializers
from .serializers import ProductSerializers
from .serializers import CompanySerializers
from .serializers import BranchSerializers
from .serializers import StockSerializers
from .serializers import UserSerializers


# Create your views here.
class ColorListAPIView(ListCreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializers


class ColorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializers


class SexListAPIView(ListCreateAPIView):
    queryset = Sex.objects.all()
    serializer_class = SexSerializers


class SexRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Sex.objects.all()
    serializer_class = SexSerializers


class SizeListAPIView(ListCreateAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializers


class SizeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializers


class CategoryListAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class StyleListAPIView(ListCreateAPIView):
    queryset = Style.objects.all()
    serializer_class = StyleSerializers


class StyleRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Style.objects.all()
    serializer_class = StyleSerializers


class ProductListAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class CompanyListAPIView(ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers


class CompanyRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers


class BranchListAPIView(ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializers


class BranchRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializers


class StockListAPIView(ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializers


class StockRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializers


class UserListAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
