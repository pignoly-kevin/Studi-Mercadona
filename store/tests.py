from django.test import TestCase
from django.utils import timezone
from .models import Category, Product, Promotion

class CategoryModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Pantoufles")

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Pantoufles")

class ProductModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Pantoufles")
        self.product = Product.objects.create(
            name="Pantoufle1",
            description="Beaux Pantoufles",
            price=150,
            image="path/to/image.jpg",
            category=self.category
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Pantoufle1")
        self.assertEqual(self.product.description, "Beaux Pantoufles")
        self.assertEqual(self.product.price, 150)
        self.assertEqual(self.product.image, "path/to/image.jpg")
        self.assertEqual(self.product.category, self.category)
        
class PromotionModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Pantoufles")
        self.product = Product.objects.create(
            name="Pantoufle1",
            description="Beaux Pantoufles",
            price=150,
            image="path/to/image.jpg",
            category=self.category
        )
        self.promotion = Promotion.objects.create(
            product=self.product,
            discount=20.0,
            start_date=timezone.now(),
            end_date=timezone.now() + timezone.timedelta(days=7)
        )

    def test_promotion_creation(self):
        self.assertEqual(self.promotion.product, self.product)
        self.assertEqual(self.promotion.discount, 20.0)
        self.assertTrue(self.promotion.start_date < self.promotion.end_date)

