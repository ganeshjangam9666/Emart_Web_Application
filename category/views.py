from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    print(request.user)
    data=Category.objects.all()
    return render(request,'Home.html',{'data':data})
