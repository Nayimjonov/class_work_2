from django.db import models
from products.models import Product


class Tag(models.Model):
    name = models.CharField(max_length=200)
    products = models.ManyToManyField(Product, related_name='tags')

    def __str__(self):
        return self.name
