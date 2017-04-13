from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    quantity = models.IntegerField()
    description = models.CharField(max_length=30)
    img = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def rent(self):
        if self.quantity > 0:
            self.quantity -= 1
            self.save()
            return True
        else:
            return False

    def return_item(self):
        if self.quantity > 0:
            self.quantity += 1
            self.save()
            return True
        else:
            return False
            
    def static_url(self):
        return 'ShoppingCart/img/' + self.img
    
    def to_dict(self):
        return {'name': self.name,
                    'price': self.price,
                    'quantity': self.quantity,
                    'description': self.description,
        'img': self.img}



class Brand(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

# class ShoppingCart(models.Model):
    # name = models.CharField(max_length=30)
    # item = models.ForeignKey(Item, on_delete=models.CASCADE)
    
    # def __str__(self):
    #     return self.name
