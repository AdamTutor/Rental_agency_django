from django.contrib import admin
from .models import Item, Brand, ShoppingCart
# Register your models here.


admin.site.register(Item)
admin.site.register(Brand)
admin.site.register(ShoppingCart)