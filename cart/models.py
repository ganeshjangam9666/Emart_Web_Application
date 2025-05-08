from django.db import models
from django.contrib.auth.models import User
from accounts.models import Customer 
from products.models import Product

class Cart(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_image = models.ImageField(upload_to='cart_images/', blank=True, null=True)
    quantity = models.IntegerField(default=1)
    added_on = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        return self.quantity * self.product_price

    def __str__(self):
        return f"{self.user.username} - {self.product_name}"
