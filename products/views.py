from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
from .pagination import ProductListPagination


class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.select_related('category').all()
        paginator = ProductListPagination()
        result_page = paginator.paginate_queryset(products, request)
        serializer = ProductSerializer(result_page, many=True)

        return paginator.get_paginated_response(serializer.data)