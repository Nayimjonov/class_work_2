from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    category = serializers.CharField(read_only=True, source='category.name')
    content = serializers.CharField(read_only=True)
    price = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)
