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

    def static_url(self):
        return 'ShoppingCart/img/' + self.img



class Brand(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
