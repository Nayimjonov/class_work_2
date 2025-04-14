from rest_framework.pagination import PageNumberPagination


class ProductListPagination(PageNumberPagination):
    page_size = 20