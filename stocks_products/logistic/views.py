from rest_framework.viewsets import ModelViewSetfrom
from rest_framework.filters import SearchFilter
django_filters.rest_framework import DjangoFilterBackend
from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer
from rest_framework.pagination import PageNumberPagination


class ProductViewSet(ModelViewSet):
    page_size = 100
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']

class StockViewSet(ModelViewSet):
    page_size = 100
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['address', 'products']
    filterset_fields = ['products']
