from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)

    def get_discounted_price(self):
        promotions = self.promotions.filter(start_date__lte=timezone.now(), end_date__gte=timezone.now())
        if promotions:
            discount = promotions[0].discount
            return self.price * (1 - discount / 100)
        return self.price

    def __str__(self):
        return self.name

class Promotion(models.Model):
    product = models.ForeignKey(Product, related_name='promotions', on_delete=models.CASCADE)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return f'{self.discount}% off on {self.product.name}'