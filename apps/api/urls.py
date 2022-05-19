from django.urls import path
from .views import ColorListCreateAPIView
from .views import ColorRetrieveUpdateDestroyAPIView
from .views import SexListCreateAPIView
from .views import SexRetrieveUpdateDestroyAPIView
from .views import SizeListCreateAPIView
from .views import SizeRetrieveUpdateDestroyAPIView
from .views import CategoryListCreateAPIView
from .views import CategoryRetrieveUpdateDestroyAPIView
from .views import StyleListCreateAPIView
from .views import StyleRetrieveUpdateDestroyAPIView
from .views import ProductListCreateAPIView
from .views import ProductRetrieveUpdateDestroyAPIView
from .views import CompanyListCreateAPIView
from .views import CompanyRetrieveUpdateDestroyAPIView
from .views import BranchListCreateAPIView
from .views import BranchForUserListAPIView
from .views import BranchRetrieveUpdateDestroyAPIView
from .views import StockListCreateAPIView
from .views import StockListAPIView
from .views import StockRetrieveUpdateDestroyAPIView
from .views import TransferListCreateAPIView
from .views import TransferRetrieveAPIView
from .views import SaleListCreateAPIView
from .views import SaleRetrieveAPIView
from .views import UserListCreateAPIView
from .views import UserRetrieveAPIView
from .views import UserRetrieveUpdateDestroyAPIView
from .views import ClientListCreateAPIView
from .views import ClientRetrieveAPIView
from .views import AccessListCreateAPIView


urlpatterns = [
    path('color/', ColorListCreateAPIView.as_view()),
    path('color/<int:pk>/', ColorRetrieveUpdateDestroyAPIView.as_view()),
    path('sex/', SexListCreateAPIView.as_view()),
    path('sex/<int:pk>/', SexRetrieveUpdateDestroyAPIView.as_view()),
    path('size/', SizeListCreateAPIView.as_view()),
    path('size/<int:pk>/', SizeRetrieveUpdateDestroyAPIView.as_view()),
    path('category/', CategoryListCreateAPIView.as_view()),
    path('category/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view()),
    path('style/', StyleListCreateAPIView.as_view()),
    path('style/<int:pk>/', StyleRetrieveUpdateDestroyAPIView.as_view()),
    path('product/', ProductListCreateAPIView.as_view()),
    path('product/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view()),
    path('company/', CompanyListCreateAPIView.as_view()),
    path('company/<int:pk>/', CompanyRetrieveUpdateDestroyAPIView.as_view()),
    path('branch/', BranchListCreateAPIView.as_view()),
    path('branch/<int:pk>/', BranchRetrieveUpdateDestroyAPIView.as_view()),
    path('branch/username/', BranchForUserListAPIView.as_view()),
    path('stock/', StockListCreateAPIView.as_view()),
    path('stock/<int:branch>/', StockListAPIView.as_view()),
    path('stock/<int:branch>/<int:product>/', StockRetrieveUpdateDestroyAPIView.as_view()), # not use
    path('transfer/', TransferListCreateAPIView.as_view()),
    path('transfer/<int:pk>/', TransferRetrieveAPIView.as_view()),
    path('sale/', SaleListCreateAPIView.as_view()),
    path('sale/<int:pk>/', SaleRetrieveAPIView.as_view()),
    path('user/', UserListCreateAPIView.as_view()),
    path('user/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view()),
    path('user/<str:username>/', UserRetrieveAPIView.as_view()),
    path('client/', ClientListCreateAPIView.as_view()),
    path('client/<int:number_document>/', ClientRetrieveAPIView.as_view()),
    path('access/', AccessListCreateAPIView.as_view()),
]
