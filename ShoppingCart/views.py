from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item, Brand
from django.contrib import messages
import json


# Create your views here.
def home(request):
    return render(request, "ShoppingCart/homepage.html")


def store(request):
    Items = Item.objects.all()
    item_dicts = {item.name: item.to_dict() for item in Items}
    Brands = Brand.objects.all()
    Json_dump = json.dumps(item_dicts)
    # print(Json_dump)
    return render(request, "ShoppingCart/store.html",{'Items': Items, 'Brands': Brands, 'Json_dump': Json_dump})




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

    