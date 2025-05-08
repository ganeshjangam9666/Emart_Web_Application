from django.contrib import admin
from .models import Cart
# Register your models here.


class CartAdmin(admin.ModelAdmin):
    list_display = ['id','product_name','product_price','product_image','quantity','product_id','user_id']

admin.site.register(Cart, CartAdmin)