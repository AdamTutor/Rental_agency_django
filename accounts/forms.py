from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



class UserRegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput)

