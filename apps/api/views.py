from django.http import Http404
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import ListAPIView
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
from apps.store.models import Transfer
from apps.store.models import DetailTransfer
from apps.store.models import Sale
from apps.store.models import DetailSale
from apps.users.models import User
from apps.users.models import Client
from apps.users.models import Access
from .serializers import ColorSerializers
from .serializers import SexSerializers
from .serializers import SizeSerializers
from .serializers import CategorySerializers
from .serializers import StyleSerializers
from .serializers import ProductSerializers
from .serializers import CompanySerializers
from .serializers import BranchSerializers
from .serializers import StockSerializers
from .serializers import TransferSerializers
from .serializers import SaleSerializers
from .serializers import UserSerializers
from .serializers import ClientSerializers
from .serializers import AccessSerializers


# Create your views here.
class ColorListCreateAPIView(ListCreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializers


class ColorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializers


class SexListCreateAPIView(ListCreateAPIView):
    queryset = Sex.objects.all()
    serializer_class = SexSerializers


class SexRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Sex.objects.all()
    serializer_class = SexSerializers


class SizeListCreateAPIView(ListCreateAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializers


class SizeRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializers


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class StyleListCreateAPIView(ListCreateAPIView):
    queryset = Style.objects.all()
    serializer_class = StyleSerializers


class StyleRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Style.objects.all()
    serializer_class = StyleSerializers


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    def perform_create(self, serializer):
        serializer.save()
        product = serializer.instance
        product.codebar += str(10101010 + product.pk)
        product.save()


class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class CompanyListCreateAPIView(ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers


class CompanyRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers


class BranchListCreateAPIView(ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializers


class BranchForUserListAPIView(ListAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializers

    def get_queryset(self):
        user = self.request.user
        branches = Branch.objects.filter(users=user)
        return branches


class BranchRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializers


class StockListCreateAPIView(ListCreateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializers


class StockRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = StockSerializers
    lookup_field = 'branch'

    def get_queryset(self):
        try:
            branch = Branch.objects.get(pk=self.kwargs['branch'])
            product = Product.objects.get(pk=self.kwargs['product'])
        except (Product.DoesNotExist, Branch.DoesNotExist):
            raise Http404
        return Stock.objects.filter(branch=branch, product=product)

    def perform_update(self, serializer):
        quantity = serializer._kwargs['data']['quantity']
        stock = serializer.instance
        stock.quantity += int(quantity)
        stock.save()


class StockListAPIView(ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializers
    lookup_field = 'branch'

    def get_queryset(self):
        branch = Branch.objects.get(pk=self.kwargs[self.lookup_field])
        return self.queryset.filter(branch=branch)


class TransferListCreateAPIView(ListCreateAPIView):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializers

    def perform_create(self, serializer):
        from_pk = serializer._kwargs['data']['branch_from']
        to_pk = serializer._kwargs['data']['branch_to']
        description = serializer._kwargs['data']['description']
        transfer = Transfer(branch_from=Branch.objects.get(pk=from_pk),
                            branch_to=Branch.objects.get(pk=to_pk),
                            description=description)
        transfer.save()
        for detail_data in serializer._kwargs['data']['details']:
            detail = DetailTransfer(transfer=transfer)
            detail.quantity = detail_data['quantity']
            detail.product = Product.objects.get(pk=detail_data['product'])
            detail.save()
        serializer.instance = transfer


class TransferRetrieveAPIView(RetrieveAPIView):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializers


class SaleListCreateAPIView(ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializers

    def perform_create(self, serializer):
        sub_total = serializer._kwargs['data']['sub_total']
        exchanged_rate = serializer._kwargs['data']['exchanged_rate']
        total = serializer._kwargs['data']['total']
        user = User.objects.get(pk=serializer._kwargs['data']['user'])
        client = Client.objects.get(pk=serializer._kwargs['data']['client'])

        sale = Sale(sub_total=sub_total,
                    exchanged_rate=exchanged_rate,
                    total=total,
                    user=user,
                    client=client)
        sale.save()

        for detail_data in serializer._kwargs['data']['details']:
            detail = DetailSale(sale=sale)
            detail.product = Product.objects.get(pk=detail_data['product'])
            detail.quantity = detail_data['quantity']
            detail.price = detail_data['price']
            detail.sub_total = detail_data['sub_total']
            detail.save()
        serializer.instance = sale


class SaleRetrieveAPIView(RetrieveAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializers


class UserListCreateAPIView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class UserRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    lookup_field = 'username'


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class ClientListCreateAPIView(ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializers


class ClientRetrieveAPIView(RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializers
    lookup_field = 'number_document'


class AccessListCreateAPIView(ListCreateAPIView):
    queryset = Access.objects.all()
    serializer_class = AccessSerializers
