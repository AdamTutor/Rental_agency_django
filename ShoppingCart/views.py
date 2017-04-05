from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item, Brand, ShoppingCart
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
    if request.method == 'POST':
        cart_item = ShoppingCart.objects.all()
        context = {"cart": cart_item}
        a = request.POST
        b = str(a)
        print(json.loads(b))
        return render(request, "ShoppingCart/cart.html", context)

    
    item.quantity += 1
    item.save()
    messages.success(request, item.name+" has been successfully returned")
    return redirect("store")

# def cart(request):
#     if request.method == 'POST':
#         cart_item = ShoppingCart.objects.all()
#         context = {"cart": cart_item}
#         a = request.POST
#         b = str(a)
#         print(json.loads(b))
#         return render(request, "ShoppingCart/cart.html", context)

def cart(request):
    if request.method == 'POST':
        cart_items = json.loads(request.body.decode("utf-8"))
        for item in cart_items['data']:
            # print(item['name'],item['name'],item['price'],item['quantity'],item['description'],item['img'])
            a = Item(name=item['name'],price=item['price'],quantity=item['quantity'],description=item['description'],img=item['img'])
            print(a.name)
        return HttpResponse("success")