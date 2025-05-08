from django.shortcuts import render
from .models import Product
# Create your views here.

# def productsbycat(request,id):
#     data=Product.objects.filter(category_id=id)
#     pl={}
#     for i in data:
#         tp=i.price-(i.discount/100)*i.price
#         pl[tp]=i
#     # tp=data.price-(data.discount/100)*data.price
#     # totl_price=data.price-
#     return render(request,'Products.html',{'pl':pl})

def productsbycat(request,id):
    data = Product.objects.filter(category_id=id)
    # tp = [product.price for product in data]
    tp=[]
    for i in data:
        tp+=[int(i.price-(i.discount/100)*i.price)]
    combined_data = zip(data, tp)
    context = {
        'combined_data': combined_data,
    }

    return render(request, 'Products.html', context)

def productDetails(request,id):
    data=Product.objects.get(id=id)
    return render(request,'ProductDetails.html',{'data':data})





