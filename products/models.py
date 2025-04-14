from django.db import models
from categories.models import Category


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    content = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
