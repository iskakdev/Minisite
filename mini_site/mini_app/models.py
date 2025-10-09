from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Category(models.Model):
    category_name = models.CharField(max_length=55, unique=True)

    def __str__(self):
        return f'{self.category_name}'


class Product(models.Model):
    product_name = models.CharField(max_length=54)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = PhoneNumberField()
    description = models.TextField()
    product_type = models.BooleanField()
    created_data = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'{self.product_name}'