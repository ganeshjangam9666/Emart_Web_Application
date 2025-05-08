from django.contrib import admin
from .models import *
# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display=['username','password','email','phone', 'address','first_name','last_name','country']


admin.site.register(Customer, CustomerAdmin)