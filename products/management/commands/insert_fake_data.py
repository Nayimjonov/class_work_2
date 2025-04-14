from django.core.management.base import BaseCommand
from faker import Faker
import random
from categories.models import Category
from products.models import Product
from tags.models import Tag


class Command(BaseCommand):
    help = "Insert 100 fake Category, Product, and Tag data"

    def handle(self, *args, **kwargs):
        fake = Faker()

        self.stdout.write("Creating categories...")
        categories = []
        for _ in range(10):
            category = Category.objects.create(
                name=fake.unique.word().capitalize(),
                description=fake.text()
            )
            categories.append(category)

        self.stdout.write("Creating tags...")
        tags = []
        for _ in range(20):
            tag = Tag.objects.create(
                name=fake.unique.word().capitalize()
            )
            tags.append(tag)

        self.stdout.write("Creating products...")
        for _ in range(1000):
            product = Product.objects.create(
                name=fake.sentence(nb_words=3),
                category=random.choice(categories),
                content=fake.text(),
                price=round(random.uniform(10.0, 1000.0), 2),
                is_active=random.choice([True, False])  # Yangi field
            )

            product.tags.set(random.sample(tags, random.randint(1, 5)))

        self.stdout.write(self.style.SUCCESS("✅ 100 ta mahsulot, 10 ta kategoriya va 20 ta tag muvaffaqiyatli yaratildi."))
