from django.urls import path
from .views import *


app_name='products'
urlpatterns =[
    path('products/<str:id>/',productsbycat,name='product'),
    path('productdetails/<int:id>/',productDetails,name='productDetails')
]