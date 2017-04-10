from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, get_user_model, login, logout
from .forms import UserLoginForm
from django.http import HttpResponse

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
            return HttpResponse("you didnt log in")
    else:
        return render(request, "accounts/login.html", {"form":myform})
            







def register_view(request):
    return render(request, "form.html", {})



def logout_view(request):
    logout(request)
    return redirect(request, "login")