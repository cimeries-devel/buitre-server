from django.urls import path
from .views import ColorListAPIView
from .views import ColorRetrieveUpdateDestroyAPIView
from .views import SexListAPIView
from .views import SexRetrieveUpdateDestroyAPIView
from .views import SizeListAPIView
from .views import SizeRetrieveUpdateDestroyAPIView
from .views import CategoryListAPIView
from .views import CategoryRetrieveUpdateDestroyAPIView
from .views import StyleListAPIView
from .views import StyleRetrieveUpdateDestroyAPIView
from .views import ProductListAPIView
from .views import ProductRetrieveUpdateDestroyAPIView
from .views import CompanyListAPIView
from .views import CompanyRetrieveUpdateDestroyAPIView
from .views import BranchListAPIView
from .views import BranchRetrieveUpdateDestroyAPIView
from .views import StockListAPIView
from .views import StockRetrieveUpdateDestroyAPIView
from .views import UserListAPIView
from .views import UserRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('color/', ColorListAPIView.as_view()),
    path('color/<int:pk>/', ColorRetrieveUpdateDestroyAPIView.as_view()),
    path('sex/', SexListAPIView.as_view()),
    path('sex/<int:pk>/', SexRetrieveUpdateDestroyAPIView.as_view()),
    path('size/', SizeListAPIView.as_view()),
    path('size/<int:pk>/', SizeRetrieveUpdateDestroyAPIView.as_view()),
    path('category/', CategoryListAPIView.as_view()),
    path('category/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view()),
    path('style/', StyleListAPIView.as_view()),
    path('style/<int:pk>/', StyleRetrieveUpdateDestroyAPIView.as_view()),
    path('product/', ProductListAPIView.as_view()),
    path('product/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view()),
    path('company/', CompanyListAPIView.as_view()),
    path('company/<int:pk>/', CompanyRetrieveUpdateDestroyAPIView.as_view()),
    path('branch/', BranchListAPIView.as_view()),
    path('branch/<int:pk>/', BranchRetrieveUpdateDestroyAPIView.as_view()),
    path('stock/', StockListAPIView.as_view()),
    path('stock/<int:pk>/', StockRetrieveUpdateDestroyAPIView.as_view()),
    path('user/', UserListAPIView.as_view()),
    path('user/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view()),
]
