from django import forms
from django.contrib.auth.hashers import make_password
from .models import Customer
from django.core.validators import MinLengthValidator
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))


    # def save(self):
    #     s=super().save(commit=False)
    #     s.password=make_password(self.cleaned_data['password'])
    #     s.save()
    #     return s



class RegisterForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['username','first_name', 'last_name', 'email', 'password','address', 'country', 'phone']

        phone = forms.CharField(
            widget=forms.TextInput(),
            validators=[MinLengthValidator(10)]
        )
        widgets = {
            'username': forms.TextInput(),
            'password': forms.PasswordInput(),
        }


    def save(self):
        c=super().save(commit=False)
        c.password=make_password(self.cleaned_data['password'])
        c.save()
        return c
    
