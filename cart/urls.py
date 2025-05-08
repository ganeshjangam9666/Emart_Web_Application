from django.urls import path
from .views import cart,add_to_cart,place_order,remove_from_cart
app_name='cart'
urlpatterns =[
    path('add-to-cart/<int:id>/', add_to_cart, name='add_to_cart'),
    path('cart/',cart,name='cart'),
    path('place_order/',place_order, name='status'),
    path('remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
]