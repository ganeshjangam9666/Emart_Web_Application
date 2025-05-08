from django.db import models
from category.models import Category
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField()
    discount = models.IntegerField()
    pic = models.ImageField(upload_to='productImages/')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name