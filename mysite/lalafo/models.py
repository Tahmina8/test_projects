from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Category(models.Model):
    category_name = models.CharField(max_length= 30, unique=True)

    def __str__(self):
        return self.category_name
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    product_name = models.CharField(max_length=60)
    price = models.PositiveIntegerField(default=0)
    description = models.TextField()
    phone_number = PhoneNumberField(region='KG')
    product_type = models.BooleanField()
    created_date = models.DateField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.product_name



