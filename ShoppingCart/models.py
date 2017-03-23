from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    quantity = models.CharField(max_length=30)
    description = models.CharField(max_length=30)


class Brand(models.Model):
    Brand = models.CharField(max_length=30)
