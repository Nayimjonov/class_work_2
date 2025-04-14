from rest_framework.views import APIView
from .serializers import ProductSerializer
from .models import Product
from .pagination import ProductListPagination


class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.filter(is_active=True)
        products = products.select_related('category').prefetch_related('tags')
        paginator = ProductListPagination()
        result_page = paginator.paginate_queryset(products, request)
        serializer = ProductSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)