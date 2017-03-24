from django.shortcuts import render, redirect
from .models import Item, Brand

# Create your views here.
def home(request):
    return render(request, "ShoppingCart/homepage.html")


def store(request):
    Items = Item.objects.all()
    Brands = Brand.objects.all()
    print(len(Items[0].img))
    return render(request, "ShoppingCart/store.html",{'Items': Items, 'Brands': Brands})


def rent(request, item_id):
    item = Item.objects.get(pk=int(item_id))
    item.quantity -= 1
    item.save()
    return redirect("store")

    


    