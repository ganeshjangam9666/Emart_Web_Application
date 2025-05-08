from django.contrib import admin
from .models import *
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display=['name', 'about', 'desc', 'pic']


admin.site.register(Category, CategoryAdmin)