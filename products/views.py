from django.db.models import QuerySet
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework_api_key.permissions import HasAPIKey

from products.api.pagination import CustomPageNumberPagination
from products.api.serializers import ProductsSerializer
from products.models import Product


class ProductCreateView(CreateAPIView):
    serializer_class = ProductsSerializer


class ProductsListView(ListAPIView):
    serializer_class = ProductsSerializer
    queryset = Product.objects.all()
    pagination_class = CustomPageNumberPagination


class ProductUpdateView(UpdateAPIView):
    serializer_class = ProductsSerializer
    queryset = Product.objects.all()


# Delete view
class ProductDeleteView(DestroyAPIView):
    serializer_class = ProductsSerializer
    queryset = Product.objects.all()


class ProductsInCategoryListView(ListAPIView):
    serializer_class = ProductsSerializer
    queryset = Product.objects.all()
    pagination_class = CustomPageNumberPagination

    def get_queryset(self) -> QuerySet:
        return self.queryset.filter(category_id=self.kwargs['pk'])
