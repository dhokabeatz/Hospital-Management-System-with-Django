from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomRegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=200,required=True)
    address = forms.CharField(max_length=200,required=True)


    class Meta:
        model = User
        fields = ['username','password1', 'password2','name', 'email', 'phone_number','address']