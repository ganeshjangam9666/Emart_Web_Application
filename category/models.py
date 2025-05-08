from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    about=models.CharField(max_length=100)
    desc=models.CharField(max_length=100)
    pic=models.ImageField(upload_to="categoryImages/")

    def __str__(self):
        return self.name