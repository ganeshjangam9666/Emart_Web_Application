from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Customer(AbstractUser):
    address =models.CharField(max_length=200)
    country = models.CharField(max_length=20)
    phone=models.CharField(max_length=10)
    def __str__(self):
        return self.username
