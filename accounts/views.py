from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate,login,logout

from category.models import Category
from .models import Customer
# Create your views here.

# def login_view(request):
#     form=LoginForm()
#     if request.method=="POST":
#         form=LoginForm(request.POST)
#         if form.is_valid():
#             username=form.cleaned_data['username']
#             password=form.cleaned_data['password']
#             user=authenticate(username,password)
#             if user is not None:
#                 return render(request,'Home.html')
#             return render(request,'Login.html',{'form':form,'error':'Invalid credentials'})
#     form=LoginForm()
#     return render(request, 'Login.html',{'form':form})

data=Category.objects.all()

def login_view(request):
    form=LoginForm()
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            user=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return render(request,'Home.html',{'data':data})
            else:
                form=LoginForm()
                return render(request, 'Login.html',{'form':form})
    form=LoginForm()
    return render(request, 'Login.html',{'form':form})


def logout_view(request):
    logout(request)
    return redirect('/login/')

def register(request):
    form=RegisterForm()
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request,'Register.html',{'form':form})
    form=RegisterForm()
    return render(request,'Register.html',{'form':form})



def contactus(request):
    return render(request, 'ContactUs.html')


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Customer

# @login_required
# def profile_view(request):
#     # Get the current logged-in user (Customer model)
#     customer = Customer.objects.get(user=request.user)  # Assuming the AbstractUser is extended with a Customer model

#     return render(request, 'Profile.html', {'customer': customer})

@login_required
def profile_view(request):
    # Get the current logged-in user (Customer model)
    customer = request.user  # Directly use the logged-in user (already an instance of Customer)

    return render(request, 'Profile.html', {'customer': customer})

