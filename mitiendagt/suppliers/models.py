from django.db import models

# Create your models here.

class Supplier(models.Model):
    name =models.CharField(max_length=250)
    email = models.EmailField(max_length=254)
    address = models.TextField(max_length=50)
    phone = models.CharField(max_length=20)
    store = models.ForeignKey("stores.Store", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)