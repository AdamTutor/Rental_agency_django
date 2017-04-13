from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, login, logout
from .forms import UserLoginForm, UserRegisterForm
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.


# def login_view(request):
#     form = UserLoginForm(request.POST or None)
#     print("THIS WORKED")
#     if form.is_valid():
#         username = form.cleaned_data.get("username")
#         password = form.cleaned_data.get("password")
#     return render(request, "accounts/login.html", {"form":form})





def login_view(request):
    myform = UserLoginForm(request.POST or None)
    if myform.is_valid():
        print('this was a post')
        data = myform.cleaned_data
        username = data['username']
        password = data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("store")
        else:
            return redirect("login")
    else:
        return render(request, "accounts/login.html", {"form":myform})
            







def register_view(request):
    myform = UserRegisterForm(request.POST or None)
    if myform.is_valid():
        Loginform = UserLoginForm()
        data = myform.cleaned_data
        username = data["username"]
        email = data["email"]
        password = data["password"]
        user = User.objects.create_user(username, email, password)
        user.save()
        login(request, user)
        return redirect("store")
    return render(request, "accounts/login.html", {"form":myform})



def logout_view(request):
    logout(request)
    return redirect("login")