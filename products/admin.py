from django.contrib import admin
from .models import Product
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'desc', 'discount', 'pic', 'category']

admin.site.register(Product, ProductAdmin)