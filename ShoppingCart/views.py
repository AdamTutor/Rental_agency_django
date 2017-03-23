from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "ShoppingCart/homepage.html")


def store(request):
    return render(request, "ShoppingCart/store.html")