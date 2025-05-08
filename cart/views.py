from django.shortcuts import render, redirect, get_object_or_404,HttpResponse
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Cart
# Create your views here.

def cart(request):
    data = Cart.objects.filter(user=request.user)
    return render(request,'Cart.html',{'data':data})



@login_required
def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)
    cart_item, created = Cart.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={
            'product_name': product.name,
            'product_price': product.price,
            'product_image': product.pic,
        }
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart:cart')


def place_order(request):
    return HttpResponse('Order placed successfully.....')



@login_required
def remove_from_cart(request, item_id):
    try:
        # Get the cart for the logged-in user
        cart = Cart.objects.filter(user=request.user)

        # Get the CartItem object that the user wants to remove
        cart_item = Cart.objects.get(id=item_id)
        
        # Remove the CartItem from the cart
        cart_item.delete()

        # Optionally, redirect to the cart page or another view
        return redirect('cart:cart')  # Assuming 'cart' is the name of your cart page URL

    except Cart.DoesNotExist:
        # If the CartItem does not exist or other error, handle it appropriately
        return redirect('cart:cart') 