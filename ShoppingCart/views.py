from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item, Brand
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, "ShoppingCart/homepage.html")


def store(request):
    counter = 0
    Items = Item.objects.all()
    Brands = Brand.objects.all()
    print(len(Items[0].img))
    return render(request, "ShoppingCart/store.html",{'Items': Items, 'Brands': Brands, 'counter': counter})




def rent(request, item_id):
    item = Item.objects.get(pk=item_id)
    if item.quantity != 0:
        item.quantity -= 1
        item.save()
        messages.success(request, item.name+" has been successfully purchased")
    else: 
        item.quantity = item.quantity
        item.save()
        messages.warning(request, item.name+" is out of stock")
    return redirect("store")

    

def return_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    item.quantity += 1
    item.save()
    messages.success(request, item.name+" has been successfully returned")
    return redirect("store")

    